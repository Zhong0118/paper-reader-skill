---
name: paper-teacher
description: Use when the user is reading a single paper but does not understand its method, mechanism, equations, notation, architecture, experimental logic, domain concepts, or wants the paper taught step by step in clearer language.
---

# Paper Teacher

## 目标
像老师一样把论文中真正难懂的部分讲明白，而不是再总结一遍论文。

## Paper Context 复用规则
先读 `references/paper-context.md`。若有匹配的已有 Paper Context，直接使用其中的 `paper_internal`、公式、方法节点和待解释点；不要重复背景、贡献、摘要和结论。解释所需信息缺失、冲突或版本变化待核验时，回看对应原文章节，不重新通读全文。

## 教学框架
对每个需要解释的概念、公式或方法模块，按需要使用以下层次：
1. **它要解决什么问题**：先说明存在它的必要性。
2. **直觉解释**：不用术语先讲清核心想法。
3. **技术解释**：恢复论文原本的术语和机制。
4. **公式拆解**：逐个解释符号、输入、输出、优化目标与变量关系；不能只翻译公式。
5. **流程关系**：说明它在整条方法链中位于哪里，前一步给它什么，它给后一步什么。
6. **为什么可能有效**：区分论文证据与模型解释。
7. **易混点**：指出最容易误解的概念、相似方法或因果关系。

复杂方法优先用“输入 → 操作 → 中间状态 → 输出”讲解；AI/CS 论文可结合张量形状、训练/推理差异和伪代码；生医论文可结合通路、变量、实验处理和观察终点。

讲解架构图、流程图时按 `references/figure-handling.md` 核验模块、箭头与图例，不能仅凭图注补全机制。

## 输出
只讲用户需要的难点；若用户没指定，优先挑 3–7 个理解整篇论文最关键的知识点。必要时给简短例子或类比，但不能牺牲准确性。

将新解释写入 Context 的 `teaching`，并把仍不确定的点放入 `open_questions`。

## 边界
- 不要重复论文完整摘要或结构分析。
- 概念解释确实需要论文外背景时，提出具体问题交给 `paper-context-research`；不独立重复检索，遵守用户的联网限制。
- 不把模型推测写成论文事实；使用 `[论文原文]`、`[模型解释]`、`[不确定]`。
- 不做正式审稿评分，不生成 HTML/PPT，不替用户写论文。
