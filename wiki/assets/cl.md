---
type: asset
ticker: CL=F
asset_class: commodity
aliases: [WTI, West Texas Intermediate, WTI crude]
tags: [oil, energy, futures]
created: 2026-08-14
updated: 2026-08-14
---

# CL=F — WTI Crude Oil futures

## What it is
NYMEX WTI (West Texas Intermediate) crude oil futures, the primary US
domestic crude benchmark. Continuous front-month contract data via yfinance.

## Current view
Trading pair-mate to [[bz]] (Brent) in an active [[bz-cl-pairs-trade|statarb
research project]]. As of the 2026 Iran–US Strait of Hormuz conflict, WTI
has moved far less violently than Brent on the same days — economically
expected, since WTI is a US-domestic benchmark with much less direct
exposure to Persian Gulf shipping disruption than the internationally-traded
Brent contract.

⚠️ **Data quirk:** printed a real negative close (-$37.63) on 2020-04-20
during the COVID demand collapse — genuine historical event, but a data
handling hazard (breaks naive `pct_change()` returns and OLS regressions
that don't account for it). See [[bz-cl-pairs-trade]] for the fix applied.

## Key data points
- 2020-04-20: closed at -$37.63 (negative price, storage capacity crisis)
- 2026-03: spiked alongside Brent during the Hormuz closure, though less
  severely than Brent on a same-day basis

## Related
[[concepts/ou-optimal-exit-rules]] · [[bz]] (pair-mate) ·
[[bz-cl-pairs-trade]] (full research)

## Position & thesis
None currently — see [[bz-cl-pairs-trade]] for why (Thesis Test not yet
completed).

## Sources
[[bz-cl-pairs-trade]]
