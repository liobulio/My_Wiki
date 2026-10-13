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

## [2026-09-24] brief | 补录 中信里昂 CLSA·IF26"AI 的最大问题"——逆"2028 见顶"共识、算力短缺持续到 2030（第 6 篇）
- 背景：当日简报首版已发（5 篇、commit 039139e）。同日重跑，`sec_fetch.py --since 2026-09-23` 三家（[[ceg]]/[[tln]]/[[vst]]）仍 **0 新增、0 flags**、无新 `raw/`；东财策略桶（qType=2）午后新上架一篇未 ingested、直贴本仓：[[citic-securities|中信证券经纪(香港)]] 转述中信里昂 CLSA《AI: The biggest questions at IF26》（AP202609241829847586）→ 补入为第 6 篇（`sources_ingested: 5→6`）。宏观桶(qType=3)空；行业桶(qType=1)余项为已录（思科）或既定剔除（Fabrinet/Lumentum/Coherent 光互联、太空算力/A 股）。
- pages touched: [[2026-09-24-clsa-if26-ai-questions]]（new source）· [[citic-securities]]（录入首条 House view + 加 CLSA/中信里昂/CSIWM 别名）· [[amd]]（new stub）· [[nvda]]（CLSA 机架经济性/5–6 年寿命）· [[ai-power-ipp-bull]]（需求侧证据 + $3.5T@2035 ROI 远端约束）· [[2026-09-24]] brief（us_equity +1、headline/方法备注/持仓 note）· index.md · brief/2026-09-24.{html,md} + index.html/README.md/_redirects
- filings read: 0（同上，Invalidation ok×4 不变——CLSA 为需求侧景气框架，不触及四条失效条件）
- fact-check: ✅ 第 33 届 CITIC CLSA Investors' Forum 2026-09-21~24 香港君悦（clsa.com）——CLSA 报告 2026-09-22 落在会期内。📌 模型/投影（算力短缺至 2030、2028 见顶为误、半导体便宜/软件贵、tokens +20× YTD、NVDA 5–6 年经济寿命、$3.5T@2035 ROI）作情景评估、不作真伪核实；方向与 NVDA/AVGO/Cisco 季报强需求一致。⚠️ 文首自述"投资/产品专员撰写、非研报"——作 CLSA 观点二手转述引用。
- is_change: false（[[citic-securities]] 此前无 House view 记录，首条不计为"变化"，与本期 [[wukuang-securities]] 处理一致）；logic_changes 空（非板块评级反转）；opportunities_new 0（NVDA/AMD 为共识大市值、作需求侧佐证，不新建 opportunity）
- render: prices.py（CEG 259.61 / TLN 295.905 / VST 136.68）→ render_brief.py 重生成 brief/2026-09-24.{html,md} + index.html

## [2026-09-25] brief | 以 SEC 文件为主轴——VST 完成 $1.5B 初级次级票据（再融资、非新增杠杆），读全文排除电力/监管误报；研报仅新增南华期货偏鸽注脚"这次加息可能是结束而非起点、连续加息定价过满"；外资桶本窗口无 dated 新内容；SEC 三家 Invalidation ok×4 不变
- SINCE = 2026-09-24（上期简报，独占）。`sec_fetch.py --since 2026-09-24`：[[ceg]]/[[tln]] **0 新增、0 flags**；[[vst]] **1 新增 8-K、1 flag**（accession 0001140361-26-037577，Items 1.01/8.01/9.01）——读全文（`data/sec/text/…txt`，568k 字符）判定为**纯融资/再融资**：完成发行 **$1.5B 初级次级票据（$850M 7.000% Series A + $650M 7.250% Series B，2057、Vistra 担保）**，用途向 Vistra 分配以赎回其 8.0%/7.0% 永续优先股（reset 2026-10/12）。`filings_read: 1`。
- pages touched: [[2026-09-24-vst-8k-junior-subordinated-notes]]（new filing source）· [[2026-09-19-nanhua-macro-fed-hawkish]]（new source）· [[nanhua-futures]]（new institution）· [[vst]]（Update history + updated 09-25，note VST notes 再融资读数）· [[ceg]]/[[tln]]（Update history + updated 09-25）· [[ai-power-ipp-bull]]（supporting evidence + VST ~7% 混合资本读数 + 南华偏鸽注脚，updated 09-25）· [[2026-09-25]] brief（new）· index.md（Briefs/Institutions/Sources）· raw/2026-09-19-nanhua-macro-fed-hawkish.md · brief/2026-09-25.{html,md} + index.html/README.md
- filings read: 1（VST 8-K = 融资事件，terminat×97 / AWS×55 / cancel×30 / PPA×1 / reject×1 全为承销协议 Ex-1.1 与契约 Ex-4.1/4.2 样板条款误报，AWS 为 "laws" 子串假命中；**无电力合约/监管事件触及 [[ai-power-ipp-bull]] 四条失效条件**，ok×4 不变）。同类误报参照 [[2026-07-16-vst-8k-receivables-facility]]。
- 研报选取：仅 1 篇（宏观，[[2026-09-19-nanhua-macro-fed-hawkish|南华期货]]）——继浦银/五矿"年内再加一次、非连续"之后更偏鸽的一家（"这次可能就是结束"、列四结构性约束）。剔除：东财策略桶同日回填的南华两篇过期周报（标注 2026-09-05 非农 / 2026-09-12 通胀，已被后续 FOMC 覆盖）；行业/策略桶其余 09-24 条目昨日已录或出范围。
- 外资桶：Apollo 最新 2026-09-23（Sløk 'Higher for Longer and the Road to 2027'，窗口外）；All-In 最新两集均 2026-09-23（Bending Spoons CEO / Steve Hilton 访谈，非周五主集，窗口外）；Goldman/Morgan Stanley 仅返回 2026 年度 outlook 常青页——记为"本窗口无新可取外资源"，按"薄简报也好过没有"继续。
- fact-check: ✅ VST $1.5B 票据（$850M 7.000% / $650M 7.250%，2057）2026-09-24 完成、用途赎回 8.0%/7.0% 永续优先股（8-K 正文 + TipRanks/Investing.com/PRNewswire/424B5 Use of Proceeds 一致）；✅ 美国联邦债务 2026-08-18 首破 $40T（CNN/NPR/Al Jazeera 2026-08，逼近 $41.1T 上限）；✅ Fed 9 月 +25bp 至 3.75%–4.00%、12-0、点阵中值 4.1%（本 wiki 既有记录一致）。📌 南华"结束而非起点/年内再加或落空/四约束/长端定价信誉"为判断框架，作情景评估、不作真伪核实。
- is_change: false（[[nanhua-futures]] 为新建机构页、无前序记录）；logic_changes 空（VST 8-K 为融资事件、非板块评级反转）；opportunities_new 0（无差异化新买点）。

## [2026-09-25] brief | 复跑补齐：Apollo「higher-for-longer 先压最弱资产负债表、CCC ~15%、move up in quality」+ 华鑫美股 AI 光互联三连（FN/LITE/COHR FY26Q4 大超，✅ 全核验）→ 新机会 ai-optical-interconnect；SEC 三家仍 0 实质、Invalidation ok×4 不变
- 背景：本条为 2026-09-25 同日复跑，补齐上一次运行遗漏的两处——(1) Apollo 今日新篇；(2) 华鑫美股光互联三篇（上次备注误称"昨日已录"，实际此前无源页，本次补录并更正）。`sec_fetch.py --since 2026-09-24` 结果不变：[[ceg]]/[[tln]] 0 新增、0 flags；[[vst]] 1 新增 8-K（已于同日先前录入 [[2026-09-24-vst-8k-junior-subordinated-notes]]）。`filings_read: 1`（不重复读）。
- sources ingested: 5（本条新增 4）——宏观 [[2026-09-25-apollo-daily-spark-higher-for-longer]]（new，Apollo/Slok）+ 行业 [[2026-09-22-huaxin-fabrinet]]/[[2026-09-22-huaxin-lumentum]]/[[2026-09-22-huaxin-coherent]]（new，华鑫）；宏观第二条 [[2026-09-19-nanhua-macro-fed-hawkish]] 沿用上一条已录。
- pages touched: 上述 4 源页 + raw/{2026-09-25-apollo-daily-spark-higher-for-longer, 2026-09-22-huaxin-fabrinet, 2026-09-22-huaxin-lumentum, 2026-09-22-huaxin-coherent}.md · 新资产页 [[fn]]/[[lite]]/[[cohr]] · 新机会 [[ai-optical-interconnect-2026-09]]（status: new，含提案 Edge/Catalyst/Invalidation）· [[apollo]]（House view + Sources，updated 09-25）· [[huaxin-securities]]（House view 光互联三连 + Sources，updated 09-25）· [[2026-09-25]] brief（重写 macro=2/industry=1/opps=1）· index.md（Briefs/Opportunities/Assets/Sources）· brief/2026-09-25.{html,md} + index.html/README.md
- filings read: 1（同上条 VST 8-K = 融资事件、误报标记；无电力/监管事件触及 [[ai-power-ipp-bull]] 四条失效条件，ok×4 不变）。
- fact-check: ✅ 华鑫光互联三家 FY26Q4 数字逐点对照各家 8-K（SEC）核验通过——FN 收入 $1,315.8M/+45%、GAAP 净利 $139.3M、non-GAAP EPS $4.10、数据中心 $669M/+68%/占 51%、FY26 $4.64B/EPS $14.09；LITE 收入 $1.006B/+109.3%、non-GAAP EPS $3.23、$7.756B 一次性非现金债务清偿损失、毛利率 50.4%、FY26 $3.014B/+83.2%；COHR 收入 $2,045.5M/+33.8%、GAAP EPS $1.19、non-GAAP EPS $1.74/+74%、DC&Comms $1.615B/+58.6%/占 79%、营业利润率 21.8%（⚠️ 注意数据中心-only YoY +66% vs 合并段 +58.6% 两种口径，研报用合并段、正确）。📌 Apollo「CCC 收益率 ~15%」为宏观图表叙事，作情景读数、不作真伪核实。
- is_change: false（[[apollo]] 延续其 2026-09-07 质量偏好；[[huaxin-securities]] 延续 AI 硬件看多；[[nanhua-futures]] 无翻转）；logic_changes 空；opportunities_new 1（[[ai-optical-interconnect-2026-09]]）。
- 外资桶：All-In 无新周五主集（最新 2026-09-23 Bending Spoons CEO）；Goldman/Morgan Stanley 无 dated 新内容；Apollo 今日新篇已录。

