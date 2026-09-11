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

## [2026-06-26] ingest | Ryan Cohen — $56B eBay plan (All-In, 4j9RPGLENNI) [re-clip now has transcript]
- raw: re-clipped with full transcript (supersedes the 2026-06-26 "incomplete clip" note above)
- pages touched (8): [[2026-06-24-ryan-cohen-ebay-gamestop]], [[ryan-cohen]], [[gme]], [[ebay]], [[activist-investing]], [[founder-led-companies]] (Cohen example), [[david-friedberg]] (interviewer), [[index]]
- stubs: [[chewy]], [[live-commerce]]
- fact-check ✅: eBay bid $56B/$125-sh rejected May 12 2026 (verified); GME Q1 revenue $835.3M +14%, collectibles $348.9M ≈42%, $9.7B cash, $2B buyback (verified). ⚠️ nuance: "$500M of his own money" (into the deal, unfiled ❓) ≠ the ~$35B GameStop pay package he DECLINED (verified). ❓ unverified: GME FCF $333M, eBay "-30M users", Cohen's 3-part plan (projection).
- cross-links: [[bill-ackman]] "vibes valuation" comment on GameStop ([[2026-06-03-ackman-market-is-missing]]); reinforces [[founder-led-companies]] + [[activist-investing]]. No positions/theses.

## [2026-06-28] ingest | All-In ep. 278 — China AI / Micron memory / IPO wave (w8ah_tA0yfg)
- raw: clipped (guests Gavin Baker, Travis Kalanick)
- pages touched (~17): NEW [[2026-06-27-allin-china-ai-micron-memory]], [[gavin-baker]], [[travis-kalanick]], [[mu]], [[nvda]], [[cerebras]], [[tsla]] (stub→page), [[openai]] (stub→page), [[zai]], [[hbm-dram-bottleneck]], [[orbital-compute]], [[ai-distillation-open-weights]]; UPDATED [[anthropic]], [[spcx]], [[ai-gatekeeping]] (scoreboard), [[chamath-palihapitiya]], [[david-sacks]], [[index]]
- stubs: [[cxmt]]
- fact-check ✅: Micron FQ4 guide ~$50B + HBM sold out + ~$100B take-or-pay (⚠️ podcast "50%/4 customers" imprecise → 16 SCAs); GLM 5.2 (744B MoE, MIT, AAII 51, beats GPT-5.5 at 1/6 cost) ✅; OpenAI Jalapeño/Broadcom ✅; Nvidia bought Groq ~$20B ✅; Cerebras IPO $185→broke deal price, $20B/750MW OpenAI ✅. ⚠️ KEY: Gavin's "Anthropic $3T / $100B revenue" = projection — actual Series H ~$965B at ~$47B run-rate. SpaceX high $225.64, −30% ✅.
- themes: [[hbm-dram-bottleneck]] (Micron), [[ai-distillation-open-weights]]/[[zai]] feed the [[ai-gatekeeping]] fragmentation scoreboard, [[orbital-compute]]. No positions/theses (per user, theses later).

## [2026-07-05] ingest | All-In ep. 279 — AI Sovereignty Wars (wgdxSCsmS-Q)
- raw: clipped (besties, no guests)
- pages touched (~15): NEW [[2026-07-04-allin-ai-sovereignty]], [[alex-karp]], [[pltr]], [[fig]], [[ai-sovereignty]], [[ai-jobs-displacement]], [[california-fiscal-risk]]; UPDATED [[anthropic]] (vertical-integration + Fable un-ban), [[nvda]] (Nemotron/sovereign), [[openai]] (ARR/relative value), [[ai-gatekeeping]] (scoreboard), [[chamath-palihapitiya]], [[david-sacks]], [[david-friedberg]], [[index]]
- stubs: [[tom-brown]], [[nemotron]]
- fact-check ✅: Palantir+Nvidia sovereign AI (Nemotron, air-gapped, June 29) ✅; Anthropic Fable un-ban (Lutnick lifted ~June 30, back July 1, Tom Brown replaced Dario) ✅; RAMP study (21,559 firms, +10.2% headcount) ✅; Klarna reversal ✅; CA "balanced" $351B but ~$20–35B/yr structural deficits ✅. ❓ Figma/Claude Design blindside (per The Information); Anthropic ~$60B ARR (vs verified ~$47B May); CA $1.4T/pension specifics (Friedberg).
- key theme = [[ai-sovereignty]]: enterprises own compute/models/data → bullish [[pltr]]/[[nvda]]/open-weights, pressures [[anthropic]] (trust). Advances the [[ai-gatekeeping]] scoreboard (fragmentation). No positions/theses.

