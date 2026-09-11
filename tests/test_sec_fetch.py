import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
from sec_fetch import flag_text, quarterly_series, html_to_text


def test_flag_text():
    f = flag_text("On November 1, 2024 the FERC rejected the amended ISA for the co-location of the data center.")
    kws = {x["keyword"] for x in f}
    assert {"FERC", "rejected", "co-locat", "data center"} <= kws
    assert any("rejected the amended" in s for x in f for s in x["snippets"])


def _e(start, end, val, form, fp, filed):
    return {"start": start, "end": end, "val": val, "form": form, "fp": fp, "filed": filed, "fy": 2025}


def test_quarterly_series_derives_from_ytd():
    facts = {"us-gaap": {"NetCashProvidedByUsedInOperatingActivities": {"units": {"USD": [
        _e("2025-01-01", "2025-03-31", 100, "10-Q", "Q1", "2025-05-01"),
        _e("2025-01-01", "2025-06-30", 250, "10-Q", "Q2", "2025-08-01"),   # H1 → Q2 = 150
        _e("2025-01-01", "2025-09-30", 450, "10-Q", "Q3", "2025-11-01"),   # 9M → Q3 = 200
        _e("2025-01-01", "2025-12-31", 700, "10-K", "FY", "2026-02-20"),   # FY → Q4 = 250
    ]}}}}
    s = quarterly_series(facts, ["NetCashProvidedByUsedInOperatingActivities"], "duration")
    vals = [(x["end"], x["val"], x["derived"]) for x in s["series"]]
    assert vals == [("2025-03-31", 100, False), ("2025-06-30", 150, True), ("2025-09-30", 200, True), ("2025-12-31", 250, True)]


def test_quarterly_series_instant_dedupes():
    facts = {"us-gaap": {"LongTermDebtNoncurrent": {"units": {"USD": [
        {"end": "2025-12-31", "val": 10, "form": "10-K", "fp": "FY", "filed": "2026-02-20"},
        {"end": "2025-12-31", "val": 11, "form": "10-Q", "fp": "Q1", "filed": "2026-05-01"},  # restated later → wins
        {"end": "2026-03-31", "val": 12, "form": "10-Q", "fp": "Q1", "filed": "2026-05-01"},
    ]}}}}
    s = quarterly_series(facts, ["LongTermDebtNoncurrent", "LongTermDebt"], "instant")
    assert [(x["end"], x["val"]) for x in s["series"]] == [("2025-12-31", 11), ("2026-03-31", 12)]


def test_html_to_text():
    t = html_to_text("<html><head><title>x</title><style>a{}</style></head><body><p>Item&nbsp;1.01</p><div>Entry into a <b>Material</b> Agreement</div></body></html>")
    assert "Item 1.01" in t and "Entry into a Material Agreement" in t and "a{}" not in t
