---
type: concept
category: strategy
aliases: [orbital compute, datacenters in space, space compute]
tags: [space, ai, datacenter, thesis]
created: 2026-06-28
updated: 2026-06-28
---

# Orbital compute (datacenters in space)

## Definition
The thesis ([[gavin-baker]]) that putting AI compute **in orbit** becomes economically rational
as **terrestrial** data-center build costs inflate — "racks in space linked with lasers," not
giant pressurized stations.

## The first-principles math
- A 1 GW terrestrial data center ≈ **$35B silicon + $25B power/cooling** (the $25B is labor-heavy
  → **inflationary**).
- In space: same ~$35B silicon **+ launch**. Reusable **Starship** could drop launch to ~**$5B**
  per GW → ~$40B in orbit vs ~$60B on the ground, and the launch line is **deflationary** over
  time. Ongoing power/cooling ≈ ~$1B/yr.
- **Implication:** favors **[[spcx|SpaceX]]'s** integrated launch+compute stack; scarce remaining
  ground capacity (100s of MW–GW) becomes "diamonds." Reinforces [[ai-power-demand]] (terrestrial
  power is the binding constraint; ~40%+ of data centers get contested).

## Caveats
- Speculative/early; thermal, latency, and reliability in orbit unproven at scale. Training needs
  **co-location** (latency) → orbital is more an **inference** story.

## Related
[[spcx]] · [[tsla]] (Megapod modular DCs) · [[ai-power-demand]] · [[hbm-dram-bottleneck]] ·
[[gavin-baker]]

## Sources
- [[2026-06-27-allin-china-ai-micron-memory]]
