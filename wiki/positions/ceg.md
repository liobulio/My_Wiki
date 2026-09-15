---
type: position
asset: "[[ceg]]"
ticker: CEG
status: open
weight:
shares: 5.891
account: IBKR
entry_date:
entry_price:
conviction: 3
thesis: "[[ai-power-ipp-bull]]"
invalidation_status: [ok, ok, ok, ok]
opened: 2026-09-11
updated: 2026-09-15
---

# CEG — Constellation Energy (open position)

## The Thesis Test
Shared with the other AI-power IPP holdings — see [[ai-power-ipp-bull]] for the Edge, the
Catalyst, and the four Invalidation conditions. `invalidation_status` above tracks them in
order: (1) hyperscaler contracts delayed/cancelled · (2) uprate/co-location restricted by
regulators · (3) solar expansion faster than expected · (4) solar rebuild cost falling.

## Summary
Real holding: **5.891 shares** at IBKR (human-supplied 2026-09-11). Weight is computed from
shares × last price by `scripts/render_brief.py`; `entry_date` / `entry_price` /
`conviction` are the human's to fill — `conviction: 3` is a placeholder.

## Conviction rationale
See [[ai-power-ipp-bull]]. Asset detail on [[ceg]].

## Filings watch
The daily brief reads every new 8-K / 10-Q / 10-K for this registrant and appends an entry
below when it bears on the thesis (regulator-restricted contracts first).

## Sources
[[ai-power-ipp-bull]] · [[ceg]]

## Update history
- 2026-09-11 — opened in the wiki from the human's stated holding (5.891 sh, IBKR).
- 2026-09-11 — 读取 8-K 2026-08-06（[[2026-08-06-ceg-8k-q2-earnings]]）与 10-Q Q2：FERC 批准 CIR 转移、NRC 批准燃料许可 → Crane（TMI-1）2027 重启路径清晰；新签 920 MW 核电 PPA；全年 EPS 指引上调至 $11.50–12.50。⚠️ 关注项：PJM 容量价格上限 $325 延长至 2029/30，无上限出清价本可达 $554.72 — 政策压制上行。Invalidation 状态：ok/ok/ok/ok。
- 2026-09-14 — brief：`sec_fetch.py --since 2026-09-11` **无新增 8-K/10-Q/10-K**（EDGAR 全文检索端点 403，见 log）。公司行动（lead，非 SEC 文件）：9/12 宣布以 **$7.15 亿**收购壳牌 RISEC（609 MW 联合循环燃气，ISO-NE），预计 2027Q1 完成，管理层称即时增厚、>10% 无杠杆回报、不影响 $50 亿回购 ✅ 已核（[[2026-09-13-soochow-power-scarcity-nuclear-ppa]]，CEG 新闻稿）。**不触发任何 Invalidation**（增量可调度容量，方向正面）。宏观背景：8 月核心 CPI +0.3%、加息预期升温、10Y 逼近 5%（[[2026-09-13-guosen-multiasset-hike-gold]]）→ 长久期现金流的利率敏感性风险上升（thesis 既列风险，非 Invalidation 条件）。Invalidation 状态：ok/ok/ok/ok（不变）。
- 2026-09-15 — brief：`sec_fetch.py --since 2026-09-14` **无新增 8-K/10-Q/10-K**（三家均 0）。需求侧继续走强：Oracle Q1 FY27 单季交付 **850 MW** 数据中心容量、TSMC 8 月营收 +53.3% YoY 创高（AI capex 未退坡，[[2026-09-14-soochow-us-weekly-hike-risk]]、[[2026-09-14-donghai-electronics-tsmc]]）；IEA 全球数据中心用电 2030 翻倍至 945 TWh（[[2026-09-14-dongguan-aidc-power]]）——均利好 firm 供给稀缺逻辑，不触发失效条件。宏观：本周 FOMC（9/16–17），8 月 PPI +5.4%、油价破 $100，CME 加息概率升至 88.1%（[[2026-09-14-soochow-us-weekly-hike-risk]]）→ 利率敏感性风险抬升（既列风险，非 Invalidation）。Invalidation 状态：ok/ok/ok/ok（不变）。