## [2026-08-01] ingest | Lipton & López de Prado — Optimal Mean-Reverting Trading Strategies (SSRN 3534445)
- raw: citation record only (raw/2020-02-08-lipton-lopez-de-prado-ou-exit-rules.md) — copyrighted PDF text not reproduced/archived, per publisher rights; SSRN/DOI links preserved for the source of truth
- pages touched (6): NEW [[2020-02-08-lipton-lopez-de-prado-ou-exit-rules]] (source), [[ou-optimal-exit-rules]] (concept, w/ LaTeX equations for the OU SDE, OLS parameter estimation, exit stopping-time, and the SR objective — standard/generic notation, not the paper's own proprietary heat-potential derivation apparatus), [[alexander-lipton]], [[marcos-lopez-de-prado]] (people), [[index]]
- fact-check ✅: paper verified on SSRN (posted 2020-02-08); later formally published (retitled) in Int'l Journal of Theoretical and Applied Finance (Jan 2021, DOI 10.1142/S0219024920500569) + a Risk Magazine version (2020) + arXiv companion (2003.10502); both authors' affiliations verified (Lipton: ADIA/MIT Connection Science/Hebrew University; López de Prado: Cornell/ADIA/True Positive Technologies); 2021 Risk.net Buy-Side Quant of the Year confirmed for both.
- note: first academic-paper source in the wiki (prior sources are podcasts/interviews). Explicitly framed as downstream of — not a replacement for — cointegration testing (per [[statarb-strategy-lab]]'s SKILL.md discipline). Candidate next application: WTI/Brent, the first pair this session to robustly pass cointegration (recent half-life ≈6 days). No positions/theses; methodology reference only.

## [2026-08-14] synthesis | BZ=F/CL=F (Brent/WTI) statarb research
- pages touched (5): NEW [[bz-cl-pairs-trade]] (synthesis), [[cl]], [[bz]] (assets); UPDATED [[ou-optimal-exit-rules]] (Related section — now reports the actual empirical test, not just a candidate application), [[index]]
- note: multi-session `statarb-strategy-lab` research. Built and validated (against the paper's own Table 1, ~0.1–0.6% error) an original implementation of the Lipton/López de Prado heat-potential Volterra solver, then applied it — the theoretically "optimal" exit underperformed a plain Bollinger Band rolling z-score rule on real BZ/CL data across every variant tried. Adopted strategy: Bollinger Bands, β=1.0093 (CADF, non-positive-price rows now excluded — fixes a real data-quality bug: CL=F printed -$37.63 on 2020-04-20, contaminating the OLS hedge-ratio regression), lookback=9d, entry/exit 2σ/1σ. Test-window (2024–2026) net Sharpe 1.30, CAGR 13.6%; calm 2024-2025 alone: Sharpe 1.95-2.34, max DD <1.2%.
- ⚠️ live risk flagged, not resolved: rolling cointegration test fails ~48% of 2024-2026 days — a genuine ~4.5-month breakdown Feb-Jul 2024 (unrelated to any war) plus the ongoing Iran-US Strait of Hormuz conflict (started 2026-03-04, Brent +65% in March, still unresolved as of last check — fact-checked via web search, see [[bz-cl-pairs-trade]] sources). Kelly sizing red flag: full-Kelly implies 12.74x leverage (est. too noisy to trust); 4x final figure is the pre-set risk cap doing the work, not Kelly converging on its own.
- no positions/theses — Thesis Test (Edge/Catalyst/Invalidation) not yet completed; human has not adopted this as a real position.

## [2026-08-14] maintenance | P&L convention bug found + fixed; multi-sector pair screen
- pages touched (4): NEW [[multisector-pairs-screen]] (synthesis); UPDATED [[bz-cl-pairs-trade]] (corrected performance table + Kelly section, methodology-fix note added), [[index]], [[log]]
- ⚠️ BUG FOUND: the P&L convention used throughout the BZ/CL work (`rets_y - beta*rets_x`, percentage returns combined directly) implicitly represents a $1-long vs $beta-short DOLLAR position, not a beta-share-ratio position — correct only when beta≈1. Surfaced while testing a new GS/WFC pair (beta=6.4, ~7.7x real price-level gap): naive convention gave a -93% max drawdown that was pure scaling artifact. Fixed with a proper dollar-neutral P&L, now `scripts/backtest.py::pair_spread_returns` for future use. Even BZ/CL (beta≈1.0093) was not immune: CAGR corrected from 13.6%→6.2%, Sharpe 1.30→1.14, Kelly full-leverage 12.74x→21.12x (capped-at-4x max DD improved -18.2%→-10.3%, now inside the stated 10-20% tolerance). Qualitative conclusions (calm-period edge real, Bollinger beats paper's optimal exit) not re-verified end-to-end against this fix — only the adopted strategy's own headline numbers were corrected.
- multi-sector screen (excluding biotech/tech per request): 30 in-sample candidates across metals/financials/industrials/ag (99% confidence Johansen). Ticker check caught GOLD resolving to "Gold.com, Inc." not Barrick (corrected to B); CT=F unresolved, excluded. Shortlisted AEM/B, DAL/UAL, GS/WFC for out-of-sample testing. AEM/B failed CADF cross-check (dropped, likely false positive). DAL/UAL and GS/WFC both cointegrated but produced losing/flat out-of-sample results (Sharpe -0.25 and -0.05) once correctly computed. No survivors this round.
- no positions/theses.

## [2026-08-23] synthesis | Negative results filed — BZ/CL walk-forward, micro-futures screen, tradability dead-end
- pages touched (6): NEW [[micro-futures-universe-screen]] (synthesis), [[pairs-trade-failure-modes]] (concept); UPDATED [[bz-cl-pairs-trade]] (substantially rewritten), [[multisector-pairs-screen]] (later rounds added), [[index]], [[log]]
- ⚠️ HEADLINE: a 34-fold walk-forward over 19 years (2009-2026, 2y rolling train → 6m OOS, params re-fit per fold) shows the previously-reported BZ/CL numbers came from an unusually favourable window. Long-run OOS Sharpe 0.53 (diff 2σ/1σ) to 0.67 (ratio 1σ/mean) with −32% to −34% max drawdown — versus the 1.30–1.86 at −5% to −7% reported from 2024-2026 alone. The two rules are statistically indistinguishable head-to-head (ratio wins 16/34 folds, mean Sharpe diff +0.06, paired t p=0.83).
- adopted strategy switched to the **log price ratio** at 1σ in / mean out — chosen on STRUCTURAL grounds, not backtest performance. β instability is the reason: re-estimating per fold, 7 of 34 folds landed outside [0.8,1.2] (range 0.116–1.457). At β=0.116 the "hedged" difference spread correlated **1.00 with Brent** — a 0.88x outright long-oil position held ~75% of the time as crude fell $100→$50 (−43.9% that fold). A ratio spread has no β to mis-estimate. Regime-switch guidance: under stress switch *thresholds* (ratio 2σ/1σ scored 0.79 in the 2011-2015 break vs −0.05 for 1σ/mean) — NOT the spread.
- structural break confirmed: US shale/Cushing blew the Brent−WTI spread from ~$0.70 (2010) to ~$17 (2012); cointegration genuinely broke for ~5 years (ADF on difference p=0.2762, half-life 42d). A pair cointegrated over a 4-year window may be describing a regime, not a law.
- look-ahead truncation test PASSED at every cutoff (20–500 days, 0 of up to 4,226 days) for the full pipeline including per-fold half-life fitting — and the deliberately leaky control FAILED with 25 mismatches, confirming the test isn't vacuous.
- ⚠️ TRADABILITY DEAD-END: every execution route closed. 1 BZ contract = $94,390 = 4.72x a $20k account (~$189k needed at 0.5x scale). USO/BNO fail cointegration outright (ADF p=0.60 full history; ratio drifted 8.11→2.47 on differential roll schedules) and die on costs (Sharpe −0.06 at 20bps, BNO trades $19.5M/day). MCL+QM are BOTH WTI (verified: $87.06 vs $87.05) so no spread exists. ICE Mini Brent exists (100bbl) but is not practically accessible — IBKR lists only full-size COIL/BZ/BB. Recommendation: paper-trade notionally.
- micro-futures screen: 66 pairs across 16 retail-sizeable CME contracts, selection on 2010-2018, walk-forward on 2019-2026. NO SURVIVOR. Two findings generalize: (1) corr(in-sample CADF p-value, OOS Sharpe) = **+0.024** — the cointegration screen had zero predictive power; (2) corr(higher-leg vol, max drawdown) = **−0.843** — volatility set the drawdowns, not statistics. Screen top-ranks were degenerate (β 0.004–0.28, half-lives 600–900d; 6A=F appeared in 9 of top 11 = one artifact, not nine relationships). Best pair 6E/6B (Sharpe 0.72, DD −11.2%) FAILS cointegration (p=0.41) and has Deflated Sharpe 0.33 vs 15 trials, 0.10 vs 66. Not adopted.
- also filed (previously unrecorded): oil-linked equity screen (KMI/OKE, likely false positives — economically backwards result), second stock-sector round (staples/utilities/REITs/materials/insurance; O/VTR failed CADF cross-check after passing Johansen; CLX/PG never cross-checked), and the BRK-B/MSFT check (both tests reject; the tutorial's ratio-ADF result was real and reproducible — it strengthened to p=0.0173 on a longer window rather than evaporating — but fixes the coefficient at 1 instead of estimating it).
- ⚠️ unresolved: the P&L convention fix (`pair_spread_returns`) was reverted at the human's explicit instruction, so difference-spread figures on [[bz-cl-pairs-trade]] use the old, somewhat overstated convention. Ratio-spread figures are unaffected — dollar-neutral IS correct for a scale-free ratio. Futures roll costs still unmodeled; 1.5bps likely optimistic for 2009-era data.
- cross-cutting lesson now documented in [[pairs-trade-failure-modes]]: statistical co-movement without an **economic convergence mechanism** does not survive out-of-sample — demonstrated across ~10 equity sectors and 66 futures pairs. BZ/CL works because Brent and WTI are the same commodity at different delivery points, tied by physical shipping arbitrage.
- no positions/theses — Thesis Test not completed, and the position cannot currently be sized regardless.

## [2026-09-11] maintenance | Daily institutional brief system built + private GitHub repo
- pages touched: [[CLAUDE]] (§2 tree, §3.1/3.5 fields, new §3.9 institution / §3.10 opportunity / §3.11 brief, §4.4 BRIEF op), `.claude/skills/daily-brief/SKILL.md`, `brief/sources.yaml`, `brief/config.yaml`, `scripts/sec_fetch.py`, `scripts/prices.py`, `scripts/render_brief.py`, `scripts/frontmatter.py`, tests/, `docs/superpowers/specs/2026-09-11-daily-brief-design.md`
- note: vault pushed to private repo github.com/liobulio/My_Wiki (statarb-strategy-lab/ git-ignored). Positions CEG 5.891 / TLN 5.407 / VST 11.523 (IBKR, ~$7.2k account) opened with the human's own Thesis Test on [[ai-power-ipp-bull]] (condition-based invalidation, no price stop). 14 institution pages seeded. PyYAML not installed → stdlib frontmatter parser; briefs carry a ```json brief-data``` block.

## [2026-09-11] brief | 首期：9/16 FOMC 加息分歧 · AI 基建 120 GW · CEG Crane 获批 · PJM $325 上限 · 新机会 MU/SNDK
- pages touched (≈40): NEW sources ×15 (11 research + 4 filings), institutions ×4 NEW (boci, donghai-futures, soochow-securities, pacific-securities) + 6 updated house views, opportunities ×2 NEW ([[mu-sndk-memory-upcycle-2026-09]], [[ai-infra-power-grid-bottlenecks-2026-09]]), [[2026-09-11]] brief, positions ×3 (update history), assets [[ceg]] [[tln]] [[vst]] [[mu]], [[index]]
- sources: foreign — Apollo ×2, BlackRock BII, PIMCO, Goldman (May baseline), Morgan Stanley; domestic — 国信, 中银国际, 东海期货, 东吴, 太平洋 (via 东方财富研报中心 API + pdftotext). Not reachable: KKR (403), JPM (no new pieces), Bridgewater (off-topic), Goldman WebFetch 403 (curl works).
- filings read: CEG 8-K 08-06 + 10-Q; TLN 8-K 08-05 + 10-Q; VST 8-K 08-07, 8-K 07-16 (Item 1.01 = receivables financing, false positive), 10-Q. `sec_fetch.py` since 2026-07-15.
- fact-check ✅: ECB +25bp 2026-09-10; NFP +162k / 4.1%; PJM 2028/29 BRA at $325 cap (uncapped $554.72); July FOMC 9-3 with 3 hike dissents; Micron FQ3 DRAM/NAND ASP +low-60s%/+mid-80s%; Helix launched 2026-06-11. ❓ unverified: PPI 5.4%, CPI 3.4%, Japan $1.1T UST, 30y 5.3%, hyperscaler capex guides (cross-checked only against Goldman's $754B consensus). Stale item caught: Goldman "Fed may cut earlier" article is 2025-07, dropped.
- ⚠️ contradictions flagged: Apollo (expects Sept hike) vs 中银国际 (one strong NFP ≠ pivot); PIMCO (fiscal/supply drives long end) vs Apollo "Bessent is right" (term premium stable).
- invalidation status: CEG/TLN/VST all ok×4; FERC+NRC approvals for Crane are reverse evidence on condition ②. Watch items: PJM price cap through 2029/30; TLN −18% since June untraced; TLN 4 GW pipeline = options, not contracts.
- rendered: brief/2026-09-11.html + brief/index.html.

