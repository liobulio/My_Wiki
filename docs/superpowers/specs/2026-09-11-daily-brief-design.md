# Daily US-Equity Institutional Brief + SEC Position Monitor — Design

Date: 2026-09-11 · Status: approved by human (chat), implementation started same day.

## Goal

Every weekday before the US open, produce a single-file HTML brief that shows (a) what
foreign and domestic institutions said about macro / industry / US equities since the last
brief, (b) where industry logic changed, (c) new buy opportunities with the one-line logic and
the institution it came from, and (d) the state of the human's real positions (CEG, TLN, VST)
against fresh SEC filings, with regulatory-restricted contracts (FERC / NRC / export control)
called out. Everything compounds inside the existing Obsidian wiki; the HTML is a rendered view.

## Decisions (from the brainstorm)

| Question | Decision |
|---|---|
| Where research comes from | Public web pages of institutions (foreign: Goldman Insights, Morgan Stanley Ideas, JPM Insights, BlackRock BII, Apollo Slok Daily Spark, Bridgewater, PIMCO, KKR; domestic: 东方财富研报中心 海外策略/美股行业 PDFs, and any reachable 中金/华泰/中信 pages) plus files the human drops into `raw/`. Public news is a lead, not the end: chase leads into SEC filings. |
| Who analyses | The LLM agent (Claude) inside Claude Code, following `CLAUDE.md` + a `/daily-brief` skill. A pure-Python script renders HTML from wiki frontmatter. No Anthropic API key in scripts. |
| SEC scope | Recent 10-K/10-Q/8-K/Form 4 list with links; XBRL core metrics for 8 quarters; new 8-K full text pulled and keyword-flagged; flagged filings read and interpreted by the agent; **regulatory-restricted contracts** (FERC rejections of co-location / uprate / PPA agreements, NRC, export controls) are the priority. 13F is phase 2. |
| Output | One file per day `brief/YYYY-MM-DD.html` + `brief/index.html` (date list, cumulative opportunities board, positions board). Single-file, inline CSS/JS, no external resources. Chinese UI, quotes and tickers kept in English. |
| Trigger | Cloud routine, weekdays 11:00 UTC (07:00 America/Toronto). Model `claude-opus-5`. Repo: private GitHub `liobulio/My_Wiki`. Routine commits + pushes; human pulls locally (Obsidian Git plugin or `git pull`). Today's initial build is done by Claude Fable 5.1 interactively. |
| Positions | CEG 5.891 sh, TLN 5.407 sh, VST 11.523 sh at IBKR, total ≈ $7,200. `shares` is human-owned; `weight` computed from price at render time. |
| Ignored | `statarb-strategy-lab/` is git-ignored and out of scope. |

### Thesis Test (human's own words, parsed)

Shared thesis page `theses/ai-power-ipp-bull.md`, linked from all three positions.

- **Edge** — All three are heavy-asset, nuclear-heavy IPPs; rebuilding takes 7–10 years. Buy
  below replacement cost while power demand rises; after contracting, remaining dispatchable
  power is still abundant.
- **Catalyst** — New power contracts with hyperscalers (AWS, Microsoft).
- **Invalidation** (condition-based, no price stop; any one triggers a review):
  1. Hyperscaler power contracts delayed or cancelled.
  2. Nuclear uprate / co-location agreements restricted by regulators (FERC etc.).
  3. Solar capacity expansion faster than expected.
  4. Solar plant rebuild cost falling.

## Wiki schema additions (CLAUDE.md §2/§3 extended)

| Folder | Page | Frontmatter |
|---|---|---|
| `wiki/institutions/` | one per institution | `type: institution`, `origin: foreign \| domestic`, `kind: sell-side \| buy-side \| media \| regulator`, `aliases`, `tags`, `created`, `updated` |
| `wiki/sources/` | existing, extended | `institution: "[[slug]]"`, `scope: [macro, industry, equity]`, `source_type` gains `filing` and `research` |
| `wiki/opportunities/` | one per buy idea, cumulative | `type: opportunity`, `ticker`, `first_seen`, `logic` (one line), `institutions: []`, `sources: []`, `status: new \| watching \| adopted \| dropped`, `updated` |
| `wiki/briefs/` | one per day, HTML data source | `type: brief`, `date`, `macro: []`, `industry: []`, `us_equity: []`, `logic_changes: []`, `opportunities: []`, `positions: []`, each view item = `{institution, origin, view, quote, source, is_change}` |
| `wiki/positions/` | existing, extended | `shares`, `account`, `invalidation_status: [ok\|watch\|hit ×4]` |

