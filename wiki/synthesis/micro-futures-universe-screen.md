---
type: synthesis
tags: [quant, statarb, pairs-trading, cointegration, futures, micro-futures, negative-result]
created: 2026-08-23
updated: 2026-08-23
---

# Micro-futures universe screen — 66 pairs, no survivor

## TL;DR
Screened every pair in the CME **micro** futures complex — the contracts small
enough to size in a ~$20k account — for a tradeable cointegrated relationship.
**66 pairs, no survivor.** The best result (6E/6B, EUR vs GBP) posted Sharpe
0.72 out-of-sample but *fails* cointegration outright (p=0.41) and has a
Deflated Sharpe of 0.10 once the 66 searches are accounted for. Filed as a
negative result so it isn't re-run.

The screen also produced two findings worth more than the pair list itself:
the cointegration test had **zero predictive power** here, and drawdowns were
driven almost entirely by **volatility, not statistics**.

## Why this search ran
Every pair found in prior work failed on *execution*, not statistics:
[[bz-cl-pairs-trade|BZ/CL]] validates but needs ~$189k to size (no accessible
Brent micro), USO/BNO fail cointegration, and MCL+QM are both WTI. So the
search was inverted — start from what is retail-sizeable, then test it.

**Data note:** micro contracts track the *identical* underlying as their
full-size counterparts (verified: MCL $87.06 = CL=F $87.06 on 2026-08-21), but
Yahoo carries almost no history for the micro tickers. Research therefore ran
on the liquid full-size series, with micro contract sizes applied only for
sizing. Selection used 2010–2018 only; the walk-forward scored 2019–2026, so
pair selection could not leak into reported performance.

## Universe (16 contracts, all retail-sizeable)
Energy MCL/MNG · Metals MGC/SIL/MHG · Equity MES/MNQ/M2K/MYM ·
FX M6E/M6A/M6B/M6J · Crypto MBT/MET · Rates 10Y

## Results — economically plausible pairs, tested on merit
Run regardless of screen rank, since the screen threshold was deliberately
permissive (95%, not the 99% used in [[multisector-pairs-screen]]).

| Pair | Micros | CADF p | Sharpe | CAGR | maxDD |
|---|---|---|---|---|---|
| ES/NQ | MES/MNQ | 0.470 | **−0.30** | −2.9% | −26.6% |
| ES/YM | MES/MYM | 0.920 | −0.07 | −0.6% | −16.5% |
| NQ/YM | MNQ/MYM | 0.088 | −0.11 | −2.4% | −36.8% |
| GC/SI | MGC/SIL | 0.212 | −0.04 | −3.9% | −56.6% |
| SI/HG | SIL/MHG | 0.256 | 0.49 | 11.1% | −53.0% |
| GC/HG | MGC/MHG | 0.158 | 0.40 | 7.1% | −56.6% |
| CL/NG | MCL/MNG | 0.014 | 0.11 | −21.4% | −87.4% |
| BTC/ETH | MBT/MET | — | 0.08 | −3.1% | −70.4% |
| 6B/6J | M6B/M6J | — | 0.40 | 3.2% | −21.1% |
| **6E/6B** | **M6E/M6B** | **0.413** | **0.72** | 4.0% | **−11.2%** |

The **equity index pairs — the most economically plausible and the cheapest to
trade — all returned negative Sharpe.** That is coherent, not bad luck: NQ has
structurally outperformed ES/YM for 15 years, so the trade fades a persistent
trend rather than a mean-reverting one.

## The two findings that generalize

**1. The cointegration screen had no predictive power.**
Correlation between in-sample CADF p-value and out-of-sample Sharpe across 66
pairs: **+0.024**. The best OOS performer failed the test (p=0.41); the best
p-value (6E/6A, p=0.0047) returned Sharpe 0.01. In this universe the test told
us nothing about what would work.

**2. Volatility set the drawdowns, not any statistical property.**
- corr(higher-leg annualized vol, max drawdown) = **−0.843**
- corr(|log vol-ratio|, max drawdown) = −0.583

FX pairs "did well" on drawdown because EUR/GBP/JPY are 8–11% vol assets;
natural gas at 60% vol produced −87% drawdowns. A $1:$1 dollar-neutral
position on mismatched-vol legs is dominated by the noisier leg. See
[[pairs-trade-failure-modes]] §6.

## Why the screen's top ranks were junk
16 of 66 pairs were CADF-significant at 5% (≈3 expected by chance), but the
top of the ranking was **degenerate**: β came back at 0.004–0.28 with
half-lives of 600–900 days. A β≈0 spread is just one leg by itself, so the
test was effectively asking whether AUD alone is stationary — which is why
**`6A=F` appeared in 9 of the top 11 pairs.** One artifact, not nine
relationships ([[pairs-trade-failure-modes]] §3).

## The survivor doesn't survive
6E/6B (M6E/M6B): Sharpe 0.72 over 7.6 years, 11/16 folds positive, max DD only
−11.2% — the one genuinely attractive risk profile found.

- t-stat = **2.00** — marginal on its own
- CADF p = **0.4132** on 2010–2018 — fails cointegration outright
- **Deflated Sharpe = 0.33** against the 15 pairs walk-forwarded,
  **0.10** against all 66 screened

Finding one t≈2 result among 66 searches is precisely the expected yield of
noise. Not adopted.

## What this establishes
The binding constraint is not the search. It is that **statistical
co-movement without an economic convergence mechanism does not survive
out-of-sample** — now demonstrated across ~10 equity sectors
([[multisector-pairs-screen]]) and 66 futures pairs here. [[bz-cl-pairs-trade|
BZ/CL]] works precisely because Brent and WTI are the same commodity at
different delivery points, tied by physical shipping arbitrage. Nothing in the
micro complex has an equivalent.

## Next steps (not done)
- No position or thesis — nothing here came close to warranting the Thesis Test.
- The BZ/CL research stands; its blocker is capital, not validity. Paper
  trading it notionally is the open recommendation.
- Not re-testing this universe without a *new economic argument* for a
  specific pair. Re-screening the same 66 pairs would only re-harvest noise.

## Sources
Built with the `statarb-strategy-lab` toolkit:
`analysis/screen_micro_futures_universe.py`,
`analysis/micro_universe_screen.csv`,
`analysis/micro_universe_walkforward.csv`,
`analysis/micro_plausible_pairs.csv`.
Methodology shared with [[bz-cl-pairs-trade]]; failure taxonomy in
[[pairs-trade-failure-modes]].
