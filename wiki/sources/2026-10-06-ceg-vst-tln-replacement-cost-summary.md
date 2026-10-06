---
type: source
source_type: research
title: "CEG / VST / TLN 重置成本研究总结"
author: "human (own research)"
publisher: "personal research notes"
institution: ""
scope: [equity, industry]
url:
published: 2026-10-06
ingested: 2026-10-06
raw: "[[raw/2026-10-06-ceg-vst-tln-replacement-cost-summary]]"
tags: [replacement-cost, tobins-q, valuation, nuclear, ipp, position-sizing]
---

# CEG / VST / TLN 重置成本研究总结 (human's own research, 2026-10-06)

## TL;DR
The human's own Tobin's-Q study of the three AI-power IPPs, measured in **physical units**
(MW × $/kW), not book value. At 2026-10-06 prices all three sit ~28% of the way from the
private-deal anchor (Q_D 1.6–1.8) to the EIA new-build anchor (Q_B ~0.5). The conservative
new-build anchor (A, Q=1) leaves **CEG +26%, VST +8%, TLN +9%**; the deal-price anchor implies
**−53% to −57%**. The thesis's weakest link: the modern-equivalent asset (MEA) for nuclear
might be a CCGT.

## Key takeaways
- **Method:** Q = EV ÷ RC; RC = Σ(capacity × new-build $/kW) + NCOWC. Book-value Q fails for
  power (fresh-start / acquisition accounting resets depreciation: TLN book age 2.6y vs
  Susquehanna 1983) — it overstates power by 3–4×. Scope: net PP&E > 25% of assets; not for
  asset-light names, REITs, regulated utilities (use EV/rate base), E&P or yieldcos.
- **Four scenarios ($/kW nuclear / CCGT / peaker / coal):** A 4,625/1,500/1,200/1,000 (MIT
  NOAK) · **B 7,821/3,000/2,500/1,500** (EIA–S&L + CEG self-reported gas) · C 15,700 (Vogtle
  actual) · **D 1,500/1,150/900/500** (private deals).
