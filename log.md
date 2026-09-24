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

## [2026-09-14] brief | 加息天平倾斜 + AI 电力主线强化；SEC 零新增文件；首次由 GitHub Actions 跑通
- pages touched (19): NEW sources ×5（[[2026-09-11-donghai-securities-us-cpi-aug]]、[[2026-09-12-guosen-ai-compute-roi]]、[[2026-09-13-guosen-multiasset-hike-gold]]、[[2026-09-13-guojin-compute-mainline-power]]、[[2026-09-13-soochow-power-scarcity-nuclear-ppa]]）、NEW institutions ×2（[[donghai-securities]]、[[guojin-securities]]）；UPDATED [[guosen]]、[[soochow-securities]] house views、[[ceg]]、[[ai-power-demand]]、[[ai-infra-power-grid-bottlenecks-2026-09]]（new → **watching**）、positions ×3、[[2026-09-14]]、[[index]]、[[log]]
- 宏观：8 月核心 CPI 环比 +0.3% 超预期 → 9/16 加息概率 70%→80%+（[[donghai-securities]]）；10Y 本周 +18BP 逼近 5%，黄金脱敏于利率（[[guosen]]）。较 09-11 简报的「50/50」框架是**实质抬升**，Apollo 9/5 的加息预测方向得到验证。
- 行业：国信自下而上测算 **2027 起数据中心落地算力仅为芯片理论量的 50–60%**（电网年新增仅 10–15 GW、持证技工是最严卡点）；国金引 DOE（AIDC 用电占比 2028 → 6.7–12%）、NERC（北美夏峰十年 +224 GW）；东吴梳理 Google–Fortum 22 年核电 PPA、NextEra 重启 615 MW、MA 州 100% 清洁自备电令。三家内资独立佐证 [[ai-infra-power-grid-bottlenecks-2026-09]] → 升为 watching。
- 持仓：`sec_fetch.py --since 2026-09-11` 三家**均无新增 8-K/10-Q/10-K**；filings_read: 0。[[ceg]] $7.15 亿收购壳牌 RISEC（609 MW CCGT，ISO-NE，2027Q1 交割）✅ 已核 —— 以**新闻 lead** 记录，未能定位对应 8-K（`efts.sec.gov` 全文检索 403）。四项 Invalidation 全部 ok×4；利率上行属 thesis 既列风险，非失效条件。
- ⚠️ 承前未解：[[tln]] 6→9 月 −18% 仍未追溯到具体 catalyst，下期优先。
- 外资桶留空（`us_equity: []`）：Apollo RSS 未更新至 09-12 后、BlackRock BII 最新仍为 09-08（上期已 ingest）、Goldman/MS 客户端渲染页无干净的 09-11 后条目 —— 不硬凑。
- ⚠️ 运行说明：本期由 **GitHub Actions** 首次跑通（云端 routine 因沙箱出网 403 + 无 GitHub 写权限而放弃）。运行在写完 wiki 页面后触及账户用量上限中断，HTML 渲染与 index/log 记账由本地补完；提交信息 `leftover files from the runner` 为 workflow 兜底步骤所生成，非正常提交。

## [2026-09-14] maintenance | 复核 SEC 文件步骤：确认三家零新增（RISEC 8-K 尚未到期）
- 承前 09-14 brief 的未解项（`efts.sec.gov` 全文检索 403，未能定位 [[ceg]] RISEC 收购对应 8-K）。改用权威口径 **data.sec.gov/submissions** 直连复核：CEG 最新文件为 2026-08-21 Form 144，无收购 8-K；`sec_fetch.py --since 2026-09-11` 重跑，三家（CEG/TLN/VST）均 0 新增、0 flag，`data/sec/*.json` 仅刷新 `fetched` 时间戳。
- 结论：RISEC 于 9/12（周五）宣布，Item 1.01 8-K 法定期限为 4 个工作日（约 9/18），期间 9/13–14 为周末 → **当前尚无对应文件属正常**，`filings_read: 0` 准确、非抓取失败。三项 Invalidation 维持 ok×4。下期（≥9/15）优先确认 RISEC 8-K 是否入档。


