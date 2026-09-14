#!/usr/bin/env python3
"""Fetch last quotes for tickers → data/prices.json. Stdlib only.

Usage: python scripts/prices.py CEG TLN VST
       python scripts/prices.py            # tickers from wiki/positions (status != closed)
"""
import json, sys, time, urllib.request, urllib.error, pathlib, datetime as dt

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (My_Wiki brief; hengkun.zhang@mail.mcgill.ca)"


def _get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/plain,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def parse_yahoo_chart(payload: str) -> dict:
    d = json.loads(payload)
    res = d["chart"]["result"][0]["meta"]
    ts = res.get("regularMarketTime")
    asof = dt.datetime.fromtimestamp(ts, dt.timezone.utc).isoformat() if ts else ""
    return {"price": float(res["regularMarketPrice"]), "currency": res.get("currency", "USD"),
            "asof": asof, "source": "yahoo", "name": res.get("longName") or res.get("shortName", "")}


def fetch_quote(ticker: str) -> dict:
    last_err = None
    for host in ("query1", "query2"):
        url = f"https://{host}.finance.yahoo.com/v8/finance/chart/{ticker}?range=1d&interval=1d"
        try:
            return parse_yahoo_chart(_get(url))
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(0.5)
    return {"error": f"{type(last_err).__name__}: {last_err}"}


def positions_tickers() -> list:
    sys.path.insert(0, str(ROOT / "scripts"))
    from frontmatter import load_frontmatter  # local stdlib parser
    out = []
    for p in sorted((ROOT / "wiki" / "positions").glob("*.md")):
        meta, _ = load_frontmatter(p)
        if meta.get("type") == "position" and meta.get("status") != "closed" and meta.get("ticker"):
            out.append(str(meta["ticker"]).upper())
    return out


def main(argv):
    tickers = [t.upper() for t in argv] or positions_tickers()
    out = {"asof": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "quotes": {}}
    for t in tickers:
        out["quotes"][t] = fetch_quote(t)
        time.sleep(0.3)
    (ROOT / "data").mkdir(exist_ok=True)
    dest = ROOT / "data" / "prices.json"
    ok = {t: q for t, q in out["quotes"].items() if "price" in q}
    if not ok and dest.exists():
        print("all quotes failed — prices.json left untouched (stale cache kept)")
        for t, q in out["quotes"].items():
            print(t, q.get("error"))
        return 1
    if len(ok) < len(out["quotes"]) and dest.exists():  # partial failure: keep the old quote for the failed tickers
        try:
            old = json.loads(dest.read_text()).get("quotes", {})
            for t, q in out["quotes"].items():
                if "price" not in q and "price" in old.get(t, {}):
                    out["quotes"][t] = dict(old[t], stale=True, error=q.get("error"))
        except Exception:  # noqa: BLE001
            pass
    dest.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    for t, q in out["quotes"].items():
        print(t, q.get("price", q.get("error")))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
