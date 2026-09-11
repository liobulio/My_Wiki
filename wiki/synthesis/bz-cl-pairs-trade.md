---
type: synthesis
tags: [quant, statarb, pairs-trading, cointegration, oil, mean-reversion]
created: 2026-08-14
updated: 2026-08-23
---

# BZ=F / CL=F (Brent/WTI) pairs trade — statarb research

## TL;DR
Statistical-arbitrage research on the Brent (`BZ=F`) / WTI (`CL=F`) crude
spread. The pair is genuinely cointegrated and is the **only** relationship
found across ~10 equity sectors and 66 futures pairs that survives
out-of-sample — because Brent and WTI are the same commodity at different
delivery points, linked by physical shipping arbitrage.

**Two things changed materially on 2026-08-23** after a 34-fold walk-forward
over 19 years of history:
1. The performance previously reported here came from an **unusually
   favourable window**. Long-run out-of-sample Sharpe is **0.53–0.67 with
   −32% to −34% max drawdown**, not the 1.30–1.86 at −5% to −7% that the
   2024–2026 window showed.
2. The pair is **not tradeable at small account size**. Every execution route
   is now closed; it needs roughly **$189k** to size at half scale.

**Not a position** — no Thesis Test completed (see bottom).

## Adopted strategy
Rolling z-score mean reversion on the **log price ratio** `log(BZ/CL)`:
- **Entry ±1σ, exit at the mean** (z crosses zero), rolling-window statistics.
- **Lookback** from the trailing-2y OU half-life, clipped to [5, 60] days.
- **No β to estimate** — this is the main reason the ratio form was preferred
  over the β-weighted difference (see β instability below).
- No maximum holding period. An acknowledged, unaddressed risk.

Superseded: the earlier adopted rule was the β-weighted **difference** spread
at 2σ in / 1σ out. Both are documented below; the walk-forward found them
statistically indistinguishable, and the ratio was chosen on structural
grounds, not on backtest performance.

### Performance — the honest version
⚠️ **The two windows disagree, and the long one is the relevant one.**

| | 2024–2026 window (as previously reported) | 2009–2026 walk-forward |
|---|---|---|
| ratio 1σ/mean | Sharpe 1.86 · CAGR 27.3% | **Sharpe 0.67 · CAGR 11.0%** |
| diff 2σ/1σ | Sharpe 1.30 · CAGR 13.6% | **Sharpe 0.53 · CAGR 4.9%** |
| Max drawdown | −5% to −7% | **−32% to −34%** |

Walk-forward protocol: 34 folds, 2-year rolling train → 6-month out-of-sample,
β and lookback re-fit per fold on training data only, net of 1.5bps.

**Head-to-head, the two rules are a coin flip.** The ratio rule wins 16 of 34
folds; mean Sharpe difference +0.06; paired t p=0.83, sign test p=0.86,
Wilcoxon p=0.85. Its higher aggregate CAGR comes from *exposure* (75% of days
in market vs 18%), not skill — mean per-fold Sharpe is 0.90 vs 0.84.

### Spread definition vs thresholds — a 2×2 attribution
Stitched out-of-sample, 34 folds:

| | 2σ in / 1σ out | 1σ in / mean out |
|---|---|---|
| **difference** | Sh 0.53 · DD −32.1% | Sh 0.35 · **DD −57.5%** |
| **ratio** | Sh 0.53 · DD −31.5% | Sh 0.67 · DD −33.7% |

Neither factor is a clean main effect — **it is an interaction.** The
aggressive thresholds *help* the ratio (+0.14) and *hurt* the difference
(−0.19, nearly doubling drawdown). The spread swap does nothing at
conservative thresholds (0.53 → 0.53) but is worth +0.32 Sharpe at aggressive
ones.

Mechanically: at matched thresholds the two spreads issue **86.7% identical
positions**; it is the thresholds that change the trading (42.2% agreement,
and exposure 18% → 75% of days). But when you hold 75% of the time, the ~13%
of days where the spreads disagree compound enormously.

## Why the ratio form was adopted — β instability
The decisive finding, and it is structural rather than empirical.

Re-estimating β per fold, **7 of 34 folds landed outside [0.8, 1.2]** (range
0.116 to 1.457, sd 0.228). At β=0.116 in the 2014-07 fold, the "hedged"
difference spread's returns correlated **1.00 with Brent** — a 0.88× outright
long-oil position held ~75% of the time, exactly as crude fell $100 → $50.
That one fold returned −43.9% and drives most of the −57.5% drawdown.

The ratio spread **cannot fail this way**: it has no β to mis-estimate and is
dollar-neutral by construction (correlation −0.02 with Brent in that same
fold). Second independent argument: through both structural-break eras the
ratio stayed marginally stationary while the dollar difference did not.

