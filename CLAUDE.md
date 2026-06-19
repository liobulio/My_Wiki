# CLAUDE.md — Investment Wiki Schema & Operating Manual

This file is the **schema**. It tells you (the LLM agent) how this wiki is structured,
what the conventions are, and what workflows to follow. Read it at the start of every
session. **Every interaction follows this schema.** When you and the human discover a
better convention, update *this file* — it is the living spec for the wiki.

---

## 0. What this is

A **personal investment wiki**, maintained entirely by you (the LLM), browsed by the
human in Obsidian. The human curates sources, directs analysis, and asks questions.
You do all the bookkeeping: reading, summarizing, cross-referencing, filing, and keeping
everything consistent.

Domain tilt: **investing / quant**. Sources are podcasts, YouTube videos & transcripts,
articles, papers, and research notes. The wiki builds a structured picture of the human's
**real investment portfolio** — positions, theses, the assets behind them, the people whose
views inform them, and the concepts/strategies in play.

The wiki is a **persistent, compounding artifact**. Knowledge is compiled once on ingest
and then kept current — never re-derived from scratch on every question. Cross-references
are already there; contradictions are already flagged; the synthesis already reflects
everything read.

---

## 1. Three layers

1. **Raw sources** (`raw/`) — immutable source documents. You **read** from them, you
   **never edit** them. This is the source of truth. Charts/images live in
   `raw/_attachments/`.
2. **The wiki** (`wiki/`) — markdown files you generate and own entirely. You create pages,
   update them as new sources arrive, maintain cross-references, keep them consistent.
3. **The schema** (this `CLAUDE.md`) — how you operate. Co-evolved over time.

Plus two navigation files at the root: **`index.md`** (content catalog) and **`log.md`**
(chronological activity log).

---

## 2. Folder conventions

```
CLAUDE.md            # this schema
index.md             # content catalog — what exists, by category
log.md               # append-only chronological activity log
raw/                 # immutable sources — read only, never edit
  _attachments/      # local copies of charts / images / screenshots
  <source files>     # transcripts, clipped articles (.md / .txt)
wiki/
  sources/           # one summary page per ingested source
  assets/            # instruments: tickers, ETFs, crypto, indices, commodities
  people/            # investors, fund managers, hosts, authors, analysts
  concepts/          # strategies, factors, metrics, models, terms
  positions/         # REAL holdings — structured frontmatter (Dataview source)
  theses/            # investment theses — the "why" behind positions/watchlist
  synthesis/         # overview.md dashboard + cross-cutting analyses, comparisons
```

### Naming
- **Files:** kebab-case, `.md`. Assets are keyed by ticker where one exists:
  `assets/aapl.md`, `assets/mtum.md`. People: `people/cliff-asness.md`. Concepts:
  `concepts/momentum-factor.md`. Sources: `sources/YYYY-MM-DD-short-slug.md`
  (date = when the source was published/recorded, fall back to ingest date).
- **Positions:** `positions/<ticker>.md` (one per open/watch holding).
- **Theses:** `theses/<ticker>-<stance>.md`, e.g. `theses/mtum-bull.md`.
- **Links:** always use Obsidian wikilinks `[[page-name]]` (or `[[page-name|alias]]`).
  Use the file basename without `.md`.

---

## 3. Page formats

Every wiki page starts with YAML frontmatter (Dataview + graph depend on it), then a body.
Use `[[wikilinks]]` everywhere a page references an entity. Convert relative dates to
absolute `YYYY-MM-DD`. Cite every non-obvious claim with the `[[source-page]]` it came from.

### 3.1 Source page — `wiki/sources/`
```yaml
---
type: source
source_type: podcast | youtube | article | transcript | paper
title: "<title>"
author: "[[<person-or-host>]]"
publisher: "<show / site / channel>"
url: <url or empty>
published: YYYY-MM-DD
ingested: YYYY-MM-DD
raw: "[[raw/<file>]]"        # link to the immutable raw file
tags: [quant, macro, ...]
---
```
Body sections:
- **TL;DR** — 2–4 sentences.
- **Key takeaways** — bullets; include timestamps `[12:30]` if the source has them.
- **Notable claims** — specific, checkable assertions (sourced quotes/numbers).
- **Entities mentioned** — `[[links]]` to assets / people / concepts.
- **Agrees / contradicts** — how this lines up with existing wiki claims. Flag conflicts
  explicitly: `⚠️ Contradicts [[other-source]]: ...`.
