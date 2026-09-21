---
type: position
asset: "[[tln]]"
ticker: TLN
status: open
weight:
shares: 5.407
account: IBKR
entry_date:
entry_price:
conviction: 3
thesis: "[[ai-power-ipp-bull]]"
invalidation_status: [ok, ok, ok, ok]
opened: 2026-09-11
updated: 2026-09-21
---

# TLN — Talen Energy (open position)

## The Thesis Test
Shared with the other AI-power IPP holdings — see [[ai-power-ipp-bull]] for the Edge, the
Catalyst, and the four Invalidation conditions. `invalidation_status` above tracks them in
order: (1) hyperscaler contracts delayed/cancelled · (2) uprate/co-location restricted by
regulators · (3) solar expansion faster than expected · (4) solar rebuild cost falling.

## Summary
Real holding: **5.407 shares** at IBKR (human-supplied 2026-09-11). Weight is computed from
shares × last price by `scripts/render_brief.py`; `entry_date` / `entry_price` /
`conviction` are the human's to fill — `conviction: 3` is a placeholder.

## Conviction rationale
See [[ai-power-ipp-bull]]. Asset detail on [[tln]].

## Filings watch
The daily brief reads every new 8-K / 10-Q / 10-K for this registrant and appends an entry
below when it bears on the thesis (regulator-restricted contracts first).

## Sources
[[ai-power-ipp-bull]] · [[tln]]

## Update history
- 2026-09-11 — opened in the wiki from the human's stated holding (5.407 sh, IBKR).
- 2026-09-11 — 读取 8-K 2026-08-05（[[2026-08-05-tln-8k-q2-earnings]]）与 10-Q Q2：>10 GW 以 $325 顶格出清；~4 GW 数据中心签约选项管线（尚未签约）；Q2 GAAP 净亏 −$92M / EPS −$2.00。⚠️ 数据缺口：股价 6 月 ~$382 → 9 月 ~$315，原因未追溯。Invalidation：ok/ok/ok/ok。
- 2026-09-14 — brief：`sec_fetch.py --since 2026-09-11` **无新增文件**。行业面为正向：Google–Fortum 22 年核电 PPA、NextEra 重启核电、DOE/NERC 电力需求数据强化 firm baseload 稀缺（[[2026-09-13-soochow-power-scarcity-nuclear-ppa]]、[[2026-09-13-guojin-compute-mainline-power]]）。⚠️ 未解：6→9 月 −18% 仍未追溯到具体 catalyst。宏观：加息预期升温、10Y 逼近 5%（利率敏感性风险）。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-15 — brief：`sec_fetch.py --since 2026-09-14` **无新增文件**。需求侧继续走强（Oracle 单季交付 850 MW、TSMC +53.3%、IEA 用电 2030 翻倍），强化 firm baseload 稀缺（[[2026-09-14-donghai-electronics-tsmc]]、[[2026-09-14-dongguan-aidc-power]]）。⚠️ 未解：6→9 月 −18% 仍未追溯到具体 catalyst，下期继续优先。宏观：本周 FOMC（9/16–17），PPI +5.4%、油价破 $100、CME 加息概率 88.1%（[[2026-09-14-soochow-us-weekly-hike-risk]]）→ 利率敏感性风险。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-16 — brief：`sec_fetch.py --since 2026-09-15` **无新增文件、0 flags**。⚠️ 未解：6→9 月 −18% 仍未追溯到具体 catalyst，下期继续优先。今日进入 **FOMC（9/16–17）**；10Y 9/14 一度触及 **5.04%** 后回落（[[us-treasury-10y]]），[[2026-09-16-spdb-intl-rates-equity|浦银]]判上行有序/AI 仍是主线、[[2026-09-16-dongxing-cpi-continuous-hike|东兴]]警示连续加息——利率敏感性属既列风险，非 Invalidation。无监管/合约事件触及失效条件。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-17 — brief：`sec_fetch.py --since 2026-09-16` **无新增文件、0 flags**。**FOMC 加息 25bp 至 3.75%–4.00%、12–0 偏鹰兑现**（[[2026-09-17-guosen-fomc-warsh]] 等四家）；加息当日美股跌、美债齐升——利率敏感性属既列风险，非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。firm baseload 稀缺逻辑不变，无监管/合约事件触及失效条件。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-18 — brief：`sec_fetch.py --since 2026-09-17` **无新增文件、0 flags**。需求侧继续走强：[[2026-09-18-greendh-futures-ai-reaccel|格林大华期货]]汇集 Nebius GPU 云再涨 ~20%（B300 年内 +56%）、Broadcom AI 收入 +221%、SpaceX 目标 20 GW 在线电力——AI 负荷把 firm baseload 推向持续偏紧，利好 TLN 未签约的可调度容量（不触发失效条件）。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。宏观利率敏感性（[[2026-09-18-dongxing-fomc-oil|东兴]] 维持 10Y 4.7–5%）属既列风险，非 Invalidation。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-21 — brief：`sec_fetch.py --since 2026-09-18` **无新增文件、0 flags**。firm baseload 稀缺再获量化佐证：[[2026-09-20-soochow-overseas-compute-power|东吴]] 引 TrendForce（2030 数据中心用电缺口 **268 GW**）、[[2026-09-21-huaxin-ai-infra-power|华鑫]]"矛盾从算力移到电力"——利好 TLN 未签约的可调度容量（Susquehanna–AWS 之外仍有余量）。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。新风险面：AI 基建融资端 CDS 走阔（[[2026-09-20-kaiyuan-oracle-nebius-cds|开源]]）——属既列利率/融资敏感性风险，非 Invalidation。Invalidation 状态：ok/ok/ok/ok（不变）。