## Risk: cointegration genuinely breaks for years at a time
| Era | Brent−WTI spread | ADF ratio | ADF difference | ratio half-life |
|---|---|---|---|---|
| 2008–2010 | $0.70 | 0.0056 ✅ | 0.0084 ✅ | 7.6d |
| **2011–2015 shale/Cushing** | **$15–17** | 0.0509 ⚠️ | **0.2762 ❌** | 42d |
| **2016–2019** | $4–7 | 0.0460 ⚠️ | **0.1550 ❌** | 25d |
| 2020–2026 | $3–5 | 0.0000 ✅ | 0.0003 ✅ | 7.3d |

The US shale boom bottlenecked WTI at Cushing and blew the spread from ~$0.70
(2010) to ~$17 (2012). Cointegration broke for roughly five years. **A pair
cointegrated over a 4-year window may be describing a regime, not a law.**

Per-era strategy Sharpe confirms the pattern — and note the fallback ranking:

| Era | diff 2σ/1σ | diff 1σ/mean | ratio 2σ/1σ | ratio 1σ/mean |
|---|---|---|---|---|
| 2011–2015 break | 0.29 | −0.55 | **0.79** | −0.05 |
| 2016–2019 | 1.34 | 1.11 | 1.42 | 1.47 |
| 2020–2026 | 0.30 | 0.67 | 0.17 | **0.84** |

**Regime-switch guidance:** under stress, switch *thresholds* (ratio 1σ/mean →
ratio 2σ/1σ, worth 0.79 vs −0.05 in the break era) — **not** the spread. Moving
to the difference spread reintroduces exactly the β failure above.

Separately: a rolling cointegration test (2yr trailing, weekly re-test) found
the gate closed ~48% of 2024–2026 days — a genuine ~4.5-month breakdown
Feb–Jul 2024 unrelated to any war, plus the Hormuz conflict below. A gated
variant with hysteresis did not clearly improve results and is not adopted.

## Live geopolitical risk — Iran/Hormuz
The Iran–US Strait of Hormuz conflict began 2026-03-04; Iran closed/attacked
shipping through the Strait (~20% of global oil supply) and Brent spiked ~65%
in March, moving far more violently than WTI (economically coherent — Brent is
the internationally-traded benchmark most exposed to Persian Gulf shipping).
**As of 2026-08-21 this is unresolved:** a ceasefire expired 2026-08-17, most
shipowners still avoid the waterway, the US says the Strait is open while Iran
says it is shut, and Brent closed $94.39. Any live signal is being taken
against an active war premium, not the statistical regime the backtest
measured.

## Look-ahead validation — passed
| Test | Result |
|---|---|
| Position builder alone (cutoffs 20/60/120/250) | PASS, 0 mismatches |
| Full walk-forward pipeline incl. per-fold half-life fitting (cutoffs 20–500) | PASS, 0 of up to 4,226 days |
| Deliberately leaky control (full-sample mean/std) | **FAILS, 25 mismatches** ✅ |

The leaky control failing is the load-bearing part — it proves the test can
detect leakage, so the passes mean something.

## Tradability — every route is closed
| Route | Status |
|---|---|
| Full-size BZ + MCL | 1 BZ = $94,390 = **4.72× a $20k account**; needs ~$189k at 0.5× scale |
| USO / BNO ETFs | **Fails cointegration** — ADF p=0.60 full, p=0.051 post-2021 |
| MCL + QM | Both are **WTI** (MCL $87.06, QM $87.05, CL $87.06) — no spread exists |
| ICE Mini Brent + MCL | Product exists (100 bbl) but not practically accessible; IBKR lists only full-size COIL/BZ/BB |

**On USO/BNO specifically:** the ETFs do not inherit the futures'
cointegration. They hold futures and roll on different schedules, injecting a
structural wedge — the USO/BNO ratio drifted **8.11 (2011) → 5.05 (2019) →
2.47 (2024)**. Full-history strategy Sharpe −0.22 / DD −46%. Post-2021 looks
better (Sharpe 0.77) but still fails cointegration (CADF p=0.137/0.125,
half-life 49.8d vs 7.3d for the futures) and dies on costs: Sharpe 0.95 at
1.5bps → 0.50 at 10bps → **−0.06 at 20bps**, against BNO trading only
$19.5M/day. The post-2021 Johansen "rank 2" is degenerate, not support.

**Current recommendation:** paper-trade notionally (track short $10k Brent /
long $10k WTI marked off futures closes). Reproduces real P&L and drawdown,
costs nothing, builds a track record for when capital allows.

