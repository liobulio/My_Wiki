---
type: position
asset: "[[vst]]"
ticker: VST
status: open
weight:
shares: 11.523
account: IBKR
entry_date:
entry_price:
conviction: 3
thesis: "[[ai-power-ipp-bull]]"
invalidation_status: [ok, ok, ok, ok]
opened: 2026-09-11
updated: 2026-10-01
---

# VST — Vistra (open position)

## The Thesis Test
Shared with the other AI-power IPP holdings — see [[ai-power-ipp-bull]] for the Edge, the
Catalyst, and the four Invalidation conditions. `invalidation_status` above tracks them in
order: (1) hyperscaler contracts delayed/cancelled · (2) uprate/co-location restricted by
regulators · (3) solar expansion faster than expected · (4) solar rebuild cost falling.

## Summary
Real holding: **11.523 shares** at IBKR (human-supplied 2026-09-11). Weight is computed from
shares × last price by `scripts/render_brief.py`; `entry_date` / `entry_price` /
`conviction` are the human's to fill — `conviction: 3` is a placeholder.

## Conviction rationale
See [[ai-power-ipp-bull]]. Asset detail on [[vst]].

## Filings watch
The daily brief reads every new 8-K / 10-Q / 10-K for this registrant and appends an entry
below when it bears on the thesis (regulator-restricted contracts first).

## Sources
[[ai-power-ipp-bull]] · [[vst]]

