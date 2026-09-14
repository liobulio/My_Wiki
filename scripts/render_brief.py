#!/usr/bin/env python3
"""Render the daily brief HTML from wiki pages + data/. Stdlib only.

  python scripts/render_brief.py                 # latest brief in wiki/briefs → brief/<date>.html + brief/index.html
  python scripts/render_brief.py --date 2026-09-11
Reads: wiki/briefs/*.md (frontmatter + ```json brief-data block), wiki/opportunities, wiki/positions, wiki/theses,
       wiki/institutions, wiki/sources (title/url lookup), data/sec/*.json, data/prices.json, brief/config.yaml
Output is self-contained: inline CSS/JS/SVG, no external resources.
"""
import argparse, datetime as dt, html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from frontmatter import load_frontmatter, parse_yaml_subset  # noqa: E402

VAULT = ROOT.name
WEEKDAY = "一二三四五六日"
STATUS = {"ok": ("✓", "正常", "good"), "watch": ("!", "关注", "warning"), "hit": ("✕", "触发", "critical")}
OPP_STATUS = {"new": "新出现", "watching": "跟踪中", "adopted": "已采纳", "dropped": "已放弃"}
FORM_DESC = {"8-K": "临时报告", "10-Q": "季报", "10-K": "年报", "4": "内部人交易"}
ITEM_DESC = {"1.01": "重大合同", "1.02": "合同终止", "2.02": "业绩", "2.03": "新增债务", "5.02": "高管变动",
             "7.01": "Reg FD 披露", "8.01": "其他事项", "9.01": "附件"}


def esc(s):
    return html.escape("" if s is None else str(s), quote=True)


def obsidian(slug, folder=None):
    f = f"{folder}/{slug}" if folder else slug
    return f"obsidian://open?vault={VAULT}&file={f}"


