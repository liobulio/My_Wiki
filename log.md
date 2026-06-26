---
type: log
---

# Log — Investment Wiki

Append-only, newest at the bottom. One entry per operation
(`ingest` · `query` · `lint` · `maintenance`). Grep the timeline with:

```
grep "^## \[" log.md | tail -5
```

---

## [2026-06-19] maintenance | Wiki initialized
- pages touched: [[CLAUDE]], [[index]], [[log]], [[overview]]
- note: Set up the schema, folder conventions, navigation files, and portfolio dashboard. Empty and ready for the first source.

## [2026-06-19] ingest | Quant Corner Ep. 47 — Does Momentum Still Work? (sample seed)
- raw: [[raw/2026-06-12-quant-corner-momentum]]
- pages touched: [[2026-06-12-quant-corner-momentum]], [[momentum-factor]], [[factor-investing]], [[mtum]], [[cliff-asness]], [[mtum-bull]], [[index]]
- stubs created (links only): [[value-factor]], [[momentum-crashes]], [[AQR]], [[dana-whitfield]]
- note: First ingest. Established baseline momentum claims (no contradictions yet). Flagged 2 data gaps on [[mtum]] (exact expense ratio, AUM/methodology) for a future lint/web-search. Position NOT created — momentum is not a real holding; proposing one to the human.

## [2026-06-19] maintenance | Removed momentum sample seed
- note: Per user request, deleted the illustrative momentum demo (raw + 6 wiki pages) and reset [[index]] to empty. Prior ingest entry above kept for history (append-only log). The MTUM watch position was never created (user declined).

## [2026-06-19] ingest | All-In Best Ideas Pitch Competition (4 picks) + fact-check
- raw: clipped via Obsidian Web Clipper (YouTube fO5sC7qS04E)
- pages touched (13): [[2026-06-12-all-in-best-ideas-pitch]], [[mgm]], [[tln]], [[akts]], [[geod]], [[aaron-cowen]], [[dan-dreyfus]], [[oleg-nodelman]], [[kyle-samani]], [[ai-power-demand]], [[radiopharmaceuticals]], [[depin]], [[all-in-best-ideas-2026-factcheck]] + [[index]]
- stubs created (links only): [[barry-diller]], [[all-in-podcast]], [[replacement-cost-investing]]
- fact-check: MGM ✅ (Diller $48.30 bid / 26.1% / Osaka 2030), TLN ✅ (~$382, AWS PPA, 2.2GW nuclear), AKTS ✅ (mostly — $318M IPO, Ac-225/nectin-4 Fast Track; "$100M Lilly" imprecise), GEOD ⚠️ revenue ~$5M actual vs ~$11M pitched (~2x overstated) + token net-inflationary + disclosed Multicoin conflict.
- ⚠️ contradiction flagged: [[geod]] pitched revenue vs reported. No positions created (none are real holdings).

## [2026-06-20] maintenance | Schema: added the Thesis Test + thesis-ownership model
- pages touched: [[CLAUDE]]
- note: Per user, every position/tracked-thesis must answer The Edge / The Catalyst / The Invalidation before opening (new §3.8). Codified ownership: human owns stance/conviction/invalidation; LLM drafts, evidences, and maintains. A "tracked thesis" = a stance the human has adopted as their own (lives in theses/), vs a pitched idea (stays on source/asset page).

## [2026-06-21] ingest | All-In news: Trillionaire / Fable Ban / Oligarchs / Iran
- raw: clipped via Obsidian Web Clipper (YouTube 3Amlu4y94Ho)
- pages touched (12): [[2026-06-20-all-in-oligarchs-fable-iran]], [[spcx]], [[anthropic]], [[amzn]], [[elon-musk]], [[chamath-palihapitiya]], [[david-sacks]], [[david-friedberg]], [[dario-amodei]], [[ai-gatekeeping]], [[ai-power-demand]] (cross-link) + [[index]]
- stubs created (links only): [[tsla]], [[cursor]], [[andy-jassy]], [[jason-calacanis]], [[oil]]
- note: News/discussion episode, not a pitch — extracted investment-relevant threads. Key: SpaceX IPO (~$2T) + Cursor deal; Anthropic Fable 5 govt ban → [[ai-gatekeeping]] hyperscaler thesis; Iran MOU (Hormuz reopening, risk-on/oil). No fact-check run (not requested); flagged SpaceX/Cursor figures + SK-Telecom/China claim as source-reported/unverified data gaps.
- ⚠️ conflict-of-interest flagged on [[david-sacks]] (WH AI czar narrating a govt action). Anthropic/Claude/Dario content recorded neutrally as attributed claims; LLM "psychoanalysis" segment marked entertainment, not fact. No positions/theses (user doing theses later).

