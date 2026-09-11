#!/usr/bin/env python3
"""SEC EDGAR monitor for the open positions. Stdlib only.

  python scripts/sec_fetch.py [--since YYYY-MM-DD] [--tickers CEG TLN] [--forms 8-K,10-Q,10-K,4]
      → data/sec/<TICKER>.json  (filings list w/ flags, 8-quarter metrics)
      → data/sec/text/<accession>.txt  (plain text of 8-K/10-Q/10-K documents; git-ignored)
  python scripts/sec_fetch.py search "FERC co-location" --tickers TLN --since 2026-08-01
      → EDGAR full-text search hits (JSON to stdout)

Rules: User-Agent carries the human's email; ≤ 10 req/s; one registrant failing never aborts the run.
"""
import argparse, datetime as dt, html, json, pathlib, re, sys, time, urllib.parse, urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sec"
UA = "My_Wiki hengkun.zhang@mail.mcgill.ca"
SLEEP = 0.12

KEYWORDS = ["FERC", "NRC", "Nuclear Regulatory", "PJM", "ERCOT", "ISO-NE", "MISO", "PUC", "co-locat", "colocat",
            "interconnect", "uprate", "PPA", "power purchase", "behind-the-meter", "behind the meter",
            "export control", "sanction", "denied", "rejected", "reject", "protest", "complaint",
            "order", "data center", "hyperscale", "Amazon", "AWS", "Microsoft", "Meta", "Google",
            "terminat", "delay", "cancel", "acquisition", "credit agreement", "notes due"]
# 8-K items worth reading in full
ITEMS_OF_INTEREST = {"1.01": "material definitive agreement", "1.02": "termination of material agreement",
                     "2.02": "results of operations", "2.03": "creation of direct financial obligation",
                     "7.01": "Reg FD disclosure", "8.01": "other events"}
METRICS = {  # metric -> (candidate tags, kind)   kind: duration | instant
    "Revenues": (["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"], "duration"),
    "NetIncomeLoss": (["NetIncomeLoss"], "duration"),
    "EPSDiluted": (["EarningsPerShareDiluted"], "duration"),
    "OperatingIncomeLoss": (["OperatingIncomeLoss"], "duration"),
    "OperatingCashFlow": (["NetCashProvidedByUsedInOperatingActivities"], "duration"),
    "Capex": (["PaymentsToAcquirePropertyPlantAndEquipment"], "duration"),
    "LongTermDebt": (["LongTermDebtNoncurrent", "LongTermDebt"], "instant"),
    "Cash": (["CashAndCashEquivalentsAtCarryingValue"], "instant"),
}


# ---------- HTTP ----------
def get(url, retries=3, timeout=30, binary=False):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "identity"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            time.sleep(SLEEP)
            return data if binary else data.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET {url}: {type(last).__name__}: {last}")


def get_json(url):
    return json.loads(get(url))