Institutions are pages (not just strings) so each accumulates a track record.

## Components

```
brief/sources.yaml          watchlist of public pages to sweep (human-editable)
scripts/sec_fetch.py        EDGAR: submissions, companyfacts, 8-K text + keyword flags → data/sec/<TICKER>.json
scripts/prices.py           quotes for weight calc → data/prices.json
scripts/render_brief.py     wiki frontmatter + data/ → brief/YYYY-MM-DD.html, brief/index.html
.claude/skills/daily-brief/SKILL.md   the daily procedure (used by cloud routine and locally)
```

### `sec_fetch.py`
- Input: tickers from `wiki/positions/*.md` frontmatter (status != closed).
- EDGAR endpoints (User-Agent with the human's email): `company_tickers.json` (CIK lookup),
  `submissions/CIK##########.json` (recent filings), `api/xbrl/companyfacts/CIK##########.json`
  (Revenues, NetIncomeLoss, EPS diluted, OperatingIncomeLoss, NetCashProvidedByOperatingActivities,
  PaymentsToAcquirePropertyPlantAndEquipment, LongTermDebt, CashAndCashEquivalents; last 8 quarterly
  values via 10-Q/10-K `frame`-deduplicated), 8-K primary document HTML → plain text.
- Flags: item codes (1.01, 1.02, 2.02, 7.01, 8.01) + keyword hits (FERC, NRC, PJM, ISO, ERCOT,
  co-locat, interconnect, uprate, PPA, power purchase, behind-the-meter, export control, sanction,
  denied, rejected, protest, order, complaint). Output `flags[]` per filing with snippet context.
- Idempotent: caches per ticker; `--since YYYY-MM-DD` marks `is_new`.
- Rate limit ≤ 10 req/s, retries with backoff; never crashes the brief on one ticker failing (records `error`).

### `render_brief.py`
- Pure stdlib + PyYAML. Parses frontmatter of briefs / opportunities / positions / institutions / theses.
- Builds day page: header (date, counts), section tabs 宏观 / 行业 / 美股观点 / 逻辑变化 / 买入机会 / 持仓.
  Each view row: institution badge (foreign = one hue, domestic = another), view text, expandable
  original quote + source link (wiki page name; also URL if present in source frontmatter).
- Positions cards: weight (shares × price / total), 8-quarter sparkline (inline SVG) for revenue /
  net income / operating cash flow, new filings list with flag chips, invalidation checklist (4 rows, ok/watch/hit).
- Index page: date list, opportunities board (grouped by status, showing logic + institutions + first_seen),
  positions board (latest), all inline.
- Output must be self-contained; no CDN, no fonts, no images except inline SVG. Light/dark via `prefers-color-scheme`.

### `/daily-brief` skill (procedure, executed by the agent)
1. `git pull`; read `CLAUDE.md`, `brief/sources.yaml`, last brief date from `wiki/briefs/`.
2. Sweep sources: fetch each watchlist page, detect items newer than last brief, save to `raw/`, ingest
   per CLAUDE.md §4.1 (fact-check included) → source pages, institution pages, asset/concept pages.
3. Also ingest any new files in `raw/` not yet referenced by a source page.
4. Run `scripts/sec_fetch.py --since <last brief date>`; read every flagged / new 8-K; write `filing`
   source pages; update position pages (update history + invalidation_status) and thesis status.
5. Chase leads: for any institution/news item touching a position, run EDGAR full-text search and
   read the filing rather than the news.
6. Write `wiki/briefs/YYYY-MM-DD.md`; create/update `wiki/opportunities/` pages.
7. Run `scripts/prices.py` then `scripts/render_brief.py`.
8. Update `index.md`, append `log.md` entry (`brief` operation type), commit, push.

## Cloud routine
- Name: `daily-us-brief`; cron `0 11 * * 1-5` (UTC) ; model `claude-opus-5`; env Default; source
  `https://github.com/liobulio/My_Wiki`; tools Bash/Read/Write/Edit/Glob/Grep/WebFetch/WebSearch.
- Prompt: self-contained pointer to `CLAUDE.md` and the skill file; commit + push to `main`.
- Risk: sandbox egress may block some hosts. First run validates; fallback is a local `launchd` job running the same skill.

## Phasing
- Phase 1 (now): everything above, validated by one full local run producing today's HTML.
- Phase 2: 13F holder changes (SEC quarterly structured dataset, run quarterly), Form 4 insider summary, price history charts.

## Out of scope
- No trading, no position-number changes without the human's confirmation (CLAUDE.md §3.5).
- No paywalled sources; no scraping behind logins.
