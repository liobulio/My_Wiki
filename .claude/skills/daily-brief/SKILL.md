---
name: daily-brief
description: Produce today's US-equity institutional brief — sweep the public research watchlist and new raw/ files, ingest them into the wiki, read new SEC filings for the open positions (regulator-restricted contracts first), write wiki/briefs/<date>.md + opportunities, render brief/<date>.html + index.html, update index.md/log.md, commit and push. Use when the user says "出今天的简报" / "daily brief" or when run by the daily-us-brief cloud routine.
---

# /daily-brief — the daily procedure (CLAUDE.md §4.4)

You are the maintainer of this investment wiki. Read `CLAUDE.md` first — every page you write
must follow its schema. Today's date is the run date (`date +%F`). Language: Chinese for
梳理/views/logic, keep quotes, tickers and numbers in the original language.

## 0. Setup
```bash
git pull --rebase origin main 2>/dev/null || true
LAST=$(ls wiki/briefs/*.md 2>/dev/null | sort | tail -1 | xargs -n1 basename 2>/dev/null | sed 's/.md//')
echo "last brief: ${LAST:-none}"
```
`SINCE` = the last brief date (exclusive) — or, if none, today minus `lookback_days` from
`brief/config.yaml`. Read `brief/sources.yaml` and `brief/config.yaml`.

## 1. Sweep institutions (foreign + domestic)
For every entry in `brief/sources.yaml`:
- `kind: rss` → fetch the feed; take items with pubDate > SINCE; fetch each item page.
- `kind: html` → fetch the page; find pieces dated > SINCE (links + dates); fetch each.
- `kind: js` → WebSearch `"<search_hint>"` with a past-week filter (and the institution name +
  "outlook" / "equity strategy" / "macro"); open the top dated hits.
- `kind: json` (东方财富) → substitute `{since}`/`{today}` in `url`, fetch JSON, keep rows whose
  `title` matches any `filter` regex; download the PDF via `pdf_url` with `{infoCode}`; extract
  text (`pdftotext` if available, else `python3 -c "import pypdf"` fallback, else read the PDF
  with the Read tool; copy the extracted text into `raw/` with a header line). Attribute the view to the broker (`orgSName`) — create
  `wiki/institutions/<broker-slug>.md` (origin: domestic) if missing. 东方财富 is the channel.
- Also: any file in `raw/` with no `wiki/sources/` page referencing it → treat as a new source.
Skip anything already ingested (grep `wiki/sources/` for the URL / infoCode). Budget: at most
~12 new sources per run — prefer (a) anything touching the open positions or their sector,
(b) a house changing its stance, (c) explicit buy ideas, (d) macro/US-equity strategy notes.
Pure A-share market recaps, 晨报 digests and ESG notes are out of scope.

## 2. INGEST each kept source (CLAUDE.md §4.1 — fact-check is mandatory)
Save the text to `raw/<YYYY-MM-DD-slug>.md` (header line: title · institution · URL), then
write `wiki/sources/<YYYY-MM-DD-slug>.md` with `source_type: research`, `institution:
"[[slug]]"`, `scope: [...]`. Update the institution page's **House view (current)** (dated
bullet, newest first) and note ⚠️ when the stance differs from its previous bullet. Update
asset/concept pages the source bears on. Fact-check hard claims with WebSearch; put verdicts
on the source page.

## 3. SEC filings for the open positions
```bash
python3 scripts/sec_fetch.py --since "$SINCE"
```
Then for every filing marked `is_new` in `data/sec/<TICKER>.json`:
- 8-K with items 1.01 / 1.02 / 2.03 / 8.01, or any filing whose `flags` include FERC / NRC /
  PUC / co-locat / interconnect / uprate / PPA / export control / denied / rejected / protest /
  terminat / cancel → **read the text** at `text_path` (Read tool) in full.
- 8-K 2.02 (earnings) and 10-Q/10-K → read the press-release exhibit and the MD&A / Liquidity /
  Regulatory sections; look for contract, PPA, uprate, co-location, capacity-market language.
- Form 4 → just list (phase 2 will summarise insiders).
Write one `wiki/sources/<filed-date>-<ticker>-<form>.md` per filing you read
(`source_type: filing`, `institution: "[[<ticker>]]"` is NOT used — use `publisher: "SEC EDGAR"`
and link the asset), with a **Thesis check** section: which of the four Invalidation
conditions on `[[ai-power-ipp-bull]]` it touches and whether the status should be
`ok | watch | hit`. Append a dated bullet to the position page's **Update history** and set
`invalidation_status` accordingly (this is maintenance, not a position-number change).
**Chase leads:** if any institution/news item mentions a position (or FERC/PJM/NRC action on
it), run `python3 scripts/sec_fetch.py search "<terms>" --tickers <T> --since <date>` and read
the filing — cite the filing, not the news.

## 4. Write the brief page `wiki/briefs/<date>.md` (CLAUDE.md §3.11)
Frontmatter counts + a 2–4 sentence **Headline** paragraph (Chinese, with `[[links]]`), then
the ```json brief-data``` block. Rules:
- every VIEW has `institution` (slug of an existing institutions page), `view` (一句话中文),
  `quote` (original words, ≤ 60 words), `source` (source-page slug), `url`, `is_change`
  (true only if it differs from the house's previous recorded view), `tickers`.
- `logic_changes`: only when a house explicitly reverses/upgrades a sector call — before/after
  in its own terms.
- `opportunities`: for each explicit buy idea create/update `wiki/opportunities/<slug>.md`
  (§3.10; `logic` = the one sentence the human needs; list every house that voiced it;
  `status: new` on first sight, `watching` when a second house echoes it; never `adopted` —
  only the human can adopt). Slug: `<ticker-or-theme>-<yyyy-mm>`.
- `positions`: one entry per open position — `note` (Chinese, 1–3 sentences: what the new
  filings mean for the thesis), `filings` (accessions you read), `invalidation_status`.
Empty buckets are fine — say so; never pad.

## 5. Render
```bash
python3 scripts/prices.py && python3 scripts/render_brief.py --date "$(date +%F)"
```
Open `brief/<date>.html` mentally: every view has a badge, every opportunity has a logic line
and at least one institution, every position card has a note.

## 6. Bookkeeping + ship
- `index.md`: add new sources / institutions / opportunities under their categories with
  one-line summaries; add the brief under a **Briefs** category.
- `log.md`: append `## [<date>] brief | <headline>` with pages touched, sources ingested,
  filings read, invalidation flags raised.
```bash
git add -A && git commit -m "Daily brief <date>: <headline>" && git push origin main
```
If push is rejected: `git pull --rebase origin main` then push again.

## Guardrails
- Never edit `raw/`. Never change `shares`, `entry_*`, `conviction` or open/close a position.
- Never write an institution view without a source page; never write a research source page without
  the raw text saved in `raw/`. For filings, `raw:` is the EDGAR folder URL (immutable by nature); the
  fetched text lives in `data/sec/text/` (git-ignored, regenerated by `sec_fetch.py`).
- A news article is a lead. The citation is the filing or the institution's own page.
- If a fetch fails, note it in `log.md` and move on — a thin brief beats no brief.