# ---------- HTML → text ----------
class _Text(HTMLParser):
    SKIP = {"script", "style", "head", "title"}
    BLOCK = {"p", "div", "br", "tr", "li", "h1", "h2", "h3", "h4", "table", "td", "th"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self._skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1
        elif tag in self.BLOCK:
            self.out.append("\n" if tag not in ("td", "th") else " | ")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.out.append(data)


def html_to_text(doc: str) -> str:
    p = _Text(); p.feed(doc)
    t = "".join(p.out)
    t = re.sub(r"[ \t\xa0]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


# ---------- flags ----------
def flag_text(text: str, keywords=KEYWORDS, ctx=160, max_per_kw=3) -> list:
    out = []
    for kw in keywords:
        hits = [m.start() for m in re.finditer(re.escape(kw), text, re.I)]
        if not hits:
            continue
        snips = []
        for h in hits[:max_per_kw]:
            s = text[max(0, h - ctx): h + len(kw) + ctx].replace("\n", " ")
            snips.append(re.sub(r"\s+", " ", s).strip())
        out.append({"keyword": kw, "count": len(hits), "snippets": snips})
    out.sort(key=lambda x: -x["count"])
    return out


# ---------- XBRL ----------
def _entries(facts: dict, tags: list):
    for tag in tags:
        u = facts.get("us-gaap", {}).get(tag, {}).get("units", {})
        if u:
            unit = next(iter(u))
            return tag, unit, [e for e in u[unit] if e.get("form") in ("10-Q", "10-K", "10-K/A", "10-Q/A")]
    return None, None, []


def quarterly_series(facts: dict, tags: list, kind: str = "duration", n: int = 8) -> dict:
    """Return {"tag":..,"unit":..,"series":[{"end","val","fp","form","derived"}]} — last n quarters, oldest first."""
    tag, unit, es = _entries(facts, tags)
    if not es:
        return {"tag": None, "unit": None, "series": []}
    by_end = {}
    if kind == "instant":
        for e in es:
            k = e["end"]
            if k not in by_end or e["filed"] > by_end[k]["filed"]:
                by_end[k] = {"end": k, "val": e["val"], "fp": e.get("fp"), "form": e["form"], "filed": e["filed"], "derived": False}
    else:
        # 1) direct quarterly values (duration ≈ one quarter)
        ytd = {}  # (start) -> {end: entry}
        for e in es:
            s, en = e.get("start"), e["end"]
            if not s:
                continue
            days = (dt.date.fromisoformat(en) - dt.date.fromisoformat(s)).days
            if 80 <= days <= 100:
                if en not in by_end or e["filed"] > by_end[en]["filed"]:
                    by_end[en] = {"end": en, "val": e["val"], "fp": e.get("fp"), "form": e["form"], "filed": e["filed"], "derived": False}
            elif 170 <= days <= 370:
                ytd.setdefault(s, {})
                if en not in ytd[s] or e["filed"] > ytd[s][en]["filed"]:
                    ytd[s][en] = e
        # 2) derive missing quarters from YTD differences (Q2 = H1−Q1, Q3 = 9M−H1, Q4 = FY−9M)
        for s, ends in ytd.items():
            prev_val, prev_end = None, None
            # the first quarter of this YTD chain is the direct quarter starting at s
            q1 = [v for k, v in by_end.items() if not v["derived"] and any(
                e.get("start") == s and e["end"] == k for e in es)]
            if q1:
                prev_val, prev_end = q1[0]["val"], q1[0]["end"]
            for en in sorted(ends):
                e = ends[en]
                if prev_val is not None and en not in by_end:
                    by_end[en] = {"end": en, "val": round(e["val"] - prev_val, 4), "fp": e.get("fp"), "form": e["form"],
                                  "filed": e["filed"], "derived": True}
                prev_val, prev_end = e["val"], en
    series = sorted(by_end.values(), key=lambda x: x["end"])[-n:]
    for x in series:
        x.pop("filed", None)
    return {"tag": tag, "unit": unit, "series": series}


# ---------- filings ----------
def cik_map():
    p = DATA / "company_tickers.json"
    if p.exists() and (time.time() - p.stat().st_mtime) < 7 * 86400:
        d = json.loads(p.read_text())
    else:
        d = get_json("https://www.sec.gov/files/company_tickers.json")
        DATA.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(d))
    return {v["ticker"].upper(): (int(v["cik_str"]), v["title"]) for v in d.values()}


def filing_docs(cik: int, accession: str) -> list:
    acc = accession.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/"
    try:
        idx = get_json(base + "index.json")
        names = [i["name"] for i in idx["directory"]["item"] if i["name"].lower().endswith((".htm", ".html", ".txt"))]
    except Exception:  # noqa: BLE001
        return []
    return [base + n for n in names if not n.endswith("-index.htm") and "xsl" not in n.lower()]


def fetch_filing_text(cik: int, accession: str, primary: str, max_bytes=3_000_000) -> tuple:
    """Returns (text, docs). Fetches primary doc + exhibits (.htm) up to max_bytes."""
    docs = filing_docs(cik, accession) or [f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession.replace('-', '')}/{primary}"]
    parts, total = [], 0
    for u in docs:
        if u.lower().endswith(".txt") and len(docs) > 1:
            continue  # the full-submission .txt duplicates everything
        try:
            raw = get(u)
        except Exception as e:  # noqa: BLE001
            parts.append(f"[[fetch error {u}: {e}]]"); continue
        total += len(raw)
        parts.append(f"===== {u.rsplit('/', 1)[-1]} =====\n" + html_to_text(raw))
        if total > max_bytes:
            parts.append("[[truncated: size limit]]"); break
    return "\n\n".join(parts), docs


def process_ticker(ticker: str, cik: int, name: str, since: str, forms: set, want_text: set) -> dict:
    out = {"ticker": ticker, "cik": cik, "name": name, "fetched": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
           "since": since, "filings": [], "metrics": {}}
    cik10 = f"{cik:010d}"
    sub = get_json(f"https://data.sec.gov/submissions/CIK{cik10}.json")
    r = sub["filings"]["recent"]
    out["sic"] = sub.get("sicDescription"); out["fiscal_year_end"] = sub.get("fiscalYearEnd")
    for i, form in enumerate(r["form"]):
        if form not in forms:
            continue
        filed = r["filingDate"][i]
        if filed < (dt.date.fromisoformat(since) - dt.timedelta(days=120)).isoformat():
            break  # list is newest-first; keep ~4 months of history for context
        acc = r["accessionNumber"][i]; prim = r["primaryDocument"][i]
        f = {"form": form, "filed": filed, "report_date": r["reportDate"][i], "accession": acc, "primary_doc": prim,
             "items": [x.strip() for x in r["items"][i].split(",") if x.strip()],
             "url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{prim}",
             "index_url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/",
             "is_new": filed >= since, "flags": [], "text_path": None}
        f["items_desc"] = [ITEMS_OF_INTEREST.get(x, "") for x in f["items"]]
        if form in want_text and f["is_new"]:
            try:
                text, docs = fetch_filing_text(cik, acc, prim)
                (DATA / "text").mkdir(parents=True, exist_ok=True)
                tp = DATA / "text" / f"{acc}.txt"; tp.write_text(text, encoding="utf-8")
                f["text_path"] = str(tp.relative_to(ROOT)); f["docs"] = docs; f["text_chars"] = len(text)
                f["flags"] = flag_text(text)
            except Exception as e:  # noqa: BLE001
                f["error"] = str(e)
        out["filings"].append(f)
    try:
        facts = get_json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik10}.json")["facts"]
        for m, (tags, kind) in METRICS.items():
            out["metrics"][m] = quarterly_series(facts, tags, kind)
    except Exception as e:  # noqa: BLE001
        out["metrics_error"] = str(e)
    return out