def wikilinks(text):
    """[[a|b]] → obsidian link; **x** → strong; newlines → paragraphs. Input is escaped first."""
    t = esc(text)
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", lambda m: f'<a class="wl" href="{obsidian(m.group(1))}">{m.group(2)}</a>', t)
    t = re.sub(r"\[\[([^\]]+)\]\]", lambda m: f'<a class="wl" href="{obsidian(m.group(1))}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    paras = [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]
    return "".join(f"<p>{p}</p>" for p in paras)


# ---------- loading ----------
def load_dir(folder, want_type=None):
    out = {}
    d = ROOT / "wiki" / folder
    if not d.exists():
        return out
    for p in sorted(d.glob("*.md")):
        meta, body = load_frontmatter(p)
        if want_type and meta.get("type") != want_type:
            continue
        m = re.search(r"^#\s+(.+)$", body, re.M)
        out[p.stem] = {"meta": meta, "body": body, "title": m.group(1).strip() if m else p.stem, "slug": p.stem}
    return out


def load_brief(path):
    meta, body = load_frontmatter(path)
    m = re.search(r"```json\s*brief-data\s*\n(.*?)\n```", body, re.S)
    data = json.loads(m.group(1)) if m else {}
    prose = body[:m.start()] if m else body
    prose = re.sub(r"^#\s+.+$", "", prose, count=1, flags=re.M).strip()
    for k in ("macro", "industry", "us_equity", "logic_changes", "opportunities", "positions"):
        data.setdefault(k, [])
    return {"meta": meta, "data": data, "prose": prose, "date": str(meta.get("date") or path.stem), "slug": path.stem}


def load_json(p, default):
    try:
        return json.loads(pathlib.Path(p).read_text())
    except Exception:  # noqa: BLE001
        return default


def build_ctx():
    ctx = {"positions": load_dir("positions", "position"), "theses": load_dir("theses", "thesis"),
           "opportunities": load_dir("opportunities", "opportunity"), "institutions": load_dir("institutions", "institution"),
           "sources": load_dir("sources"), "prices": load_json(ROOT / "data" / "prices.json", {"quotes": {}}),
           "sec": {}, "briefs": []}
    for p in sorted((ROOT / "data" / "sec").glob("*.json")):
        if p.stem.isupper():
            ctx["sec"][p.stem] = load_json(p, {})
    cfg = ROOT / "brief" / "config.yaml"
    ctx["config"] = parse_yaml_subset(cfg.read_text()) if cfg.exists() else {}
    for p in sorted((ROOT / "wiki" / "briefs").glob("*.md")):
        ctx["briefs"].append(load_brief(p))
    return ctx


# ---------- formatting ----------
def fmt_money(v, unit="USD"):
    if v is None:
        return "–"
    if unit and "shares" in unit:
        return f"{v:.2f}"
    a = abs(v)
    if a >= 1e9:
        s = f"{v / 1e9:.2f}B"
    elif a >= 1e6:
        s = f"{v / 1e6:.0f}M"
    else:
        s = f"{v:,.0f}"
    return "$" + s.replace("$-", "-$") if not s.startswith("-") else "-$" + s[1:]


def fmt_date_cn(d):
    try:
        x = dt.date.fromisoformat(d)
        return f"{x.year}年{x.month}月{x.day}日 周{WEEKDAY[x.weekday()]}"
    except Exception:  # noqa: BLE001
        return d


def inst_name(ctx, slug):
    i = ctx["institutions"].get(slug)
    return i["title"] if i else slug


def inst_origin(ctx, slug, fallback="foreign"):
    i = ctx["institutions"].get(slug)
    return (i["meta"].get("origin") if i else None) or fallback


def source_info(ctx, slug):
    s = ctx["sources"].get(slug)
    if not s:
        return {"title": slug, "url": ""}
    return {"title": s["meta"].get("title") or s["title"], "url": s["meta"].get("url") or ""}


# ---------- components ----------
def badge(ctx, slug, origin=None):
    o = origin or inst_origin(ctx, slug)
    lab = "外资" if o == "foreign" else "内资"
    return (f'<a class="badge" data-origin="{esc(o)}" href="{obsidian(slug, "wiki/institutions")}" '
            f'title="{esc(inst_name(ctx, slug))}"><span class="dot"></span>{lab} · {esc(inst_name(ctx, slug))}</a>')


def view_row(ctx, v):
    src = source_info(ctx, v.get("source", ""))
    url = v.get("url") or src["url"]
    tick = "".join(f'<span class="tk">{esc(t)}</span>' for t in v.get("tickers", []) or [])
    chg = '<span class="chip chg">观点变化</span>' if v.get("is_change") else ""
    quote = v.get("quote") or ""
    q = f'<blockquote lang="en">{esc(quote)}</blockquote>' if quote else ""
    link = f'<a href="{esc(url)}" target="_blank" rel="noopener">原文 ↗</a> · ' if url else ""
    wl = f'<a class="wl" href="{obsidian(v.get("source", ""), "wiki/sources")}">wiki: {esc(src["title"])}</a>' if v.get("source") else ""
    return (f'<li class="view">{badge(ctx, v.get("institution", ""), v.get("origin"))}{chg}{tick}'
            f'<div class="vt">{esc(v.get("view", ""))}</div>'
            f'<details><summary>原文与来源</summary>{q}<div class="src">{link}{wl}</div></details></li>')


def section_views(ctx, key, title, items, empty="今日无新增。"):
    body = "".join(view_row(ctx, v) for v in items) if items else f'<p class="empty">{empty}</p>'
    return f'<section id="{key}"><h2>{title} <span class="n">{len(items)}</span></h2><ul class="views">{body}</ul></section>'


def section_logic(ctx, items):
    if not items:
        body = '<p class="empty">今日没有记录到行业逻辑的变化。</p>'
    else:
        body = "".join(
            f'<div class="lc">{badge(ctx, x.get("institution", ""))}<h3>{esc(x.get("sector", ""))}</h3>'
            f'<div class="ba"><div><span class="lab">之前</span>{esc(x.get("before", ""))}</div>'
            f'<div><span class="lab">现在</span>{esc(x.get("after", ""))}</div></div>'
            f'<div class="src"><a class="wl" href="{obsidian(x.get("source", ""), "wiki/sources")}">wiki: {esc(source_info(ctx, x.get("source", ""))["title"])}</a></div></div>'
            for x in items)
    return f'<section id="logic"><h2>行业逻辑变化 <span class="n">{len(items)}</span></h2>{body}</section>'


def opp_card(ctx, slug, today=None):
    o = ctx["opportunities"].get(slug)
    if not o:
        return f'<div class="opp"><h3>{esc(slug)}</h3><p class="empty">缺少 wiki/opportunities/{esc(slug)}.md</p></div>'
    m = o["meta"]
    insts = m.get("institutions") or []
    insts = [re.sub(r"[\[\]]", "", i) for i in (insts if isinstance(insts, list) else [insts])]
    st = m.get("status", "new")
    is_new = today and str(m.get("first_seen")) == today
    tk = f'<span class="tk big">{esc(m["ticker"])}</span>' if m.get("ticker") else ""
    new_chip = '<span class="chip new">今日新增</span>' if is_new else ""
    return (f'<div class="opp" data-status="{esc(st)}">{tk}<h3><a class="wl" href="{obsidian(slug, "wiki/opportunities")}">{esc(m.get("title") or o["title"])}</a></h3>'
            f'<p class="logic">{esc(m.get("logic", ""))}</p>'
            + ("".join(f'<div class="tt"><span class="lab">{lab}</span>{esc(m.get(k))}</div>'
                       for k, lab in (("edge", "Edge"), ("catalyst", "Catalyst"), ("invalidation", "Invalidation")) if m.get(k))
               and f'<details class="ttest"><summary>Thesis Test（提案）</summary>'
                   + "".join(f'<div class="tt"><span class="lab">{lab}</span>{esc(m.get(k))}</div>'
                             for k, lab in (("edge", "Edge"), ("catalyst", "Catalyst"), ("invalidation", "Invalidation")) if m.get(k))
                   + '</details>' or "")
            + f'<div class="who">{"".join(badge(ctx, i) for i in insts)}</div>'
            f'<div class="meta"><span class="chip st-{esc(st)}">{OPP_STATUS.get(st, st)}</span>'
            f'{new_chip}<span>首次出现 {esc(m.get("first_seen", ""))}</span></div></div>')


def section_opps(ctx, slugs, today):
    body = "".join(opp_card(ctx, s, today) for s in slugs) if slugs else '<p class="empty">今日没有新的买入机会。</p>'
    return f'<section id="opps"><h2>买入机会 <span class="n">{len(slugs)}</span></h2><div class="grid">{body}</div></section>'


def sparkline(series, unit, label, w=180, h=44):
    pts = [(x["end"], x["val"]) for x in series if isinstance(x.get("val"), (int, float))]
    if len(pts) < 2:
        return f'<div class="spark"><div class="sl">{esc(label)}</div><div class="empty">无数据</div></div>'
    vals = [v for _, v in pts]
    lo, hi = min(vals + [0]), max(vals + [0])
    rng = (hi - lo) or 1
    n = len(pts); pad = 4
    xs = [pad + i * (w - 2 * pad) / (n - 1) for i in range(n)]
    ys = [pad + (hi - v) * (h - 2 * pad) / rng for v in vals]
    zero_y = pad + (hi - 0) * (h - 2 * pad) / rng
    path = " ".join(f"{'M' if i == 0 else 'L'}{xs[i]:.1f},{ys[i]:.1f}" for i in range(n))
    dots = "".join(f'<circle class="hit" cx="{xs[i]:.1f}" cy="{ys[i]:.1f}" r="7"><title>{esc(pts[i][0])}: {esc(fmt_money(vals[i], unit))}</title></circle>' for i in range(n))
    last = f'<circle cx="{xs[-1]:.1f}" cy="{ys[-1]:.1f}" r="3.5" class="last"/>'
    latest = fmt_money(vals[-1], unit)
    delta = ""
    # YoY vs the quarter ending 12 months earlier (matched by date, so a missing quarter cannot shift the comparison)
    last_end = pts[-1][0]
    yago = f"{int(last_end[:4]) - 1}{last_end[4:7]}"
    prev = next((v for e, v in pts if e[:7] == yago), None)
    if prev not in (0, None):
        pct = (vals[-1] - prev) / abs(prev) * 100
        delta = f'<span class="delta {"up" if pct >= 0 else "down"}">{"+" if pct >= 0 else ""}{pct:.0f}% 同比</span>'
    return (f'<div class="spark"><div class="sl">{esc(label)} <span class="mono">{esc(latest)}</span>{delta}</div>'
            f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)} 近{n}季">'
            f'<line x1="{pad}" x2="{w - pad}" y1="{zero_y:.1f}" y2="{zero_y:.1f}" class="zero"/>'
            f'<path d="{path}" class="line"/>{last}{dots}</svg>'
            f'<div class="sx">{esc(pts[0][0][:7])} → {esc(pts[-1][0][:7])}</div></div>')