## [2026-09-15] brief | FOMC 前瞻：加息近确定，焦点转向"是否连续加息"；浦银国际唯一立场反转；SEC 零新增文件
- pages touched (18): NEW sources ×4（[[2026-09-14-soochow-us-weekly-hike-risk]]、[[2026-09-12-spdb-intl-cpi-25bp]]、[[2026-09-14-donghai-electronics-tsmc]]、[[2026-09-14-dongguan-aidc-power]]）、NEW institutions ×2（[[spdb-international]]、[[dongguan-securities]]）、NEW asset [[tsm]]；UPDATED [[soochow-securities]]/[[donghai-securities]] house views、[[nvda]]、[[ai-power-demand]]、[[ai-infra-power-grid-bottlenecks-2026-09]]、positions ×3、[[2026-09-15]]、[[index]]、[[log]]
- 宏观/美股：本周 **FOMC（9/16–17）**加息近板上钉钉。[[spdb-international|浦银国际]]把路径判断由"9 月不加息"**改判"9 月或加息 25bp"**（8 月核心 CPI 环比 0.29% + 非农 16.2 万双双超预期）——本期唯一 `logic_change`；但判断 Fed 不会给连续加息指引。[[soochow-securities|东吴]]美股周观点呼应又略有张力：真正风险不是"是否加息"（已定价），而是"**是否连续加息**"，市场或借长端上行压制估值（本周道指 −1.6%）。8 月 PPI **+5.4%**、油价因美伊冲突**破 $100** ✅ 已核。
- 行业/AI 需求侧：[[tsm|台积电]] 8 月营收 **+53.3% 创新高**（前 8 月 +39.3%）✅；Oracle Q1 FY27 单季交付 **850 MW** 数据中心容量、营收 +30% ✅；东莞引 IEA 全球数据中心用电 2030 翻倍至 **945 TWh**、英伟达 TDP 300W→1400W。均为 [[ai-power-demand]] / [[ai-infra-power-grid-bottlenecks-2026-09]] 的需求侧确认（非新机构，opportunities_new: 0）。
- 持仓：`sec_fetch.py --since 2026-09-14` 三家（CEG/TLN/VST）**均 0 新增、0 flags**，filings_read: 0。承前 09-14 maintenance 的优先项——[[ceg]] RISEC 收购（9/12 宣布）对应 **Item 1.01 8-K 至 9/15 仍未入档**：CEG 最新文件为 2026-08-13 Form 4，法定期限约 9/18（4 个工作日），当前无档属正常，继续下期确认。四项 Invalidation 全部 ok×4（维护性更新，非持仓数字变动）。
- ⚠️ 承前未解：[[tln]] 6→9 月 −18% 仍未追溯到具体 catalyst，下期优先。
- 去重：东海证券 09-11 CPI 报告（infoCode AP202609141829350601）经核对与上期 [[2026-09-11-donghai-securities-us-cpi-aug]] 为同一篇，已跳过。
- 外资桶留空（macro 仅内资）：Apollo Daily Spark RSS 无 09-14 后新条目、BlackRock/Goldman/MS 客户端渲染页无干净的 09-14 后日期条目——与前两期一致，不硬凑。
- rendered: brief/2026-09-15.html + brief/2026-09-15.md（手机版）+ brief/index.html + README。全部硬数据 web 核实通过（PPI 5.4%、核心 CPI 0.3%、非农 16.2 万、油价破 $100、Oracle $19.35B、TSMC +53.3%）。

## [2026-09-16] brief | FOMC 今日开会；浦银"利率上行有序/AI 仍是主线"vs 东兴"不排除连续加息"；SEC 零新增
- pages touched: [[2026-09-16]], [[2026-09-16-spdb-intl-rates-equity]], [[2026-09-16-dongxing-cpi-continuous-hike]], [[spdb-international]], [[dongxing-securities]], [[federal-reserve-rate-path]], [[us-treasury-10y]], [[ceg]], [[tln]], [[vst]], index.md
- sources ingested: 2（东方财富研报中心：浦银国际 09-16 利率→中美股市策略；东兴证券 09-16 8 月 CPI 点评·连续加息）。跳过 联储/万联/中邮 三篇 8 月 CPI 反应（与上期重复）；行业页当日为 A 股链条，无美股电力标的 → industry 空；外资公开源无 09-15 后新篇（Apollo/BlackRock/Goldman/MS）。
- filings read: 0 —— `sec_fetch.py --since 2026-09-15` 确认 [[ceg]]/[[tln]]/[[vst]] 均 0 新增文件、0 flags。
- invalidation flags: 无新增；三家 ok×4 不变（维护性更新）。长久期现金流利率敏感性为 [[ai-power-ipp-bull]] 既列风险，非失效条件。
- fact-check: 10Y 一度触及 5.04%（2007-07 以来首次）✅；8 月 CPI 0.4%/3.4%、核心 0.3%/2.4% ✅；FactSet Q3 +28.7% ✅；加息概率 CME ~88%（浦银口径 >90%，⚠️ 略高）；SP500 fwd P/E 19.1x projection-adjacent。
- opportunities_new: 0（两篇均宏观/策略，无显式买入标的）。

