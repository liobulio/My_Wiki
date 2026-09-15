---
type: source
source_type: research
title: "算电共舞，从制造之城到AIDC电力底座"
author: "[[dongguan-securities]]"
publisher: "东方财富研报中心"
institution: "[[dongguan-securities]]"
scope: [industry]
url: https://pdf.dfcfw.com/pdf/H3_AP202609141829372317_1.pdf
published: 2026-09-14
ingested: 2026-09-15
raw: "[[raw/2026-09-14-dongguan-aidc-power.md]]"
tags: [ai-power, data-center, power-equipment, hvdc]
---

# 东莞证券 · 算电共舞：AIDC 电力底座（2026-09-14）

## TL;DR
东莞证券电力设备团队（李嘉俊/黄秀瑜）专题：单机柜功耗从传统 DC 的 3–8 kW 跃升至 AIDC 的 20–100 kW，
驱动供配电从 UPS 向 **800V 高压直流（HVDC）** 迭代；9/4 中央网信办等七部门首提探索算力设施 800V 高压直流
架构。落地标的为 A 股电源设备（易事特/铭普光磁/奥海科技）——**超出本 wiki 美股范围，仅作需求侧背景**。
对本 wiki 有价值的是其需求侧数据（英伟达功耗路线、IEA 全球数据中心用电翻倍），印证 [[ai-power-demand]]。

## Key takeaways（需求侧，与本 wiki 相关部分）
- **英伟达 GPU 功耗路线**：TDP 从 V100 300W → B200 ~1000W → **GB300 单卡 1400W**；整机柜层面 VeraRubin（VR200，
  2026）72 GPU **2300W**、VR300（2027）**3600W**。英伟达力推 800VDC 架构。
- **全球数据中心用电（IEA）**：2024 年 415 TWh → **2030 年 945 TWh（翻倍）**；占总用电比重 2014 年 1.5% → 2030 年 3%。
- **政策**：9/4《促进数字化绿色化协同转型发展实施方案（2026–2030）》首提探索算力设施 800V 高压直流供电、
  推动超百千瓦单机柜部署。
- **技术路线**：HVDC、直流不间断电源、固态变压器（SST，"硅进铜退"）三线替代传统交流配电。
- **A 股标的（范围外）**：易事特（300376，UPS/HVDC 龙头）、铭普光磁（002902，磁性元器件）、奥海科技（002993，
  "电源+芯片"，ATS 5500W AI 服务器电源）。

## Notable claims
- "IEA 预测，2030 年全球数据中心用电量将达到 945TWh，较 2024 年的 415TWh 实现翻倍增长"（原文）。
- "英伟达 GPU 设计功耗从 300W 升至 1400W"（GB300，原文）。

## Entities mentioned
[[nvda]]（GPU 功耗路线、800VDC）· [[ai-power-demand]] · IEA · 中央网信办 · 易事特/铭普光磁/奥海科技（A 股，范围外）

## Fact-check / Data gaps
- IEA 945 TWh（2030）为**机构预测/projection**；与本 wiki 既有 DOE/NERC 需求侧数据（[[2026-09-13-guojin-compute-mainline-power]]）
  方向一致，量级可信，未逐项独立核实。
- 英伟达功耗路线（1400W/2300W/3600W）来自英伟达《800VDC Architecture》白皮书口径，属公司规划。
- 中国 UPS 市场规模（2026 超大功率 ¥71.2 亿 +19.66%）与 A 股标的财务为国内口径，与美股无关，未核实。

## Agrees / contradicts
- **Agrees** [[ai-power-demand]] / [[ai-power-ipp-bull]] 的需求侧：数据中心用电结构性上行、firm 供给稀缺。
  与 [[2026-09-13-guojin-compute-mainline-power]]（电力是算力 Beta）、[[2026-09-12-guosen-ai-compute-roi]]（电网年增
  仅 10–15 GW）同源。
- 无矛盾；本报告落点在 A 股电源设备供给链，与美股 IPP 持仓仅共享需求侧宏观背景。

## Sources
raw: [[raw/2026-09-14-dongguan-aidc-power.md]]