def filing_row(f, cik):
    items = " ".join(f'<span class="chip it">{esc(i)} {esc(ITEM_DESC.get(i, ""))}</span>' for i in f.get("items", []) if i != "9.01")
    flags = "".join(f'<span class="chip fl" title="{esc(x["snippets"][0] if x.get("snippets") else "")}">{esc(x["keyword"])}×{x["count"]}</span>'
                    for x in (f.get("flags") or [])[:6])
    new = '<span class="chip new">新</span>' if f.get("is_new") else ""
    return (f'<li class="filing"><span class="form">{esc(f["form"])}</span><span class="fd">{esc(FORM_DESC.get(f["form"], ""))}</span>'
            f'<span class="mono">{esc(f["filed"])}</span>{new}{items}'
            f'<a href="{esc(f["url"])}" target="_blank" rel="noopener">EDGAR ↗</a><div class="flags">{flags}</div></li>')


def position_card(ctx, ticker, note=None, brief_filings=None, inv_override=None):
    pos = next((p for p in ctx["positions"].values() if str(p["meta"].get("ticker", "")).upper() == ticker), None)
    meta = pos["meta"] if pos else {}
    sec = ctx["sec"].get(ticker, {})
    q = ctx["prices"].get("quotes", {}).get(ticker, {})
    price = q.get("price")
    shares = float(meta.get("shares") or 0)
    value = price * shares if price else None
    total = sum((ctx["prices"].get("quotes", {}).get(str(p["meta"].get("ticker", "")).upper(), {}).get("price") or 0) * float(p["meta"].get("shares") or 0)
                for p in ctx["positions"].values() if p["meta"].get("status") != "closed")
    acct = float(ctx["config"].get("account_total_usd") or 0) or total
    w_pos = value / total * 100 if value and total else 0
    w_acct = value / acct * 100 if value and acct else 0
    inv = inv_override or meta.get("invalidation_status") or []
    thesis_slug = re.sub(r"[\[\]]", "", str(meta.get("thesis", "")))
    th = ctx["theses"].get(thesis_slug)
    inv_labels = []
    if th:
        inv_labels = th["meta"].get("invalidations") or []
        if not isinstance(inv_labels, list) or not inv_labels:  # fallback: numbered list under the Invalidation heading
            sec_txt = th["body"].split("**The Invalidation**", 1)[-1].split("\n## ", 1)[0]
            inv_labels = [re.sub(r"\s+", " ", x) for x in re.findall(r"^\s*\d\.\s+(.+?)(?=^\s*\d\.|\Z)", sec_txt, re.M | re.S)]
    inv_rows = ""
    for i, s in enumerate(inv):
        icon, lab, cls = STATUS.get(s, STATUS["ok"])
        txt = inv_labels[i] if i < len(inv_labels) else f"条件 {i + 1}"
        inv_rows += f'<li class="inv {cls}"><span class="ic">{icon}</span><span class="lab">{lab}</span><span>{esc(re.sub(r"[*_]", "", txt))}</span></li>'
    m = sec.get("metrics", {})
    sparks = "".join(sparkline(m.get(k, {}).get("series", []), m.get(k, {}).get("unit"), lab) for k, lab in
                     [("Revenues", "营收"), ("NetIncomeLoss", "净利润"), ("OperatingCashFlow", "经营现金流"), ("EPSDiluted", "稀释 EPS")])
    filings = [f for f in sec.get("filings", []) if f.get("is_new") or (brief_filings and f["accession"] in brief_filings)]
    filings = sorted(filings, key=lambda f: f["filed"], reverse=True)[:8]
    fl = "".join(filing_row(f, sec.get("cik")) for f in filings) or '<li class="empty">本期无新申报。</li>'
    name = sec.get("name") or q.get("name") or ticker
    price_s = f"${price:,.2f}" if price else "–"
    note_html = '<p class="note">' + wikilinks(note) + '</p>' if note else ""
    shares_html = f'<span class="mono">{esc(shares)} 股</span><span class="mono">≈ ${value:,.0f}</span>' if value else ""
    thesis_title = th["title"] if th else thesis_slug
    inv_html = inv_rows or "<li class=empty>未设置</li>"
    return (f'<article class="pos" id="pos-{esc(ticker)}"><header><span class="tk big">{esc(ticker)}</span><h3>{esc(name)}</h3>'
            f'<span class="mono">{price_s}</span>{shares_html}</header>'
            f'<div class="wrow"><div class="wbar" title="占持仓 {w_pos:.1f}% · 占账户 {w_acct:.1f}%"><div style="width:{w_acct:.1f}%"></div></div>'
            f'<span class="wlab">账户占比 {w_acct:.0f}% · 持仓占比 {w_pos:.0f}%</span></div>'
            f'{note_html}'
            f'<div class="cols"><div><h4>论点失效条件 <a class="wl" href="{obsidian(thesis_slug, "wiki/theses")}">{esc(thesis_title)}</a></h4><ul class="invs">{inv_html}</ul></div>'
            f'<div><h4>近 8 季（SEC XBRL）</h4><div class="sparks">{sparks}</div></div></div>'
            f'<h4>新申报 <span class="n">{len(filings)}</span></h4><ul class="filings">{fl}</ul>'
            f'<div class="src"><a class="wl" href="{obsidian(ticker.lower(), "wiki/positions")}">wiki 持仓页</a> · <a class="wl" href="{obsidian(ticker.lower(), "wiki/assets")}">资产页</a></div></article>')


