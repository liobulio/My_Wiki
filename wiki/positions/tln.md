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
updated: 2026-09-30
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
- 2026-09-22 — brief：`sec_fetch.py --since 2026-09-21` **无新增文件、0 flags**。firm/清洁电力长期需求再获权威上修：[[2026-09-22-cpost-iaea-nuclear-uprate|中邮]]引 **IAEA 连续第六年上调**核电装机预期（2060 高情景 1284 GW，已核）——利好 TLN 未签约的可调度核电容量。AI 存储/算力 capex 未退坡：[[2026-09-22-pacific-electronics-ai-memory|太平洋]]记 AMAT FY26Q3 DRAM/HBM 设备放量（间接支撑数据中心用电刚性）。⚠️ 利率面：[[2026-09-22-guoxin-sec-fed-hawkish-hike|国新]]（10Y 收 5.021% 新高、10 月加息概率近 60%）vs [[2026-09-22-soochow-us-weekly-post-hike|东吴]]（不具备连续加息基础、利率压估值不改 AI 景气）——续加持续性两家分歧，属既列利率敏感性风险、非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-23 — brief：`sec_fetch.py --since 2026-09-22` **无新增文件、0 flags**。算力交付实证 firm baseload 需求刚性：[[2026-09-23-huaxin-nvda-rubin|华鑫]]记 NVDA FY27Q2 数据中心 **$89B/+117%、Rubin 全面量产**、[[2026-09-23-huaxin-avgo-ai-semi|AVGO]] AI 半导体 $16.7B/+221%——利好 TLN 未签约的可调度容量（Susquehanna–AWS 之外余量）。宏观 [[2026-09-23-dongfang-jincheng-overseas-hike|东方金诚]]：美日加息、10Y 周收 5.01%、8 月零售强韧。⚠️ [[2026-09-22-boci-ai-mainline-recheck|中银]]"1998 而非 2000"——利率是核心估值约束，属既列利率敏感性风险、非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-24 — brief：`sec_fetch.py --since 2026-09-23` **无新增文件、0 flags**。需求侧延续：[[2026-09-22-huaxin-cisco-ai-network|华鑫·思科]]记 FY2026 hyperscaler AI 基础设施订单 **$9.3B（~4.5× YoY）、FY27 $7.5B（+87.5%）**——数据中心建设未退坡，利好 TLN 未签约可调度容量；[[2026-09-24-wukuang-ai-revolution|五矿]]把**电力/并网/高速互联列为海外稀缺基础设施首选**（框架背书 firm 电力稀缺）。⚠️ 利率面：[[2026-09-24-spdb-us-macro-warsh-hike|浦银]]/[[2026-09-24-wukuang-fed-sep-review|五矿]] 一致"年内再加一次、非连续加息周期"、[[2026-09-24-boci-allocation-china-bonds-us-equity|中银]]美债下调——属既列利率敏感性风险、非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-25 — brief：`sec_fetch.py --since 2026-09-24` **无新增文件、0 flags**（CEG/TLN 均 0；VST 1 新增为纯融资再融资）。本期以 SEC 文件为主、外资桶无窗口内新内容。宏观新增偏鸽侧注脚：[[2026-09-19-nanhua-macro-fed-hawkish|南华期货]]判"这次加息可能是结束而非起点、市场对连续加息定价过满"（列四结构性约束）——若长端见顶回落利好未签约可调度容量的长久期估值；利率维持高位仍属既列风险、非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-28 — brief：`sec_fetch.py --since 2026-09-25` **无新增文件、0 flags**。需求侧成交实证：[[2026-09-27-soochow-power-shortage-aidc|东吴缺电周报]]记 **Luminant（VST）–New Era 20 年 ≥207 MW PPA**（[[2026-09-21-newera-8k-vistra-luminant-ppa]]）、Kodiak/Woodway 表后天然气项目、Google–Georgia Power 核电增容——数据中心"直接找发电商长约/表后直供"模式扩散，利好 TLN 未签约可调度容量（Susquehanna–AWS 之外余量）。⚠️ **德州暂停新的州级数据中心许可**——对存量并网资产中性偏正、列为 watch。宏观利率维持高位（[[2026-09-28-apollo-daily-spark-warsh-rate-hike|Apollo·Warsh]]/[[2026-09-27-guosen-multiasset-hike-nasdaq-gold|国信]]）属既列风险、非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-29 — brief：`sec_fetch.py --since 2026-09-28` **无新增文件、0 flags**。需求侧长期硬指引：[[2026-09-29-soochow-overseas-compute-alibaba-20gw|东吴·海外算力周]]记**阿里云栖大会目标"2032 年全球数据中心规模超 20GW"**、AIDC 交付链系统性拉动电力（真武 V900 2027Q1、Qwen4 训练中，✅ 已核）——超大规模云长期用电指引，利好 TLN 未签约可调度容量（Susquehanna–AWS 之外余量）。⚠️ 利率面：[[2026-09-28-cmbc-intl-overseas-macro-rates|民银国际]]记 **10Y 收 5.17%（9/25）、周 +16bp、10 月加息时点提前**（✅ CNBC：周五 5.23%、2007 以来最高）——属既列利率敏感性风险、非 Invalidation。⚠️ 未解：6→9 月股价 −18% 仍未追溯到具体 catalyst，下期继续优先。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-30 — brief：`sec_fetch.py --since 2026-09-29` **1 新增 8-K、6 flags——读全文判定为资本回报 + CEO 交接、无电力合约/监管事件**。[[2026-09-29-tln-8k-capacity-monetization-ceo|8-K 2026-09-29]]（Items 5.02/7.01/8.01/9.01）：①**CEO 交接**——McFarland 2026-12-31 卸任、**Terry Nutt 自 2027-01-01 起任 CEO**（✅ 已核）；②**PJM 容量货币化**——子公司 TEM 出售 2027/28（~6.5 GW）+ 2028/29（~6.0 GW）已出清容量收入 **~$15 亿**（经 Citi、折现 SOFR+200bps，**仅容量不含电量**，保留运营/履约义务），③用于 **$15 亿 uncollared ASR**、SRP 上调至 **$30 亿**、按当前股价回购**逾 10% 流通股**、目标净杠杆 3.5×（✅ 全核）。flags 中 terminat×121/AWS×19/cancel×3 **全为 EX-10.1/10.2 雇佣与离职协议样板条款误报**，**无任何 AWS/Susquehanna 电力合约变更**。方向中性偏正：把已出清 PJM 容量现金流提前变现回购逾 10% 流通股=管理层判断股价低估 + 现金流确定，且**保留电量上行敞口**；SOFR+200bps 融资成本延续既列利率敏感性关注（呼应 [[vst]] ~7%）、非 Invalidation。宏观利率续创新高（[[2026-09-29-cpost-overseas-macro-yields-rising|中邮]]记 30Y 5.5252%/2004 以来新高、10Y 盘中 ~5.23%；[[2026-09-30-spdb-monthly-strategy-earnings-resilience|浦银]]"高利率下靠盈利兑现"）属既列风险。⚠️ 该 8-K 仍**未直接解释 6→9 月股价 −18%**，数据缺口继续挂账。Invalidation 状态：ok/ok/ok/ok（不变）。