def load_positions() -> list:
    sys.path.insert(0, str(ROOT / "scripts"))
    from frontmatter import load_frontmatter
    t = []
    for p in sorted((ROOT / "wiki" / "positions").glob("*.md")):
        meta, _ = load_frontmatter(p)
        if meta.get("type") == "position" and meta.get("status") != "closed" and meta.get("ticker"):
            t.append(str(meta["ticker"]).upper())
    return t


def fulltext_search(q: str, ciks: list, since: str, until: str = None) -> dict:
    until = until or dt.date.today().isoformat()
    params = {"q": q, "dateRange": "custom", "startdt": since, "enddt": until}
    if ciks:
        params["ciks"] = ",".join(f"{c:010d}" for c in ciks)
    url = "https://efts.sec.gov/LatestSearchResults?" + urllib.parse.urlencode(params)
    d = get_json(url)
    hits = []
    for h in d.get("hits", {}).get("hits", []):
        s = h["_source"]; adsh = s.get("adsh", ""); fid = h.get("_id", "")
        cik = s.get("ciks", [""])[0].lstrip("0")
        doc = fid.split(":", 1)[1] if ":" in fid else ""
        hits.append({"form": s.get("form"), "filed": s.get("file_date"), "entity": (s.get("display_names") or [""])[0],
                     "accession": adsh, "url": f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-', '')}/{doc}"})
    return {"query": q, "total": d.get("hits", {}).get("total", {}).get("value"), "hits": hits}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", default="fetch", choices=["fetch", "search"])
    ap.add_argument("query", nargs="?", default=None)
    ap.add_argument("--since", default=(dt.date.today() - dt.timedelta(days=7)).isoformat())
    ap.add_argument("--tickers", nargs="*", default=None)
    ap.add_argument("--forms", default="8-K,10-Q,10-K,4")
    ap.add_argument("--text-forms", default="8-K,10-Q,10-K", help="forms whose documents are downloaded + flagged")
    a = ap.parse_args(argv)
    tickers = [t.upper() for t in (a.tickers or load_positions())]
    cm = cik_map()
    if a.cmd == "search":
        ciks = [cm[t][0] for t in tickers if t in cm]
        print(json.dumps(fulltext_search(a.query, ciks, a.since), indent=2, ensure_ascii=False)); return 0
    DATA.mkdir(parents=True, exist_ok=True)
    forms, want = set(a.forms.split(",")), set(a.text_forms.split(","))
    summary = []
    for t in tickers:
        if t not in cm:
            summary.append(f"{t}: not in company_tickers.json"); continue
        cik, name = cm[t]
        try:
            res = process_ticker(t, cik, name, a.since, forms, want)
        except Exception as e:  # noqa: BLE001
            res = {"ticker": t, "cik": cik, "name": name, "error": str(e), "filings": [], "metrics": {}}
        (DATA / f"{t}.json").write_text(json.dumps(res, indent=1, ensure_ascii=False))
        new = [f for f in res["filings"] if f.get("is_new")]
        flagged = [f for f in new if f.get("flags")]
        summary.append(f"{t}: {len(res['filings'])} filings kept, {len(new)} new since {a.since}, {len(flagged)} with flags"
                       + (f", ERROR {res['error']}" if res.get("error") else ""))
        for f in new:
            top = ", ".join(f"{x['keyword']}×{x['count']}" for x in f["flags"][:6])
            summary.append(f"   {f['form']:5} {f['filed']} items={','.join(f['items']) or '-'}  {top}")
    print("\n".join(summary))
    return 0


if __name__ == "__main__":
    sys.exit(main())
