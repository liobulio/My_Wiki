---
type: synthesis
title: "SPCX — reverse DCF and sum-of-the-parts (2026-10-09)"
tags: [valuation, reverse-dcf, sotp, spcx, ai, starlink]
created: 2026-10-13
updated: 2026-10-13
---

# SPCX — reverse DCF and sum-of-the-parts (2026-10-09)

Asked by the human: for a growth/tech name where [[replacement-cost-investing|replacement cost]]
does not apply, how do we judge whether today's price is reasonable? This page applies the two
tools that play the role of the replacement-cost anchors for [[spcx]]. Framework arithmetic, not
a forecast or advice. Price = 2026-10-09 close **$161.63**.

## Inputs (SEC filings unless marked)

| Item | Value | Source |
|---|---|---|
| Shares | Class A 7,607M + Class B 5,569M (2026-06-30) + ~391M Class A for Cursor (closed 2026-08-14) ≈ **13.57B** | Q2 earnings release (8-K 2026-08-04); Cursor share count from media, 8-K 2026-08-14 Item 2.01 |
| Market cap | **≈ $2.19T** | computed |
| Cash + marketable securities | $93.5B + $6.5B | Q2 release |
| Total debt | $39.4B | Q2 release |
| **Net cash** | **+$60.6B** | computed |
| **EV** | **≈ $2.13T** | computed |
| Q2 revenue | $7.81B (+92% YoY) → run-rate **$31.3B** | 10-Q XBRL |
| Segments Q2 (rev / op. income / adj. EBITDA) | Connectivity $4.29B / +$1.66B / $2.60B · Space $0.96B / −$0.54B / −$0.21B · AI $2.56B / −$1.26B / +$1.15B | Q2 release |
| Adj. EBITDA run-rate | $14.2B | computed |
| Capex | Q2 $18.4B; H1 $28.5B vs H1 operating cash flow $3.5B → **H1 FCF ≈ −$25B** | release / XBRL |
| Backlog (RPO) | $47.5B | 10-Q |
| Starlink subscribers | 12.0M (6.0M a year earlier) | Q2 release |
| Compute contracts | Google $920M/month Oct 2026–Jun 2029; Anthropic $1.25B/month to May 2029; ≈$26B/yr combined; **90-day termination after set dates** | media citing the June S-1/8-K filings ([letsdatascience](https://letsdatascience.com/news/spacex-rents-ai-compute-to-google-and-anthropic-f9510cdb), [WAM](https://www.wam.ae/en/article/179bkl9-spacex-lands-google-compute-deal-after-anthropic)) |
| Management targets | $100B ARR by end-2026; $1T revenue pulled forward to 2030 | media on the Q2 call — **not in the release** ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/space-exploration-technologies-corp-spcx-050338024.html)) |

Multiples today: **EV / run-rate revenue ≈ 68×, EV / adj. EBITDA ≈ 151×**, FCF negative.

## 1. Reverse DCF — what the price assumes (the "anchor A" analogue)
Simplification: interim FCF ≈ 0 net (capex currently consumes all operating cash), so
EV ≈ year-10 FCF × exit multiple ÷ (1+r)¹⁰. At a **30% FCF margin**:

| Discount rate | Exit 20× FCF | Exit 25× | Exit 30× |
|---|---|---|---|
| 9% | rev $841B · **39%/yr** | rev $673B · **36%** | rev $561B · **33%** |
| 10% | $922B · **40%** | $737B · **37%** | $614B · **35%** |
| 12% | $1,104B · **43%** | $883B · **40%** | $736B · **37%** |

- Central case (10%, 25×, 30% margin): **year-10 FCF ≈ $221B** (≈2× Apple's today) on
  **≈$740B revenue** → **~37%/yr for 10 years** from the $31B run-rate.
- Margin sensitivity (10%, 25×): 20% → 43%/yr · 25% → 40% · 35% → 35%.
- If the **$100B ARR target** for end-2026 is hit, the remaining requirement drops to
  **~25%/yr for 9 years**. So the price is roughly "management's 2026 target is achieved and
  growth then compounds at ~25%".

## 2. Sum-of-the-parts on today's run-rates (the "D → B" analogue)

| Part | Basis | Low | Mid | High |
|---|---|---|---|---|
| Connectivity (Starlink) | adj. EBITDA $10.4B × 15 / 25 / 40 | $156B | $260B | $416B |
| Space (launch) | revenue $3.85B × 5 / 10 / 20 | $19B | $38B | $77B |
| AI (xAI, X, cloud) | forward revenue ~$29B (contracts $26B + rest) × 5 / 10 / 20 | $145B | $291B | $581B |
| Cursor | deal value $60B, haircut in low case | $30B | $60B | $60B |
| Net cash | | $61B | $61B | $61B |
| **Total** | | **$411B** | **$710B** | **$1,195B** |
| **Per share** | ÷ 13.57B | **$30 (−81%)** | **$52 (−68%)** | **$88 (−46%)** |

- Even the high case on today's businesses explains **~55%** of the market cap. The remaining
  **~$1T is paid for things not yet in the run-rate**: Starship economics, the $100B-ARR / $1T-revenue
  path, orbital compute, the mobile network built on the new spectrum.
- Cross-check: **$100B ARR × 20 sales + net cash ≈ $2.06T ≈ $152/share** — today's price is
  close to capitalising the year-end ARR target at ~20× sales.

## 3. Floor (the "anchor D" analogue)
Net cash $61B + PV of backlog ~$42B + Starlink at mature-telecom 8× EBITDA $83B + launch at 3×
sales $12B + Cursor $30B ≈ **$227B ≈ $17/share (−90%)**. Unlike a power plant there is no
physical floor near the price: if growth disappoints, multiple and earnings fall together.
The compute contracts are cancellable on 90 days' notice after set dates, so even that leg is
softer than a utility PPA.

## Read
- The price is a bet on **~35–40%/yr revenue growth for a decade** (or ~25%/yr after a $100B
  exit-2026 ARR). Current businesses at generous multiples justify roughly **$50–90/share**.
- What would make it reasonable: the **$100B ARR** print by Q4 2026 results; AI segment adj.
  EBITDA margin holding as the Google contract ramps in Q4; capex/revenue falling from ~2.4×
  (Q2) toward ~1×.
- What would prove it wrong (observable): ARR well short of $100B at end-2026; a Google or
  Anthropic termination notice; Connectivity growth dropping under ~40% YoY; capex needing more
  debt/equity than the $61B net cash.
- Compare [[ceg-vst-replacement-cost-2026-10-06]]: there, the gap to the conservative anchor A
  is +8–26% with a deal-price floor −53% to −57%; here the floor is −90% and the "anchor" is a
  growth rate, not a price.

## Data gaps
Fully diluted share count (options/RSUs incl. assumed Cursor awards) · full-year capex guide ·
contract start dates and termination dates from the filings themselves · segment capex split ·
Cursor share count from the 8-K text (media figure used).

## Sources
SpaceX Q2 2026 earnings release ([8-K 2026-08-04](https://www.sec.gov/Archives/edgar/data/0001181412/000162828026052515/earningsreleaseq22608042.htm)) ·
10-Q 2026-06-30 (SEC XBRL companyfacts, CIK 1181412) · Cursor close ([TipRanks](https://www.tipranks.com/news/company-announcements/spacex-finalizes-cursor-acquisition-via-stock-issuance), [VKTR](https://www.vktr.com/ai-market/spacex-completes-60-billion-cursor-acquisition/)) ·
compute contracts (links above) · Yahoo close 2026-10-09 · [[spcx]] · [[replacement-cost-investing]]
