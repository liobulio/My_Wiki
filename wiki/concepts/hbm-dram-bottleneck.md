---
type: concept
category: term
aliases: [HBM, DRAM bottleneck, high bandwidth memory, AI memory crunch]
tags: [semis, memory, ai, supply-chain]
created: 2026-06-28
updated: 2026-06-28
---

# HBM / DRAM bottleneck

## Definition
The thesis ([[gavin-baker]]) that **memory — specifically DRAM, and stacked HBM (high-bandwidth
memory) — is the single most important bottleneck in AI**, because model performance is gated by
memory capacity and bandwidth, not just compute.

## How it works
- **HBM** = DRAM dies stacked (8→12→16 high) and packaged onto the GPU; an advanced, hard
  process. Only **3 firms** make AI-grade HBM/DRAM: **[[mu|Micron]], SK Hynix, Samsung**.
- Data centers **hoover up DRAM** → ~**30–40% of hyperscaler capex** is memory; new fab capacity
  takes ~2+ years to ramp.
- **Take-or-pay contracts** with floor prices (Micron's 16 SCAs ≈ $100B) lock in margins above
  prior-cycle peaks → a structurally better cycle than past commodity-DRAM busts.

## Why it matters (investment relevance)
- **Long the 3 HBM makers** ([[mu]] et al.) — sold-out supply, pricing power, improved structure.
- **Consumer-electronics margin squeeze ("AIL"):** DRAM scarcity → Apple/Mac, Xbox/Switch/
  PlayStation price hikes; demand destruction in price-sensitive consumer vs price-insensitive
  AI. **CXMT** (China) may flood *consumer-grade* DRAM but can't make AI-grade HBM.
- Ties to [[ai-power-demand]] (memory + power are the two scarce inputs) and [[orbital-compute]]
  (rising terrestrial build cost).

## Related
[[mu]] · [[nvda]] · [[ai-power-demand]] · [[orbital-compute]] · [[gavin-baker]]

## Sources
- [[2026-06-27-allin-china-ai-micron-memory]]