## [2026-06-21] maintenance | Schema: fact-check is now MANDATORY on every ingest
- pages touched: [[CLAUDE]]
- note: Per user ("always fact check when ingesting"), added a mandatory fact-check step to the ingest flow (§4.1, step 2): verify hard claims via web, record ✅/⚠️/❌/❓ verdicts with citations, separate facts from forecasts. Never skip, even when unprompted.

## [2026-06-21] factcheck | Retroactively fact-checked the 2026-06-20 All-In news episode
- pages touched: [[spcx]], [[anthropic]], [[amzn]], [[2026-06-20-all-in-oligarchs-fable-iran]]
- verdicts: SpaceX IPO ✅ ($135, +19%→$161, >$2T, passed AMZN) but ⚠️ raise ~$75B not $85B; Cursor $60B/~$4B ARR ✅; Fable ban ✅ corroborated (SK Telecom named by multiple outlets; Amazon-flagged codebase→vuln jailbreak); Iran MOU ✅ framework but ⚠️ "$300B reconstruction" → actually ~$24–25B frozen assets, and enriched-uranium removal NOT yet agreed (open 60-day item).
- ⚠️ corrections flagged inline + on entity pages. ❓ left unverified: SpaceX 2025 revenue/retail split, Pakistan mediator, Illinois crypto-tax specifics.

## [2026-06-21] maintenance | Refined [[ai-gatekeeping]] — agree-vs-diverge + timescale
- pages touched: [[ai-gatekeeping]], [[chamath-palihapitiya]], [[david-friedberg]], [[index]]
- note: User found the "opposing theses" framing confusing. Clarified that Chamath & Friedberg AGREE concentration pressure is real now and disagree only on whether it's DURABLE (Chamath: unreplicable KYC moat → sticks; Friedberg: disaggregation + commoditization → breaks). Added a comparison table + a timescale reconciliation ("concentrate, then fragment"). Dropped the misleading "cartel vs counter-thesis" labels.

## [2026-06-21] maintenance | New concept: [[replacement-cost-investing]] (resolves stub)
- pages touched: [[replacement-cost-investing]], [[index]]
- note: Per user request. Wrote the "buy a hard asset below replacement cost" concept (definition, Tobin's Q link, Sam Zell / Equity Office playbook, value-trap & obsolescence risks). Resolves the stub referenced by [[tln]] / [[dan-dreyfus]] / [[ai-power-demand]]. (Separately: YouTube _TJFqEhxQg4 ingest pending a clipped transcript in raw/.)

## [2026-06-26] ingest | Bill Ackman — "What the Market is Missing" (All-In, _TJFqEhxQg4)
- raw: clipped (this is the previously-blocked _TJFqEhxQg4 — now has a full transcript)
- pages touched (10): [[2026-06-03-ackman-market-is-missing]], [[bill-ackman]], [[hhh]], [[psus]], [[insurance-float-compounding]], [[founder-led-companies]], [[amzn]] (Ackman view), [[spcx]] (Ackman pre-IPO view), [[index]]
- stubs: [[warren-buffett]], [[msft]], [[meta]], [[openai]], [[ryan-cohen]], [[sarah-friar]], [[ron-baron]], [[salesforce]]
- fact-check ✅: HHH→Berkshire-2.0 verified (Vantage insurer ~$2.1B, Pershing ~47%, up to $1B preferred); PSUS verified ($5B IPO Apr 2026, −18% debut) ⚠️ discount now ~24–29% not 18%; track record ~28× net ≈ ~16% CAGR consistent. ⚠️ Timeline: taped pre-SpaceX-IPO — Ackman's "$750B–$1T" vs actual ~$1.77T (cross-link [[2026-06-20-all-in-oligarchs-fable-iran]]).
- note: actionable thesis = [[hhh]]. "MSFT/META/AMZN undervalued" + rubber-band call flagged as opinion. No positions/theses.

## [2026-06-26] maintenance | GameStop/Ryan Cohen clip incomplete — no transcript
- note: raw/"GameStop CEO Ryan Cohen's $56B Plan to Take Over eBay" (4j9RPGLENNI) has only the description/chapters, NOT the transcript body. NOT ingested. Needs a re-clip with the transcript before it can be processed.
