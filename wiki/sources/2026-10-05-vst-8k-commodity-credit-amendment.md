---
type: source
source_type: filing
title: "Vistra 8-K — Items 1.01 / 2.03: Eleventh Amendment to Commodity-Linked Credit Agreement (revolver maturity extended 1yr)"
author: "[[vst]]"
publisher: "SEC EDGAR"
scope: [equity]
url: https://www.sec.gov/Archives/edgar/data/1692819/000114036126038468/ef20083016_8k.htm
published: 2026-10-05
ingested: 2026-10-05
raw: "https://www.sec.gov/Archives/edgar/data/1692819/000114036126038468/"
accession: 0001140361-26-038468
tags: [filing, 8-k, financing, credit-facility]
---

# VST 8-K 2026-10-05 — Commodity-Linked 循环信贷第十一次修订（展期 1 年，纯融资、非电力合约）

## TL;DR
`sec_fetch.py` 把它标成 credit agreement×125 / terminat×93 / **AWS×41** / PJM×22 / ERCOT×21 / FERC×6 / PUC×3 / cancel×3——读全文（8-K 正文 + EX-10.1 共 ~110 万字）后判定为**纯融资/展期事件**：Vistra Operations Company LLC（Vistra 间接全资子公司，"Borrower"）于 **2026-09-30** 签署对 2022-02-04 **Commodity-Linked Credit Agreement**（Citibank 为 Administrative Agent）的**第十一次修订**，主要内容为**将循环信贷到期日由 2026-09-30 展期至 2027-09-29**，并作若干与 Borrower 的 Corporate Credit Agreement 一致的条款调整。该 facility 是 Vistra 用于对冲商品/电力敞口的**抵押信贷额度**，所有 PJM/ERCOT/CAISO/ISO-NE/MISO/NYISO、FERC/PUCT、AWS、terminat/cancel 命中**均为信贷协议定义条款样板**（如 "Applicable Settlement Price" 对各 ISO 的结算价定义、治理法/制裁/bail-in/终止承诺等标准条款），**无任何电力合约、监管事件或 AWS 交易内容**。

## Thesis check
四项 [[ai-power-ipp-bull]] Invalidation **均无触及**，VST `invalidation_status` 维持 `ok/ok/ok/ok`：
- #1 hyperscaler 合约推迟/取消——**未触及**（"AWS×41" 为假命中，全文无 AWS 交易；"terminat×93" 为 Mandatory Termination of Revolving Credit Commitments 等信贷条款）。
- #2 增容/共址被 FERC/NRC/PUC 限制——**未触及**（PJM/ERCOT/FERC/PUCT 均来自结算价与定义条款，非监管行动）。
- #3/#4 光伏——无关。

**对论点的实质含义（中性）**：这是对一项**既有对冲信贷额度的例行 1 年展期**（到期前一天签署），非新增杠杆、非电力合约、非监管事件。延续本仓"利率/融资敏感性"既列关注——但本次仅为到期日滚动，未披露新定价/利差数字，信息量低。属与 [[2026-09-24-vst-8k-junior-subordinated-notes]]（$1.5B 次级票据）、[[2026-07-16-vst-8k-receivables-facility]]（应收账款融资）同类的**融资性 8-K 误报**。

## Notable claims
- "the Credit Agreement was amended to, among other things, (i) extend the Revolving Credit Maturity Date ... from September 30, 2026 to September 29, 2027 and (ii) make certain other amendments consistent with the terms of the Borrower's Corporate Credit Agreement" ——✅ 8-K 正文 Item 1.01。
- Exhibit 10.1：Eleventh Amendment to Credit Agreement, dated September 30, 2026, by and among Vistra Operations Company LLC (Borrower), the lenders party thereto and Citibank, N.A. (Administrative Agent and Collateral Agent)——✅ Item 9.01。
- 签署人 William M. Quinn, SVP and Treasurer；文件 2026-10-02 签署、2026-10-05 FILED AS OF DATE（CONFORMED PERIOD OF REPORT 2026-09-30）。

## Fact-check / Data gaps
- ✅ 事件为 Commodity-Linked Credit Agreement 第十一次修订、循环到期日 2026-09-30→2027-09-29——直接引自 8-K 正文。
- 📌 关键词误报（credit agreement/terminat/AWS/PJM/ERCOT/FERC/PUC/cancel）为 `sec_fetch.py` 已知"需读全文分类"类型——本例 flags 全部落在 EX-10.1 信贷协议定义/样板条款。
- ⚠️ 数据缺口：未披露本次展期后的额度规模、利差（Applicable Margin）或费率变化——8-K 仅摘要展期事实，细节在 EX-10.1 定义层未给汇总数字。

## Entities mentioned
[[vst]] · [[ai-power-ipp-bull]]