## Why the theoretically "optimal" exit underperformed
Tested three escalating attempts to apply [[ou-optimal-exit-rules]]: a fixed
exit from a single Monte Carlo scenario; per-trade entry-conditional exits via
Monte Carlo; and per-trade exits via an original, validated implementation of
the paper's own Volterra/heat-potential solver (matched the paper's Table 1 to
~0.1–0.6% on two of three cases). **All three underperformed the plain
Bollinger baseline.** Best-supported reasons:
- The paper optimizes **E[pnl/τ] for a single isolated trade**, not annualized
  portfolio Sharpe across many sequential trades.
- Exit levels are computed once from **frozen training-period** OU parameters
  and never revisited mid-trade; the rolling rule re-derives its signal daily.
- A precisely-optimal-but-brittle rule loses to a simple adaptive heuristic
  when the assumed model doesn't quite match reality — the same logic behind
  naive 1/N beating mean-variance optimization out of sample.

## Data-snooping accounting
~12 strategy variants have now been scored against overlapping windows. A
Deflated Sharpe check on the ratio rule's 2024–2026 result gave DSR 0.99 →
0.66 depending on assumed cross-trial Sharpe dispersion; at the pessimistic
end it drops below the 0.95 bar. Return skew 6.6 / kurtosis 98 (one +13.25%
war day) makes the Sharpe estimate itself fragile. The walk-forward above is
the more trustworthy evidence precisely because it doesn't depend on one
window.

## ⚠️ P&L convention — unresolved inconsistency
A real bug was found on 2026-08-14: `rets_y − β·rets_x` implicitly represents
a **$1-long vs $β-short dollar position**, not a β-share-ratio position —
harmless at β≈1, badly wrong otherwise (found via GS/WFC at β=6.4 producing a
−93% drawdown that was pure artifact). It was fixed via
`backtest.py::pair_spread_returns`, and that fix was **later reverted at the
human's explicit instruction**.

Consequences to keep in mind:
- The **difference-spread** numbers on this page use the old (reverted)
  convention and are therefore somewhat overstated. Under the corrected
  convention the 2024–2026 figures were CAGR 6.2% / Sharpe 1.14, not
  13.6% / 1.30.
- The **ratio-spread** numbers are **unaffected** — for a scale-free ratio,
  dollar-neutral is the correct convention, so `ret_BZ − ret_CL` is right as
  written. This is a further point in the adopted strategy's favour.

## Data quality
`CL=F` printed a negative close (−$37.63) on 2020-04-20 — the real historic
negative-WTI event. Genuine, but an extreme high-leverage outlier in an OLS
hedge-ratio regression, and `pct_change()` is meaningless once price crosses
zero. Now excluded generically in `cointegration.py::cadf_test` (β shifted
+1.3%; contamination had been working *against* reported results). Verified
on 2026-08-22 that exactly one row is dropped across 2007–2026.

Futures contract-roll costs (the continuous `=F` series hides the cost of
rolling expiring contracts) remain **unmodeled** — a bigger distortion over 19
years than over 2.5. 1.5bps is also likely optimistic for 2009-era futures.

## Not a position
Per this wiki's rule, a position isn't opened until the human supplies **the
Thesis Test** — the Edge, the Catalyst, and specifically the Invalidation.
Given the live Hormuz situation, the documented five-year cointegration
breakdown, and the fact that the position cannot currently be sized at all,
the Invalidation matters more than usual here.

## Related
[[pairs-trade-failure-modes]] · [[micro-futures-universe-screen]] ·
[[multisector-pairs-screen]] · [[ou-optimal-exit-rules]] · [[bz]] · [[cl]]

## Sources
Built with the `statarb-strategy-lab` toolkit. Key scripts:
`walkforward_bz_cl_ratio_vs_diff.py`, `attribution_spread_vs_thresholds.py`,
`lookahead_test_ratio_strategy.py`, `strategy_uso_bno_ratio.py`,
`strategy_bz_cl_ratio_1sigma.py`.
Iran/Hormuz context verified via web search:
- [Strait of Hormuz disruption sends oil prices surging](https://blogs.worldbank.org/en/opendata/strait-of-hormuz-disruption-sends-oil-prices-surging)
- [Al Jazeera — attacks dent Hormuz reopening hopes (2026-08-12)](https://www.aljazeera.com/economy/2026/8/12/oil-prices-rise-as-attacks-dent-hopes-for-strait-of-hormuz-reopening)
- [CNBC — Iran signals it wants war to end (2026-08-21)](https://www.cnbc.com/2026/08/21/oil-prices-us-iran.html)
Contract specs: [ICE Mini Brent (100 bbl)](https://www.ice.com/products/79696476/Mini-Brent-Crude-Futures-100-BBL) ·
[CME Micro WTI](https://www.cmegroup.com/markets/energy/crude-oil/micro-wti-crude-oil.contractSpecs.html)