def section_positions(ctx, brief_positions):
    by_t = {str(p.get("ticker", "")).upper(): p for p in brief_positions}
    cards = ""
    for pos in sorted(ctx["positions"].values(), key=lambda p: str(p["meta"].get("ticker"))):
        if pos["meta"].get("status") == "closed":
            continue
        t = str(pos["meta"].get("ticker", "")).upper()
        bp = by_t.get(t, {})
        cards += position_card(ctx, t, bp.get("note"), set(bp.get("filings") or []), bp.get("invalidation_status"))
    cards = cards or "<p class=empty>暂无持仓。</p>"
    return f'<section id="positions"><h2>我的持仓 <span class="n">{len(ctx["positions"])}</span></h2>{cards}</section>'


CSS = """
:root{color-scheme:light;--surface:#fcfcfb;--plane:#f9f9f7;--ink:#0b0b0b;--ink2:#52514e;--muted:#898781;--grid:#e1e0d9;--axis:#c3c2b7;--border:rgba(11,11,11,.10);
--foreign:#2a78d6;--domestic:#eb6834;--good:#0ca30c;--warning:#fab219;--critical:#d03b3b;--up:#006300;--seq:#2a78d6;--seqbg:#cde2fb}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--surface:#1a1a19;--plane:#0d0d0d;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--foreign:#3987e5;--domestic:#d95926;--up:#0ca30c;--seq:#3987e5;--seqbg:#184f95}}
:root[data-theme=dark]{color-scheme:dark;--surface:#1a1a19;--plane:#0d0d0d;--ink:#fff;--ink2:#c3c2b7;--muted:#898781;--grid:#2c2c2a;--axis:#383835;--border:rgba(255,255,255,.10);--foreign:#3987e5;--domestic:#d95926;--up:#0ca30c;--seq:#3987e5;--seqbg:#184f95}
*{box-sizing:border-box}body{margin:0;background:var(--plane);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif}
a{color:inherit}.wl{color:var(--ink2);text-decoration:underline dotted}.mono{font-variant-numeric:tabular-nums;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.92em;color:var(--ink2)}
.wrap{max-width:1080px;margin:0 auto;padding:20px 20px 60px}
header.top{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:baseline;border-bottom:1px solid var(--grid);padding-bottom:12px;margin-bottom:12px}
header.top h1{font-size:22px;margin:0}header.top .sub{color:var(--ink2)}header.top nav{margin-left:auto;display:flex;gap:12px;font-size:14px}
nav.toc{position:sticky;top:0;background:var(--plane);z-index:2;display:flex;flex-wrap:wrap;gap:4px;padding:8px 0;border-bottom:1px solid var(--grid);margin-bottom:16px}
nav.toc a{text-decoration:none;padding:4px 10px;border-radius:999px;border:1px solid var(--border);font-size:13px;color:var(--ink2)}nav.toc a:hover{background:var(--surface)}
.headline{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:14px 18px;margin-bottom:18px}.headline p{margin:.4em 0}
section{margin:26px 0}h2{font-size:18px;margin:0 0 10px;display:flex;align-items:center;gap:8px}h2 .n{font-size:12px;background:var(--surface);border:1px solid var(--border);border-radius:999px;padding:0 8px;color:var(--ink2)}
h3{font-size:16px;margin:4px 0}h4{font-size:13px;color:var(--ink2);margin:14px 0 6px;font-weight:600}
ul.views{list-style:none;margin:0;padding:0;display:grid;gap:10px}li.view{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px}
.badge{display:inline-flex;align-items:center;gap:6px;font-size:12px;padding:2px 9px 2px 6px;border-radius:999px;border:1px solid var(--border);text-decoration:none;color:var(--ink2);margin:0 6px 4px 0;vertical-align:middle}
.badge .dot{width:9px;height:9px;border-radius:50%;background:var(--foreign);display:inline-block}.badge[data-origin=domestic] .dot{background:var(--domestic)}
.badge[data-origin=foreign]{border-color:color-mix(in srgb,var(--foreign) 45%,transparent)}.badge[data-origin=domestic]{border-color:color-mix(in srgb,var(--domestic) 45%,transparent)}
.chip{display:inline-block;font-size:11px;padding:1px 7px;border-radius:999px;border:1px solid var(--border);color:var(--ink2);margin:0 4px 4px 0;vertical-align:middle}
.chip.chg{border-color:var(--warning);color:var(--ink)}.chip.chg::before{content:"△ "}.chip.new{border-color:var(--foreign);color:var(--ink)}.chip.fl{background:var(--surface)}.chip.it{border-style:dashed}
.chip.st-adopted{border-color:var(--good)}.chip.st-dropped{opacity:.6;text-decoration:line-through}
.tk{display:inline-block;font-family:ui-monospace,Menlo,monospace;font-size:12px;font-weight:600;padding:1px 6px;border-radius:4px;background:var(--plane);border:1px solid var(--grid);margin-right:4px;vertical-align:middle}.tk.big{font-size:15px;padding:2px 8px}
.vt{margin:6px 0 4px;font-size:15.5px}details{font-size:13.5px;color:var(--ink2)}summary{cursor:pointer;user-select:none}blockquote{margin:8px 0;padding:6px 12px;border-left:3px solid var(--grid);color:var(--ink2);font-style:italic}
.src{font-size:12.5px;color:var(--muted);margin-top:6px}.empty{color:var(--muted);font-style:italic}
.lc{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px;margin-bottom:10px}.ba{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ba .lab{display:block;font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
@media(max-width:640px){.ba{grid-template-columns:1fr}}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}.opp{background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 14px}.opp .logic{margin:6px 0;font-size:14.5px}.opp .meta{font-size:12px;color:var(--muted);display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:6px}
.opp[data-status=dropped]{opacity:.65}.ttest{margin:6px 0}.tt{font-size:13px;margin:4px 0;padding-left:8px;border-left:2px solid var(--grid)}.tt .lab{display:inline-block;min-width:82px;font-size:11px;font-weight:600;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
article.pos{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 16px;margin-bottom:14px}article.pos>header{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px}article.pos h3{margin:0}
.wrow{display:flex;align-items:center;gap:10px;margin:10px 0}.wbar{flex:1;height:10px;background:var(--seqbg);border-radius:4px;overflow:hidden}.wbar div{height:100%;background:var(--seq);border-radius:4px 0 0 4px}.wlab{font-size:12px;color:var(--ink2);white-space:nowrap;font-variant-numeric:tabular-nums}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}@media(max-width:760px){.cols{grid-template-columns:1fr}}
ul.invs{list-style:none;padding:0;margin:0;display:grid;gap:6px}li.inv{display:grid;grid-template-columns:22px 40px 1fr;gap:6px;align-items:start;font-size:13.5px;padding:6px 8px;border-radius:6px;border:1px solid var(--border)}
li.inv .ic{font-weight:700;text-align:center;border-radius:50%;width:20px;height:20px;line-height:20px;font-size:12px;color:#fff}li.inv.good .ic{background:var(--good)}li.inv.warning .ic{background:var(--warning);color:#0b0b0b}li.inv.critical .ic{background:var(--critical)}
li.inv .lab{font-size:12px;color:var(--ink2)}li.inv.critical{border-color:var(--critical)}li.inv.warning{border-color:var(--warning)}
.sparks{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px}.spark .sl{font-size:12.5px;color:var(--ink2);display:flex;gap:6px;align-items:baseline;flex-wrap:wrap}.spark .sx{font-size:10.5px;color:var(--muted)}
.spark svg{display:block;max-width:100%}.spark .line{fill:none;stroke:var(--seq);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}.spark .zero{stroke:var(--axis);stroke-width:1;stroke-dasharray:2 3}.spark .last{fill:var(--seq)}.spark .hit{fill:transparent;cursor:crosshair}.spark .hit:hover{fill:color-mix(in srgb,var(--seq) 25%,transparent)}
.delta{font-size:11.5px;color:var(--muted)}.delta.up{color:var(--up)}.delta.down{color:var(--critical)}
ul.filings{list-style:none;padding:0;margin:0;display:grid;gap:6px}li.filing{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:13px;padding:6px 8px;border:1px solid var(--border);border-radius:6px}li.filing .form{font-weight:700;font-family:ui-monospace,Menlo,monospace}li.filing .fd{color:var(--muted);font-size:12px}li.filing .flags{flex-basis:100%}
.note{background:var(--plane);border-left:3px solid var(--foreign);padding:8px 12px;border-radius:0 6px 6px 0;font-size:14px}.note p{margin:.3em 0}
table.list{width:100%;border-collapse:collapse;font-size:14px}table.list td,table.list th{padding:8px 6px;border-bottom:1px solid var(--grid);text-align:left;vertical-align:top}table.list th{font-size:12px;color:var(--muted);font-weight:600}
footer{margin-top:40px;color:var(--muted);font-size:12px;border-top:1px solid var(--grid);padding-top:10px}
"""

