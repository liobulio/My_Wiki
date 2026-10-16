#!/usr/bin/env python3
"""Week-ahead calendar → data/calendar.json (the brief's 本周前瞻 section).

  python scripts/calendar_fetch.py               # next 7 calendar days
  python scripts/calendar_fetch.py --days 10

Sources: Fed FOMC calendar page · Nasdaq economic-events and earnings APIs · TreasuryDirect
upcoming auctions · NYSE holidays (static list below, check yearly). Earnings are filtered to
the book (open + watch positions) plus brief/config.yaml `calendar_tickers`. Stdlib only.
"""
import html
import json
import pathlib
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from frontmatter import load_frontmatter, parse_yaml_subset  # noqa: E402

ET = ZoneInfo("America/New_York")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126 Safari/537.36", "Accept": "application/json"}
# NYSE full closures / early closes (13:00 ET). Source: nyse.com holiday calendar — re-check each January.
NYSE = {"2026-11-26": "美股休市（感恩节）", "2026-11-27": "美股提前收盘 13:00（感恩节次日）",
        "2026-12-24": "美股提前收盘 13:00（平安夜）", "2026-12-25": "美股休市（圣诞节）",
        "2027-01-01": "美股休市（元旦）", "2027-01-18": "美股休市（马丁·路德·金日）",
        "2027-02-15": "美股休市（总统日）", "2027-03-26": "美股休市（耶稣受难日）"}
# Headline US releases only (exact names as Nasdaq lists them); regional Fed surveys and sub-indices are noise here.
ECON_EXACT = {"CPI", "Core CPI", "PPI", "Core PPI", "Nonfarm Payrolls", "Unemployment Rate", "GDP", "PCE Price Index",
              "Core PCE Price Index", "Retail Sales", "Core Retail Sales", "ISM Manufacturing PMI", "ISM Non-Manufacturing PMI",
              "ISM Services PMI", "JOLTS Job Openings", "Initial Jobless Claims", "Michigan Consumer Sentiment",
              "CB Consumer Confidence", "Durable Goods Orders", "Housing Starts", "FOMC Meeting Minutes", "Beige Book",
              "Employment Cost Index"}
AUCTION_TERMS = ("2-Year", "3-Year", "5-Year", "7-Year", "10-Year", "20-Year", "30-Year", "TIPS")
MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August",
                                      "September", "October", "November", "December"], 1)}


def _get(url, timeout=20):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def parse_fomc(html):
    """Fed calendar page → [(date_of_decision_day, 'statement'/'SEP')]."""
    out = []
    for year_m in re.finditer(r"(\d{4}) FOMC Meetings(.*?)(?=\d{4} FOMC Meetings|$)", html, re.S):
        year = int(year_m.group(1))
        for mon, days in re.findall(r'fomc-meeting__month[^>]*>\s*<strong>([^<]+)</strong>.*?fomc-meeting__date[^>]*>([^<]+)<',
                                    year_m.group(2), re.S):
            mon = mon.split("/")[-1].strip()
            nums = re.findall(r"\d+", days)
            if mon in MONTHS and nums:
                out.append((date(year, MONTHS[mon], int(nums[-1])), "*" in days))
    return out


def nasdaq_time(hhmm):
    """Nasdaq's `gmt` field is already US Eastern (PPI shows 08:30) — keep it as is."""
    return hhmm if re.fullmatch(r"\d{1,2}:\d{2}", hhmm or "") else ""


def is_key_econ(name):
    name = (name or "").strip()
    return name in ECON_EXACT or bool(re.match(r"Fed Chair \w+ Speaks$", name))


def book_tickers():
    out = []
    for p in sorted((ROOT / "wiki" / "positions").glob("*.md")):
        meta, _ = load_frontmatter(p)
        if meta.get("status") in ("open", "watch") and meta.get("ticker"):
            out.append(str(meta["ticker"]).upper())
    return out


