---
name: paper-evidence-review
description: Use when the user wants to know whether a paper's main claims are supported by its own experiments, results, tables, figures, ablations, proofs, or other internal evidence, including strengths, weaknesses, and overclaiming.
---

# Paper Evidence Review

## 目标
回答一个核心问题：**作者说了什么，论文内部到底拿什么支持，支持力度有多强？** 这里只审目标论文自己的证据，不拿后来论文替作者补证据。

## Paper Context 复用规则
先读 `references/paper-context.md`。若存在匹配 Context，直接从 `paper_internal.claims`、实验、结果和 `source_map` 开始，不重新总结论文。只有 Claim 或 Evidence 缺失、冲突或无法定位时，才回看相关原文章节。

## Claim–Evidence 方法
对主要 Claim 建立表：

| Claim | 类型 | Evidence | 位置 | 支持度 | 原因 |
|---|---|---|---|---|---|

图表证据按 `references/figure-handling.md` 实际查看；读不清的图不能视为已经核验。只读摘要或证据无法访问时，标记 Not assessable，区分“没有证据”与“尚未读取证据”。

支持度只用：`Strong / Moderate / Weak / Unsupported / Not assessable`。

检查：Evidence 是否直接回答 Claim；baseline/对照是否充分；ablation 是否隔离关键组件；结果是否跨数据集/设置稳定；结论是否超出实验覆盖；图表、正文与结论是否一致；理论 Claim 是否给出证明、假设与适用条件。

创新性先只评估论文内部可证明部分。是否领域首创、是否领先同期工作，交给 `paper-context-research` 外部核验。

Strong 表示直接证据覆盖该 Claim 及关键条件；Moderate 表示有直接支持但覆盖或控制有限；Weak 表示间接或明显受限；Unsupported 表示已检查的可用证据未支持该主张；Not assessable 表示材料缺失或不可读。评分需结合论文类型与理由，不作机械打分。

## 输出
1. 3–8 个核心 Claim–Evidence 条目；
2. 最强 1–3 条证据；
3. 最明显的证据缺口与过度外推；
4. 哪些结论可以接受，哪些仍需外部验证；
5. 需要交给 `paper-context-research` 或 `paper-method-critic` 的问题。

写入 Context 的 `evidence_review`。

## 边界
- 本阶段不重复外部检索。
- 不做全面偏差、混杂、统计审计。
- 不给录用分数或接受/拒绝决定，除非用户明确要求转换成审稿格式。