## [2026-09-28] brief | 持仓 VST 的 Catalyst 直接兑现：Luminant–New Era 20 年 207 MW 天然气 PPA（Odessa 燃气厂表后直供，追进一手 8-K）+ 德州暂停州级数据中心许可（列 watch）；SEC 三家 0 新增、ok×4 不变；Apollo·Warsh 无前瞻指引 / 国信实际利率成核心变量（10Y 5.2%）
- SINCE = 2026-09-25（上期简报，独占）；09-26/27 周末。SEC `sec_fetch.py --since 2026-09-25`——[[ceg]]/[[tln]]/[[vst]] 均 **0 新增、0 flags**。
- sources ingested: 4——宏观 [[2026-09-28-apollo-daily-spark-warsh-rate-hike]]（Apollo/Slök, new）+ [[2026-09-27-guosen-multiasset-hike-nasdaq-gold]]（国信, new）+ 行业 [[2026-09-27-soochow-power-shortage-aidc]]（东吴缺电周报, new）+ 文件 [[2026-09-21-newera-8k-vistra-luminant-ppa]]（New Era 8-K, filings_read=1）。
- pages touched: 上述 4 源页 + raw/{2026-09-27-soochow-power-shortage-aidc, 2026-09-27-guosen-multiasset-hike-nasdaq-gold, 2026-09-28-apollo-daily-spark-warsh-rate-hike}.md（New Era 为 EDGAR 文件、raw=EDGAR URL）· [[apollo]]/[[guosen]]/[[soochow-securities]]（House view 各加 dated bullet）· 持仓 [[ceg]]/[[tln]]/[[vst]] Update history + updated 09-28（ok×4 不变）· 论点 [[ai-power-ipp-bull]]（新增 Catalyst 兑现证据 bullet、updated 09-28）· [[2026-09-28]] brief（macro=2/industry=1/us_equity=0/opps=0）· index.md（Briefs/Sources）· brief/2026-09-28.{html,md} + index.html/README.md/_redirects · prices（CEG 263.27 / TLN 304.42 / VST 138.46）
- filings read: 1（[[2026-09-21-newera-8k-vistra-luminant-ppa]]，交易对手方 New Era 8-K Ex-99.1；线索来自东吴缺电周报，遵循 news=线索、citation=文件）——**Catalyst 型正面事件**、无失效条件触及，VST invalidation ok×4 不变。
- invalidation flags: 无触及。⚠️ 新增 **watch 观察项**（记录于持仓 note/论点，未改 invalidation_status）：德克萨斯州暂停新的州级数据中心许可——对存量已并网发电资产中性偏正（巩固 firm 电力稀缺）；仅当演化为对新增用电负荷的系统性限制、拖慢数据中心落地节奏，才属 Invalidation #1（hyperscaler 合约推迟）上游风险。
- fact-check: ✅ Luminant–New Era 20 年 / 保底 200 MW / 至多 207 MW / Odessa 1,180 MW 燃气厂表后直供 / 27Q3 商供 / Vistra 5% 权益 + ROFR/ROFO / Midland 493 英亩 1.4 GW——New Era 8-K Ex-99.1 与 DataCenterDynamics/Latitude Media/Nasdaq/Yahoo Finance 逐点一致；✅ 国信 美债 10Y 本周 +16BP、伦敦金现 -2.01% 与市场方向一致；Apollo Warsh 沟通/措辞（"a dose of accommodation"、无前瞻指引）经 CNBC 多篇佐证。📌 缺电指数为东吴自建口径、作情绪读数。
- is_change: false（[[apollo]] 延续 higher-for-longer/move up in quality；[[guosen]] 延续加息后利率路径不确定性框架；[[soochow-securities]] 缺电周报为事件跟踪、未反转板块评级）；logic_changes 空；opportunities_new 0（东吴推荐为 A 股缺电链、Apollo/国信为宏观；既有 [[ai-optical-interconnect-2026-09]] 本期无新增背书、维持 new）。
- 未取/受限：All-In **Ep 290（2026-09-26 周五主集，AI 恐慌叙事/Anthropic·OpenAI 推迟 IPO/开源竞争）**——关联偏弱且 transcript 未在本次运行取得，**未 ingest，留待下期/human 补 transcript**；Apollo Daily Spark 正文 JS 渲染未整篇抓取（据索引+CNBC 佐证复原、已在源页透明标注）；东财桶另有大量 A 股晨报/北交所/端侧 AI/港股消费出范围条目未取。

## [2026-09-28] brief | 补扫周一新研报3篇——华鑫「高位美债和AI催化博弈」(10Y破5.2%但顶部5–5.2%、美股哑铃) + 太平洋 LITE FY26Q4 $1.01B/+109%(第二家光互联实证→ai-optical-interconnect升watching) + 太平洋 AMD Q2 数据中心$6.72B/+107%(MI350，需求侧硬数据)
- pages touched: [[2026-09-28-huaxin-us-rates-ai-barbell]], [[2026-09-26-pacific-lite-optical]], [[2026-09-26-pacific-amd-datacenter]], [[huaxin-securities]], [[pacific-securities]], [[amd]], [[ai-optical-interconnect-2026-09]], [[2026-09-28]] (brief), index.md, brief/2026-09-28.{html,md}
- sources ingested: 3 (补扫，累计本日 7)；filings read: 0 new (SEC --since 2026-09-28 仍 0 新增、ok×4 不变)
- note: 同日首轮brief已发(SINCE=2026-09-25)；东财API当日晚间新增周一研报，本轮补录同日内容(append，未覆写)。opportunities_new 仍 0(既有机会获第二家背书、升watching、非新开)。fact-check ✅ AMD $11.5B/+50%·DC $6.7B/+107%·GAAP GM 54%对SEC 8-K逐点核验；LITE数据与已核FY26Q4一致；⚠️华鑫「10月加息>70%」略高于CME ~64–67%。

## [2026-09-29] brief | 需求侧超大规模云长期用电蓝图——东吴海外算力周记阿里云栖大会「2032年全球数据中心超20GW」+ AIDC对电力系统性拉动(真武V900/Qwen4，✅TechNode核实)；新入库民银国际海外宏观周报(10Y 5.17%/周+16bp、10月加息时点提前，✅CNBC佐证)；SEC三家0新增0flags、ok×4不变
- pages touched: [[2026-09-29-soochow-overseas-compute-alibaba-20gw]], [[2026-09-28-cmbc-intl-overseas-macro-rates]], [[cmbc-international]] (new), [[soochow-securities]], [[us-treasury-10y]], [[ai-optical-interconnect-2026-09]], [[ai-power-ipp-bull]], [[ceg]], [[tln]], [[vst]], [[2026-09-29]] (brief), index.md, brief/2026-09-29.{html,md}
- sources ingested: 2 (宏观1: 民银国际·海外宏观周报第37期; 行业1: 东吴·海外算力周·阿里20GW)；filings read: 0 (SEC --since 2026-09-28: CEG/TLN/VST 均 0 新增、0 flags、ok×4 不变)
- note: 新建机构页 [[cmbc-international]](民银国际，origin domestic，首次入库)。opportunities_new 0——东吴/民银推荐或为A股或宏观、无新开US标的；既有机会 [[ai-optical-interconnect-2026-09]] 获第三家(东吴 ECOC 2026 CPO/NPO点名Coherent/Lumentum)背书、status维持watching。fact-check ✅ 阿里2032年20GW/真武V900(M890的3倍)/Qwen4训练中经TechNode/KuCoin/cloudcomputing-news核实；民银10Y 5.17%(9/25收)/+16bp/10月加息概率抬升与CNBC(周五触及5.23%、2007以来最高、10月~64%)方向量级一致；⚠️民银数据表Brent现货$66.36与正文"油价高位"矛盾、疑字段错位。未取：Apollo公共feed最新2026-09-23无新Daily Spark；raw/内6个All-In YouTube转写(2026-06/07加入、无源页)为历史backlog、超本日窗口、留待专门补录。

## [2026-09-29] brief | 同日复跑补扫——太平洋(张世杰)海外AI半导体景气三连(Intel DCAI $6.26B/+59%、Teradyne $1.33B/+104%/半导体测试+128%、ADI $4.02B/+40%/通信+75.7%，✅全核验)作firm电力需求侧景气佐证；SEC三家CEG/TLN/VST --since 2026-09-29仍0新增0flags、ok×4不变；无新开机会
- pages touched: [[2026-09-28-pacific-intel-datacenter]], [[2026-09-28-pacific-teradyne-test]], [[2026-09-28-pacific-adi-analog]], [[intc]], [[ter]], [[adi]], [[pacific-securities]], [[ai-optical-interconnect-2026-09]], [[2026-09-29|briefs/2026-09-29]], index.md, brief/2026-09-29.html+md
- sources ingested: 3 (太平洋 Intel/Teradyne/ADI 点评，均东财 API 命中·pdftotext·raw 保存·web 核实)
- filings read: 0 (sec_fetch --since 2026-09-29：CEG/TLN/VST 均 0 新增、0 flags)
- invalidation flags: 无变化，[[ceg]]/[[tln]]/[[vst]] ok×4
- note: 复跑发现earlier run(SINCE=2026-09-28)未覆盖的3篇2026-09-29 US-equity点评(Intel/TER/ADI单股景气)；均为回顾性需求侧实证、非组合标的、非买入机会；sources_ingested 2→5

## [2026-09-30] brief | 持仓 TLN 一手 8-K：CEO 交接（Terry Nutt 2027-01-01 任 CEO）+ PJM 已出清容量货币化 ~$15亿（Citi/SOFR+200bps、仅容量不含电量）+ $15亿 uncollared ASR（回购逾10%流通股、SRP→$30亿、净杠杆3.5×）——资本回报+接班、无电力合约/监管事件、terminat×121/AWS×19 flags 全为雇佣协议误报、ok×4 不变、方向中性偏正；新入库中邮·海外宏观周报（30Y 5.5252%/2004以来新高、10Y ~5.23%）+浦银·策略月报（高利率下靠盈利兑现、双向注脚）；太平洋 Marvell FY27Q2 数据中心 $2.17B/+46%/1.6T出货（光互联电芯片侧旁证，✅官方核）
- pages touched: [[2026-09-29-tln-8k-capacity-monetization-ceo]], [[2026-09-29-cpost-overseas-macro-yields-rising]], [[2026-09-30-spdb-monthly-strategy-earnings-resilience]], [[2026-09-28-pacific-marvell-optical]], [[mrvl]], [[tln]], [[positions/tln|tln-position]], [[ai-power-ipp-bull]], [[ai-optical-interconnect-2026-09]], [[china-post-securities]], [[spdb-international]], [[pacific-securities]], [[2026-09-30]], index.md, log.md, brief/2026-09-30.html + .md
- sources ingested: 4（1 filing TLN 8-K + 3 research：中邮海外宏观周报 / 浦银策略月报 / 太平洋 Marvell）
- filings read: 1（TLN 8-K 2026-09-29，accession 0001622536-26-000074，Items 5.02/7.01/8.01/9.01——读全文）
- SEC：`sec_fetch.py --since 2026-09-29`——CEG 0 新增/0 flags、VST 0 新增/0 flags、TLN 1 新增/6 flags（读全文判为资本回报+接班、无实质电力事件）
- invalidation flags raised: 无。CEG/TLN/VST 均 ok/ok/ok/ok（不变）
- fact-check（✅）：TLN Terry Nutt CEO/$15亿 ASR/SRP→$30亿/$15亿 PJM 容量货币化（6.5+6.0GW/Citi/净杠杆3.5×）经 Talen IR+GlobeNewswire+rttnews 逐点核实；Marvell FY27Q2 $2.74B/+37%、DC $2.17B/+46%/占79%、FY27 指引~$12B(~45%)/DC~60% 官方核实；中邮 30Y 5.5252%(2004高)/10Y ~5.23% 与民银/CNBC 方向一致
- opportunities_new: 0（TLN 8-K 为持仓维护；ai-optical-interconnect 获 Marvell 电芯片/DSP 侧旁证、非新增券商、status 维持 watching）
- 未取：Apollo feed 顶部 "Higher for Longer and the Road to 2027"（无 pubDate、同 higher-for-longer 主线、无边际、略过）；太平洋 Amphenol/国信华鑫 A 股 AI 应用周报等出范围

