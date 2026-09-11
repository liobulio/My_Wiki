import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
from prices import parse_yahoo_chart
from frontmatter import split_frontmatter


def test_parse_yahoo_chart():
    payload = json.dumps({"chart": {"result": [{"meta": {"currency": "USD", "regularMarketPrice": 288.45,
                                                          "regularMarketTime": 1789140823, "longName": "Constellation"}}]}})
    q = parse_yahoo_chart(payload)
    assert q["price"] == 288.45 and q["currency"] == "USD" and q["asof"].startswith("2026-")


def test_frontmatter_subset():
    meta, body = split_frontmatter('---\ntype: position\nticker: TLN\nshares: 5.407\nweight:\n'
                                   'thesis: "[[ai-power-ipp-bull]]"\ninvalidation_status: [ok, watch, ok, ok]\n'
                                   'tags:\n  - a\n  - b\n---\n# body\n')
    assert meta["ticker"] == "TLN" and meta["shares"] == 5.407 and meta["weight"] == ""
    assert meta["thesis"] == "[[ai-power-ipp-bull]]"
    assert meta["invalidation_status"] == ["ok", "watch", "ok", "ok"] and meta["tags"] == ["a", "b"]
    assert body.startswith("# body")
