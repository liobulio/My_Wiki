---
type: source
source_type: filing
title: "New Era Energy & Digital 8-K — 20-year, up-to-207 MW gas PPA with Vistra/Luminant (Ector County/Odessa)"
author: "[[vst]]"
publisher: "SEC EDGAR"
scope: [equity]
url: https://www.sec.gov/Archives/edgar/data/2028336/000121390026101642/ea030571601ex99-1.htm
published: 2026-09-21
ingested: 2026-09-28
raw: "https://www.sec.gov/Archives/edgar/data/2028336/000121390026101642/"
accession: 0001213900-26-101642
tags: [filing, 8-k, ppa, vistra, luminant, data-center, gas]
---

# New Era 8-K 2026-09-21 — 20 年 · 至多 207 MW · Luminant（Vistra 子公司）向 TCDC 供电 PPA

## TL;DR
交易对手方 **New Era Energy & Digital, Inc.（Nasdaq 上市 AI 数据中心开发商，SEC CIK 2028336）** 于 **2026-09-21** 公告并 8-K
披露：与 **Vistra 旗下 [[vst|Luminant]]** 签署 **20 年**电力购买协议（此后逐年自动续期），为其位于**德州 Midland（二叠纪盆地）
493 英亩、规划 1.4 GW** 的 Texas Critical Data Centers（TCDC）**一期**提供**保底 200 MW、至多 207 MW** 表后天然气基荷电力。
电力来自 **Vistra 位于德州 Odessa 的 1,180 MW 燃气电厂**（"located immediately adjacent to the TCDC site"），
**预计 2027 年 Q3 开始商业供电**。首次供电后 Vistra 获得**受电部分数据中心 5% 无投票权权益**，并取得
**TCDC 未来开发的优先拒绝权（ROFR）+ New Era 其他项目的优先要约权（ROFO）**。这是本仓 [[vst]] 把**未签约可调度
天然气容量长期货币化**的一个具体成交——属 [[ai-power-ipp-bull]] 的 **Catalyst 型事件**（新签长期供电合约、再定价存量容量）。

## Thesis check
四项 [[ai-power-ipp-bull]] Invalidation **均无触及**，`invalidation_status` 维持 `ok/ok/ok/ok`：
- #1 hyperscaler 合约推迟/取消——**反向（正面）**：非取消，而是**新签** 20 年长约。对手方是 AI 数据中心开发商 New Era/TCDC，
  非具名超大规模云厂商，但同为长期 firm 电力买家，直接对应 Edge"把未签约可调度电力卖进偏紧市场"。
- #2 增容/共址被 FERC/NRC/PUC 限制——**未触及**（表后天然气供电、无核电增容/监管条款）。⚠️ 但见 [[2026-09-27-soochow-power-shortage-aidc]]：
  **德州暂停新的州级数据中心许可**（等待电力/水资源基础设施审查）——尚未落到具体项目、对存量已并网发电资产（如 Odessa）反而巩固稀缺性；
  列为 watch 观察项而非触及（本 PPA 供电资产为存量、非新建审批范畴）。
- #3/#4 光伏——无关。

**对论点的实质含义（正面）**：这是本仓论点里"存量可调度电力签长约再定价"的教科书式成交——20 年期限、保底 200 MW、
供电资产为 Vistra 已并网的 Odessa 1,180 MW 燃气机组（表后直供、免并网排队），且 Vistra 额外拿到项目 5% 权益 + ROFR/ROFO
的上行期权。规模相对 VST 全机队不大（≤207 MW / 1,180 MW 单厂），但**验证需求侧愿以 20 年长约锁定 firm 电力**、且是"数据中心
直接找发电商表后直供"模式（绕开并网瓶颈）的又一实证，方向利多。

## Notable claims（均引自 8-K Ex-99.1 press release，✅ 已核）
- "minimum of 200 MW and up to 207 MW of power for Phase 1"；合约期 **20 年**，此后逐年自动续期——✅ 8-K Ex-99.1。
- 供电来自 **Vistra Odessa 1,180 MW 燃气电厂**，"immediately adjacent to the TCDC site"；**预计 2027 Q3 商业供电**——✅。
- Vistra 获 **5% 无投票权权益**（受电部分）+ TCDC 未来开发 **ROFR** + New Era 其他项目 **ROFO**——✅。
- 数据中心：德州 **Midland**（二叠纪盆地）、**493 英亩**、规划总量 **1.4 GW**——✅。
- 公告日 **2026-09-21**（New Era 新闻稿 + Nasdaq/DCD/Latitude Media 报道一致）。

## Fact-check / Data gaps
- ✅ 交易条款（20 年、200/207 MW、Odessa 1,180 MW、Q3 2027、5% 权益 + ROFR/ROFO、Midland 493 英亩 1.4 GW）——New Era 8-K Ex-99.1
  与 DataCenterDynamics / Latitude Media / Nasdaq / Yahoo Finance 新闻稿一致。
- 📌 **归档说明**：这是**交易对手方（New Era）的 8-K**，非 [[vst]] 自身文件；`sec_fetch.py --since 2026-09-25` 下 VST **0 新增文件**
  （PPA 公告日 09-21 早于本期 SINCE，且未构成 VST 层面的 8-K 触发事件）。据 SKILL 的"把线索追进文件"原则，直接引用 New Era 的
  一手 8-K/新闻稿而非二手报道；[[2026-09-27-soochow-power-shortage-aidc|东吴缺电周报]]为发现该成交的线索来源。
- 📌 New Era 同期另有 424B5（募资）文件——与本 PPA 的电力条款无关，未展开。

## Entities mentioned
[[vst]] · [[ai-power-ipp-bull]] · [[ai-power-demand]] · [[2026-09-27-soochow-power-shortage-aidc]]