JS = """
document.querySelectorAll('nav.toc a').forEach(a=>a.addEventListener('click',e=>{const t=document.querySelector(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'});history.replaceState(null,'',a.getAttribute('href'));}}));
"""


def page(title, body, sub=""):
    gen = dt.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    return (f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{CSS}</style></head><body><div class="wrap">{body}'
            f'<footer>生成于 {esc(gen)} · 数据：SEC EDGAR (XBRL companyfacts / submissions)、Yahoo Finance 报价、wiki 页面。'
            f'不构成投资建议——这是个人知识库的自动整理。</footer></div><script>{JS}</script></body></html>')


def render_day(brief, ctx):
    d = brief["data"]; date = brief["date"]
    n_src = brief["meta"].get("sources_ingested", "")
    top = (f'<header class="top"><h1>美股机构简报</h1><span class="sub">{esc(fmt_date_cn(date))}</span>'
           f'<span class="sub mono">来源 {esc(n_src)} · 申报 {esc(brief["meta"].get("filings_read", ""))} · 新机会 {esc(brief["meta"].get("opportunities_new", ""))}</span>'
           f'<nav><a href="index.html">总览</a><a class="wl" href="{obsidian(brief["slug"], "wiki/briefs")}">wiki</a></nav></header>')
    toc = ('<nav class="toc"><a href="#macro">宏观</a><a href="#industry">行业</a><a href="#us_equity">美股观点</a>'
           '<a href="#logic">逻辑变化</a><a href="#opps">买入机会</a><a href="#positions">持仓</a></nav>')
    headline = f'<div class="headline">{wikilinks(brief["prose"])}</div>' if brief["prose"] else ""
    body = (top + toc + headline + section_views(ctx, "macro", "宏观", d["macro"]) + section_views(ctx, "industry", "行业", d["industry"])
            + section_views(ctx, "us_equity", "美股观点", d["us_equity"]) + section_logic(ctx, d["logic_changes"])
            + section_opps(ctx, d["opportunities"], date) + section_positions(ctx, d["positions"]))
    return page(f"美股机构简报 {date}", body)