- **Four adjustments:** RUL as an annuity-factor ratio, not linear (nuclear ×0.75); AFUDC
  (nuclear ×1.36, CCGT ×1.10); NCOWC = inventory + receivables − payables; MEA (coal → $500
  site value; nuclear's MEA might be CCGT $3,000).
- **EV bridge rules:** pair ARO with NDT (otherwise CEG EV overstated ~$14.6B); deduct
  held-for-sale so the numerator and denominator cover the same assets.
- **Results (10-06):** EV CEG $123.6B / VST $75.0B / TLN $27.2B. Q_B 0.46 / 0.52 / 0.50 ·
  stacked-adjustment Q 0.48 / 0.60 / 0.56 · nuclear-MEA=CCGT Q 0.80 / 0.66 / 0.63.
- **Contract leg:** TLN ~85% of nuclear contracted (AWS 1,920 MW to 2042, ~$18B) — contract
  upside largely realised; VST ≤~19%; CEG ~25% (rough) and its PPA cash arrives 2029–32. CEG's
  own sensitivity: +$20–50/MWh on 1 GW → +$0.40–1.00 2029 EPS ≈ +$9–22/share undiscounted.
- **Observable falsifiers:** (1) next ≥1 GW plant deal < $900/kW; (2) CEG signs ≥3 GW of
  nuclear long-term contracts at near-AWS premiums before 2027 (confirms the multiple); (3) gas
  turbine lead times shrink below 3 years (the $3,000/kW denominator collapses).
- **Sizing:** energy bucket ~$5,200 of a $7,200 account, unlevered; three-name correlation
  0.66–0.78 → **1.22 effective independent bets**, ~48.7% annual vol; half-Kelly at μ=15% ≈
  **$1,600**; $2,000 reserved as MCL margin; GS/MS pair rejected (coint p=0.515, half-life 111d).

## Notable claims
- CEG fleet 54,420 MW (nuclear 22,069 · CCGT 23,000 · peakers 5,214 · other 4,137) from the
  8-K plant-by-plant table; VST 43,484 MW (nuclear 6,478 · CCGT 22,167 · peakers 4,822 · coal
  8,743 · solar+storage 1,274) from 10-K Item 2; TLN 15,700 MW (nuclear 2,245 = 90% of
  Susquehanna; CCGT/peaker/coal split estimated).
- Deal comps (EV basis): Lotus 2,600 MW $745/kW (closed 2025-10) · Cogentrix 5,500 MW
  $829–859/kW (pending) · Calpine 23,000 MW $1,421–1,495/kW (closed 2026-01; $1,241 on 27.7 GW).
- 2026-09-09 → 10-06: CEG +1.4%, VST +5.6%, TLN +15.6% (TLN's Q_B 0.46 → 0.50).

## Fact-check / data gaps (spot-check by the LLM, 2026-10-06)
- ✅ Shares: CEG 354.31M, VST 335.64M, TLN 47.91M (10-Q covers, SEC XBRL).
- ✅ CEG debt $24,700M (LTD 19,111 + current 363 + short-term borrowings 5,226), cash $697M,
  NCI $345M; VST cash $435M, preferred $2,476M, NCI $12M; TLN debt $9,572M, cash $231M,
  NDT $1,997M ("TLN 漏掉 NDT $20 亿" correction confirmed), ARO $531M (SEC XBRL, 2026-06-30).
- ⚠️ VST debt $20,508M vs XBRL `LongTermDebt` $19,595M — the $913M difference is presumably
  the receivables financing / forward repurchase items the bridge includes; not reconciled.
- ⚠️ "Price 2026-10-06 close" — the prices ($298.12 / $159.54 / $369.67) were taken intraday
  (at 14:53 ET the market was still open: CEG $298.38, VST $159.80, TLN $371.56). Immaterial.
- ✅ 9/9 → 10/6 moves match Yahoo daily closes (CEG 293.9 → ~298, VST 151.1 → ~159.5, TLN
  319.7 → ~370).
- ➕ **Comp missing from D:** CEG's March 2026 sale of 4.4 GW of PJM gas (Bethlehem, York 1/2,
  Hay Road, Edge Moor) to LS Power for ~$5B ≈ **$1,136/kW**
  ([POWER](https://www.powermag.com/constellation-to-sell-4-4-gw-of-pjm-gas-power-assets-to-ls-power-for-5b-in-regulatory-divestiture/)) —
  above the $900 falsifier line, between Cogentrix and Calpine. Falsifier #1 not hit by it.
- ➕ Cogentrix: FERC approval August 2026, close expected late 2026
  ([Gas Processing News](https://www.gasprocessingnews.com/news/2026/01/vistra-to-buy-cogentrix-energy-in-47-b-deal-amid-surging-power-demand/)).
- Open items carried from the source's own table: VST pension & derivative net liabilities, CEG
  derivatives, retail-business value, TLN fleet split, Calpine $1.7B cash acquired, CEG ~25%
  contracted, AI-capex growth path (second-hand). Referenced scripts/CSVs (`news_watch.py`,
  `vst_tln_teardown.py`, `*replacement_cost*.csv`, `重置成本估值操作手册.md`) are **not in this repo**.

## Entities mentioned
[[ceg]] · [[vst]] · [[tln]] · [[replacement-cost-investing]] · [[ai-power-ipp-bull]] ·
[[kelly-criterion]] · Calpine · Cogentrix · Lotus · LS Power · Energy Harbor

## Agrees / contradicts
- Supersedes the LLM's quick estimate filed earlier the same day (now rewritten as
  [[ceg-vst-replacement-cost-2026-10-06]]): that one omitted ARO/NDT and held-for-sale (CEG EV
  $130B vs $123.6B here) and took VST coal as 4.57 GW (10-K says 8,743 MW).
- Agrees with [[dan-dreyfus]]'s TLN "below replacement cost" framing on B (Q 0.50) but shows
  how much it depends on the anchor: on D, TLN is at Q 1.60.
- ⚠️ Sharpens [[ai-power-ipp-bull]]: the Edge holds on new-build anchors, fails on deal anchors,
  and its weakest link (nuclear MEA = CCGT) is not among the thesis's four Invalidations.
