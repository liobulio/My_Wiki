# Daily Institutional Brief + SEC Monitor — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A weekday cloud routine that sweeps public institutional research, monitors CEG/TLN/VST SEC filings, writes everything into the Obsidian wiki, and renders a single-file Chinese HTML brief per day plus an index page.

**Architecture:** The LLM agent does all reading/analysis and writes structured wiki pages (frontmatter = data). Two stdlib-ish Python scripts fetch deterministic data (EDGAR, quotes) into `data/`. One Python renderer turns wiki frontmatter + `data/` into `brief/*.html`. A repo-resident skill file is the procedure both the cloud routine and a local run follow.

**Tech Stack:** Python 3.11+ (stdlib + PyYAML), SEC EDGAR JSON APIs, Yahoo/Stooq quotes, Claude Code cloud routine (`claude-opus-5`), private GitHub repo `liobulio/My_Wiki`.

**Spec:** `docs/superpowers/specs/2026-09-11-daily-brief-design.md`

## Global Constraints
- Never edit `raw/`; never invent position numbers (CLAUDE.md §3.5). `shares` are human-owned: CEG 5.891, TLN 5.407, VST 11.523.
- HTML output is self-contained: inline CSS/JS/SVG only, no CDN, no fonts, no images.
- Chinese UI; institution quotes, tickers, numbers stay in original language.
- `statarb-strategy-lab/` is git-ignored and untouched.
- EDGAR requests carry `User-Agent: My_Wiki hengkun.zhang@mail.mcgill.ca`, ≤ 10 req/s.
- Scripts must not abort the whole brief on one ticker/source failure — record `error` and continue.
- Only PyYAML may be added as a dependency (`pip install pyyaml`); everything else stdlib.

---

### Task 1: Repo hygiene + private GitHub remote
**Files:** Modify `.gitignore` (done), commit pending wiki pages; create `liobulio/My_Wiki` (private) and push.
- [ ] `git add -A && git commit -m "Commit pending statarb wiki pages (BZ/CL, screens, failure modes)"`
- [ ] `gh repo create liobulio/My_Wiki --private --source=. --remote=origin --push`
- [ ] Verify: `git remote -v` shows origin; `gh repo view liobulio/My_Wiki --json visibility` → PRIVATE.

### Task 2: Schema extension in CLAUDE.md
**Files:** Modify `CLAUDE.md` §2 tree, §3 (add 3.9 institution, 3.10 opportunity, 3.11 brief; extend 3.1 with `institution`/`scope`/`filing`; extend 3.5 with `shares`/`account`/`invalidation_status`), §4 (add 4.4 BRIEF), §6 (log op `brief`).
- [ ] Edit sections as listed; keep existing wording elsewhere.
- [ ] Commit `Schema: institutions, opportunities, briefs, filing sources, BRIEF operation`.

### Task 3: Positions, shared thesis, assets
**Files:** Create `wiki/theses/ai-power-ipp-bull.md`, `wiki/positions/{ceg,tln,vst}.md`, `wiki/assets/{ceg,vst}.md`; modify `wiki/assets/tln.md`, `index.md`, `log.md`.
**Interfaces (produced):** position frontmatter keys read by scripts: `ticker`, `status`, `shares`, `account`, `thesis`, `invalidation_status` (list of 4 × `ok|watch|hit`).
- [ ] Write thesis page with the human's Thesis Test verbatim (Edge/Catalyst/4 Invalidations), `stance: bullish`, `status: active`, `conviction` left as `3` with a note it is the human's to set.
- [ ] Write 3 position pages (`status: open`, `weight:` empty — computed; `entry_price` empty; `conviction: 3` flagged for human confirmation).
- [ ] Commit `Positions: CEG/TLN/VST + shared AI-power IPP thesis`.

### Task 4: `scripts/prices.py`
**Files:** Create `scripts/prices.py`, `tests/test_prices.py`.
**Interfaces:** `fetch_quote(ticker) -> dict(price: float, currency: str, asof: str, source: str)`; CLI `python scripts/prices.py CEG TLN VST` writes `data/prices.json` `{ "CEG": {...}, ... , "asof": iso }`. Yahoo chart API first, Stooq CSV fallback.
- [ ] Test: `parse_stooq_csv("Symbol,Date,Time,Open,High,Low,Close,Volume\nCEG.US,2026-09-10,22:00:00,1,2,3,250.5,1")` → 250.5.
- [ ] Implement; run live; commit.

