import sys, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import render_brief as rb


def _ctx():
    ctx = rb.build_ctx()
    ctx["opportunities"]["test-opp"] = {"slug": "test-opp", "title": "t", "body": "", "meta": {
        "ticker": "VST", "title": "测试机会", "logic": "逻辑一句话", "institutions": ["[[cicc]]"], "first_seen": "2026-01-02", "status": "new"}}
    return ctx


def test_render_day_structure():
    brief = rb.load_brief(ROOT / "tests" / "fixtures" / "brief_min.md")
    assert brief["date"] == "2026-01-02" and len(brief["data"]["macro"]) == 1
    h = rb.render_day(brief, _ctx())
    assert 'data-origin="foreign"' in h and 'data-origin="domestic"' in h
    assert "观点变化" in h and "逻辑一句话" in h and "测试头条" in h
    assert "<svg" in h  # sparkline from live SEC cache (TLN)
    assert 'class="inv warning"' in h
    assert not re.search(r'<(script|link)[^>]+(src|href)="https?://', h)
    assert 'obsidian://open?vault=' in h


def test_sparkline_and_money():
    s = rb.sparkline([{"end": "2025-03-31", "val": 1e9}, {"end": "2025-06-30", "val": 2e9}], "USD", "营收")
    assert "<svg" in s and "$2.00B" in s
    assert rb.fmt_money(-1.5e9) == "-$1.50B" and rb.fmt_money(2.5e6) == "$2M"


def test_render_index():
    h = rb.render_index(_ctx())
    assert "机会看板" in h and "跟踪的机构" in h