def render_index(ctx):
    briefs = sorted(ctx["briefs"], key=lambda b: b["date"], reverse=True)
    rows = ""
    for b in briefs:
        summary = re.sub(r"[*\[\]]", "", b["prose"]).split("\n")[0][:140]
        counts = " / ".join(esc(b["meta"].get(k, "")) for k in ("sources_ingested", "filings_read", "opportunities_new"))
        rows += (f'<tr><td><a href="{esc(b["date"])}.html">{esc(fmt_date_cn(b["date"]))}</a></td>'
                 f'<td>{esc(summary)}</td><td class="mono">{counts}</td></tr>')
    opps = sorted(ctx["opportunities"].values(), key=lambda o: (str(o["meta"].get("status")), str(o["meta"].get("first_seen"))), reverse=True)
    groups = ""
    for st in ("new", "watching", "adopted", "dropped"):
        items = [o for o in opps if o["meta"].get("status", "new") == st]
        if items:
            groups += f'<h3>{OPP_STATUS[st]} <span class="n">{len(items)}</span></h3><div class="grid">{"".join(opp_card(ctx, o["slug"]) for o in items)}</div>'
    latest = briefs[0] if briefs else None
    pos_section = section_positions(ctx, latest["data"]["positions"] if latest else [])
    inst_rows = "".join(f'<tr><td>{badge(ctx, s)}</td><td>{esc(i["meta"].get("kind", ""))}</td><td><a href="{esc(i["meta"].get("watch_url", ""))}" target="_blank" rel="noopener">{esc(i["meta"].get("watch_url", ""))[:60]}</a></td></tr>'
                        for s, i in sorted(ctx["institutions"].items(), key=lambda kv: (kv[1]["meta"].get("origin", ""), kv[0])))
    latest_link = f'<a href="{esc(latest["date"])}.html">最新一期</a>' if latest else ""
    latest_date = latest["date"] if latest else "—"
    body = (f'<header class="top"><h1>美股机构简报 · 总览</h1><span class="sub">{len(briefs)} 期 · 最新 {esc(latest_date)}</span>'
            f'<nav>{latest_link}</nav></header>'
            '<nav class="toc"><a href="#briefs">每日简报</a><a href="#opps">机会看板</a><a href="#positions">持仓</a><a href="#insts">机构</a></nav>'
            f'<section id="briefs"><h2>每日简报</h2><table class="list"><tr><th>日期</th><th>头条</th><th>来源/申报/新机会</th></tr>{rows or "<tr><td colspan=3 class=empty>还没有简报</td></tr>"}</table></section>'
            f'<section id="opps"><h2>买入机会看板 <span class="n">{len(opps)}</span></h2>{groups or "<p class=empty>还没有记录任何机会。</p>"}</section>'
            + pos_section +
            f'<section id="insts"><h2>跟踪的机构 <span class="n">{len(ctx["institutions"])}</span></h2><table class="list"><tr><th>机构</th><th>类型</th><th>巡查页面</th></tr>{inst_rows}</table></section>')
    return page("美股机构简报 · 总览", body)


# ---------- phone-readable Markdown digest (rendered natively by GitHub on mobile) ----------
WIKI_FOLDERS = ("sources", "institutions", "assets", "positions", "theses", "opportunities", "concepts", "people", "synthesis", "briefs")


def wikilinks_to_text(text):
    """[[slug|alias]] -> alias, [[slug]] -> slug, and drop markdown emphasis. For plain-text contexts
    such as table cells, where a stray | or [ ] would break the rendering."""
    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", lambda m: m.group(2), text)
    t = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1), t)
    return re.sub(r"[*_`]", "", t)


def md_link_target(ctx, slug):
    """Where does this wikilink slug live? Returns a repo-relative path from brief/, or None."""
    # order matters: a bare ticker like [[ceg]] means the ASSET page (positions carry `asset: "[[ceg]]"`),
    # even though wiki/positions/ceg.md shares the basename.
    for key, folder in (("sources", "sources"), ("institutions", "institutions"), ("opportunities", "opportunities"),
                        ("theses", "theses")):
        if slug in ctx.get(key, {}):
            return f"../wiki/{folder}/{slug}.md"
    for folder in WIKI_FOLDERS:  # fall back to a filesystem probe for pages we don't preload
        if (ROOT / "wiki" / folder / f"{slug}.md").exists():
            return f"../wiki/{folder}/{slug}.md"
    return None


def md_links(text, ctx):
    """[[slug|alias]] / [[slug]] -> a tappable relative GitHub link, or plain text if the page is missing."""
    def alias(m):
        slug, label = m.group(1).strip(), m.group(2).strip()
        target = md_link_target(ctx, slug)
        return f"[{label}]({target})" if target else label

    def plain(m):
        slug = m.group(1).strip()
        target = md_link_target(ctx, slug)
        return f"[{slug}]({target})" if target else slug

    t = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", alias, text)
    return re.sub(r"\[\[([^\]]+)\]\]", plain, t)


def md_view(ctx, v, ctx_idx, n):
    src = source_info(ctx, v.get("source", ""))
    url = v.get("url") or src["url"]
    origin = v.get("origin") or inst_origin(ctx, v.get("institution", ""))
    tag = "外资" if origin == "foreign" else "内资"
    name = inst_name(ctx, v.get("institution", ""))
    inst_target = md_link_target(ctx, v.get("institution", ""))
    inst_md = f"[{name}]({inst_target})" if inst_target else name
    chg = " · **△ 观点变化**" if v.get("is_change") else ""
    tickers = (" · " + " ".join(f"`{t}`" for t in v.get("tickers", []) or [])) if v.get("tickers") else ""
    out = [f"**{ctx_idx}. {tag} · {inst_md}**{chg}{tickers}", "", v.get("view", "")]
    quote = (v.get("quote") or "").strip()
    if quote:
        out += ["", "<details><summary>原文</summary>", "", f"> {quote}", "", "</details>"]
    links = []
    src_target = md_link_target(ctx, v.get("source", ""))
    if src_target:
        links.append(f"[wiki: {src['title']}]({src_target})")
    if url:
        links.append(f"[原文 ↗]({url})")
    if links:
        out += ["", " · ".join(links)]
    return "\n".join(out)