## [2026-09-17] brief | 靴子落地：美联储加息 25bp 至 3.75%–4.00%、12–0 全票偏鹰（2023-07 以来首次），内资在"后续路径"上分歧
- pages touched: [[2026-09-17]], [[2026-09-17-spdb-intl-fomc-hike-hawkish]], [[2026-09-17-guosen-fomc-warsh]], [[2026-09-17-boci-fomc-less-optimistic]], [[2026-09-17-donghai-fomc-hike-landed]], [[spdb-international]], [[guosen]], [[boci]], [[donghai-securities]], [[ceg]], [[tln]], [[vst]], index.md
- sources ingested: 4（东方财富研报中心 09-17 FOMC 决议点评：国信"认清沃什"·中银"不如市场乐观"·东海"靴子落地"·浦银"加息偏鹰"）。均为已建档、可追踪立场演变的券商。跳过 万联/国元国际/国投期货/东方金诚/粤开 等同题一次性快评（高度重复）；行业页 09-17 为 A 股链条（半导体设备/CoWoS/光通信/电力设备）无美股电力标的 → industry 空；外资公开源无 09-16 后新篇（Apollo/BlackRock/Goldman/MS）；All-In 本周新集未落地。
- filings read: 0 —— `sec_fetch.py --since 2026-09-16` 确认 [[ceg]]/[[tln]]/[[vst]] 均 0 新增文件、0 flags。
- invalidation flags: 无新增；三家 ok×4 不变（维护性更新）。FOMC 加息推升的长久期现金流利率敏感性为 [[ai-power-ipp-bull]] 既列风险，非失效条件。
- logic_changes: 1 —— [[guosen|国信]] 自 9/12"如需加息，一次足矣"边际转鹰为 9/17"不排除年内再加一次"（is_change=true）。
- fact-check: 加息 25bp 至 3.75%–4.00%、12–0 全票、16/18 官员年内看再加息、沃什任主席、2023-07 以来首次加息 ✅（CNBC/Kiplinger + 四家券商交叉核实）；点阵图 12/4/2/0 分布、2026/27 利率中值 4.1%、2028 才降息 ✅（四家一致）；国信当日盘中数据（标普 −0.8%/纳指 −0.7%、2Y +13bp/10Y +7bp、美元 +0.6%）与中银"会前期货隐含 ~3.8 次"为 data point，未逐位复核。
- opportunities_new: 0（四篇均宏观/策略，无显式买入标的）。

