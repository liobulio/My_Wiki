---
type: synthesis
title: "CEG / VST / TLN — Tobin's Q and remaining room (2026-10-06)"
tags: [replacement-cost, tobins-q, ai-power, ipp, valuation, position-sizing]
created: 2026-10-06
updated: 2026-10-06
---

# CEG / VST / TLN — Tobin's Q and remaining room (2026-10-06)

Canonical numbers come from the human's own study
[[2026-10-06-ceg-vst-tln-replacement-cost-summary]] (method, EV bridges, fleets, comps — see
there). This page applies them to the **current book** ([[ceg]] 2.9455 sh, [[vst]] 5.7615 sh;
[[tln]] closed 2026-09-14) to answer the profit-taking question. Framework arithmetic, not a
forecast or advice.

> An earlier quick LLM estimate on this page (same day) is superseded: it skipped ARO/NDT
> pairing and held-for-sale (CEG EV $130B vs $123.6B) and used 4.57 GW for VST coal (10-K: 8,743 MW).

## Where price sits (from the source)

| | CEG | VST | TLN |
|---|---|---|---|
| EV | $123.6B | $75.0B | $27.2B |
| Q — D private deals | 1.82 | 1.66 | 1.60 |
| Q — stacked adjustments | 0.48 | 0.60 | 0.56 |
| Q — nuclear MEA = CCGT | 0.80 | 0.66 | 0.63 |
| Q — B EIA new-build | 0.46 | 0.52 | 0.50 |
| Position between D and B | 27.9% | 30.3% | 27.5% |

Implied share price at each anchor (interpolation, not a target):

| Anchor | CEG | VST | TLN |
|---|---|---|---|
| D private deals | $141 (−53%) | $70 (−56%) | $157 (−57%) |
| **Now** | **$298** | **$160** | **$370** |
| **A conservative new-build, Q=1** | **$375 (+26%)** | **$172 (+8%)** | $403 (+9%) |
| D–B midpoint | $423 (+42%) | $218 (+36%) | $543 (+47%) |
| Stacked adjustments, Q=1 | $672 | $311 | $808 |
| B EIA, Q=1 (theoretical ceiling) | $705 | $365 | $929 |

## Applied to the current book

| | Shares | Entry | Now | Unrealised | Value now | Value at A | Value at D |
|---|---|---|---|---|---|---|---|
| CEG | 2.9455 | $294 | $298.12 | +1.4% | $878 | $1,105 | $415 |
| VST | 5.7615 | $151 | $159.54 | +5.7% | $919 | $991 | $403 |
| **Total** | | | | **+$61** | **$1,797** | **$2,096 (+$299)** | **$819 (−$979)** |

- **"Profit-taking" is not really the situation:** CEG is +1.4% and VST +5.7%. The
  realised loss (−$321: CEG −$85, VST −$58, TLN −$178) is already booked from the 2026-09-14 sales (CEG closed $264.6 that day; it went
  on to close as low as $254.0 on 09-30 before the PPA run-up).
- **To the first anchor (A) the remaining room is small and lopsided:** +$299 to A versus
  −$979 to D. VST is only +8% from its A anchor, so its case rests on B-type nuclear costs or
  contract value; CEG still has +26% to A.
- **D understates contracted names** (it carries no contract value). That matters less for CEG
  (~25% contracted, rough) and VST (≤~19%) than it did for TLN (~85%).
- **Size vs the source's own Kelly line:** half-Kelly at μ=15% ≈ $1,600 for the bucket; the
  book after the 09-14 trims is ~$1,800, roughly that size. μ is the human's number to set.
- **What would move the anchors (falsifiers):** next ≥1 GW plant deal below $900/kW (the
  March 2026 LS Power–CEG deal at ~$1,136/kW did not hit it); CEG signing ≥3 GW of nuclear
  long-term contracts at near-AWS premiums before 2027 (the Google deal on 2026-10-06 adds
  890 MW uprate + 2,700 MW existing supply — [[2026-10-06-ceg-google-nuclear-uprate-ppa]] — and
  counts toward it once pricing is known); gas-turbine lead times falling under 3 years.

## Exit anchor = A (human-chosen 2026-10-06) — remaining value
Prices 2026-10-06 15:29 ET (intraday).

| | Shares | Entry | Now | Anchor A | Left per share | **Left in $** | Entry → A total |
|---|---|---|---|---|---|---|---|
| CEG | 2.9455 | $294 | $297.20 | $375 | +$77.80 (+26.2%) | **+$229** | +$239 (+27.6%) |
| VST | 5.7615 | $151 | $158.61 | $172 | +$13.39 (+8.4%) | **+$77** | +$121 (+13.9%) |
| **Book** | | | $1,789 | $2,096 | | **+$306 (+17.1%)** | +$360 |

- 75% of the remaining room is CEG ($229 of $306); VST has $77 left.
- Realised loss from 09-14 is −$321; if both reach A, the whole AI-power episode nets
  **≈ +$38** (−$321 + $239 + $121).
- μ in the Kelly line is a free 5–30% input, not a forecast — no sizing conclusion is drawn from it.

## Sources
[[2026-10-06-ceg-vst-tln-replacement-cost-summary]] · [[ai-power-ipp-bull]] ·
[[replacement-cost-investing]] · Yahoo prices 2026-10-06 intraday