## [2026-09-30] brief | 同日补扫（第二次跑）——需求侧 Amphenol +55% + 银河期货美联储10月加息核
- pages touched: [[wiki/briefs/2026-09-30]]（sources_ingested 4→6、macro+1/industry+1）, [[2026-09-28-pacific-amphenol-connectors]], [[2026-09-30-galaxy-futures-fed-oct-commodities]], [[aph]]（新建）, [[galaxy-futures]]（新建）, [[pacific-securities]], [[ai-power-ipp-bull]], index.md
- sources ingested: 2（行业一 [[2026-09-28-pacific-amphenol-connectors|太平洋·安费诺 Amphenol FY26Q2]]、宏观一 [[2026-09-30-galaxy-futures-fed-oct-commodities|银河期货·美联储10月通胀补考]]）
- filings read: 0（本次补扫无新增 SEC 文件；`sec_fetch.py --since 2026-09-29` 仍为 CEG 0/VST 0/TLN 1（已于第一次跑读毕），Invalidation ok×4 不变）
- fact-check（✅）：Amphenol FY26Q2 收入 $8.76B/+55%（record、超一致 5.5%、订单 $10.7B/book-to-bill 1.23）经官方+媒体核；⚠️ EPS 官方调整后 $1.35（太平洋列 ~$1.4）、通信 +85% 为含 CommScope 并购总口径（有机 +42%）。银河期货 9/17 加息 25bp 至 3.75%–4.00%（2023 以来首次）/12:0/点阵图年内再一次+2027 不降息/沃什偏鹰 经 CNBC/Schwab/美联储声明核
- invalidation flags raised: 无。CEG/TLN/VST 均 ok/ok/ok/ok（不变）
- opportunities_new: 0（Amphenol 为 [[ai-optical-interconnect-2026-09]] 连接器/线缆侧旁证、非新增券商、status 维持 watching；非新开机会）
- 说明：第一次跑将 Amphenol 记为"需求侧已饱和"略过，补扫改判入库（继 Marvell/ADI/Intel/Teradyne 后连接器/线缆侧独立第三方景气实证）；华鑫计算机周报（GPT-6/Claude Opus 5.5、腾讯云 Agent/GPU 租金）偏中国 AI 应用 digest、出核心范围，未取

## [2026-10-01] brief | 清淡一日：Apollo·Slök「Everyone Is Talking About AI」——AI 话术近历史高位、hype 跑在 payoff 前；SEC 三家 0 新增/0 flags、ok×4 不变
- pages touched: [[2026-10-01-apollo-daily-spark-everyone-talking-ai]]（新建 source + raw）, [[apollo]]（House view 加 10-01 bullet）, [[ai-power-ipp-bull]]（加 10-01 需求侧远端约束注脚）, [[ceg]]/[[tln]]/[[vst]]（Update history 加 10-01、updated→2026-10-01、ok×4 不变）, [[2026-10-01]]（brief 页）, brief/2026-10-01.{html,md} + index.html + README.md, index.md, log.md
- sources ingested: 1（[[2026-10-01-apollo-daily-spark-everyone-talking-ai|Apollo·Slök Daily Spark「Everyone Is Talking About AI」]]，外资/macro+industry）
- filings read: 0（`sec_fetch.py --since 2026-09-30`：CEG 0 新增/0 flags、TLN 0/0、VST 0/0）
- opportunities new: 0（Apollo 系降温式风险提示、非买入逻辑；既有 [[ai-optical-interconnect-2026-09]] 本期无新增券商背书、status 不变）
- invalidation flags: 无变化（ok×4）。Apollo AI-ROI 怀疑论（"hype>payoff"、69% 采用/29% 量化、价值链 41% 依赖 -59%）记为本仓 **Invalidation #1（超大规模云电力合约推迟/取消）的上游**远端提示——无电力合约推迟/取消实证，不触发
- note: 10/01 中国国庆、东财研报桶无窗口内新内容；09-30 浦银/银河/中邮/太平洋 Amphenol+Marvell 已于 09-30 简报入库（infoCode 核对）。剔除华鑫计算机周报（GPT-6/Claude Opus 5.5，AI 应用 digest 出范围）、All-In 最新集（09-30 Jake Paul/Chainsmokers 嘉宾访谈，低信号）、Apollo "Higher for Longer and the Road to 2027"（经核 2026-09-23 出窗口、主线重复）。硬数据✅：标题/要点句经 apollo.com 两次抓取一致，69%/29%/2%、41% vs -59% 经 Apollo 同系列页佐证；⚠️ 本日图表精确百分比 JS 未取数、以"近历史高位"定性

## [2026-10-01] brief | 同日补扫（第二次跑）：追入一手 FERC 令——PJM Reliability Backstop Procurement 暂缓五个月，持仓 CEG/TLN Invalidation #2（FERC/PJM）由 ok→watch
- pages touched: [[ferc]]（新建机构页，regulator/domestic）, [[2026-09-29-ferc-pjm-backstop-suspension]]（新建 source filing + raw 编译文本）, [[ceg]]（Update history + invalidation_status #2 ok→watch）, [[tln]]（Update history + invalidation_status #2 ok→watch）, [[vst]]（Update history、维持 ok×4）, [[ai-power-ipp-bull]]（加"监管通道首个具体事件"evidence bullet）, [[2026-10-01]]（brief 页：headline 加同日补扫段、industry 桶加 FERC VIEW、三持仓 note+invalidation_status 更新、方法备注、frontmatter sources_ingested 1→2）, brief/2026-10-01.{html,md} + index.html + README.md, index.md, log.md
- sources ingested: 1（[[2026-09-29-ferc-pjm-backstop-suspension]]，FERC eLibrary accession 20260929-3099，source_type filing）。本日累计 2。
- filings read: 0 SEC 文件——`sec_fetch.py --since 2026-10-01` CEG/TLN/VST 均 0 新增/0 flags；复核 `--since 2026-09-28`：CEG 0、TLN 1（无关的容量货币化 8-K，已于 09-30 读毕）、VST 0 → **无公司 8-K 报送该 FERC 事件**，故引一手 FERC 令而非新闻（news is a lead）。`sec_fetch` 全文检索端点 403。
- opportunities new: 0
- invalidation flags: **CEG/TLN Invalidation #2（核电增容/共址被 FERC/NRC/PUC 监管限制）ok→watch**；VST 维持 ok×4。判别：FERC 2026-09-29 接受但暂缓 PJM「Reliability Backstop Procurement」五个月（生效 2027-02-28、附退款+paper hearing）、PJM 撤回 9/30 拍卖（~6,831 MW）、三处判可能 unjust and unreasonable（成本分摊/输电商退出/LSE 抵押），CEG/NRG/TLN 股价当日跌、TD Cowen 称"renewed (and acute) uncertainty"——属 Invalidation #2 所指 FERC/PJM 通道迄今最具体事件（非 hit：暂缓的是 backstop 采购机制，且 CEG/VST 本是其 Joint Stakeholder 共同提出方，未限制任一自身增容/共址协议）。VST 维持 ok：ERCOT/德州为主、共同提出方、firm 电力敞口（Odessa 表后直供）不依赖 PJM backstop。co-location 规则另案、预计 2027 Q1–Q2 出令，下期优先盯。
- note: 外资 feed（apolloacademy.com RSS）无 10/01–10/02 新 Daily Spark；对持仓做定向新闻扫（Yahoo/Benzinga「CEG, NRG, TLN… FERC Delays PJM's Plan」）追入一手 FERC 令。raw/ 中 6 个未入库 All-In 转写（AI Sovereignty Wars 等）经核均为 2026-06/07 旧集、与 09 月以来日度简报节奏不匹配、出同日补扫范围，未取。硬数据✅：FERC 令日期 2026-09-29/accession 20260929-3099、5 个月暂缓至 2027-02-28、撤回 9/30 拍卖、~6,831 MW、三处 flagged issues、Swett 原话、Joint Stakeholder 作者（Constellation/Vistra/AlphaGen/Earthrise）——Utility Dive/Bloomberg/EnergyConnects/RTO Insider/mgrid.org/pjm.com 多源核。

## [2026-10-02] brief | CEG Catalyst 兑现：Amazon–Calvert Cliffs 20 年 PPA（690 MW 含 190 MW uprate），持仓 Invalidation 不变
- pages touched: [[2026-09-30-ceg-amazon-calvert-cliffs-ppa]], [[2026-10-02-apollo-daily-spark-payrolls-no-longer-weak]], [[apollo]], [[ceg]]（asset+position）, [[ai-power-ipp-bull]], [[2026-10-02]], index.md, log.md, brief/2026-10-02.{html,md}
- sources ingested: 2——①[[2026-09-30-ceg-amazon-calvert-cliffs-ppa]]（公司新闻稿、published 2026-09-30、上期未覆盖、因直接关涉 [[ceg]] Catalyst/Invalidation 本期追入）：CEG 与 Amazon 签 20 年 PPA、Calvert Cliffs 供电 690 MW（含 190 MW uprate）、>$3B 全厂投资、~190 MW 新无碳容量 2030–2032 上线、支持再延寿 20 年、电量照旧全进 PJM 电网（非 co-location）✅ 公司稿+6 家媒体核；②[[2026-10-02-apollo-daily-spark-payrolls-no-longer-weak]]（Apollo·Slök、macro）：breakeven 就业~200k→近 0、+90k 为稳健、higher-for-longer。
- filings read: 0——`sec_fetch.py --since 2026-10-01` CEG/TLN/VST 均 0 新增/0 flags（`--since 2026-09-28` 复核：CEG 0、TLN 1 为已读 9/29 容量货币化 8-K、VST 0）→ 无对应 Calvert Cliffs 8-K，故引公司一手新闻稿（news is a lead）。`sec_fetch` 全文检索端点 403。
- opportunities new: 0（Calvert Cliffs 为持仓 Catalyst 事件、非机构新开买入逻辑；Apollo 为宏观注脚）
- invalidation flags: 无变化——[[ceg]]/[[tln]] 维持 ok/watch/ok/ok（#2 watch 缘于 9/29 FERC/PJM backstop、本期无新进展）、[[vst]] 维持 ok×4。Calvert Cliffs 的 grid-connected 结构（非 co-location）对 CEG Invalidation #2 为缓释/偏正但未触及阈值、未改状态。
- note: 外资 feed——apolloacademy.com RSS 最新仍 09-30「Infrastructure」（出窗口）；Apollo 10-02 Daily Spark 经 apollo.com 抓取入库。Goldman/MS/JPM/BlackRock 本周无触及持仓/板块的窗口内新策略。东财桶 10/02 因中国国庆（10/1–8）无 US/AI/电力条目（策略桶均 A 股 PMI/财政/北交所、宏观桶 0、行业桶 16 条无匹配）。FERC co-location 程序经核无 10 月新进展（最近 2026-06、预计 2027 Q1–Q2 出令）、下期续盯。硬数据✅：Calvert Cliffs 690/190 MW、20 年、>$3B、2030–2032、1,790 MW 全厂、"continue flowing to the PJM regional grid" 原话——ENR/NucNet/Fox/ANS/Maryland Matters/StockTitan 六源核。

## [2026-10-02] brief | 同日补扫（第二次跑）：全渠道零新增——SEC 三家 0/0、FERC 自 9/29 暂缓令后无新令、Invalidation 全线不变，补齐 TLN/VST 持仓页至 2026-10-02
- pages touched: [[2026-10-02]]（brief 方法备注+同日补扫块）, [[ceg]]（position）, [[tln]]（position）, [[vst]]（position）, log.md, brief/2026-10-02.{html,md}
- sources ingested: 0——重跑无新源。外资 feed：Apollo RSS 最新仍 09-30「Infrastructure」（10-02 Daily Spark 首跑已入库）、All-In 最新仍 09-30「Jake Paul & The Chainsmokers」（名人访谈、低信号、10-01 已剔、本日 RSS 无周五新集）、Goldman/MS 经 WebSearch 复核窗口内无新策略（命中均旧稿）。东财三桶 10/02 零窗口匹配（策略 5 行/宏观 0 行/行业 16 行均不含 US/AI/电力关键词，中国国庆 10/1–8 续）。
- filings read: 0——`sec_fetch.py --since 2026-10-02` CEG/TLN/VST 均 0 新增/0 flags（与首跑一致）。
- opportunities new: 0。
- invalidation flags: 无变化——对 Invalidation #2 watch 主线定向追查：FERC/PJM backstop 自 2026-09-29 暂缓令（[[2026-09-29-ferc-pjm-backstop-suspension]]）后**无新令**；媒体（247WallSt「VST 115% upside」、techi「PJM delay puts contracts first」）为 lead、非一手文件、不入库。[[ceg]]/[[tln]] 维持 ok/watch/ok/ok、[[vst]] 维持 ok/ok/ok/ok。
- note: 本次仅补齐首跑遗留——首跑只更新了 [[ceg]] 持仓页 Update history（brief-data 的 TLN/VST 10-02 note 已写、但持仓页 Update history 与 `updated` 仍停在 10-01），本次为 [[tln]]/[[vst]] 补 2026-10-02 bullet 并将 `updated` 置 2026-10-02。sources_ingested=2（均首跑）/filings_read=0/opportunities_new=0 不变。

