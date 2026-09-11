---
type: concept
category: model
aliases: [statarb failure modes, why pairs trades fail, cointegration pitfalls]
tags: [quant, statarb, pairs-trading, cointegration, methodology]
created: 2026-08-23
updated: 2026-08-23
---

# Pairs-trade failure modes

The recurring ways a statistical-arbitrage pair looks tradeable and isn't.
Each item here was found empirically in this wiki's own research
([[bz-cl-pairs-trade]], [[multisector-pairs-screen]],
[[micro-futures-universe-screen]]) — not copied from a textbook. Check a new
candidate against this list before believing a backtest.

## 1. Cointegration without a convergence mechanism
The single most predictive filter found so far. A pair needs an **economic
force that pushes the spread back**, not just statistical co-movement.

- [[bz]]/[[cl]] works because Brent and WTI are *the same commodity at
  different delivery points*, linked by physical shipping arbitrage. If the
  gap exceeds transport cost, cargoes move and close it.
- Gold/silver, EUR/GBP, ES/NQ, airlines, banks are all *correlated* — but
  nothing forces their ratio back. Across ~10 equity sectors and 66 futures
  pairs, none of them survived out-of-sample.

Correlation is co-movement; cointegration is a testable statistical property;
**convergence pressure is an economic claim.** Only the third one is an edge.

## 2. The in-sample cointegration test can have zero predictive power
Measured directly on 66 micro-futures pairs: correlation between in-sample
CADF p-value and out-of-sample Sharpe = **+0.024**. The best OOS performer
*failed* cointegration (p=0.41); the best p-value (p=0.0047) returned Sharpe
0.01. Passing the test is a necessary hygiene check, not evidence of an edge.

## 3. Degenerate β ≈ 0 — the "spread" is just one leg
If the fitted hedge ratio collapses toward zero, `y − βx` degenerates to `y`
alone, and the cointegration test is really an ADF on a single series that
happened to look range-bound in-sample. Tell-tale signs: β < ~0.3, and a
half-life in the hundreds of days.

In the micro screen, **`6A=F` (AUD) appeared in 9 of the top 11 ranked pairs**
with β of 0.004–0.28 and half-lives of 600–900 days. That is one artifact
presenting as nine relationships.

## 4. β instability turns a "hedge" into a directional bet
The most dangerous version, because it is invisible in aggregate statistics.
Walk-forward on [[bz]]/[[cl]] re-estimated β on each fold: **7 of 34 folds
landed outside [0.8, 1.2]**, ranging 0.116 to 1.457.

In the 2014-07 fold at β=0.116, the "hedged" spread's returns correlated
**1.00 with Brent** — a 0.88× outright long-oil position, held ~75% of the
time, exactly as crude fell from $100 to $50. That single fold produced a
−43.9% return.

**A ratio (or log-ratio) spread cannot fail this way** — it has no β to
mis-estimate and stays dollar-neutral by construction (correlation −0.02 in
that same fold). This is the strongest argument for the ratio formulation,
and it is structural, not a backtest result.

## 5. A dollar spread can't stay stationary across price-level shifts
When the underlying ranges $45–$111, a constant *dollar* difference cannot be
stationary, but a *ratio* can. On [[bz]]/[[cl]], through both structural-break
eras the ratio stayed marginally stationary while the dollar difference clearly
did not (2011–2015: ratio p=0.0509 vs difference p=0.2762).

## 6. Volatility, not statistics, sets the drawdown
Across 66 pairs: correlation of the higher-leg volatility with max drawdown
= **−0.843**; vol-ratio mismatch with drawdown = −0.583. Pairs "did well" on
drawdown mainly by being low-vol (FX at 8–11%) and "did badly" by being
high-vol (natural gas at 60% → −87% drawdowns). A $1:$1 dollar-neutral
position on legs with mismatched vol is dominated by the noisier leg — it is a
directional bet wearing a hedge.

## 7. The dollar-vs-share P&L convention
`rets_y − β·rets_x` (percentage returns combined) implicitly represents a
**$1-long vs $β-short dollar position** that must be rebalanced daily — not a
static β-share-ratio position. Harmless at β≈1, badly wrong otherwise. Found
via a GS/WFC pair (β=6.4) that produced a −93% drawdown which was pure scaling
artifact. See [[bz-cl-pairs-trade]] for the full accounting and the current
status of this convention in the codebase.

## 8. Structural breaks the training window can't see
[[bz]]/[[cl]] cointegration genuinely broke for ~5 years: the US shale boom
bottlenecked WTI at Cushing and blew the spread from ~$0.70 (2010) to ~$17
(2012). ADF on the difference went to p=0.28 and half-life to 42 days. Any
strategy assuming a stable relationship was trading a moving target. A pair
that is cointegrated *today* over a 4-year window may simply be inside a
regime, not describing a permanent law.

## 9. ETF proxies do not inherit the underlying's cointegration
USO/BNO fail cointegration outright (ADF p=0.60 full history) even though
Brent/WTI futures pass at p≈0.0000. The ETFs hold futures and **roll on
different schedules**, injecting a structural wedge: the USO/BNO ratio drifted
8.11 (2011) → 2.47 (2024). They are portfolios-plus-a-roll-policy, not the
underlying.

## 10. Multiple testing — the screen manufactures winners
66 pairs at the 5% level yields ~3 false positives before any real
relationship exists. The best micro-universe pair (6E/6B, Sharpe 0.72) had a
t-stat of 2.00 but a **Deflated Sharpe of 0.33 against 15 trials and 0.10
against 66** — far below the 0.95 bar. Finding one t≈2 result in 66 searches
is the expected yield of noise. Always deflate by the number of variants
actually tried, including the ones you discarded.

## 11. Tradability is a constraint, not an afterthought
A validated strategy you cannot size is not a strategy. [[bz]]/[[cl]] trades
in 1,000-barrel contracts (~$94k each) with no accessible Brent micro, so it
needs roughly **$189k to size at half scale** — the research is sound and the
position is inaccessible at small account sizes. Screen the *tradeable*
universe first rather than finding a pair and then discovering the contract
size. (Though note: doing exactly that in the micro universe still found
nothing — see [[micro-futures-universe-screen]].)

## Related
[[ou-optimal-exit-rules]] · [[bz-cl-pairs-trade]] ·
[[multisector-pairs-screen]] · [[micro-futures-universe-screen]] ·
[[bz]] · [[cl]]