### Task 5: `scripts/sec_fetch.py`
**Files:** Create `scripts/sec_fetch.py`, `tests/test_sec_fetch.py`, `tests/fixtures/companyfacts_min.json`.
**Interfaces:**
```python
KEYWORDS = ["FERC","NRC","PJM","ERCOT","ISO-NE","MISO","co-locat","colocat","interconnect","uprate","PPA","power purchase","behind-the-meter","export control","sanction","denied","rejected","reject","protest","complaint","order"]
def flag_text(text: str) -> list[dict]      # [{"keyword":..., "snippet":...}] snippet = ±160 chars
def quarterly_series(facts: dict, tag: str, n: int = 8) -> list[dict]   # [{"end":"2026-06-30","val":..,"form":"10-Q","fy":..,"fp":..}]
def load_positions(wiki_dir) -> list[str]   # tickers where status != closed
# CLI: python scripts/sec_fetch.py --since 2026-09-01 [--tickers CEG TLN VST] → data/sec/<TICKER>.json
```
Output JSON shape per ticker: `{ticker, cik, name, fetched, filings:[{form, filed, accession, url, primary_doc, items:[..], is_new, flags:[..], error?}], metrics:{Revenues:[..], NetIncomeLoss:[..], ...}, error?}`.
XBRL tags (try in order per metric): Revenues: `Revenues`,`RevenueFromContractWithCustomerExcludingAssessedTax`; NetIncome: `NetIncomeLoss`; EPS: `EarningsPerShareDiluted`; OpIncome: `OperatingIncomeLoss`; OCF: `NetCashProvidedByUsedInOperatingActivities`; Capex: `PaymentsToAcquirePropertyPlantAndEquipment`; Debt: `LongTermDebtNoncurrent`,`LongTermDebt`; Cash: `CashAndCashEquivalentsAtCarryingValue`.
Quarterly dedupe rule: keep entries with `fp` in Q1..Q3 from 10-Q and derive Q4 from 10-K FY minus sum of Q1–Q3 when the FY value exists (mark `derived: true`); dedupe on `end`, prefer latest `filed`.
- [ ] Tests: `flag_text("...the FERC rejected the amended ISA...")` returns FERC + rejected hits; `quarterly_series` on fixture returns 8 sorted entries with derived Q4.
- [ ] Implement with `urllib`, 0.12 s sleep between requests, 3 retries; HTML→text via `html.parser` subclass.
- [ ] Run live for CEG TLN VST with `--since 2026-08-01`; inspect flags; commit.

### Task 6: Watchlist + institution pages
**Files:** Create `brief/sources.yaml`, `wiki/institutions/*.md` (goldman-sachs, morgan-stanley, jpmorgan, blackrock, apollo, bridgewater, pimco, kkr, cicc 中金, huatai 华泰, citic-securities 中信, eastmoney-research-center 东方财富研报中心), update `index.md`.
`sources.yaml` entry shape: `- id, institution: <slug>, origin: foreign|domestic, url, kind: html|rss|json, note`.
- [ ] Write yaml; write stub institution pages (Who / Views / Track record / Sources); commit.

### Task 7: `scripts/render_brief.py`
**Files:** Create `scripts/render_brief.py`, `tests/test_render_brief.py`, `tests/fixtures/brief_min.md`.
**Interfaces:** `load_frontmatter(path) -> (meta: dict, body: str)`; `render_day(brief_meta, ctx) -> str`; `render_index(ctx) -> str`; CLI `python scripts/render_brief.py [--date YYYY-MM-DD]` writes `brief/<date>.html` and `brief/index.html`. `ctx = {positions, theses, opportunities, institutions, sec, prices, briefs}`.
Brief frontmatter consumed (from CLAUDE.md §3.11): `macro/industry/us_equity: [{institution, origin, view, quote, source, url, is_change}]`, `logic_changes: [{sector, before, after, institution, source}]`, `opportunities: [<opportunity-slug>]`, `positions: [{ticker, note, filings:[accession], invalidation_status:[..]}]`.
- [ ] Load `dataviz` skill before writing sparkline/palette code.
- [ ] Test: render fixture → HTML contains institution badge with `data-origin="foreign"`, contains a `<svg` sparkline, contains no `http` in `<script src`/`<link`.
- [ ] Implement; run on a fixture; open in browser pane to eyeball; commit.

### Task 8: `/daily-brief` skill
**Files:** Create `.claude/skills/daily-brief/SKILL.md` (procedure from spec, step-by-step, with exact commands), `brief/README.md` (how to open, how to pull).
- [ ] Write; commit.

### Task 9: First full run (today, interactive)
- [ ] Sweep `brief/sources.yaml` for items published ≤ 7 days; save to `raw/`, ingest per CLAUDE.md (fact-check).
- [ ] Run `sec_fetch.py --since 2026-08-15`; read flagged 8-Ks; write filing source pages; update positions.
- [ ] Write `wiki/briefs/2026-09-11.md`, opportunities pages; run prices + renderer; update `index.md`, `log.md`; commit; push.
- [ ] Show the HTML to the human.

### Task 10: Cloud routine
- [ ] `RemoteTrigger create`: name `daily-us-brief`, cron `0 11 * * 1-5`, model `claude-opus-5`, env `env_01CnzCNjN1MAp86pNZhK1j5p`, repo `https://github.com/liobulio/My_Wiki`, tools Bash/Read/Write/Edit/Glob/Grep/WebFetch/WebSearch, prompt pointing at CLAUDE.md + skill.
- [ ] Trigger one run, read `get_run_log`, confirm egress to sec.gov and institution sites works; note fallback if not.