## [2026-09-17] brief | 重跑增补：FOMC 后续路径纳入第三种落点——东方金诚"平台观察期"、粤开 K 型分化+泰勒规则量化
- pages touched: [[2026-09-17]], [[2026-09-17-dongfang-jincheng-fomc-hawkish-hike]], [[2026-09-17-yuekai-fomc-k-shaped]], [[dongfang-jincheng]], [[yuekai-securities]], index.md, brief/2026-09-17.{html,md}
- context: 当日简报已于本日建档（4 篇 FOMC 点评）。本次重跑复扫东方财富 09-17 策略/宏观/行业 API，复核 SEC——[[ceg]]/[[tln]]/[[vst]] 仍 0 新增、0 flags。
- sources ingested: +2（原 4 → 6）。改判上一版跳过的两篇：[[dongfang-jincheng|东方金诚]]（评级机构，给出"一次预防性加息→高利率平台观察期"的第三种落点、新增声明删"供应冲击"→能源通胀转持续性）、[[yuekai-securities|粤开证券]]（12 页宏观深度，非快评：泰勒规则失业率口径 3.88% vs GDP 口径 4.09%、差 21bp；统一利率放大 K 型分化；直指美股"AI 牛市"能否免疫高利率——切中持仓风险背景）。仍跳过 万联(港股资金面)/国元国际/国投期货 等一次性快评。
- filings read: 0 —— `sec_fetch.py --since 2026-09-16` 三家均 0 新增、0 flags。
- invalidation flags: 无新增；ceg/tln/vst 均 ok×4 不变。粤开点出的"AI 牛市对高利率的敞口"归入 [[ai-power-ipp-bull]] 既列风险，非失效条件。
- fact-check: 两篇的 FOMC 硬数据（25bp 至 3.75%–4.00%、12–0 全票、点阵图中值 4.1%、16/18 年内再加、核心 PCE 3.4%、8 月 CPI 3.4%/核心环比 0.3%）与当日已核验来源交叉一致 ✅；泰勒规则 3.88%/4.09%、"平台观察期"、"AI 牛市免疫高利率"为机构测算/判断（projection，非核验项）；会后市场快照（10Y 破 5%、DXY 100.3、金价 $4265）为粤开记录，与国信当日方向一致（data point）。
- opportunities_new: 0（两篇均宏观，无显式买入标的）。新增 TODO 链接 [[taylor-rule]]（概念页待写）。

## [2026-09-18] brief | 加息落地次日叙事转回"AI 资本开支还能加速多久"——格林大华把 AI 电力/内存需求量化到每 GW；东兴 vs 东海对"是否连续加息"分歧
- pages touched: [[2026-09-18]], [[2026-09-18-greendh-futures-ai-reaccel]], [[2026-09-18-dongxing-fomc-oil]], [[2026-09-18-guosen-us-bull-bears]], [[green-dahua-futures]], [[dongxing-securities]], [[guosen]], [[mu-sndk-memory-upcycle-2026-09]], [[ai-infra-power-grid-bottlenecks-2026-09]], [[ceg]], [[tln]], [[vst]], index.md, brief/2026-09-18.{html,md}
- sources ingested: 3（各占一桶，重信号不注水）：宏观 [[2026-09-18-dongxing-fomc-oil|东兴·加息防高油价扩散]]（会后第一框架、与东海"不支持连续加息"张力）、行业 [[2026-09-18-greendh-futures-ai-reaccel|格林大华·AI 投资再加速]]（把 AI 电力/内存需求量化到每 GW，直切持仓；新建机构页 [[green-dahua-futures]]）、美股 [[2026-09-18-guosen-us-bull-bears|国信策略·美股长牛背后大小熊]]（回应"AI 牛市 vs 高利率"）。09-18 API 余下多为 FOMC 后续快评，与上期三种落点高度重复，跳过。外资公开源无新篇（Apollo 最新 09-16 < SINCE；BlackRock/GS/MS 客户端无干净新条目；All-In 周五集未落地）。
- filings read: 0 —— `sec_fetch.py --since 2026-09-17` [[ceg]]/[[tln]]/[[vst]] 三家均 0 新增、0 flags。
- invalidation flags: 无新增；ceg/tln/vst 均 ok×4 不变。格林大华的"每 GW"需求量化强化 firm 电力稀缺（正向，不触发失效条件）；东兴维持 10Y 4.7–5%、不排除连续加息 → 长久期利率敏感性属 [[ai-power-ipp-bull]] 既列风险，非 Invalidation。
- fact-check: ✅ Nebius 10/1 起 GPU 云涨 ~20%（H100 $3.85→$4.50 / B300 $7.85→$9.50、年内累计 ~56%，Benzinga/HostingJournalist）；✅ Broadcom Q3 AI 收入 $16.7B +221% YoY / +54% QoQ、指引 FY27 ~$1150 亿 / FY28 ~$2300 亿（Broadcom IR + CNBC）；✅ Oracle Q1 FY27 单季 850 MW（前期已核）。SemiAnalysis"2028 两家垄断 70–80% 算力"、Anthropic 2030 GDP 情景、"$11 万亿 capex"、Nvidia/Broadcom 未来财年指引均为投影/情景（不核验）。⚠️ 格林大华季报图注多处张冠李戴数据来源（编辑瑕疵，不影响已核硬数据）；国信正文将 1998 LTCM 误写为"1990/07-09"（排版笔误）。
- opportunities_new: 0；两页更新——[[mu-sndk-memory-upcycle-2026-09]] 供给紧张获第二家机构（格林大华）佐证 → new 升 watching；[[ai-infra-power-grid-bottlenecks-2026-09]] 追加"每 GW"量化证据、机构名单 +1（[[green-dahua-futures]]）。