- **Charts** — embed `![[raw/_attachments/<img>]]` with a one-line read of each.

### 3.2 Asset page — `wiki/assets/`
```yaml
---
type: asset
ticker: <TICKER>
asset_class: equity | etf | crypto | bond | index | commodity | fx
aliases: [<other names>]
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```
Body: **What it is** · **Current view** (the evolving synthesis) · **Key data points** ·
**Related** `[[people]]` / `[[concepts]]` · **Position & thesis** links · **Sources**.

### 3.3 Person page — `wiki/people/`
```yaml
---
type: person
role: investor | manager | host | author | analyst
affiliation: "<firm / show>"
aliases: []
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```
Body: **Who** · **Views & style** · **Notable calls** (with outcomes if known) ·
**Sources**.

### 3.4 Concept page — `wiki/concepts/`
```yaml
---
type: concept
category: strategy | factor | metric | model | term
aliases: []
tags: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```
Body: **Definition** · **How it works** · **Pros / cons** · **Who uses it** ·
**Related** `[[concepts]]` · **Sources**.

### 3.5 Position page — `wiki/positions/` (the structured one)
```yaml
---
type: position
asset: "[[<ticker>]]"
ticker: <TICKER>
status: open | watch | closed
weight: <pct of portfolio, number>
entry_date: YYYY-MM-DD
entry_price: <number or empty>
conviction: <1-5>
thesis: "[[<ticker>-<stance>]]"
opened: YYYY-MM-DD
updated: YYYY-MM-DD
---
```
Body: **Summary** · **Conviction rationale** · **Catalysts** · **Risks** ·
**What would change my mind** (falsifiers) · **Sources** · **Update history** (dated
bullets — append, don't overwrite).

> Positions are the human's real book. Never invent or alter position numbers — only the
> human supplies weights/prices/conviction. If a source implies a change, propose it and
> wait for confirmation before editing frontmatter.

### 3.6 Thesis page — `wiki/theses/`
```yaml
---
type: thesis
asset: "[[<ticker>]]"
stance: bullish | bearish | neutral
conviction: <1-5>
status: active | playing-out | invalidated
opened: YYYY-MM-DD
updated: YYYY-MM-DD
---
```
Body: **Thesis** (one paragraph) · **Supporting evidence** (each bullet sourced) ·
**Risks / counter-thesis** · **Falsifiers** (what would invalidate it) · **Sources**.

### 3.7 Synthesis pages — `wiki/synthesis/`
`overview.md` is the portfolio dashboard (see §5). Other synthesis pages are cross-cutting
analyses, comparisons, and answers worth keeping (see Query, §4.2).

---

## 4. The three operations

### 4.1 INGEST — add a source to the wiki
Trigger: human drops/pastes/links a source and says to process it.

Source can arrive 4 ways — get it into `raw/` first:
1. **Pasted text** → save to `raw/<YYYY-MM-DD-slug>.md` (add a header line with title/source).
2. **File already in `raw/`** → just read it.
3. **URL** → fetch it (WebFetch), convert to markdown, save to `raw/<YYYY-MM-DD-slug>.md`.
   (You cannot pull YouTube/podcast audio — the human supplies a transcript for those.)
4. **Charts/images** → save to `raw/_attachments/`, and **view them** (read tool on the
   image) before writing — LLMs can't read inline images in one pass with the text.

Then run the ingest flow:
1. **Read** the raw source fully. View any charts.
2. **Discuss** key takeaways with the human (briefly) — let them steer emphasis.
3. **Write the source page** in `wiki/sources/` (§3.1).
4. **Create/update entity pages** the source touches — `assets/`, `people/`, `concepts/`.
   Create **stub pages** for important entities mentioned but not yet documented, and link
   them (a `[[link]]` to a not-yet-created page is fine and marks a TODO).
5. **Update positions & theses** if the source bears on them — but per §3.5, *propose*
   position-number changes; don't edit them unilaterally.
6. **Flag contradictions** — when the source conflicts with an existing claim, note it on
   both the source page and the affected entity page with `⚠️`.
7. **Update `index.md`** — add new pages to the right category with one-line summaries;
   refresh summaries that changed.
8. **Append to `log.md`** — one entry (§6).

A single ingest typically touches **10–15 pages**. That's expected — the value is in the
bookkeeping.

### 4.2 QUERY — answer a question against the wiki
1. **Read `index.md` first** to find candidate pages. Use search (grep / qmd if installed)
   to widen.
2. **Drill into** the relevant pages and read them.
3. **Answer** with `[[links]]` and citations to source pages. Be concrete; surface
   contradictions and uncertainty rather than smoothing them over.
4. **Offer to file it back** — good answers (a comparison, an analysis, a discovered
   connection) should become a `wiki/synthesis/` page so explorations compound. If filed,
   update `index.md` and `log.md`.

Answers can take other forms when useful: a comparison table, a Marp slide deck, a
matplotlib chart (save image to `raw/_attachments/` or a `synthesis/` asset folder).

### 4.3 LINT — health-check the wiki
On request, scan for and report (with suggested fixes):
- **Contradictions** between pages.
- **Stale claims** newer sources have superseded.
- **Orphan pages** with no inbound links.
- **Missing entity pages** — important things mentioned but lacking a page (the `[[link]]`
  TODOs).
- **Missing cross-references** — pages that should link but don't.
- **Data gaps** — facts worth a web search to fill.
- **Next questions / sources** to investigate.
Then append a `lint` entry to `log.md` summarizing what was found.

---

## 5. The portfolio dashboard

`wiki/synthesis/overview.md` is the live dashboard. It uses Dataview over `wiki/positions`.
Keep these queries working (requires the Dataview plugin enabled in Obsidian):

```dataview
TABLE ticker, weight + "%" AS Weight, conviction AS Conv, status, thesis
FROM "wiki/positions"
WHERE status != "closed"
SORT weight DESC
```

When positions change, the table updates automatically — you don't hand-maintain it.

---

## 6. index.md and log.md

### index.md (content-oriented catalog)
Organized by category: **Sources · Assets · People · Concepts · Positions · Theses ·
Synthesis**. Each entry: `- [[page]] — one-line summary`. Update on every ingest and
whenever you file a synthesis page. This is your first stop on a query.

### log.md (chronological, append-only)
One entry per operation, newest at the bottom. **Consistent grep-able prefix** so
`grep "^## \[" log.md | tail -5` shows recent activity:

```
## [YYYY-MM-DD] ingest | <Source Title>
- pages touched: [[a]], [[b]], [[c]]
- note: <one line — key takeaway or contradiction flagged>
```

Operation types: `ingest`, `query`, `lint`, `maintenance`. Never rewrite past entries.

---

## 7. Working principles

- **You write the wiki; the human writes the sources.** Never ask the human to do
  bookkeeping.
- **Link liberally.** A `[[link]]` to a page that doesn't exist yet is a feature — it marks
  the next page to write.
- **Cite everything non-obvious.** Trace claims back to `[[source]]` pages.
- **Flag, don't smooth.** Surface contradictions and stale claims; don't quietly overwrite.
- **Positions are real.** Treat `positions/` frontmatter as the human's actual book —
  propose changes, get confirmation, never invent numbers. Nothing here is financial advice;
  it's the human's own record of their own decisions.
- **Append, don't destroy.** Update-history sections and `log.md` are append-only.
- **Keep it consistent.** Same source referenced the same way everywhere; one entity = one
  page (use `aliases` for alternates).
- **Co-evolve the schema.** When a convention isn't working, update this file and note it in
  `log.md` as a `maintenance` entry.
```