def md_section_views(ctx, title, items):
    if not items:
        return f"### {title}\n\n_今日无新增。_\n"
    body = "\n\n".join(md_view(ctx, v, i + 1, len(items)) for i, v in enumerate(items))
    return f"### {title}（{len(items)}）\n\n{body}\n"


def md_opportunity(ctx, slug, today=None):
    o = ctx["opportunities"].get(slug)
    if not o:
        return f"- `{slug}`（缺少页面）"
    m = o["meta"]
    insts = m.get("institutions") or []
    insts = [re.sub(r"[\[\]]", "", i) for i in (insts if isinstance(insts, list) else [insts])]
    names = " · ".join(inst_name(ctx, i) for i in insts)
    st = OPP_STATUS.get(m.get("status", "new"), m.get("status", "new"))
    tk = f"`{m['ticker']}` " if m.get("ticker") else ""
    target = md_link_target(ctx, slug)
    title = m.get("title") or o["title"]
    head = f"#### {tk}[{title}]({target})" if target else f"#### {tk}{title}"
    out = [head, "", f"**逻辑** — {m.get('logic', '')}", "",
           f"状态 **{st}** · 首次出现 {m.get('first_seen', '')} · 出自 {names}"]
    tt = [(k, lab) for k, lab in (("edge", "Edge 我们看到什么"), ("catalyst", "Catalyst 什么会触发重估"), ("invalidation", "Invalidation 什么证明它错了")) if m.get(k)]
    if tt:
        out += ["", "<details><summary>Thesis Test（我起草的提案，未经你采纳）</summary>", ""]
        out += [f"- **{lab}** — {m.get(k)}" for k, lab in tt]
        out += ["", "</details>"]
    return "\n".join(out)


def md_position(ctx, ticker, note=None, brief_filings=None, inv_override=None):
    pos = next((p for p in ctx["positions"].values() if str(p["meta"].get("ticker", "")).upper() == ticker), None)
    meta = pos["meta"] if pos else {}
    sec = ctx["sec"].get(ticker, {})
    q = ctx["prices"].get("quotes", {}).get(ticker, {})
    price = q.get("price")
    shares = float(meta.get("shares") or 0)
    value = price * shares if price else None
    total = sum((ctx["prices"].get("quotes", {}).get(str(p["meta"].get("ticker", "")).upper(), {}).get("price") or 0) * float(p["meta"].get("shares") or 0)
                for p in ctx["positions"].values() if p["meta"].get("status") != "closed")
    acct = float(ctx["config"].get("account_total_usd") or 0) or total
    w_pos = value / total * 100 if value and total else 0
    w_acct = value / acct * 100 if value and acct else 0
    name = sec.get("name") or q.get("name") or ticker
    out = [f"### {ticker} — {name}", ""]
    line = f"**${price:,.2f}**" if price else "价格未知"
    if value:
        line += f" · {shares:g} 股 ≈ **${value:,.0f}** · 账户占比 {w_acct:.0f}% · 持仓占比 {w_pos:.0f}%"
    out += [line, ""]
    if note:
        out += [md_links(note, ctx), ""]

    inv = inv_override or meta.get("invalidation_status") or []
    thesis_slug = re.sub(r"[\[\]]", "", str(meta.get("thesis", "")))
    th = ctx["theses"].get(thesis_slug)
    inv_labels = []
    if th:
        inv_labels = th["meta"].get("invalidations") or []
        if not isinstance(inv_labels, list) or not inv_labels:
            sec_txt = th["body"].split("**The Invalidation**", 1)[-1].split("\n## ", 1)[0]
            inv_labels = [re.sub(r"\s+", " ", x) for x in re.findall(r"^\s*\d\.\s+(.+?)(?=^\s*\d\.|\Z)", sec_txt, re.M | re.S)]
    if inv:
        icons = {"ok": "✅", "watch": "⚠️", "hit": "❌"}
        th_target = md_link_target(ctx, thesis_slug)
        th_md = f"[{th['title'] if th else thesis_slug}]({th_target})" if th_target else (th["title"] if th else thesis_slug)
        out += [f"**失效条件** — {th_md}", ""]
        for i, st in enumerate(inv):
            lab = STATUS.get(st, STATUS["ok"])[1]
            txt = re.sub(r"[*_]", "", inv_labels[i]) if i < len(inv_labels) else f"条件 {i + 1}"
            out.append(f"- {icons.get(st, '✅')} **{lab}** — {txt}")
        out.append("")

    m = sec.get("metrics", {})
    rows = [("营收", "Revenues"), ("净利润", "NetIncomeLoss"), ("经营现金流", "OperatingCashFlow"), ("稀释 EPS", "EPSDiluted")]
    ends = []
    for _, key in rows:
        for x in m.get(key, {}).get("series", []):
            if x["end"] not in ends:
                ends.append(x["end"])
    ends = sorted(ends)[-4:]
    if ends:
        out += ["<details><summary>近 4 季（SEC XBRL）</summary>", "",
                "| 指标 | " + " | ".join(e[:7] for e in ends) + " |",
                "|---|" + "---|" * len(ends)]
        for lab, key in rows:
            series = {x["end"]: x["val"] for x in m.get(key, {}).get("series", [])}
            unit = m.get(key, {}).get("unit")
            cells = [fmt_money(series[e], unit) if e in series else "–" for e in ends]
            out.append(f"| {lab} | " + " | ".join(cells) + " |")
        out += ["", "</details>", ""]

    filings = [f for f in sec.get("filings", []) if f.get("is_new") or (brief_filings and f["accession"] in brief_filings)]
    filings = sorted(filings, key=lambda f: f["filed"], reverse=True)[:8]
    if filings:
        out += [f"**新申报（{len(filings)}）**", ""]
        for f in filings:
            items = " ".join(f"`{i} {ITEM_DESC.get(i, '')}`".strip() for i in f.get("items", []) if i != "9.01")
            flags = " ".join(f"`{x['keyword']}×{x['count']}`" for x in (f.get("flags") or [])[:5])
            out.append(f"- **{f['form']}** {FORM_DESC.get(f['form'], '')} {f['filed']} {items} [EDGAR ↗]({f['url']})"
                       + (f"\n  {flags}" if flags else ""))
        out.append("")
    else:
        out += ["_本期无新申报。_", ""]
    return "\n".join(out)