## [2026-09-18] brief | 重跑增补：外资桶补入 All-In/Brad Gerstner（Altimeter）"这不是 2000 泡沫"+"power equipment sold out" 双向切中持仓
- 背景：09-18 简报已产出并提交（c71b5a0），本次为同日重跑。重扫确认：SEC `sec_fetch --since 2026-09-17` 三家（[[ceg]]/[[tln]]/[[vst]]）**0 新增、0 flags**；东方财富 09-18 策略/宏观/行业已全量扫过，前次已取三篇高信号（东兴/格林大华/国信），其余为 FOMC 点评重复或 A 股/华为链越界。
- 新增来源（外资桶，前次为空）：重扫 All-In libsyn feed 落地一批嘉宾专访，筛出唯一高信号且直切持仓的一集——[[2026-09-17-all-in-gerstner-no-bubble]]（09-17 发布、会前录制）。经 podscripts.co 取得部分机器转录（~16.6k 字）。
- pages touched: [[2026-09-17-all-in-gerstner-no-bubble]]（新源）、[[brad-gerstner]]（新人物页）、[[all-in-podcast]]（House view +1）、[[ai-infra-power-grid-bottlenecks-2026-09]]（机构 +1、Who says so +1）、[[ai-power-ipp-bull]]（supporting evidence +1）、[[2026-09-18]] 简报（sources_ingested 3→4、us_equity +1、三仓 note 补 Gerstner 佐证）、index.md、raw/2026-09-17-all-in-gerstner-no-bubble.md、brief/2026-09-18.{html,md}
- sources ingested: 1（Gerstner／All-In）| filings read: 0 | opportunities new: 0
- 核实：NVDA ~14× 完税 GAAP、"not 2000"、半导体=纳指 70% ✅（Gerstner 自述框架，FourWeekMBA 佐证）；"两实验室 2028 控 >半算力" ✅（SemiAnalysis/Dylan Patel 投影）；⚠️ 2027 GW 数字为投影且与公开 SemiAnalysis 略有出入（Gerstner 43GW 总/14GW 实验室 vs 公开 ~50GW/~18GW），标注投影不作事实核实。
- invalidation flags: 无变动，三仓 ok×4（Gerstner 为叙事佐证，非文件/非持仓数字变动）；利率敏感性（Gerstner"10Y 到 5.5% 对股市是重负"）仍属既列风险。
- 其余同期 All-In 专访（Satya Nadella、Dina Powell McCormick 数据中心、JD Vance、Nick Shirley）按"重信号不注水"未纳入；Apollo Daily Spark 最新 09-16（<SINCE，跳过）。