## [2026-10-05] brief | VST 融资展期 8-K（非电力合约）+ 太平洋核电框架/国信需求验证/东吴非农/All-In 电网——Invalidation 全线不变（CEG/TLN ok/watch/ok/ok、VST ok×4）
- pages touched: [[2026-10-05]]（brief）· [[2026-10-05-vst-8k-commodity-credit-amendment]] · [[2026-10-03-pacific-nuclear-dispatchable]] · [[2026-10-02-guosen-ai-demand-verification]] · [[2026-10-03-soochow-sept-payrolls]] · [[2026-10-02-all-in-superintelligence-gdp]] · [[ceg]] · [[tln]] · [[vst]] · [[ai-power-ipp-bull]] · [[pacific-securities]] · [[guosen]] · [[soochow-securities]] · [[all-in-podcast]] · index.md · brief/2026-10-05.html+md
- SINCE = 2026-10-02（上期简报日，独占）。
- sources ingested: 4——①[[2026-10-03-pacific-nuclear-dispatchable|太平洋·核电是长期机会]]（东财行业桶，框架：瓶颈转向可调度供电/长期看核电/AI 用电只能落在可调度电源上）②[[2026-10-02-guosen-ai-demand-verification|国信·AI 投资进入需求验证期]]（东财行业桶，需求验证=#1 上游 + "北美数据中心建设受电力/劳工约束"=背书电力 binding constraint）③[[2026-10-03-soochow-sept-payrolls|东吴·9 月非农]]（东财策略桶，macro：+2.9 万软/失业率 4.2%，但加息降温仅一时、美债回吐）④[[2026-10-02-all-in-superintelligence-gdp|All-In 10-02]]（外资 podcast，podscripts 转录要点：AI 建设史上最大押注/美国电网 25 年持平/数据中心即公用事业）。
- filings read: 1——`sec_fetch.py --since 2026-10-02`：[[vst]] 1 新增 8-K（[[2026-10-05-vst-8k-commodity-credit-amendment]]，Items 1.01/2.03/9.01）读全文判定为 **Commodity-Linked 对冲循环信贷第十一次修订、循环到期日 2026-09-30→2027-09-29 一年期展期**，credit agreement×125/AWS×41/PJM/ERCOT/FERC 等 flags 全为信贷协议定义与样板条款误报、无电力合约/监管事件/非新增杠杆，不触任一失效条件；[[ceg]] 2 新增均 Form 4（内部人、仅列示、不深读）；[[tln]] 0 新增/0 flags。
- fact-check: ✅ 9 月美国非农 +29,000（预期区间 84k–95k）、失业率升至 4.2%、7+8 月合计下修 60,000、时薪 +0.1%/同比 +3.0%（CNBC/Bloomberg/Babypips 一致，东吴所引与官方一致）。太平洋/国信为框架与行业判断（projection/背景数据）；All-In GDP 数字为主持人口述框架（"8 月非农 +162k" 已被 9 月报告下修、标注旧值）。
- opportunities new: 0——四源无新开 US 标的买入逻辑（国信点名阿里-W/爱芯元智为中国/港股、出本仓范围；All-In 无具体 pick）。
- invalidation flags: 无变化——FERC/PJM backstop 自 2026-09-29 暂缓令后无新令、CEG co-location 程序（预计 2027 Q1–Q2 出令）无进展 → [[ceg]]/[[tln]] 维持 ok/watch/ok/ok、[[vst]] 维持 ok/ok/ok/ok。
- 未取/剔除：Apollo RSS/Daily Spark 页最新仍 09-30「Infrastructure」/10-02「payrolls」（已入库）、10-03/10-04 周末无新 Spark；Goldman/MS WebSearch 仅返回 2026 Outlook 旧稿（出窗口）、JPM/BlackRock/Bridgewater/PIMCO/KKR/Blackstone 无窗口内触及持仓/板块新策略；东财桶逢中国国庆（10/1–8）命中多为 A 股 PMI/工业利润/光伏/风电/军工周报，仅上述 3 篇匹配 US/AI/电力。
- note: sources_ingested=4 / filings_read=1 / opportunities_new=0。

## [2026-10-05] brief | 同日补扫（第二次跑）：全渠道零新增——SEC 复跑同首跑、外资 feed 与东财三桶无窗口内新内容、太平洋「算电协同」A 股产业链政策周报判出范围，Invalidation 全线不变
- pages touched: [[2026-10-05]]（brief 方法备注+同日补扫块）, [[ceg]]（position）, [[tln]]（position）, [[vst]]（position）, log.md, brief/2026-10-05.{html,md}
- sources ingested: 0——重跑无新源。外资 feed：apolloacademy.com RSS 最新仍 09-30「Infrastructure」长文、无 10-03–10-05 Daily Spark；Goldman/MS/JPM/BlackRock/Bridgewater/PIMCO/KKR/Blackstone 公共页无窗口内触及持仓/板块的新稿。东财三桶 10-03–10-05：策略桶命中仅 [[2026-10-03-soochow-sept-payrolls|东吴非农]]（已入库）、宏观桶 0 行、行业桶命中 [[2026-10-03-pacific-nuclear-dispatchable|太平洋核电]]（已入库）+ 新见 **太平洋「算电协同配套政策逐步完善，重视产业链长期机遇」**（AP202610031830126544，与核电篇同日同所）判为 **A 股电新产业链政策周报**——China 供给侧/政策口径、无 US 持仓增量且已被太平洋核电框架篇覆盖，**出范围不入库**；上海证券 Meta 智能眼镜（端侧 AI）出范围。
- filings read: 0——`sec_fetch.py --since 2026-10-02` 复跑同首跑：[[ceg]] 2 新增均 Form 4（内部人、仅列示）、[[tln]] 0、[[vst]] 仅首跑已读的融资展期 8-K（[[2026-10-05-vst-8k-commodity-credit-amendment]]），本跑无新增 8-K/10-Q/10-K。
- opportunities new: 0。
- invalidation flags: 无变化——FERC/PJM backstop 自 2026-09-29 暂缓令（[[2026-09-29-ferc-pjm-backstop-suspension]]）后仍**无新令**、CEG 独立 co-location 程序（预计 2027 Q1–Q2 出令）无进展。[[ceg]]/[[tln]] 维持 ok/watch/ok/ok、[[vst]] 维持 ok/ok/ok/ok。
- note: 首跑 sources_ingested=4 / filings_read=1 / opportunities_new=0 维持不变；本次仅为三持仓补一条「同日补扫（第二次跑）」Update history 备查 + 在 brief 方法备注追一条第二次跑说明，并重渲染。

## [2026-10-06] brief | CEG Catalyst 第三次兑现——Google 20 年 PPA（890 MW uprate）+ 15 年 2,700 MW 供电，并网结构绕开 co-location，Invalidation 全线不变
- pages touched: [[2026-10-06-ceg-google-nuclear-uprate-ppa]]（新源）, [[ceg]]（asset）, [[ai-power-ipp-bull]]（thesis）, [[positions/ceg|ceg-position]], [[positions/tln|tln-position]], [[positions/vst|vst-position]], [[2026-10-06|brief]], index.md, log.md, brief/2026-10-06.html+md
- SINCE = 2026-10-05（上期简报日、独占）。
- sources ingested: 1——由新闻线索（utilitydive/gurufocus/Benzinga「Google–Constellation nuclear deal」）**追入一手联合新闻稿**（Google Cloud Press Corner + blog.google）：[[2026-10-06-ceg-google-nuclear-uprate-ppa]]。CEG 与 Google 2026-10-06 盘前签两段式长约——① 20 年 PPA 兜底 11 台自有核电机组 uprate 新增 890 MW（IL/PA/NJ）、>$4.3B 投资、首台增容 2028；② 15 年供电协议锁 PJM 内 2,700 MW 存量产能；另附 5 年 Google Cloud/Gemini 技术联盟。**电量全部进 PJM 电网（并网、非 co-location/非表后）**。✅ 全核（Google 官方新闻稿 + mugglehead/gurufocus/investing.com/Benzinga 一致）；⚠️ PPA 价/容量成分/15 年供电定价未披露、uprate 逐台 NRC 时点未给、无对应 8-K（按 Calvert Cliffs 同例以公司一手新闻稿为一手源）。
- filings read: 0——`sec_fetch.py --since 2026-10-05`：[[ceg]] 0 新增、[[tln]] 0、[[vst]] 1（accession 0001140361-26-038468，为 10-05 已读并入库的融资展期 8-K [[2026-10-05-vst-8k-commodity-credit-amendment]]、因 --since 含当日被标 is_new、本跑非新内容、不重复深读）。
- 机构研究侧零新增（macro/industry/us_equity 三桶空、honest 非 padding）：中国国庆（10/1–8）续，东财三桶 --since 2026-10-05 仅命中 A 股口径（北大经研所「调结构」、东兴晨报、东吴「有色金属周报：美元指数强势」）全部出范围；Apollo RSS 最新仍 09-30「Infrastructure」、无 10-03 后 Daily Spark；Goldman/MS（WebSearch 复核）/JPM/BlackRock/Bridgewater/PIMCO/KKR/Blackstone 公共页无窗口内触及持仓/板块新稿；All-In 下集预计 10-09 未出。
- opportunities new: 0——CEG–Google 属持仓 Catalyst 兑现（记入 positions）、非机构板块观点反转；无机构在窗口内新开 US 标的买入逻辑。logic_changes: []。
- invalidation flags: 无变化——CEG–Google 为并网结构、对 Invalidation #2 缓释/偏正，但不解决 9/29 FERC/PJM backstop 暂缓（推至 2027-02-28）与独立 co-location 程序（预计 2027 Q1–Q2），且 890 MW uprate 自身仍需 NRC 批准 → [[ceg]] 维持 ok/watch/ok/ok；[[tln]] 同业间接利好、维持 ok/watch/ok/ok；[[vst]] 维持 ok/ok/ok/ok。
- note: sources_ingested=1 / filings_read=0 / opportunities_new=0。下期优先盯：①CEG–Google 是否补 8-K（Item 1.01）②890 MW uprate 逐台 NRC 审批时点③FERC/PJM backstop 2027-02-28 复效 + 独立 co-location 程序（2027 Q1–Q2）。

## [2026-10-06] brief | 同日补扫（第二次跑）：全渠道零新增——SEC 复跑同首跑、定向追查 CEG–Google 长约仍无对应 8-K、外资 feed 与东财三桶无窗口内新内容，Invalidation 全线不变（CEG/TLN ok/watch/ok/ok、VST ok×4）
- pages touched: [[positions/ceg|ceg-position]], [[positions/tln|tln-position]], [[positions/vst|vst-position]], [[2026-10-06|brief]]（补第二次跑方法备注）, index.md, log.md, brief/2026-10-06.html+md（重渲染）
- SINCE = 2026-10-05（同首跑、独占）。
- SEC：`sec_fetch.py --since 2026-10-05` 复跑同首跑——[[ceg]] 0 新增、[[tln]] 0、[[vst]] 1（accession 0001140361-26-038468、为 10-05 已读的融资展期 8-K [[2026-10-05-vst-8k-commodity-credit-amendment]]、本跑非新内容）。`filings_read=0`。
- 定向追查：**CEG–Google 两段式长约是否补 8-K（Item 1.01）**——EDGAR 全文检索端点 403、CEG 自 10-05 起 EDGAR 0 新文件、WebSearch 亦未定位到对应 8-K（CNBC 口径「3.6 GW」= 890 MW uprate + 2,700 MW 存量供电），故 [[2026-10-06-ceg-google-nuclear-uprate-ppa]] 仍以公司一手联合新闻稿为一手源、下期续查。
- 机构研究侧复核仍零：Apollo RSS 最新仍 09-30「Infrastructure」、无 10-04–10-06 Daily Spark；Goldman/MS/JPM/BlackRock/Bridgewater/PIMCO/KKR/Blackstone 公共页与 All-In（下集预计 10-09）无窗口内触及持仓的新稿；东财三桶 10-05–10-06 命中仅北大「调结构」预测报告、东兴晨报、东吴「有色金属周报：美元指数强势」——全 A 股/非 US-equity、判出范围不入库。
- invalidation flags: 无变化——[[ceg]] ok/watch/ok/ok · [[tln]] ok/watch/ok/ok · [[vst]] ok/ok/ok/ok。三持仓 Update history 均补第二次跑 bullet。
- note: sources_ingested=1 / filings_read=0 / opportunities_new=0（维持首跑值）。下期优先盯：①CEG–Google 是否补 8-K（Item 1.01）②890 MW uprate 逐台 NRC 审批时点③FERC/PJM backstop 2027-02-28 复效 + 独立 co-location 程序（2027 Q1–Q2）。
## [2026-09-28] maintenance | 持仓变更：TLN 全部清仓，VST / CEG 各减仓一半
- pages touched: [[tln]], [[vst]], [[ceg]], [[index]]
- 人工提供的持仓变更，按 §3.5「positions 是人的真实账本」照录，未改动任何未经告知的数字：
  - **TLN 5.407 → 0**，`status: open → closed`，新增 `closed: 2026-09-28`
  - **VST 11.523 → 5.7615**（算术一半）
  - **CEG 5.891 → 2.9455**（算术一半）
