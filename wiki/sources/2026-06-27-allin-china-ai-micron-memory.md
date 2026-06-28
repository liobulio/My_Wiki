---
type: source
source_type: youtube
title: "Socialists Sweep NYC, China Catches Up in Coding, AI Memory Crunch, Micron's Blowout Quarter"
author: "[[all-in-podcast]]"
publisher: "All-In Podcast (ep. 278)"
url: https://www.youtube.com/watch?v=w8ah_tA0yfg
published: 2026-06-27
ingested: 2026-06-28
raw: "raw/Socialists Sweep NYC, China Catches Up in Coding, AI Memory Crunch, Micron's Blowout Quarter.md"
tags: [news, ai, semis, memory, china, space, ipo, macro]
---

# All-In ep. 278 — China AI / Micron memory crunch / IPO wave

News episode with guests **[[gavin-baker]]** (Atreides Management) and **[[travis-kalanick]]**
(Uber founder; now AI startup "Adams"). Politics kept brief; the AI/semis/IPO content is the
substance.

## TL;DR
China's **GLM 5.2** ([[zai]]) is a frontier-class **open-weight** model — evidence for the
[[ai-gatekeeping|fragmentation]] thesis. **[[mu|Micron]]** blew out earnings as **[[hbm-dram-bottleneck|HBM/DRAM]]**
becomes *the* AI bottleneck (spilling into Apple/console prices). [[orbital-compute|Datacenters
in space]] pencil out as terrestrial build costs inflate. IPO wave: [[anthropic]] (Gavin: ~$3T),
[[spcx|SpaceX]] (off its highs), [[cerebras]] (broke deal price).

## 1. Politics (brief) `[01:14]`
DSA/Mamdani-endorsed socialists swept NYC Democratic primaries. Chamath frames some races as a
"referendum on AI" (Anthropic-funded anti-AI vs OpenAI-funded pro-AI PACs). Social-media-ban-
under-16 debate (Canada/UK/Australia/Florida). **Opinion/worldview — not actionable.**

## 2. China open-source AI / distillation / OpenAI's chip `[45:18]`
- **[[zai|Z.ai]] GLM 5.2:** open-weight (MIT), 744B params (MoE, ~40B active), 1M context; AAII
  score 51 (best open-weight ever); beats GPT-5.5 on coding at ~1/6 the cost; ~matches Claude
  Fable/Opus 4.8. → [[ai-distillation-open-weights]].
- **Distillation** ([[gavin-baker]]): harvest API reasoning traces (phone farms, masked
  accounts) to cheaply approach the frontier — "a cheat sheet."
- **Composable "council of LLMs"** (Karpathy): router → your own open-weight model + frontier
  models as conductors. Open-source shifts value **frontier-lab margins → infra providers**
  (frontier ~90% of $ value, open-source ~80%+ of tokens).
- **[[nvda|Nvidia]] = "American open-source champion"** (could release a top open model; channel
  conflict stops it). **[[openai]]'s "Jalapeño" chip** (Broadcom) → ASIC threat to Nvidia.
- GLM trained on **Huawei** chips (indigenization; "AI in a box" exported cheap). [[david-sacks]]
  (AI czar): pro-export, "shock clock" vs China; don't self-handicap.

## 3. Micron / AI memory crunch `[1:01:49]`
- **[[mu|Micron]]** blowout: revenue ~4× YoY, **FQ4 guide ~$50B**; 2026 **HBM sold out**;
  take-or-pay floor-price contracts. **[[hbm-dram-bottleneck|DRAM is THE bottleneck]]** (~30–40%
  of hyperscaler capex). 3 HBM makers (Micron, SK Hynix, Samsung).
- **Consumer spillover ("AIL"):** Apple raising prices (MacBook Neo $699→$799; Mac Studio +25%);
  Xbox/Switch/PlayStation too. **CXMT** (China) IPO → cheap consumer DRAM, but can't make AI-grade
  HBM. Elon's **Terrafab** targeting memory (Intel partnership).

## 4. Distributed compute & datacenters in space `[1:10:23]`
- **[[orbital-compute]]:** 1 GW = ~$35B silicon + ~$25B power/cooling terrestrially (inflationary);
  reusable Starship → ~$5B launch → space cheaper over time. Favors [[spcx|SpaceX]]'s stack;
  remaining ground capacity becomes "diamonds."
- **[[tsla|Tesla]] "Megapod"** trademark (filed 2026-06-18): modular GPU+battery+cooling data-
  center units, rumored for Supercharger sites (reinforces Tesla/SpaceX merger talk).