## [2026-09-21] brief | AI 资本开支的两面：电力更紧（东吴 TrendForce 268GW 缺口/华鑫"矛盾从算力移到电力"）vs 融资更贵（开源 CDS 走阔/国金 Oracle 毛利率降）；新机会 美国炼油商重置成本
- SINCE = 2026-09-18（上期简报，独占）。周一取东方财富研报中心 09-19/09-20/09-21 策略/宏观/行业；09-18 报告多为 FOMC 后续点评（上期已覆盖），不重复。按"重信号不注水"选 6 篇。
- sources ingested: 6 | filings read: 0 | opportunities new: 1
- 新增来源：[[2026-09-20-soochow-overseas-compute-power]]（东吴·电力趋紧，TrendForce 161GW/+31%、2030 缺口 268GW）、[[2026-09-21-huaxin-ai-infra-power]]（华鑫·电力设备）、[[2026-09-20-kaiyuan-storage-upcycle]]（开源·存储）、[[2026-09-20-kaiyuan-oracle-nebius-cds]]（开源·Oracle/Nebius/CDS）、[[2026-09-21-guojin-oracle-rpo-margin]]（国金·Oracle 毛利率/FCF）、[[2026-09-20-donghai-us-refiners-highs]]（东海·美国炼油商新高）
- 新机构页：[[kaiyuan-securities]]（开源证券）、[[huaxin-securities]]（华鑫证券）。institution House view 更新：[[soochow-securities]]、[[guojin-securities]]、[[donghai-securities]]。
- 新机会页：[[us-refiners-replacement-cost-2026-09]]（东海，status new，已填提案 edge/catalyst/invalidation）。更新机会页：[[ai-infra-power-grid-bottlenecks-2026-09]]（+东吴 TrendForce/+华鑫/+信用侧 CDS 提示、机构 +1）、[[mu-sndk-memory-upcycle-2026-09]]（+开源"长约锁供给"、机构 +1）。
- pages touched: 上述 6 源 + 2 新机构 + 3 机构更新 + 1 新机会 + 2 机会更新 + [[ceg]]/[[tln]]/[[vst]]（Update history +1、ok×4 不变）、[[2026-09-21]] 简报、index.md、raw/（6 份 pdftotext 抽取文本）、brief/2026-09-21.{html,md}、brief/README.md
- 核实：Oracle FY27Q1 营收 $19.3B+30%/OCI+121%/RPO $664B（+$209B YoY）/EPS $1.92/指引 ≥$90B ✅（Oracle 官方 2026-09-10）；TrendForce 2026 用电 161GW/+31%、2030 491GW、缺口 268GW ✅；美国柴油裂解创纪录（ULSD 一度 $102.20/桶）✅。⚠️ CoreWeave CDS 报告"900bp"vs 公开 ~855bp（取盘中高点、标近似）；⚠️ 东海炼油个股 YTD 涨幅（VLO+158% 等）高于 Benzinga/CNBC 的 +80%+，可能取不同基点，标"偏高待核实"（"创新高"方向无争议）。
- invalidation flags: 无变动，三仓 ok×4（无新增 SEC 文件、0 flags；新研报为叙事佐证，非文件/持仓数字变动）；利率/融资敏感性（AI 举债推高折现率、算力厂商 CDS 走阔）仍属既列风险，非 Invalidation。
- 未取到的桶：macro=[]（本窗口无专门宏观策略新源）；外资——Apollo Daily Spark RSS 仅返回无日期播客条目、Goldman AM Pulse 最新 09-08（<SINCE）、Goldman/MS 客户端页仅见旧年度 S&P 目标、All-In 无窗口内新集转录——均记"本窗口无新可取外资源"，按"薄简报也好过没有"继续。