- ⚠️ 两项数据缺口，等人补：
  1. **卖出日期与成交价均未提供** → 三笔已实现盈亏无法计算，`entry_price` 本就为空，现在连出场价也没有，这三个持仓的真实收益率目前**无法从 wiki 重建**。
  2. VST/CEG 的 5.7615 / 2.9455 是按「一半」推算的；若实际卖到整数股，余额需要更正。
- ⚠️ 需要人来判断（§3.8：conviction 归人，不归我）：TLN 是三只 AI-power IPP 里唯一被**完全**清掉的，而它 6→9 月 −18% 的原因从 09-11 起挂到现在仍未追溯到 catalyst。若清仓是因某条 Invalidation 被触发，[[ai-power-ipp-bull]] 的 `status` 与 `invalidation_status` 需要一并更新——我没有替你改，目前仍为 ok×4。
- note: 减仓后组合仍 100% 集中在同一个 [[ai-power-ipp-bull]] 论点上（VST+CEG），**集中度未因减仓而分散，只是规模减半**。

## [2026-10-06] maintenance | 持仓更正：买入 09-09 高点、减仓/清仓日为 09-14
- pages touched: [[ceg]], [[vst]], [[tln]] (positions), [[index]]
- 人工更正：三只均在 **2026-09-09 当日最高点**买入，TLN 清仓与 CEG/VST 减半发生在 **2026-09-14**（此前 9/28 条目记的是录入日）。`entry_price` 按 Yahoo 日线 9/9 盘中高回填：CEG $298.08 · VST $151.56 · TLN $326.09；TLN `closed` 改为 09-14，CEG/VST 加 `trimmed: 2026-09-14`。
- ⚠️ 9/14 卖出成交价仍缺 → 已实现亏损只能给区间（CEG ~$64–99、VST ~$36–64、TLN ~$122–218），待 IBKR 成交记录补准。

## [2026-10-06] query | CEG/VST 是否仍低于重置成本（止盈判断）
- pages touched: NEW [[ceg-vst-replacement-cost-2026-10-06]], [[index]]
- note: wiki 此前无人工重置成本估算（仅 Dreyfus 的 TLN $45B）。新建口径（论点原框架）CEG EV/RC ~0.3–0.6、VST ~0.4–0.75 → Edge 未被价格用完；按存量电厂成交价口径 CEG ~0.8–1.1、VST ~1.0–1.4。EV 用 10-06 盘中价（Google 长约当日 CEG +11.8%）+ 2026-06-30 10-Q XBRL。

## [2026-10-06] ingest | CEG / VST / TLN 重置成本研究总结（人自己的研究）
- pages touched: NEW [[2026-10-06-ceg-vst-tln-replacement-cost-summary]]; REWRITTEN [[ceg-vst-replacement-cost-2026-10-06]]; UPDATED [[replacement-cost-investing]], [[ai-power-ipp-bull]] (risks), [[ceg]], [[vst]], [[tln]], [[index]]; raw moved from repo root → `raw/2026-10-06-ceg-vst-tln-replacement-cost-summary.md`
- fact-check: ✅ shares/debt/cash/NCI/preferred/TLN NDT $1,997M via SEC XBRL; ⚠️ VST debt $20,508M vs XBRL LTD $19,595M (+$913M unreconciled); ⚠️ "10-06 close" was intraday; ➕ missing comp LS Power–CEG 4.4 GW ~$1,136/kW (2026-03); ➕ Cogentrix FERC-approved Aug 2026, closing late 2026.
- note: supersedes the LLM's quick estimate from earlier today. Applied to the book: CEG ~0% / VST +5% vs entry; +$299 to anchor A vs −$979 to anchor D; post-trim book ~$1,800 ≈ the study's half-Kelly $1,600 at μ=15%.

## [2026-10-06] maintenance | 成交价由人补齐
- pages touched: [[ceg]], [[vst]], [[tln]] (positions), [[ceg-vst-replacement-cost-2026-10-06]], [[index]]
- 人给定：CEG 买 $294 / 09-14 减仓 $265 · VST $151 / $141 · TLN $322 / $289 清仓 → 取代按 9/9 盘中高的回填。已实现 −$321.47（CEG −$85.42 · VST −$57.62 · TLN −$178.43）；剩余仓位浮盈 +$61（CEG +1.4% · VST +5.7%）。

## [2026-10-06] query | 以锚点 A 为退出线的剩余盈利空间
- pages touched: [[ai-power-ipp-bull]] (exit anchor), [[ceg]], [[vst]] (positions `exit_anchor`), [[ceg-vst-replacement-cost-2026-10-06]]
- 人选定退出锚点 A（Q=1 保守新建）：CEG $375 · VST $172。按 15:29 ET 价（CEG $297.20 / VST $158.61）剩余空间 CEG +$229（+26.2%）· VST +$77（+8.4%）· 合计 +$306（+17.1%）；若双双到 A，含 09-14 已实现 −$321 整段净 ≈ +$38。μ 为 5–30% 任选值、不作预测。

## [2026-10-06] maintenance | 简报显示距退出锚点 A 的距离
- pages touched: `scripts/render_brief.py`, `tests/test_render_brief.py`, CLAUDE.md §3.5, `brief/2026-10-06.{html,md}`, `brief/index.html`
- 持仓卡新增一行：距 `exit_anchor` 还差 %（≈ $）+ 买入→锚点进度条；到达后变黄色"已到退出锚点 A"。Markdown 手机版同步。新增 `anchor_info()` + 测试；schema 加 `exit_price` / `exit_anchor` 字段。
- 顺手修复：持仓备注 `<p class="note">` 内嵌 `<p>` 导致的空白备注条（改为 `<div>`）。今日简报按真实持仓重渲染（CEG 2.9455 / VST 5.7615，TLN 已移出）。

## [2026-10-07] brief | 10 月 Fed 加息路径内资分歧 + 需求侧 AI 硬件续强；SEC 零新增、Invalidation 全线不变
- pages touched: [[2026-10-07-soochow-holiday-overseas-rates]], [[2026-10-07-boci-us-inflation-demand]], [[2026-10-07-guosen-sept-payrolls]], [[2026-10-07-soochow-overseas-compute-ai-hardware]], [[soochow-securities]], [[boci]], [[guosen]], [[us-treasury-10y]], [[ai-power-ipp-bull]], [[ceg]], [[vst]], [[2026-10-07]], index.md, brief/2026-10-07.{html,md}
- sources_ingested: 4（均东财研报中心渠道）· filings_read: 0 · opportunities_new: 0
- SEC：`sec_fetch.py --since 2026-10-06` CEG 0 新增（27 kept）/ VST 0 新增（31 kept）/ TLN 已清仓（status closed、0 股）；三家 `is_new` 均空。CEG–Google 两段式长约仍无对应 8-K（Item 1.01），维持一手联合新闻稿为源、下期续查。
- 主线（macro 三 VIEW）：10 月 Fed 路径内资分歧——**东吴**据 BEA 年度修订（26Q1/Q2 GDP 上修 0.4/0.7pp、PCE 下修，✅ 核）+ 弱非农判"10 月或跳过加息"（is_change=true、较本家 10-03 偏鸽）；**中银**反向判"四季度仍存加息空间"（居民收入韧性 + AI 投资支撑通胀，把 AI capex 列为联储鹰派理由）；**国信**居中——FedWatch 10 月加息概率骤降至 19%、10Y ~5.20%，但"政策航向难改"。假期 10Y 一度破 5.3%——长久期 PPA 现金流利率敏感性既列风险双向注脚、非 Invalidation。
- 需求侧（industry 1 VIEW）：东吴海外算力周——台系 CCL 9 月营收翻倍（台光电子 215.32 亿新台币/+168.9% YoY，✅ 核）、Rubin 平台 PCB 层数/材料代际升级、Q4 AI 服务器加速批量交付——数据中心建设/用电未退坡的第三方实证。
- fact-check：BEA 2026 年度修订（Q2 GDP +0.7pp→2.2%、Q1→2.5%、PCE −0.3pp）✅、台光电子 2026-09 营收 +168.87% ✅、9 月非农 +2.9 万/失业 4.2% ✅（与 10-03 东吴、官方一致）；各家 10 月政策预测为 projection、记入双向观测。
- us_equity 空（honest，假期回顾篇归 macro）；`logic_changes: []`、`opportunities_new: 0`。出范围未入库：东财大量 A 股口径研报、Apollo 无 10-04 后新 Daily Spark、Goldman/MS/JPM 仅年度展望、All-In 下集预计 10-09。
- Invalidation flags：无新增。CEG ok/watch/ok/ok（#2 缘于 9/29 FERC/PJM backstop，无新令；890 MW uprate 仍需 NRC）· VST ok/ok/ok/ok（ERCOT 为主、不依赖 PJM backstop）。

## [2026-10-07] brief | 同日补扫（第二次跑）——全渠道零新增、Invalidation 全线不变
- pages touched: [[2026-10-07]], [[ceg]], [[vst]], brief/2026-10-07.{html,md}, log.md
- SEC：`sec_fetch.py --since 2026-10-07` 复跑同首跑——CEG 0 新增（27 kept）/ VST 0 新增（31 kept）/ TLN 已清仓；三家 `is_new` 均空、`filings_read=0`。
- 定向续查 CEG–Google 两段式长约 8-K（Item 1.01）：CEG 自 10-05 起 EDGAR 仍 0 新文件、无对应 8-K，[[2026-10-06-ceg-google-nuclear-uprate-ppa]] 维持一手联合新闻稿为源、下期续查。
- 外资公共 feed（Apollo 最新仍 09-30「Infrastructure」、Goldman/MS/JPM/BlackRock/Bridgewater/PIMCO/KKR/Blackstone、All-In 下集 10-09）无窗口内触及持仓新稿；东财三桶 10-07 复查无新增在范围 US-equity 稿（命中国信四季度展望/多资产周报、开源各周报、国金计算机系列、对外经贸大学贸易月报等均 A 股/非 US-equity，维持出范围）。
- Invalidation flags：无新增。CEG ok/watch/ok/ok · VST ok/ok/ok/ok。两持仓 Update history 均补第二次跑 bullet；`sources_ingested=4/filings_read=0/opportunities_new=0` 维持首跑值。