def render_markdown(brief, ctx):
    """The phone version: GitHub renders this natively in its mobile app, private repo and all."""
    d = brief["data"]
    date = brief["date"]
    meta = brief["meta"]
    out = [f"# 美股机构简报 {date}", "",
           f"_{fmt_date_cn(date)} · 来源 {meta.get('sources_ingested', '')} · 申报 {meta.get('filings_read', '')} · 新机会 {meta.get('opportunities_new', '')}_", ""]
    if brief["prose"]:
        out += [md_links(brief["prose"].strip(), ctx), ""]
    out += ["---", ""]
    out.append(md_section_views(ctx, "宏观", d["macro"]))
    out.append(md_section_views(ctx, "行业", d["industry"]))
    out.append(md_section_views(ctx, "美股观点", d["us_equity"]))

    if d["logic_changes"]:
        out.append(f"### 行业逻辑变化（{len(d['logic_changes'])}）\n")
        for x in d["logic_changes"]:
            out += [f"**{x.get('sector', '')}** — {inst_name(ctx, x.get('institution', ''))}", "",
                    f"- 之前：{x.get('before', '')}", f"- 现在：{x.get('after', '')}", ""]
    else:
        out.append("### 行业逻辑变化\n\n_今日没有记录到行业逻辑的变化。_\n")

    if d["opportunities"]:
        out.append(f"### 买入机会（{len(d['opportunities'])}）\n")
        out += [md_opportunity(ctx, s, date) + "\n" for s in d["opportunities"]]
    else:
        out.append("### 买入机会\n\n_今日没有新的买入机会。_\n")

    out.append("## 我的持仓\n")
    by_t = {str(p.get("ticker", "")).upper(): p for p in d["positions"]}
    for pos in sorted(ctx["positions"].values(), key=lambda p: str(p["meta"].get("ticker"))):
        if pos["meta"].get("status") == "closed":
            continue
        t = str(pos["meta"].get("ticker", "")).upper()
        bp = by_t.get(t, {})
        out.append(md_position(ctx, t, bp.get("note"), set(bp.get("filings") or []), bp.get("invalidation_status")))

    out += ["---", "",
            f"_不构成投资建议 —— 个人知识库的自动整理。网页版：`brief/{date}.html`（下载后用浏览器打开）。_"]
    return "\n".join(out) + "\n"


def update_briefs_readme(ctx, out_dir):
    """Keep a dated index at the top of brief/README.md so the folder itself is the phone entry point."""
    readme = out_dir / "README.md"
    start, end = "<!-- BRIEFS:START -->", "<!-- BRIEFS:END -->"
    rows = ["| 日期 | 头条 |", "|---|---|"]
    for b in sorted(ctx["briefs"], key=lambda b: b["date"], reverse=True):
        summary = wikilinks_to_text(b["prose"]).replace("\n", " ").strip()
        summary = re.sub(r"^\**头条\**[：:]\s*", "", summary)
        summary = summary.replace("|", "/")  # a raw pipe would break the table row
        summary = re.sub(r"\s+", " ", summary)[:110]
        rows.append(f"| [{b['date']}]({b['date']}.md) | {summary} |")
    block = start + "\n\n## 每日简报（手机版）\n\n手机上直接点日期即可阅读；网页版是同名 `.html`。\n\n" + "\n".join(rows) + "\n\n" + end
    text = readme.read_text(encoding="utf-8") if readme.exists() else "# brief/\n"
    if start in text and end in text:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), lambda _: block, text, flags=re.S)
    else:
        text = text.rstrip("\n") + "\n\n" + block + "\n"
    readme.write_text(text, encoding="utf-8")
    return readme


def write_pages_redirects(ctx, out_dir):
    """Cloudflare Pages _redirects, regenerated each run so /latest always points at the newest
    brief. Bookmark <site>/latest once on the phone and it stays current."""
    briefs = sorted(ctx["briefs"], key=lambda b: b["date"], reverse=True)
    if not briefs:
        return None
    newest = briefs[0]["date"]
    lines = ["# generated by scripts/render_brief.py — do not hand-edit",
             f"/latest /{newest}.html 302",
             f"/latest.md /{newest}.md 302"]
    dest = out_dir / "_redirects"
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return dest


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    ap.add_argument("--out", default=str(ROOT / "brief"))
    a = ap.parse_args(argv)
    ctx = build_ctx()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    briefs = ctx["briefs"]
    if a.date:
        briefs = [b for b in briefs if b["date"] == a.date]
        if not briefs:
            print(f"no brief for {a.date} in wiki/briefs"); return 1
    for b in briefs:
        (out / f"{b['date']}.html").write_text(render_day(b, ctx), encoding="utf-8")
        print("wrote", out / f"{b['date']}.html")
        (out / f"{b['date']}.md").write_text(render_markdown(b, ctx), encoding="utf-8")
        print("wrote", out / f"{b['date']}.md")
    (out / "index.html").write_text(render_index(ctx), encoding="utf-8")
    print("wrote", out / "index.html")
    print("wrote", update_briefs_readme(ctx, out))
    red = write_pages_redirects(ctx, out)
    if red:
        print("wrote", red)
    return 0


if __name__ == "__main__":
    sys.exit(main())