- **Distributed inference** (not training — needs co-location): Bit Tensor / Targon / Venice;
  Power Wall + GPU + Starlink idea. **Inference disaggregation** (prefill = memory-capacity,
  decode = memory-bandwidth); [[nvda|Nvidia]]'s **Groq** + **[[cerebras]]** for decode in front
  of old GPUs (extends GPU life 7–12 yrs).

## 5. IPO update `[1:27:23]`
- **[[anthropic]]:** Gavin "worth ~$3T," ending year "well over $100B" run-rate, ~85% inference
  margins. (⚠️ see fact-check — actual private mark ~$1T.)
- **[[spcx|SpaceX]]:** off its post-IPO high (~$200+); small float; insiders had 6-mo liquidity
  for a decade → maybe less of a lockup wall; ~half of employees bought the IPO.
- **[[cerebras]]:** **broke deal price** after first public quarter (margin guide-down); ~$20B
  OpenAI inference contract. Market can absorb the ~$4T IPO backlog (private→public shift).

## ✅ Fact-check (2026-06-28)
- **[[mu]] — ✅ verified:** FQ4 revenue guide **$50B ±$1B** (vs ~$44B est, ~$11B yr-ago); 2026 HBM
  sold out; **16 Strategic Customer Agreements ≈ $100B**, take-or-pay floor pricing > prior-cycle
  peaks; GM >81%. ⚠️ podcast's "~50% of revenue / 4 customers" is imprecise (real: 16 deals, 20%
  of DRAM + ⅓ of NAND through 2030). — [TechTimes](https://www.techtimes.com/articles/319032/20260625/micron-q3-2026-earnings-100b-contracts-signals-ai-memory-cycle-break.htm), [TheNextWeb](https://thenextweb.com/news/micron-q3-fy2026-earnings-revenue-hbm-ai-memory)
- **[[zai]] GLM 5.2 — ✅ verified:** released 2026-06-16, MIT, 744B (MoE 40B active), 1M context,
  AAII **51** (best open-weight), beats GPT-5.5 on coding at **1/6 cost**. — [VentureBeat](https://venturebeat.com/technology/z-ais-open-weights-glm-5-2-beats-gpt-5-5-on-multiple-long-horizon-coding-benchmarks-for-1-6th-the-cost)
- **[[openai]] Jalapeño — ✅ verified:** OpenAI+Broadcom inference chip (June 24), ~50% cheaper
  than GPUs, 9-mo design cycle, part of 10 GW deal. — [CNBC](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip.html)
- **[[nvda]] / Groq — ✅ verified:** Nvidia bought Groq assets ~**$20B** (Dec 2025), its largest
  deal; inference-era bet. — [CNBC](https://www.cnbc.com/2025/12/24/nvidia-buying-ai-chip-startup-groq-for-about-20-billion-biggest-deal.html)
- **[[cerebras]] — ✅ verified:** CBRS IPO priced **$185**, opened $350, peaked ~$386, then fell
  ~to deal price after Q1 (GM guide 47%→36–38%); **>$20B / 750 MW OpenAI** contract through 2028
  (+$1B loan, warrants). — [Yahoo](https://finance.yahoo.com/markets/stocks/articles/cerebras-stock-offers-clear-warning-200345721.html), [stocksdownunder](https://stocksdownunder.com/cerebras-systems-nsdqcbrs-q1-2026/)
- **⚠️ [[anthropic]] "$3T" — Gavin's projection, NOT the mark:** actual **Series H $65B raise at
  ~$965B** post-money (~$1T); run-rate **~$47B** (from $30B; $10B in 2025). $3T / "$100B+ this
  year" are bullish *opinions*. — [Anthropic](https://www.anthropic.com/news/series-h), [VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth)
- **[[spcx]] — ✅:** IPO $135 @ $1.75T → +19% to $160.95; post-IPO high **$225.64**, since **−30%**
  (podcast's "~$200, retreated" is right). — [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/261995745-spacex-spcx-ipo-price-401-115-valuation-starlink-xai-tradingkey)
- **❓ Source-reported:** Tesla "Megapod" trademark; Apple/console exact price hikes; CXMT IPO timing.

## Entities
People: [[gavin-baker]], [[travis-kalanick]], [[chamath-palihapitiya]], [[david-sacks]] ·
Assets: [[mu]], [[nvda]], [[cerebras]], [[tsla]], [[openai]], [[zai]], [[anthropic]], [[spcx]],
[[amzn]] (CXMT _stub_) · Concepts: [[hbm-dram-bottleneck]], [[orbital-compute]],
[[ai-distillation-open-weights]], [[ai-gatekeeping]], [[ai-power-demand]]
