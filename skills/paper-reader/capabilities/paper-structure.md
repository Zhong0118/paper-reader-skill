---
name: paper-structure
description: Use when the user has a single academic paper and wants to understand its research question, paper structure, method backbone, claimed contributions, experiments, results, or overall argument before deeper explanation or critique.
---

# Paper Structure

## 目标
把一篇论文的“骨架”搭清楚：研究问题 → 方法 → 实验/证据 → 结论。只做结构理解，不承担教学式展开、审稿式挑刺、外部文献检索或知识库成稿。

## Paper Context 复用规则
先读 `references/paper-context.md`。若存在与当前论文匹配的已有 Paper Context，优先复用；只回看原文中缺失、冲突或需要定位证据的部分，不重新通读已经可靠提取的章节。若没有 Context，才从用户提供的 PDF/正文/链接建立最小 Context。

## 工作步骤
1. 确认论文身份与来源质量；无法可靠读取的内容标 `[不确定]`，不要补猜。
2. 判定论文类型：AI/算法、系统工程、实验实证、生医/临床、理论、综述或其他；按类型调整分析重点。
3. 提取：研究问题、动机、任务/假设、方法主线、关键实验、主要结果、作者结论、作者自述局限。
4. 提取作者明确声明的贡献，并区分：
   - `[原文声明]`：必须绑定 Section/Figure/Table/Page 等证据位置。
   - `[模型归纳]`：必须说明推导依据，不能伪装成作者声明。
5. 将结果写入 Context 的 `paper_internal` 与 `source_map`；保留其他阶段已有内容。

## 输出
默认给用户一个紧凑结构：
- 一句话研究问题
- 为什么要做
- 方法主线（输入 → 核心处理 → 输出）
- 关键贡献（带证据标签）
- 最关键实验与结果
- 论文实际证明了什么
- 作者明确承认的局限

## 边界
- 不做外部检索来验证“是否世界首创”；只能说明作者如何定位自己的工作。
- 不展开公式和基础概念教学；交给 `paper-teacher`。
- 不判断 Claim 是否被证据充分支持；交给 `paper-evidence-review`。
- 不系统检查偏差、混杂和统计设计；交给 `paper-method-critic`。
- 不生成 HTML/PPT，不替用户写论文。
