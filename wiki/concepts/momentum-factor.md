---
type: concept
category: factor
aliases: [momentum, cross-sectional momentum, trend]
tags: [quant, factor]
created: 2026-06-19
updated: 2026-06-19
---

# Momentum factor

## Definition
The empirical tendency for assets that have outperformed over the **trailing 6–12 months** to
continue outperforming over the **next 1–3 months**. A core member of the [[factor-investing]]
zoo, documented across stocks, bonds, currencies, and commodities.

## How it works
- Rank a universe by past return (commonly 12-month return skipping the most recent month).
- Go long top performers, short/avoid bottom performers; rebalance periodically.
- Returns are largely independent of [[value-factor]] — the two are **negatively correlated**,
  which is why they're often combined (see [[cliff-asness]] / [[AQR]] research).

## Pros / cons
- **Pro:** Robust, persistent, works across asset classes; diversifies value.
- **Con:** **[[momentum-crashes]]** — a fat left tail. Worst drawdowns hit in sharp post-crash
  rebounds (e.g. spring 2009) when the short side rips higher. You are compensated for bearing
  this crash risk.
- **Con:** Long flat stretches; not a standalone strategy.

## Who uses it
- [[cliff-asness]] and [[AQR]] — momentum is central to their multi-factor research.
- Retail implementation: [[mtum]] and similar factor ETFs.

## Related
[[factor-investing]] · [[value-factor]] · [[momentum-crashes]] · [[mtum]]

## Sources
- [[2026-06-12-quant-corner-momentum]] — primer; value/momentum negative correlation; crash risk.