## [2026-10-07] maintenance | daily-brief skill 写明退出锚点
- pages touched: `.claude/skills/daily-brief/SKILL.md`
- 渲染层 10-06 起已自动显示"距退出锚点 A"（10-07 两次跑的 `brief/2026-10-07.{html,md}` 均含），但 routine 写的头条/持仓备注没提。现要求：备注开头写距锚点距离；≤5% 进头条；到达则头条以 ⚠️ 打头；锚点需重算时只提议、不改 `exit_anchor`（`exit_*` 列入不可改字段）。

## [2026-10-07] maintenance | VST 退出计划：到锚点 A 再减仓一半
- pages touched: [[vst]] (positions `exit_plan`), `scripts/render_brief.py`, `tests/test_render_brief.py`, CLAUDE.md §3.5, daily-brief SKILL, `brief/2026-10-07.{html,md}`
- 人定：VST 到 `exit_anchor`（$172）时再减仓一半（5.7615 → 2.88075）。简报持仓行显示"到达后：…"，到达时显示"按计划：…"并进头条。

## [2026-10-08] brief | ⚠️ VST 临近退出锚点 A（+3.2%）+ FOMC 9月纪要偏鹰；SEC 近零新增
- pages touched: [[2026-10-08]] (brief), `brief/2026-10-08.{html,md}`, `brief/README.md`/`index.html`, [[2026-10-08-donghai-futures-fomc-minutes-hawkish]], [[2026-10-08-ajian-us-sept-payrolls]], [[ajian-securities]] (new institution), [[donghai-futures]] (house view), [[ceg]] + [[vst]] (Update history + invalidation_status 复核), index.md, data/prices.json, data/sec/*.json
- SINCE=2026-10-07。SEC `sec_fetch --since 2026-10-07`：CEG 0 新增（27 kept）· VST 1 新增=Form 4（0001728553-26-000008、report_date 2026-10-06、0 items/0 flags、仅列示不深读）· TLN 已清仓。`filings_read=0`。
- 退出锚点 A（prices.py 后）：⚠️ **VST $166.72 → 距 $172 仅 +3.2%（≤5%，头条已 ⚠️ 提示 + 附 exit_plan「到锚点再减仓一半 5.7615→2.88075」）**；CEG $299.59 → 距 $375 +25.2%。两锚点基于 2026-06-30 BS、11-06 Q3 10-Q 后需重算（仅提议）。
- 新增 2 源（东财渠道、均 macro）：①东海期货梳理 **FOMC 9 月会议纪要**——全票 9 月加息、多数官员年内或再加一次、偏鹰；纪要**把"强劲 AI 投资或增加需求压力"列为上行通胀风险**（✅ Bloomberg/Chase/CNBC 多源核，纪要 10-07 美东发布），与中银 10-07 同源同向。②爱建证券（新机构页）9 月非农点评"年内加息概率仍较高"（12 月加息 25bp 概率仍较高、Fed 全年失业率 4.3%→4.1%）。
- CEG–Google 两段式长约仍无对应 8-K（Item 1.01）、CEG 自 10-05 起 EDGAR 0 新文件——维持一手联合新闻稿为源、下期续查。industry/us_equity 空（honest）、logic_changes=[]、opportunities_new=0。出范围未入库：诚通/交银国际/东海证券/西南/华金等多家非农/宏观 digest 口径重复，择增量最大的 FOMC 纪要 + 爱建收录；Apollo 最新仍 09-30、外资 js houses 仅年度展望、All-In 下集 10-09 未出。
- Invalidation 全线不变：CEG ok/watch/ok/ok（#2 缘于 9/29 FERC/PJM backstop，无新令；890 MW uprate 待 NRC；co-location 程序 2027 Q1–Q2 无进展）· VST ok/ok/ok/ok（ERCOT 为主、不依赖 PJM backstop）。sources_ingested=2 / filings_read=0 / opportunities_new=0。

## [2026-10-08] brief | 第二次跑（同日补扫）：方正中期"市场定价 3–4 轮加息/10Y 5.29% 2002 新高/AI 发债抢资本"入库 + IPP 随 10Y 新高回落（VST 退出锚点 proximity 由 +3.2% 松回 +10.5%）
- pages touched: [[2026-10-08]] (brief：macro 桶加第 3 条 VIEW、头条/备注重写、追加「同日补扫」节、sources_ingested 2→3), `brief/2026-10-08.{html,md}`, `brief/README.md`/`index.html`, [[2026-10-08-fangzheng-zhongqi-global-macro-oct]] (新 source), [[fangzheng-zhongqi-futures]] (新机构页), [[us-treasury-10y]] (current view + 10Y 5.29%), [[ceg]] + [[vst]] (Update history 补第二次跑 bullet + 价/锚点距离更新), index.md, data/prices.json
- SINCE=2026-10-08。SEC 复跑 `sec_fetch --since 2026-10-08`：CEG 0 新增（27 kept、is_new 空）· VST 0 新增（32 kept、is_new 空；首跑 Form 4 已不在窗口）· TLN 已清仓。`filings_read=0`，同首跑。
- **价格第二次跑重取（prices.py）**：两只利率敏感 IPP 随 **10Y 美债冲多年新高**同步回落——CEG $299.59→**$282.34（−5.8%）**、距 $375 **+32.8%**；VST $166.72→**$155.72（−6.6%）**、距 $172 **+10.5%**。晨间 VST 曾 +3.2%（≤5%、头条 ⚠️），午后回落后**已离开 ≤5% 区间**——头条/备注改写、去 ⚠️ proximity 领起；`exit_plan`（再减仓一半 5.7615→2.88075）维持事先承诺、俟再触 $172 由人确认执行。两锚点基于 2026-06-30 BS、11-06 Q3 10-Q 后需重算（仅提议）。
- 新增 1 源（东财渠道、macro、新机构页）：方正中期期货月度《全球宏观经济 2026-10》"最棘手问题在于国债"——本窗口**最鹰**：利率互换/CME 定价美联储 **3–4 轮加息**、远高于 9 月点阵图"再加一轮至 4–4.25%"；全球国债抛售潮、**10Y 美债 5.29%（2002-06 以来新高）**，把 **"AI 企业争抢资本/AI 发债抢资本"列为长端收益率攀升主因之一**；美国 Q4 G7 增速最快、全年 2–2.25%、8 月 PPI +5.4%。✅ web 核：8 月 PPI +5.4%（由 7 月 4.8% 升、高于预期 5.3%、环比 +0.4%，BabyPips/Crypto Briefing/NCH）；10Y 10-07 触及 5.34–5.35%（2002 以来最高）、10-08 回落 ~5.27%，Yahoo/CNBC/Forbes **明确印证"AI 基础设施建设抽离债市资金、推高增长与长期中性利率预期"**——与本报告 AI↔国债归因一致。"3–4 轮"为市场定价 projection，与东吴"10 月或跳过"对立、纳利率风险双向观测（非 Invalidation）。
- 出范围：东财三桶 10-08 另命中东海证券「海外观察：9 月非农技术性反弹后回归」（与已入库爱建/国信/东吴非农同口径、不重复入库）、方正中期中国宏观、国金 A 股策略、国信 ETF、东吴黄金 ETF/电力设备周报、开源/华鑫等——A 股/非 US-equity 或同口径 digest。Apollo RSS 仍 09-30「Infrastructure」、外资 js houses 仅年度展望、All-In 下集 10-09（周五）未出。
- Invalidation 全线不变：CEG ok/watch/ok/ok（#2 缘于 9/29 FERC/PJM backstop、无新令；890 MW uprate 待逐台 NRC；co-location 程序 2027 Q1–Q2 无进展）· VST ok/ok/ok/ok（ERCOT 为主、不依赖 PJM backstop）。sources_ingested=3 / filings_read=0 / opportunities_new=0。

## [2026-10-09] brief | 中期选举(2026-11-03)→AI基础设施/数据中心监管收紧：新政策风险面(Invalidation #1上游watch)；SEC近零新增、退出锚点远未触及
- pages touched: [[2026-10-09]]（brief）· [[2026-10-09-soochow-us-midterm-elections]] · [[2026-10-09-cpost-overseas-macro-yields-tech]] · [[2026-10-09-guojin-ai-capture-value]]（新源）· [[soochow-securities]] · [[china-post-securities]] · [[guojin-securities]]（House view）· [[ceg]] · [[vst]]（Update history + invalidation_status）· [[ai-power-ipp-bull]]（Risks 新增中选政策风险）· index.md · brief/2026-10-09.{html,md}
- SINCE = 2026-10-08（上期简报日，独占）。`sec_fetch.py --since 2026-10-08`：[[ceg]] **0 新增 8-K/10-Q/10-K、0 flags**（27 filings kept）· [[vst]] **1 新增 = Form 4**（accession 0001940494-26-000008、filed 2026-10-08、0 items/0 flags，按 SKILL 仅列示、不深读）· [[tln]] 已清仓。`filings_read=0`。CEG–Google 两段式长约仍无对应 8-K（Item 1.01）——CEG 自 10-05 起 EDGAR 0 新文件，[[2026-10-06-ceg-google-nuclear-uprate-ppa]] 维持一手联合新闻稿为源、下期续查。
- **本期核心增量 = 新政策风险面**：两家内资**独立**提出 **2026-11-03 美国中期选举 → AI 基础设施/数据中心建设监管收紧**——[[2026-10-09-soochow-us-midterm-elections|东吴]]宏观深度"左翼民主党上台越多，要求科技企业承担数据中心扩张的电网/电力/环境外部成本、推升单位 capex、约束 AI CAPEX，甚至限制前沿模型训练/数据中心扩张速率"；[[2026-10-09-cpost-overseas-macro-yields-tech|中邮]]海外周报"若民主党控两院、数据中心建设或面临更严格政策限制、压制相关股票估值"。判定：属 [[ai-power-ipp-bull]] **Invalidation #1（超大规模云电力合约推迟/取消）的上游政策风险**——催化有明确日期（11-03）、方向负面、强度未知、**目前无电力合约推迟/取消实证**，故 [[ceg]]/[[vst]] **#1 维持 ok、新增为 watch 观察项**（已并入 thesis Risks / counter-thesis）；选后视两院控制权与左翼席位再评。
- 退出锚点 A（`prices.py` 后）：[[ceg]] $285.07 → 距 $375 **+31.5%（≈$89.93）**；[[vst]] $156.14 → 距 $172 **+10.2%（≈$15.86）**——均 >5%、无头条 ⚠️（`exit_plan` 对 VST 维持事先承诺、俟再触 $172 由人确认执行）。两锚点基于 2026-06-30 BS、11-06 Q3 10-Q 后需重算（仅提议）。
- 新增 3 源（东财渠道）：①东吴证券·美国中期选举观战指南（macro）②中邮证券·海外宏观周报（macro+equity：资金向 AI 集中/市场广度恶化/看好硬件龙头、年底前或再加息一次、中东地缘能源风险）③国金证券·AI 双视角 捕获率/价值创造率（industry：计算机业捕获率 <10%、总潜在捕获收入 ~$4000 亿，#1 上游变现框架）。
- ✅ web 核实：沙特机场遇袭（Houthi 对利雅得 King Khalid + 阿布哈，10-06/07，**3 死 36 伤**，Al Jazeera/Time/Japan Times/Gulf Business）；8 月 PCE（核心环比 +0.2%/同比 +3.0%、整体同比 +3.4%、名义 +0.9%/实际 +0.6%、储蓄率 4.1%，BEA/CNBC）；9 月非农 +2.9 万/失业率 4.2%（同已入库口径）。中选民调/席位（RCP 226–185、支持率 38.2%）、"年底前仍一次加息"、国金捕获率测算均 projection/模型估算、不作事实核验。
- 出范围：中信证券财富管理(香港)「谁将受益于 AI 建设？」实为**菲律宾房地产**（Pax Silica/吕宋走廊、Ayala/Robinsons/Filinvest Land，非 US）、国信证券「AI 的挤出效应」（荀玉根、正文日期 09-28/29 旧稿重挂、A 股重估口径）、大同市场日报、北大全球流动性、山西 AI 投研系列、上海证券计算机周报、华鑫汽车周报（英伟达投 Figure AI/AMD 收 World Labs）等——A 股/非 US-equity。Apollo RSS 仍 09-30「Infrastructure」、外资 js houses 仅年度展望、**All-In 最新仍 10-02「Super Intelligence Summit…」（已入库）、周五新集未出**。
- `logic_changes: []`（无板块观点反转）；`opportunities_new: 0`（中邮"看好美股硬件龙头"为板块 tilt、非单一标的买入逻辑，不另开 opportunity 页）。Invalidation 全线不变：[[ceg]] ok/watch/ok/ok · [[vst]] ok/ok/ok/ok。sources_ingested=3 / filings_read=0 / opportunities_new=0。

## [2026-10-09] brief | (第三次跑·补扫) 万联"10月按兵不动"+国信"AI挤出效应/特朗普9项AI行政令现状顺风反向锚"入库(sources 3→5)；prices.py重取盘中价 CEG $285.07→$298.95(+4.9%·距$375 +25.4%)·VST $156.14→$159.57(+2.2%·距$172 +7.8%)；SEC/Invalidation全线不变
- pages touched: [[wiki/sources/2026-10-09-wanlian-us-sept-payrolls]], [[wiki/sources/2026-09-29-guosen-ai-crowding-out]], [[wiki/institutions/wanlian-securities]], [[guosen]], [[ai-power-ipp-bull]], [[ceg]], [[vst]], [[wiki/briefs/2026-10-09]], [[index]], raw/×2, data/prices.json, brief/2026-10-09.{html,md}
- 本次为同日**第三次跑**（上两次已入库东吴中选+中邮海外周报+国金 AI 双视角 3 源）。本跑补扫东财 10-09 新命中、择 2 入库（均 macro、非 Invalidation）：
  - [[2026-10-09-wanlian-us-sept-payrolls|万联证券]]（新机构页 [[wanlian-securities]]）：9 月非农 **+2.9 万**（预期 8.9 万、前值 13.3 万）、失业率 4.2%、时薪同比 +3.02%、前两月下修 6 万；判就业偏弱但可控、**基准情形 10 月按兵不动**——偏鸽/跳过侧，与 [[2026-10-07-soochow-holiday-overseas-rates|东吴]]"或跳过"同侧、与 [[2026-10-09-cpost-overseas-macro-yields-tech|中邮]]"年底前再加一次"/[[2026-10-08-ajian-us-sept-payrolls|爱建]]/[[2026-10-07-boci-us-inflation-demand|中银]]/[[2026-10-08-donghai-futures-fomc-minutes-hawkish|东海]] 对立，纳利率双向观测；若 10 月不加→长端上行缓解、对长久期 PPA/VST ~7% 新发成本**边际利好**（既列利率敏感性风险、非 Invalidation）。
  - [[2026-09-29-guosen-ai-crowding-out|国信证券]]（荀玉根总量团队，报告日 09-29、10-09 分发扫到）：AI 挤出效应——美国=资本挤劳动（信息技术就业 −3.0% CAGR）；**美股 IPO 募资硅基占 79.3%、美股硅基发债依赖显著上升**（印证 AI 融资虹吸，呼应中邮/方正中期，属 Invalidation #1 上游融资可持续性，ok 不变）；政策端**特朗普 2025 年至今约 9 项 AI 行政令**加码 AI/数据中心基建（含 **EO 14318"加快数据中心基础设施联邦许可"**）——为东吴/中邮中选"监管或收紧"风险提供**现状顺风 vs 未来风险**反向锚（已补入 [[ai-power-ipp-bull]] Risks）。
  - **再评**：首/次跑曾把国信「AI 挤出效应」判"A 股重估口径"而未读入库；本跑读全文后推翻该判定、改为入库（正文含实质 US 口径）。中信证券财富管理(香港)「谁将受益于 AI 建设？」本跑下载原文确认=**菲律宾房地产**（Ayala/Robinsons/Filinvest Land），维持出范围。
- SEC：`sec_fetch.py --since 2026-10-08` 同首/次跑——[[ceg]] **0 新增、0 flags**（27 kept）、[[vst]] **1 新增=Form 4**（0001940494-26-000008、0 items/0 flags、仅列示）、[[tln]] 已清仓。`filings_read=0`。CEG–Google 两段式长约仍无对应 8-K（Item 1.01），[[2026-10-06-ceg-google-nuclear-uprate-ppa]] 维持一手联合新闻稿为源、下期续查。
- `prices.py` 第三次跑重取 2026-10-09 盘中价：[[ceg]] **$298.95**（首跑 $285.07）→ 距 $375 **+25.4%（≈$76.05）**；[[vst]] **$159.57**（首跑 $156.14）→ 距 $172 **+7.8%（≈$12.44）**——均 >5%、无头条 ⚠️。
- ✅ web 核实：9 月非农 **+29k / 失业率 4.2% / 时薪 +0.1%mom·+3.0%yoy**（BLS "Employment Situation 2026 M09"、CNBC 2026-10-02）；特朗普 AI 行政令方向已核（含 EO 14318 加速数据中心许可），精确"9 项"为国信统计口径（❓不逐项核）。
- `logic_changes: []`；`opportunities_new: 0`。Invalidation 全线不变：[[ceg]] ok/watch/ok/ok · [[vst]] ok/ok/ok/ok。sources_ingested=5（累计本日）/ filings_read=0 / opportunities_new=0。

## [2026-10-09] maintenance | 外资桶失血诊断与修复
- pages touched: `brief/sources.yaml`, `.claude/skills/daily-brief/SKILL.md`
- 诊断：09-14 → 10-09 共 20 期简报，观点 内资 72 / 外资 6，6 期外资为 0。原因：①Apollo 用的 apolloacademy.com/feed 自 09-30 冻结（apollo.com Daily Spark 页 10-06–10-09 每日都有新稿）——10 天来被记成"外资无新稿"；②Goldman/MS 标为 js 只走 WebSearch，只搜到年度展望——实测 GS sitemap 有 10-06「30 年美债还会更高吗」、10-08「债券是否更值得配置」，MS HTML 里有「加息环境下的股市」「AI capex」「央行加息」等，均漏掉；③html 页用 WebFetch 常 403/超时，失败被当作"无新内容"；④~12 条预算被东财命中填满，外资又以"未触及持仓"被剔除。
- 修复：Apollo → apollo.com Daily Spark（html）；GS → sitemap-1.xml + lastmod；MS → html + link_pattern；SKILL 改为外资先扫、一律 curl+浏览器 UA、每源一行扫描结果、>5 个工作日无新稿标"疑似失效"、外资至少保留 4 个名额、宏观/利率/AI capex 类外资稿不因"未点名持仓"剔除。

## [2026-10-09] maintenance | 新增 Investing.com 线索源 + All-In 每条视频必上简报 + 暂存未来日报格式
- pages touched: `brief/sources.yaml`, daily-brief SKILL, CLAUDE.md §3.11, `scripts/render_brief.py`, `tests/test_render_brief.py`, NEW [[investing-com]], NEW `docs/future 每日持仓总结.md`, [[index]]
- Investing.com：文章页对脚本 403、原生 RSS 只留最近 10 条 → 主路线为 Google News RSS 限定 site:investing.com（持仓 / 核电·电力·FERC·NRC / Fed·美债三组查询，实测可用，例：10-08「Why is Vistra stock sliding today?」）。进简报新栏目「新闻线索」，持仓相关的逐条追一手并标注已追/未追。
- All-In：`must_show: true`，YouTube 频道每条新视频（正片、峰会、访谈、片段）都进简报新栏目「节目更新」，不过相关性筛选、不占 ~12 条预算；按视频 id 去重而不是按 SINCE 日期（周五下午上传会漏）。云端字幕可能被 YouTube 拦截，拿不到时标"文字稿缺失"照样上。
- 「future 每日持仓总结」8 栏格式按人要求存档于 docs/，status: parked，暂不实施。

## [2026-10-09] brief | 第四次跑·新版式：All-In 6 clip 入节目更新 + Investing.com 新闻线索上线 + 外资补缺高盛长端利率研报
- pages touched: [[2026-10-09]]（brief 改写为新版式 shows+leads）, [[2026-10-06-goldman-30y-treasury-yields]]（新）, [[2026-10-09-all-in-sacks-economy-stronger]]/[[2026-10-08-all-in-calacanis-ai-boom-benefit]]/[[2026-10-08-all-in-daniel-ek-ai-health]]/[[2026-10-06-all-in-friedberg-ai-wars]]/[[2026-10-05-all-in-friedberg-rates-banking-shock]]/[[2026-10-03-all-in-chamath-superintelligence]]（6 clip·新）, [[goldman-sachs]]/[[all-in-podcast]]（机构 house view 更新）, [[ceg]]/[[vst]]（update history + 价重取）, index.md, brief/2026-10-09.{html,md}
- sources ingested: 12（研究 6：高盛 30Y 美债 + 既有东吴中选/中邮/万联/国金/国信；shows 6：All-In 本周 clip）；filings_read: 0
- 版式：本跑把 HEAD 已落地的 shows（节目更新）+ leads（新闻线索）新版式正式应用到 10-09（前三次跑为旧版式）。All-In 本周 6 条 clip（10-03→10-09、`must_show`、按 video id 去重）全收录，**均 ⚠️ 文字稿缺失**（YouTube 转录 API 在 CI 被封、podscripts 无 per-clip 页、描述为模板）——`transcript: false`、仅凭标题归档、不作事实源。
- leads（9 条、持仓头条优先，来自 Investing.com Google News RSS + 原生 RSS）：CEG「BMO 重申/因 Google 跳涨」→追一手 [[2026-10-06-ceg-google-nuclear-uprate-ppa]]；VST 内部人售股（CFO Moldovan $3.3m/president Hudson $3.5m）→已列示 Form 4；CEG/VST 10-08「sliding」→长端美债新高估值回撤、无一手；「Pimco tells FT 10Y 或探 6%」仅媒体转述、不入库为 PIMCO VIEW；「Fed 纪要年内或再加一次」一手已入库（东海）。
- 外资补缺（核心增量）：[[2026-10-06-goldman-30y-treasury-yields]]（foreign·macro）——Qubbaj「长端自定价、联储不护长债；债务漂移非螺旋、30Y 5.5% 历史便宜、有回落至 ~4.25% 空间」，长久期 PPA 现金流利率敏感性既列风险的双向注脚；修补 Goldman 自 2026-05-28 久未入库的外资缺口。
- SEC 宽窗 `sec_fetch.py --since 2026-10-01`：[[ceg]] 仅 2 Form 4（0 flags）、[[vst]] 3 新增＝2 Form 4 + 1 份已读的 10-05 融资展期 8-K（[[2026-10-05-vst-8k-commodity-credit-amendment]]）；无新 8-K/10-Q/10-K 需深读、`filings_read=0`；CEG–Google 长约仍无对应 8-K（Item 1.01）、续查。
- 价（prices.py 重取 2026-10-09）：[[ceg]] $299.37 距 $375 +25.2%（≈$75.63）· [[vst]] $161.07 距 $172 +6.8%（≈$10.93，较三次跑 $159.57 走近、仍 >5% 无头条 ⚠️）。
- Apollo Daily Spark 新 URL（apollo.com/wealth/the-daily-spark）为 JS 渲染、curl 取不到文章链接——本跑未取到新 Slök，下期需换路由/WebSearch 补。
- logic_changes=[]·opportunities_new=0。Invalidation 全线不变：[[ceg]] ok/watch/ok/ok · [[vst]] ok×4。中选政策风险（2026-11-03）维持 Invalidation #1 上游 watch。

## [2026-10-12] brief | 持仓无一手新事件；中选政策风险获两家外资(MS/PIMCO)独立印证(Invalidation #1上游watch)；SEC零新增、退出锚点远未触及
- pages touched: [[2026-10-12]]（brief 新）, [[2026-10-12-lczq-fomc-ai-macro-variable]]（新·联储证券）, [[2026-10-11-soochow-cpi-preview-oil]]（新）, [[2026-10-11-soochow-power-shortage-google-ceg-ppa]]（新）, [[2026-10-10-morgan-stanley-midterm-market-impact]]（新·外资）, [[2026-10-06-pimco-cyclical-outlook-growth-holds]]（新·外资补扫）, [[2026-10-10-all-in-claude-conscious-bond-market]]/[[2026-10-12-all-in-chamath-software-ip-worthless]]/[[2026-10-12-all-in-shkreli-pharma-quantum]]（3 shows·新）, [[lianchu-securities]]（新机构页）, [[morgan-stanley]]/[[pimco]]/[[soochow-securities]]/[[all-in-podcast]]（house view 更新）, [[ai-power-ipp-bull]]（Risks：中选风险 +MS/PIMCO 外资印证）, [[ceg]]/[[vst]]（update history + 价重取）, index.md, brief/2026-10-12.{html,md}
- sources ingested: 8（研究 5：联储证券 FOMC+AI 新宏观变量 / 东吴 CPI 前瞻 / 东吴缺电主线 CEG–Google / 大摩中选 / PIMCO 季度展望；shows 3：All-In 10-10→10-12）；filings_read: 0
- SEC `sec_fetch.py --since 2026-10-09`：[[ceg]] 27 kept / **0 新增 8-K/10-Q/10-K、0 flags**、[[vst]] 33 kept / **0 新增、0 flags**、`filings_read=0`（[[tln]] 已清仓）；[[2026-10-06-ceg-google-nuclear-uprate-ppa|CEG–Google 两段式长约]]仍无对应 8-K（Item 1.01）、维持一手新闻稿为源、下期续查。
- 外资桶（核心增量 2 家）：[[2026-10-10-morgan-stanley-midterm-market-impact|大摩]]"若民主党取得更多国会控制→科技/**能源生产商**政治审视"（点名能源生产商）+ [[2026-10-06-pimco-cyclical-outlook-growth-holds|PIMCO 季度展望]]"AI 相关信用须为**美国中选政治**寻求更高补偿、AI 繁荣褪色列基准风险"（10-06、上期外资扫漏、补扫纳入）——至此东吴/中邮+MS/PIMCO 四家跨内外资/股债独立提出中选政策风险；两家外资同记缓冲（分裂政府/央行可信度）→ Invalidation #1 维持 ok、watch 不变，已并入 [[ai-power-ipp-bull]] Risks。
- 利率/需求读数（非 Invalidation）：[[2026-10-12-lczq-fomc-ai-macro-variable|联储证券]]"9 月 +25bp→3.75–4.00%、偏鹰、AI 投资成新宏观变量"，⚠️ 记 **AI 超大规模云发债信用利差近期小幅改善**＝#1 上游融资可持续性偏正读数；[[2026-10-11-soochow-cpi-preview-oil|东吴]]"10 月加息概率 ~17%、10-14 看 9 月 CPI"（双向观测）；需求侧 [[2026-10-11-soochow-power-shortage-google-ceg-ppa|东吴缺电主线]]复述 CEG–Google 890MW 长约 + Google–Black Hills 怀俄明 $18 亿（✅ 多源核）+ OpenRouter Token +2283%。
- shows：[[all-in-podcast|All-In]] 10-10→10-12 三条新视频（`must_show`、按 video id 去重）——周五正集「Claude 是否有意识 / 债券市场」+ Chamath「软件 IP 一文不值」+ Shkreli「做空量子 / AI 制药」，**均 ⚠️ 文字稿缺失**（youtube-transcript-api 在 CI RequestBlocked、podscripts 无 per-episode 页）、`transcript: false`、仅凭标题/章节归档。
- ⚠️ 弃入：中航证券「美国中期选举下大类资产表现」（AP202610121830339886）PDF 为 CID 字体、pdftotext 全部乱码（年年年）、无法读取原文 → 按"不读不写"弃入（中选主题已由 MS + 东吴覆盖）。
- 价（prices.py 2026-10-12）：[[ceg]] $291.98 距 $375 **+28.4%（≈$83.03）** · [[vst]] $158.60 距 $172 **+8.4%（≈$13.40）**——均 >5%、无头条 ⚠️；锚点基于 2026-06-30 资产负债表、11-06 Q3 10-Q 后重算。
- logic_changes=[]·opportunities_new=0（东吴柴发/燃发为 A 股标的、Citi 两只电力公用股为未读 lead、均不开 opportunity 页）。Invalidation 全线不变：[[ceg]] ok/watch/ok/ok · [[vst]] ok×4。

## [2026-10-12] brief | 同日补扫（第二次跑）：全渠道零新增、仅刷新盘中价重渲染
- pages touched: [[ceg]]/[[vst]]（update history +「同日补扫，第二次跑」条目 + 价重取）, [[2026-10-12]]（brief 价/方法备注更新）, brief/2026-10-12.{html,md}, brief/README.md
- SEC 复跑 `sec_fetch.py --since 2026-10-09` 同首跑：[[ceg]] 27 kept / **0 新增 8-K/10-Q/10-K、0 flags、`is_new` 空**、[[vst]] 33 kept / **0 新增、0 flags**、`filings_read=0`；CEG–Google 两段式长约仍无对应 8-K（Item 1.01）、维持一手新闻稿为源。
- 外资 feed 零新增：Apollo Daily Spark 仍 JS 渲染（curl 空）、Goldman sitemap 无 ≥10-10 新 insights、MS `/ideas` 窗口内仅已入库 [[2026-10-10-morgan-stanley-midterm-market-impact|中选专题]]（"stock-rally-rising-rates-risks" 实为 2026-09-09、窗外）、All-In YouTube 最新三条（yZR8QW4qQmM/TLeh41_uhZ4/TBLHdXABwAg）即首跑已入 shows（无新视频）。
- 东财三桶 10-09–10-12 命中项全为首跑已入库（联储证券 FOMC/东吴 CPI/东吴缺电）或出范围（中航中选 PDF 字体乱码续弃、国金 AI 策略周报/公用事业长协电价/通信 OpenAI ARR、东吴公用事业/电力设备等均 A 股口径或非持仓 US 标的）——确认首跑覆盖完整。
- 价（prices.py 2026-10-12 第二次跑重取）：[[ceg]] **$293.89**（较首跑 $291.98 +0.7%）距 $375 **+27.6%（≈$81.11）** · [[vst]] **$158.095**（较首跑 $158.60 −0.3%）距 $172 **+8.8%（≈$13.91）**——均 >5%、无头条 ⚠️；锚点基于 2026-06-30 资产负债表、11-06 Q3 10-Q 后重算。
- sources ingested: 0（新增）；filings_read: 0；logic_changes=[]·opportunities_new=0。Invalidation 全线不变：[[ceg]] ok/watch/ok/ok · [[vst]] ok×4。中选政策风险（2026-11-03）维持 Invalidation #1 上游 watch。

## [2026-10-13] query | SPCX 反向 DCF + 分部估值
- pages touched: NEW [[spcx-reverse-dcf-sotp-2026-10-09]], [[spcx]], [[index]]
- 数据：Q2 2026 8-K/10-Q（收入 $7.81B +92%、分部、现金 $100B、债务 $39.4B、股数 13,176M + Cursor ~391M、capex $18.4B、backlog $47.5B）；Google/Anthropic 合同与管理层 $100B ARR / 2030 $1T 目标为媒体口径。
- 结论：EV ≈ $2.13T = 68× 收入；现价隐含 10 年 ~37%/年收入增速（若年底达 $100B ARR 则 ~25%/年）；按当前业务分部估值 $30/$52/$88，底 ~$17——无物理托底，锚点是增速而非价格。

## [2026-10-13] maintenance | TLN 转观察名单 + 简报信息过载治理
- pages touched: [[tln]] (positions: status watch, buy_anchor_proposed 322, exit_anchor 403, anchor_floor 157), `scripts/render_brief.py`, `tests/test_render_brief.py`, daily-brief SKILL, CLAUDE.md §3.5/§3.11, `brief/2026-10-12.{html,md}`
- TLN：人要求作为潜在买入对象跟踪。新增「观察名单」栏：现价、距买入线（提议 $322，待人确认）、距锚点 A $403、下方底 D $157。现价 $379.77 → 需再跌 15.2% 才到买入线。
- 过载诊断（10-05→10-12）：手机版 7–12k 字，头条 970–1,634 字，单条观点均 400–640 字，持仓备注 420–990 字，头条里塞满运行元数据。治理：持仓/观察名单前置；头条 ≤3 句 ~150 字、观点 ≤80 字、持仓备注 ≤120 字、节目无关集只写"与持仓无关"、线索 ≤5；运行元数据移到页脚 `run_note`；渲染器新增 LENGTH WARNING，skill 要求清零后再提交。

## [2026-10-13] brief | 持仓无一手事件；TLN 首次纳入观察名单（买入线 $322、未进入区间）；中邮边际转鸽
- pages touched: [[2026-10-13]], [[2026-10-12-cpost-overseas-macro-oct-pause]], [[2026-10-12-all-in-friedberg-ai-religion]], [[china-post-securities]], [[ceg]], [[vst]], [[tln]], index.md, brief/2026-10-13.{html,md}
- SEC `--since 2026-10-12`：CEG 27 / TLN 29 / VST 33 filings kept，三家均 0 新增 8-K/10-Q/10-K、0 flags、is_new 空、filings_read=0。CEG–Google 两段式长约仍无对应 8-K（Item 1.01）、维持一手新闻稿为源。
- sources_ingested=2：①[[2026-10-12-cpost-overseas-macro-oct-pause|中邮海外周报]]（research/macro）引沃勒"加息但不在连续会议"→判 10 月或暂停、12 月再加（本家较 10-09 转鸽）；把 OpenAI 收入低于报道（✅ FT：$50B vs $70B、10-08 Nasdaq −1.25%）的 AI 收入审视 + 中选后监管收紧列短期逆风——Invalidation #1 上游、无实证、#1 ok/watch。②[[2026-10-12-all-in-friedberg-ai-religion|All-In·Friedberg「AI 催生新宗教」]]（shows，⚠️ 文字稿缺失）。
- 外资桶本窗口无新在范围稿：Goldman 最新 insights 10-09（中国 AI 模型）/10-08（bonds）均 ≤SINCE 或非持仓口径；MS 相关 TOTM「AI Safety/Compute Spending」经 WebSearch 核为 2026-09-23（窗外）；Apollo Daily Spark 仍 JS 渲染（curl 空）；PIMCO/KKR/BlackRock/Bridgewater/Blackstone evergreen 或窗外——foreign slot 确无 >SINCE 项、由 domestic 填（按 SKILL）。东财三桶命中多为 A 股/非持仓 US（金元 AI-RSI、中银 TMT 周报、东吴公用事业新质生产力/电力设备等）或已入库；中航「美国中选大类资产」PDF CID 字体乱码续弃。
- leads 5（持仓/板块优先）：Oppenheimer power-tech 首选股（未读原文、不入库）、Fermi–AMD 德州 AI 项目、Oklo DOE 同位素（非本仓）、CPI/财报周预览、油价推升高利率。
- 退出/买入锚点（prices.py 2026-10-13）：CEG $293.89→距 $375 +27.6%；VST $158.13→距 $172 +8.8%（均 >5% 无 ⚠️）；TLN（观察名）$379.77→距买入线 $322 需 −15.2%（未进入买入区间）、距 A $403 −6.1%、距底 D $157 +141.9%。CEG/VST 锚点基于 2026-06-30 资产负债表、11-06 Q3 10-Q 后重算。
- logic_changes=[]、opportunities_new=0。Invalidation 全线不变：CEG ok/watch/ok/ok · VST ok/ok/ok/ok · TLN(watch) ok/watch/ok/ok。中选政策风险（2026-11-03）维持 #1 上游 watch（本期 +中邮再度印证）。render_brief LENGTH WARNING 已清零。
