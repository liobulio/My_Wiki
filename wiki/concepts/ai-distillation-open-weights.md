---
type: concept
category: term
aliases: [distillation, open-weight models, composable models, council of LLMs]
tags: [ai, open-source, china, models]
created: 2026-06-28
updated: 2026-06-28
---

# Distillation & open-weight / composable models

## Definition
Two linked ideas: **distillation** (cheaply approaching the frontier by training on a stronger
model's outputs) and **composable / open-weight** model stacks (mixing your own open model with
frontier models). Together they argue the frontier's lead is **narrow and leaky**.

## How it works
- **Distillation** ([[gavin-baker]]): harvest **reasoning traces** from a frontier model's API
  (phone farms, masked accounts) → feed into RL/pretraining → "a **cheat sheet**" to near the
  frontier at a fraction of the cost. Once close, a model can do its own RL ("cat out of the bag").
- **Composable "council of LLMs"** (Karpathy): a **router** sends most queries to your cheap
  **open-weight** model; only the hardest go to frontier models acting as "conductors."
- **Value shift:** open-source moves economics **from frontier-lab margins → infra providers**
  (frontier tokens ~90% of $ value, but open-weight ~80%+ of tokens processed).

## Why it matters (investment relevance)
- **Direct evidence for [[ai-gatekeeping|fragmentation]]:** China's **[[zai|GLM 5.2]]** (MIT,
  frontier-class coding at ~1/6 cost) shows open-weight catching up — supports [[david-friedberg]]'s
  side over a durable hyperscaler oligopoly.
- Bullish **AI infrastructure** (clouds, inference chips, [[hbm-dram-bottleneck|memory]]); pressures
  **standalone frontier-lab** pricing power. [[nvda|Nvidia]] could be the "American open champion."
- **Geopolitics:** GLM trained on **Huawei** chips; censorship (Taiwan/Tiananmen) is forkable by
  US firms ([[david-sacks]]: pro-export, "shock clock" vs China).

## Related
[[ai-gatekeeping]] · [[zai]] · [[nvda]] · [[openai]] · [[gavin-baker]] · [[david-friedberg]]

## Sources
- [[2026-06-27-allin-china-ai-micron-memory]]