## [2026-09-22] brief | 加息落地后如何应对——东吴"股市锚定盈利而非利率、利率压估值≠改AI景气"vs国新"10Y收5.021%新高/10月加息概率近60%、加息非治本"；需求侧IAEA第六次上调核电装机 + AMAT FY26Q3 HBM设备放量；SEC三家0新增、Invalidation ok×4
- SINCE = 2026-09-21（上期简报，独占）。周一取东方财富研报中心 09-21/09-22 策略/宏观/行业（宏观 qType=3 当日 0 命中）；多篇"加息利空落地"策略周报与 09-17 FOMC 复盘重叠，仅取国新（含新增市场定价+"非治本"独家判断）代表当日宏观。按"重信号不注水"选 4 篇。
- sources ingested: 4 | filings read: 0 | opportunities new: 0
- 新增来源：[[2026-09-22-soochow-us-weekly-post-hike]]（东吴·美股周观点·加息落地后如何应对）、[[2026-09-22-cpost-iaea-nuclear-uprate]]（中邮·IAEA 第六次上调核电装机）、[[2026-09-22-guoxin-sec-fed-hawkish-hike]]（国新·9 月 FOMC 解读）、[[2026-09-22-pacific-electronics-ai-memory]]（太平洋·AMAT FY26Q3）
- 新机构页：[[china-post-securities]]（中邮证券）、[[guoxin-securities]]（国新证券，注意与既有 [[guosen|国信证券]] 区分）。institution House view 更新：[[soochow-securities]]、[[pacific-securities]]。
- 新资产页：[[amat]]（Applied Materials，stub）。资产更新：[[us-treasury-10y]]（+10Y 收 5.021% 新高、2Y 4.725%、10 月加息概率近 60%）。thesis 支撑证据 +1：[[ai-power-ipp-bull]]（IAEA 核电需求上修）。机会更新：[[mu-sndk-memory-upcycle-2026-09]]（+太平洋 AMAT 设备侧佐证、机构 +1）。
- pages touched: 上述 4 源 + 2 新机构 + 2 机构更新 + 1 新资产 + [[us-treasury-10y]] + [[ai-power-ipp-bull]] + [[mu-sndk-memory-upcycle-2026-09]] + [[ceg]]/[[tln]]/[[vst]]（Update history +1、ok×4 不变）、[[2026-09-22]] 简报、index.md、raw/（4 份 pdftotext 抽取文本）、brief/2026-09-22.{html,md}、brief/README.md
- 核实：IAEA 连续第六年上调、2050 高情景 1045GW（去年 992）、2060 高 1284GW/低 696GW ✅（IAEA/World Nuclear News，2025 基准 377.1GW/413 台）；AMAT FY26Q3 营收 ~$9.12B(+25%)、DRAM 含 HBM 封装 +52% YoY 创纪录、Q4 指引中值 $10.25B ✅；8 月零售 +1.2%（预期 0.8%）✅；FOMC 25bp 至 3.75%–4.00%、10Y ~5.02% 新高 ✅（09-17 已核）。⚠️ 东吴柴油 $6.45/加仑高于最近确认值（9/7 $5.967、EIA 9/14 $6.29），点位偏高待核（"创纪录"方向无争议）；⚠️ 东吴 Brent $104.87/WTI $100.30 为周内数（EIA 8 月 Brent 均价 ~$91），未逐日核；⚠️ AMAT EPS 口径——太平洋 GAAP $3.17(+43%) vs 公司非 GAAP $3.50(+41%)，引用须注明。
- invalidation flags: 无变动，三仓 ok×4（无新增 SEC 文件、0 flags；IAEA/AMAT 为需求侧佐证，利率上行属既列利率/融资敏感性风险，均非 Invalidation）。⚠️ 记：东吴指上周美股公用事业领跌（利率驱动的估值波动），本仓 IPP 短期或同此——属估值层面，不触及四条失效条件。
- 未取到的桶：macro 仅 1 篇（国新，其余当日加息复盘与上期重叠）；剔除 09-22 太平洋《新能源+AI·十五五新型电力系统》（中国储能政策/A 股主题，出范围）；外资——Apollo Daily Spark RSS 窗口内无新条目（最新 09-16）、Goldman/MS/BlackRock 客户端页与 All-In 无窗口内新内容——均记"本窗口无新可取外资源"，按"薄简报也好过没有"继续。

## [2026-09-23] brief | AI 行情"1998 而非 2000"——中银 FCF 分化框架 + 华鑫 NVDA/AVGO 硬件端强现金流实证
- sources ingested: 4 — [[2026-09-22-boci-ai-mainline-recheck]]（中银·AI 主线再审视，头条）、[[2026-09-23-huaxin-nvda-rubin]]（华鑫·NVDA FY27Q2）、[[2026-09-23-huaxin-avgo-ai-semi]]（华鑫·AVGO FY26Q3）、[[2026-09-23-dongfang-jincheng-overseas-hike]]（东方金诚·海外周报）
- pages touched: [[2026-09-23]] brief · 4 source pages · institutions [[boci]]/[[dongfang-jincheng]]/[[huaxin-securities]] · assets [[avgo]]（new stub）/[[nvda]]（FY27Q2 + Rubin）· thesis [[ai-power-ipp-bull]]（需求侧硬数据 + 中银利率约束）· positions [[ceg]]/[[tln]]/[[vst]] · index.md
- filings read: 0 — `sec_fetch.py --since 2026-09-22` 三家（CEG/TLN/VST）均 0 新增、0 flags；无新 `raw/` 文件（近日大体量 All-In 转录均为 6–7 月存量、已建源页）
- invalidation flags: 无——三家 Invalidation ok×4 不变（维护性更新）。中银"利率是核心估值约束"+ 东方金诚 10Y 周收 5.01% 属既列利率/融资敏感性风险，非 Invalidation
- opportunities: opportunities_new 0；NVDA/AVGO 为共识大市值、作本仓需求侧佐证，不新建 opportunity
- fact-check ✅: NVDA FY27Q2 营收 $96.2B/DC $89B(+117%)/非GAAP EPS $2.22/Q3 指引 $108B（NVIDIA 官方）；AVGO FY26Q3 营收 $29.59B/AI 半导体 $16.7B(+221%)/FCF $13.7B(46% 营收)/Q4 AI $21.7B（Broadcom 官方）；美国 8 月零售 +1.2%（控制组 +1.4%，Census）；日央行加息至 1.25%/31 年最高/7:2（CNBC）。📌 指引/评级/"1998 vs 2000"框架为投影/判断
- is_change: 仅中银 true（本家由 FOMC 利率视角转入 AI 周期定位/FCF 分化产业框架）；logic_changes 空（非板块评级反转）
- 外资桶：Apollo RSS 窗口内仅存量长文（无 dated 日更）、Goldman/MS/BlackRock/All-In 客户端渲染页无窗口内新内容——记"本窗口无新可取外资源"，按"薄简报也好过没有"继续
- rendered: brief/2026-09-23.html · brief/2026-09-23.md · brief/index.html