def main(argv):
    days = 7
    for i, a in enumerate(argv):
        if a.startswith("--days"):
            days = int(a.split("=", 1)[1]) if "=" in a else int(argv[i + 1])
    today = datetime.now(ET).date()
    end = today + timedelta(days=days)
    cfg = parse_yaml_subset((ROOT / "brief" / "config.yaml").read_text(encoding="utf-8"))
    book = book_tickers()
    watch = set(book) | {str(t).upper() for t in (cfg.get("calendar_tickers") or [])}
    rows, errors = [], []

    try:
        for d, sep in parse_fomc(_get("https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm")):
            if today <= d <= today + timedelta(days=max(days, 14)):   # FOMC shows up to two weeks out
                rows.append({"date": d.isoformat(), "time": "14:00", "kind": "fed",
                             "event": "FOMC 利率决议" + ("（含点阵图 / SEP）" if sep else "") + " · 14:30 记者会", "tickers": []})
    except Exception as e:  # noqa: BLE001
        errors.append(f"fomc: {e}")

    d = today
    while d <= end:
        if d.weekday() < 5:
            try:
                data = json.loads(_get(f"https://api.nasdaq.com/api/calendar/economicevents?date={d}"))
                seen = set()
                for r in (data.get("data") or {}).get("rows") or []:
                    name = (r.get("eventName") or "").strip()
                    if r.get("country") == "United States" and is_key_econ(name) and name not in seen:
                        seen.add(name)
                        rows.append({"date": d.isoformat(), "time": nasdaq_time(r.get("gmt", "")), "kind": "data",
                                     "event": r["eventName"].strip(), "consensus": html.unescape(r.get("consensus") or "").replace("\xa0", " ").strip(),
                                     "previous": html.unescape(r.get("previous") or "").replace("\xa0", " ").strip(), "tickers": []})
            except Exception as e:  # noqa: BLE001
                errors.append(f"econ {d}: {e}")
            try:
                data = json.loads(_get(f"https://api.nasdaq.com/api/calendar/earnings?date={d}"))
                for r in (data.get("data") or {}).get("rows") or []:
                    sym = (r.get("symbol") or "").upper()
                    if sym in watch:
                        t = (r.get("time") or "").replace("time-pre-market", "盘前").replace("time-after-hours", "盘后") \
                            .replace("time-not-supplied", "")
                        rows.append({"date": d.isoformat(), "time": t, "kind": "earnings",
                                     "event": f"{sym} 财报" + (f"（预期 EPS {r['epsForecast']}）" if r.get("epsForecast") else ""),
                                     "tickers": [sym], "in_book": sym in book})
            except Exception as e:  # noqa: BLE001
                errors.append(f"earnings {d}: {e}")
        if d.isoformat() in NYSE:
            rows.append({"date": d.isoformat(), "time": "", "kind": "holiday", "event": NYSE[d.isoformat()], "tickers": []})
        d += timedelta(days=1)

    try:
        for a in json.loads(_get("https://www.treasurydirect.gov/TA_WS/securities/upcoming?format=json")):
            ad = (a.get("auctionDate") or "")[:10]
            if ad and today.isoformat() <= ad <= end.isoformat() and any(t in a.get("securityTerm", "") for t in AUCTION_TERMS):
                rows.append({"date": ad, "time": "13:00", "kind": "auction",
                             "event": f"{a['securityTerm']} {a.get('securityType', '')}".strip(), "tickers": []})
    except Exception as e:  # noqa: BLE001
        errors.append(f"treasury: {e}")

    rows.sort(key=lambda r: (r["date"], r["time"] or "99"))
    path = ROOT / "data" / "calendar.json"
    path.write_text(json.dumps({"asof": today.isoformat(), "days": days, "rows": rows, "errors": errors},
                               ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(rows)} calendar rows {today}→{end} → {path}" + (f" · errors: {errors}" if errors else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
