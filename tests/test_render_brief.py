import sys, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import render_brief as rb


def _ctx():
    ctx = rb.build_ctx()
    ctx["opportunities"]["test-opp"] = {"slug": "test-opp", "title": "t", "body": "", "meta": {
        "ticker": "VST", "title": "测试机会", "logic": "逻辑一句话", "institutions": ["[[cicc]]"], "first_seen": "2026-01-02", "status": "new", "edge": "E1", "catalyst": "C1", "invalidation": "I1"}}
    return ctx


def test_render_day_structure():
    brief = rb.load_brief(ROOT / "tests" / "fixtures" / "brief_min.md")
    assert brief["date"] == "2026-01-02" and len(brief["data"]["macro"]) == 1
    h = rb.render_day(brief, _ctx())
    assert 'data-origin="foreign"' in h and 'data-origin="domestic"' in h
    assert "观点变化" in h and "逻辑一句话" in h and "测试头条" in h
    assert "Thesis Test（提案）" in h and ">I1<" in h
    assert "<svg" in h  # sparkline from live SEC cache (TLN)
    assert 'class="inv warning"' in h
    assert not re.search(r'<(script|link)[^>]+(src|href)="https?://', h)
    assert 'obsidian://open?vault=' in h


def test_sparkline_and_money():
    s = rb.sparkline([{"end": "2025-03-31", "val": 1e9}, {"end": "2025-06-30", "val": 2e9}], "USD", "营收")
    assert "<svg" in s and "$2.00B" in s and "同比" not in s
    # YoY matches by date: a missing quarter must not shift the comparison
    gap = [{"end": "2025-03-31", "val": 100}, {"end": "2025-06-30", "val": 200}, {"end": "2025-09-30", "val": 300},
           {"end": "2025-12-31", "val": 400}, {"end": "2026-06-30", "val": 300}]
    assert "+50% 同比" in rb.sparkline(gap, "USD", "x")
    assert rb.fmt_money(-1.5e9) == "-$1.50B" and rb.fmt_money(2.5e6) == "$2M"


def test_render_index():
    h = rb.render_index(_ctx())
    assert "机会看板" in h and "跟踪的机构" in h


def test_render_markdown_is_phone_readable():
    brief = rb.load_brief(ROOT / "tests" / "fixtures" / "brief_min.md")
    md = rb.render_markdown(brief, _ctx())
    assert md.startswith("# 美股机构简报 2026-01-02")
    assert "### 宏观（1）" in md and "### 行业（1）" in md
    assert "_今日无新增。_" in md                      # empty us_equity stated, not padded
    assert "<details><summary>原文</summary>" in md    # quotes collapsible on GitHub
    assert "△ 观点变化" in md                          # is_change surfaced
    assert "Thesis Test（我起草的提案，未经你采纳）" in md
    assert "✅" in md and "⚠️" in md                    # invalidation checklist icons
    assert "## 我的持仓" in md
    assert "[[" not in md                              # every wikilink resolved or flattened


def test_wikilinks_to_text_strips_pipes_for_table_cells():
    assert rb.wikilinks_to_text("见 [[ceg|CEG 页]] 与 [[tln]]") == "见 CEG 页 与 tln"
    assert "[[" not in rb.wikilinks_to_text("**[[a|b]]**")