## [2026-09-24] brief | 加息落地一周后卖方在"再加几次"上收敛——浦银/五矿"年内再加一次、非连续"、中银配置"中债美股占优"、五矿AI框架把"电力/并网/高速互联"列为海外稀缺基础设施首选、华鑫思科FY2026 AI订单$9.3B/~4.5×
- pages touched: [[2026-09-24-spdb-us-macro-warsh-hike]], [[2026-09-24-wukuang-fed-sep-review]], [[2026-09-24-boci-allocation-china-bonds-us-equity]], [[2026-09-24-wukuang-ai-revolution]], [[2026-09-22-huaxin-cisco-ai-network]], [[wukuang-securities]]（新）, [[csco]]（新）, [[boci]], [[spdb-international]], [[huaxin-securities]], [[ai-power-ipp-bull]], [[ceg]], [[tln]], [[vst]], [[2026-09-24]], index.md, brief/2026-09-24.{html,md}
- sources ingested: 5（宏观 2：浦银·沃什加息周期 / 五矿·Fed 9 月点评；美股策略 2：中银·资产配置月报 / 五矿·AI 革命框架；行业 1：华鑫·思科 AI 网络）。剔除华鑫其余美股光互联/网络点评（Fabrinet/Ciena/Lumentum/Credo/Coherent/Astera/Tower）、开源国产算力、浦银 Muse、信通院太空算力、A 股晨报/北交所/ESG。
- filings read: 0 — `sec_fetch.py --since 2026-09-23` 三家（CEG/TLN/VST）均 0 新增、0 flags。Invalidation ok×4 不变（无监管/合约事件触及四条失效条件）。
- fact-check: ✅ 思科 FY26Q4 $17.3B/+18%、FY26 $63.3B/+12%、非 GAAP EPS $1.22/+23%、AI 基础设施订单 FY26 $9.3B（~4.5×）、FY27 $7.5B、FY27 指引 $72.2–73.4B/+15%、OCF $14.2B（Cisco IR/newsroom+Investing.com/Fierce）；✅ Fed 9 月 +25bp 至 3.75%–4%、12-0、2026/2027 点阵中值 4.1%、16/18 至少再加一次、沃什未提交点（Investing.com/Chase/KuCoin）。📌 12 月加息/年底油价/指引/评级/AI"工业革命级"/capex 收入比 128% 为投影，作情景评估。
- opportunities: 0 new（CSCO 为共识大市值、作本仓需求侧佐证，不新建 opportunity）。
- 外资桶：Apollo RSS 窗口内仅存量长文（无 dated 日更）；Goldman/MS/BlackRock/All-In 无窗口内新内容——记"本窗口无新可取外资源"，按"薄简报也好过没有"继续。
- render: prices.py（CEG 263.88 / TLN 300.34 / VST 137.97）→ render_brief.py 生成 brief/2026-09-24.{html,md} + index.html/README.md/_redirects。
