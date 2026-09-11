---
type: synthesis
tags: [quant, statarb, pairs-trading, cointegration, metals, financials, industrials, agriculture]
created: 2026-08-14
updated: 2026-08-14
---

# Multi-sector cointegration screen (metals, financials, industrials, ag)

## TL;DR
Extended the [[bz-cl-pairs-trade|BZ/CL statarb methodology]] to four new
sectors (excluding biotech and tech, per request): metals & mining,
financials/banks, industrials/transportation, agriculture/softs. Screened
30 in-sample candidates across the four sectors; the three most
economically-defensible were taken to out-of-sample validation.
**All three failed or were dropped before backtesting.** No new pair
survived this round. Documented here anyway, per this project's own rule
to report failures and near-misses, not just winners.

## Screening results (in-sample, 2020-2024, Johansen @ 99% confidence)
| Sector | Pairs tested | Passed | Read |
|---|---|---|---|
| Metals & mining | 136 | 6 | Half were trivial (futures vs. their own spot ETF — GC=F/GLD, SI=F/SLV — not real pairs trades, just ETF-arbitrage-tight tracking). |
| Financials/banks | 66 | 5 | Similar issue — some passes were a stock vs. the sector ETF it's a component of. |
| Industrials/transport | 78 | 19 | **12 of 19 involved UAL as one leg** — a strong sign of a shared COVID-crash artifact (all travel/industrial names cratered and recovered together in 2020) rather than 19 genuine relationships. |
| Agriculture/softs | 36 | 0 | Honest null result — corn/wheat/soybeans/coffee/cocoa/sugar don't share a tight enough relationship despite the "agriculture" label. |

**Ticker verification finding:** `GOLD` does NOT resolve to Barrick as
expected — it's "Gold.com, Inc." Barrick rebranded to Barrick Mining
Corporation, ticker `B`, verified by identity check before use. `CT=F`
(cotton) returned no identifiable info and was excluded rather than
guessed. Same discipline that caught WTI→W&T Offshore and BZ→Kanzhun
earlier this session — every ticker in a new universe needs an identity
check, not just a plausible price range.

## Shortlist taken to validation — all failed
| Pair | Stage | Result |
|---|---|---|
| AEM / B (gold miners) | Dropped before backtesting | **Fails CADF** (p=0.05–0.10 both directions, not significant) despite passing the Johansen screen (thin margin, 2.03) — a likely false positive, consistent with the ~1.4 expected false positives at this screen's confidence level. |
| DAL / UAL (airlines) | Backtested | Cointegrated by CADF but asymmetric (only one direction significant); half-life more than doubles depending on whether COVID is included (32d vs 48d — opposite pattern from BZ/CL). Test-window (2024–2026) result: **Sharpe -0.25, CAGR -2.0%, max DD -17.7%/605d — a losing strategy.** |
| GS / WFC (banks) | Backtested | Cleanly cointegrated by both Johansen and CADF, stable half-life (~45-48d) — the most robust candidate of the three going in. Test-window result: **Sharpe -0.05, CAGR -0.8%, max DD -12.5%/616d — flat/slightly negative, no real edge.** (An early, uncorrected run of this pair showed a -93% drawdown; that was a P&L scaling artifact from GS/WFC's large price-level gap, not a real result — see the methodology fix on [[bz-cl-pairs-trade]].) |

## Why these likely failed (not just "bad luck")
- Both surviving candidates (DAL/UAL, GS/WFC) have **much slower half-lives**
  (32-48 days) than BZ/CL (~9 days) — fewer independent mean-reversion
  cycles fit inside the same test window, meaning less statistical power
  and fewer trades (31 and 38 respectively) to validate an edge from.
- Equity pairs carry idiosyncratic company-level risk (management, capital
  structure, M&A) that commodity benchmark pairs don't — a weaker prior
  that a price-level relationship reflects a stable economic constraint
  versus temporary co-movement.
- The industrials screen's UAL-heavy cluster is a concrete illustration of
  why an in-sample Johansen pass isn't sufficient on its own — a shared
  macro shock (COVID) can manufacture apparent cointegration across many
  pairs at once without it being durable.

## Later rounds (added 2026-08-23) — also all negative
Three further screens were run after the four sectors above. None produced a
survivor, and none had been filed until now.

**Oil-linked equities vs WTI.** Screened producers and midstream names against
`CL=F`, looking for an equity leg that could substitute for the inaccessible
Brent contract. Only KMI and OKE passed — flagged as **likely false positives**
because the result is economically backwards: the weaker-story midstream firms
passed while every stronger-story producer (XOM, CVX, COP, EOG) failed clearly.
Consistent with the ~1 false positive expected at this sample size.

**Second stock-sector round** (staples, utilities, REITs, materials,
insurance). O/VTR (REITs) showed a strong Johansen margin but **failed the CADF
cross-check** — the identical pattern as AEM/B above. CLX/PG (staples) had a
thin Johansen margin, was flagged as likely noise, and was never CADF-checked;
it remains formally untested rather than cleared.

**BRK-B / MSFT**, checked on request at the standard 95% level (not the 99%
wide-screen threshold), plus Johansen and half-life. Both cointegration tests
rejected clearly. A tutorial the human found reported a "cointegrated" verdict
for this pair, but its own proper Engle-Granger test returned p=0.065 (not
significant) — only an ad-hoc ADF on the raw *price ratio* passed (p≈0.03),
which fixes the coefficient at 1 rather than estimating it. Worth recording
honestly: that ratio result **strengthened** on a longer 2020–2024 window
(p=0.0173) rather than evaporating as a short-window fluke would. The
tutorial's two tests genuinely disagree with each other; the standard estimated-β
test is the one to weight, but the ratio finding was real and reproducible,
not an artifact. See [[pairs-trade-failure-modes]] §1 — neither test supplies
an economic convergence mechanism for a conglomerate vs a software company.

## Next steps (not yet done)
- Could revisit financials/industrials with a training window that
  excludes or down-weights the COVID period more deliberately (as was
  needed for BZ/CL's half-life estimate), to see if any candidate looks
  different once that distortion is controlled for.
- Metals & mining's weaker candidates (HG=F/PL=F, AEM/GDX, AEM/GDXJ) were
  not yet taken to out-of-sample testing — lower priority given AEM/B's
  failure, but not formally ruled out.
- No position/thesis pages — nothing here survived to the point of being a
  candidate worth the Thesis Test.

## Sources
Built with the `statarb-strategy-lab` toolkit; see [[bz-cl-pairs-trade]] for
the shared methodology and the P&L correction this screen's testing
uncovered. Failure taxonomy: [[pairs-trade-failure-modes]]. The equivalent
search over retail-sizeable futures contracts is
[[micro-futures-universe-screen]] — also a null result.