## Update history
- 2026-09-11 — opened in the wiki from the human's stated holding (11.523 sh, IBKR).
- 2026-09-11 — 读取 8-K 2026-08-07（[[2026-08-07-vst-8k-q2-earnings]]）、8-K 2026-07-16（[[2026-07-16-vst-8k-receivables-facility]]，融资性、无关）与 10-Q Q2：Ongoing Adj. EBITDA +30%；Helix（KKR/NVIDIA/KIA）优先供电方；FERC 批准 Cogentrix；Meta PPA 贡献自 2027 起；2028 仅对冲 72%。Invalidation：ok/ok/ok/ok。
- 2026-09-14 — brief：`sec_fetch.py --since 2026-09-11` **无新增文件**。行业面正向（同 CEG/TLN：超大规模云厂商长期核电 PPA 持续、DOE/NERC 电力需求上修）。VST 2028 仅对冲 72%，对上行电价敞口最大——利率敏感性与电价同为关注项；本周无监管/合约新事件触及 Invalidation。宏观：加息预期升温、10Y 逼近 5%。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-15 — brief：`sec_fetch.py --since 2026-09-14` **无新增文件**。需求侧继续走强（Oracle 单季交付 850 MW、TSMC +53.3%、IEA 用电 2030 翻倍，[[2026-09-14-donghai-electronics-tsmc]]、[[2026-09-14-dongguan-aidc-power]]）。VST 2028 仅对冲 72%，对上行电价敞口最大——AI 电力需求上行对未对冲部分为正面，利率敏感性为反向关注项；本周无监管/合约事件触及 Invalidation。宏观：本周 FOMC（9/16–17），PPI +5.4%、油价破 $100、CME 加息概率 88.1%（[[2026-09-14-soochow-us-weekly-hike-risk]]）。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-16 — brief：`sec_fetch.py --since 2026-09-15` **无新增文件、0 flags**。VST 2028 仅对冲 72%，对上行电价敞口最大——AI 电力需求上行为正面，利率为反向关注项。今日进入 **FOMC（9/16–17）**；10Y 9/14 一度触及 **5.04%** 后回落（[[us-treasury-10y]]），[[2026-09-16-spdb-intl-rates-equity|浦银]]判上行有序/AI 仍是主线、[[2026-09-16-dongxing-cpi-continuous-hike|东兴]]警示连续加息（10Y 目标 4.7–5%）——利率敏感性属既列风险，非 Invalidation。无监管/合约事件触及失效条件。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-17 — brief：`sec_fetch.py --since 2026-09-16` **无新增文件、0 flags**。**FOMC 加息 25bp 至 3.75%–4.00%、12–0 偏鹰兑现**（[[2026-09-17-spdb-intl-fomc-hike-hawkish]] 等四家）。VST 2028 仅对冲 72%，对上行电价敞口最大——AI 电力需求上行为正面，加息推升的利率敏感性为反向关注项（既列风险，非 Invalidation）。无监管/合约事件触及失效条件。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-18 — brief：`sec_fetch.py --since 2026-09-17` **无新增文件、0 flags**。需求侧再获强化（[[2026-09-18-greendh-futures-ai-reaccel|格林大华期货]]：GPU 涨价潮、Nvidia 每 GW 营收 Vera Rubin ~$400 亿、SpaceX 20 GW 在线电力目标）——VST 2028 仅对冲 72%、对上行电价敞口最大，AI 电力需求上行对未对冲部分为正面。宏观利率敏感性（[[2026-09-18-dongxing-fomc-oil|东兴]] 维持 10Y 4.7–5%、不排除年内连续加息）为反向关注项，属既列风险、非 Invalidation。无监管/合约事件触及失效条件。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-21 — brief：`sec_fetch.py --since 2026-09-18` **无新增文件、0 flags**。上行电价敞口逻辑再获背书：[[2026-09-20-soochow-overseas-compute-power|东吴]] 引 TrendForce（2026 用电 +31%、2030 缺口 268 GW）、[[2026-09-21-huaxin-ai-infra-power|华鑫]]"电力供给约束倒逼"——VST 2028 仅对冲 72%、对未对冲部分的上行电价最敏感，方向正面（不触发失效条件）。新风险面：AI 基建融资端 CDS 走阔、Oracle FCF 转负（[[2026-09-20-kaiyuan-oracle-nebius-cds|开源]]/[[2026-09-21-guojin-oracle-rpo-margin|国金]]）——属既列利率/融资敏感性风险，非 Invalidation。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-22 — brief：`sec_fetch.py --since 2026-09-21` **无新增文件、0 flags**。需求侧再获权威背书：[[2026-09-22-cpost-iaea-nuclear-uprate|中邮]]引 **IAEA 连续第六年上调**核电装机预期（2060 高情景 1284 GW，已核）——firm/清洁电力长期需求上修，对 VST 未对冲的可调度容量方向正面；[[2026-09-22-pacific-electronics-ai-memory|太平洋]]记 AMAT DRAM/HBM 设备放量（AI 电力需求刚性延续）。⚠️ 利率面：[[2026-09-22-guoxin-sec-fed-hawkish-hike|国新]]（10Y 收 5.021% 新高）vs [[2026-09-22-soochow-us-weekly-post-hike|东吴]]（利率压估值不改 AI 景气、上周公用事业领跌）——VST 2028 仅对冲 72%、对上行电价最敏感，AI 电力需求为正面、利率上行为反向关注项（既列风险，非 Invalidation）。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-23 — brief：`sec_fetch.py --since 2026-09-22` **无新增文件、0 flags**。上行电价敞口逻辑再获需求侧硬数据背书：[[2026-09-23-huaxin-nvda-rubin|华鑫]]记 NVDA FY27Q2 数据中心 **$89B/+117%、Rubin 全面量产**、[[2026-09-23-huaxin-avgo-ai-semi|AVGO]] AI 半导体 $16.7B/+221%——算力交付放量=数据中心电力刚性，VST 2028 仅对冲 72%、对未对冲部分的上行电价最敏感，方向正面。⚠️ 利率面：[[2026-09-23-dongfang-jincheng-overseas-hike|东方金诚]]记 10Y 周收 5.01%、美日加息；[[2026-09-22-boci-ai-mainline-recheck|中银]]"利率是核心估值约束"——利率上行为反向关注项，属既列利率敏感性风险、非 Invalidation。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-24 — brief：`sec_fetch.py --since 2026-09-23` **无新增文件、0 flags**。上行电价敞口逻辑再获需求侧背书：[[2026-09-22-huaxin-cisco-ai-network|华鑫·思科]]记 FY2026 hyperscaler AI 基础设施订单 **$9.3B（~4.5× YoY）、FY27 $7.5B（+87.5%）**——数据中心用电刚性延续；[[2026-09-24-wukuang-ai-revolution|五矿]]把**电力/并网/高速互联列为海外稀缺基础设施首选**。VST 2028 仅对冲 72%、对未对冲部分上行电价最敏感，需求侧方向正面。⚠️ 利率面：[[2026-09-24-spdb-us-macro-warsh-hike|浦银]]（12 月或再加、年底布伦特 90–100）、[[2026-09-24-wukuang-fed-sep-review|五矿]]（点阵 4.1%、市场反应钝化）、[[2026-09-24-boci-allocation-china-bonds-us-equity|中银]]（美股上调、美债下调）——利率上行为反向关注项，属既列风险、非 Invalidation。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-25 — brief：`sec_fetch.py --since 2026-09-24` **1 新增文件、1 flag**——读全文判定为**纯融资/再融资**：8-K 2026-09-24（[[2026-09-24-vst-8k-junior-subordinated-notes]]，Items 1.01/8.01）完成发行 **$1.5B 初级次级票据**（$850M 7.000% Series A + $650M 7.250% Series B，2057 到期，Vistra 担保），用途为向 Vistra 分配以赎回其 8.0%/7.0% 永续优先股（reset 日 2026-10/12）——**负债管理、非新增杠杆**，terminat/AWS/cancel/PPA 均为承销协议/契约样板条款误报，**无电力合约/监管事件触及失效条件**。关键读数：VST 长久期（2057）混合资本新发成本约 **7%**，是本仓利率/融资敏感性既列风险的具体读数。宏观新增偏鸽侧注脚：[[2026-09-19-nanhua-macro-fed-hawkish|南华期货]]判"这次加息可能是结束而非起点、市场对连续加息定价过满"（列四结构性约束）——若成立、长端见顶回落利好长久期 PPA 估值；仍属既列利率风险、非 Invalidation。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-28 — brief：`sec_fetch.py --since 2026-09-25` **0 新增文件、0 flags**。**Catalyst 型正面事件**：经 [[2026-09-27-soochow-power-shortage-aidc|东吴缺电周报]]线索追进一手文件——**VST 旗下 Luminant 与 New Era 签 20 年 PPA**（保底 200 MW、至多 207 MW，供电来自 Vistra **Odessa 1,180 MW 燃气厂**、表后直供、预计 **27Q3** 商供；Vistra 另获受电部分数据中心 **5% 权益 + ROFR/ROFO**，[[2026-09-21-newera-8k-vistra-luminant-ppa]]，✅ 已核）——把未签约可调度天然气容量长期货币化、绕开并网瓶颈的教科书式成交，直接对应 Edge/Catalyst。规模相对全机队不大（≤207/1,180 MW 单厂），方向利多。⚠️ **德克萨斯州暂停新的州级数据中心许可**（待电力/水资源审查）——对存量已并网发电资产（如 Odessa/ERCOT 机队）中性偏正（巩固 firm 电力稀缺），列为 **watch**；仅当演化为对新增用电负荷的系统性限制、拖慢数据中心落地节奏，才属 Invalidation #1 的上游风险，持续跟踪。宏观：[[2026-09-28-apollo-daily-spark-warsh-rate-hike|Apollo·Warsh 无前瞻指引]] + [[2026-09-27-guosen-multiasset-hike-nasdaq-gold|国信]]"实际利率成核心变量、10Y 5.2% 关键点位"——利率维持高位/波动为反向关注项，属既列风险、非 Invalidation（呼应 VST ~7% 新发成本）。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-29 — brief：`sec_fetch.py --since 2026-09-28` **0 新增文件、0 flags**。需求侧长期硬指引：[[2026-09-29-soochow-overseas-compute-alibaba-20gw|东吴·海外算力周]]记**阿里云栖大会目标"2032 年全球数据中心规模超 20GW"**、AIDC 交付链对"芯片/光互联/存储/**电力**/工程集成"系统性拉动（真武 V900 2027Q1、Qwen4 训练中，✅ 已核）——超大规模云 20GW 级十年用电蓝图，背书 firm 电力需求时间跨度；VST 2028 仅对冲 72%、对未对冲部分上行电价最敏感，方向正面（不触发失效条件）。⚠️ 利率面：[[2026-09-28-cmbc-intl-overseas-macro-rates|民银国际]]记 **10Y 收 5.17%（9/25）、周 +16bp、年内再加一次时点提前至 10 月**（✅ CNBC：周五 5.23%、2007 以来最高）——呼应 VST ~7% 新发成本，属既列利率敏感性风险、非 Invalidation。New Era 20 年 PPA（[[2026-09-21-newera-8k-vistra-luminant-ppa]]）本期无新进展；德州数据中心暂停许可维持 watch。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-10-01 — brief：`sec_fetch.py --since 2026-09-30` **无新增文件、0 flags**（10/01 中国国庆、东财桶无窗口内新内容）。本期唯一在窗口内新源 [[2026-10-01-apollo-daily-spark-everyone-talking-ai|Apollo·Slök「Everyone Is Talking About AI」]]：标普 500 财报会提 "AI" 公司占比近历史高位、Slök 警示"hype has moved faster than the payoff"（延续 69% 采用 / 仅 29% 量化、"41% 依赖 -59%"价值链利润错配）——属 **Invalidation #1 的上游**（AI 付费回报 → 云厂 capex → 电力合约）、仅远端提示、无电力合约推迟/取消实证，**ok 不变**；VST 2028 仅对冲 72%、对未对冲部分上行电价最敏感，需求侧硬数据（Marvell DC +46%、Amphenol 通信 +85%、NVDA DC +117%）仍指向用电刚性。New Era 20 年 PPA（[[2026-09-21-newera-8k-vistra-luminant-ppa]]）本期无新进展；德州数据中心暂停许可维持 watch。Invalidation 状态：ok/ok/ok/ok（不变）。
