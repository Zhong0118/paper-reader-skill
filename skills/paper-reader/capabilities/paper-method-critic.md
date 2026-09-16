---
name: paper-method-critic
description: Use when the user wants a deeper methodological critique of a study, including experimental design, controls, confounders, bias, statistics, measurement validity, causal inference, reproducibility, robustness, generalizability, or externally documented limitations.
---

# Paper Method Critic

## 目标
在已经理解论文之后，检查“这个研究设计本身靠不靠谱”，并在存在 `external_context` 时利用后续研究、复现结果和 benchmark 局限增强判断，而不是再次解释论文。

## Paper Context 复用规则
先读 `references/paper-context.md`。优先复用 `paper_internal`、`evidence_review` 与 `external_context`；只回看 Methods、Experiments、Statistics、Supplement、Limitations 等必要部分。若外部脉络缺失但用户的问题涉及 SOTA、复现、benchmark 局限或后续验证，先调用 `paper-context-research`，不要自己再独立搜索一遍。

## 方法学检查
先识别研究类型，再选择框架。

按研究类型选用：
- 设计是否能回答研究问题；
- 对照/baseline 是否合理、公平、充分；
- 混杂、选择偏差、测量偏差、数据泄漏；
- 数据量、抽样、独立重复和统计功效；
- p 值、置信区间、效应量、多重比较、误差条/多 seed；
- 指标是否与真正目标一致；
- 因果结论是否超出设计；
- 消融、敏感性、鲁棒性是否足够；
- 数据/代码/参数与可复现性；
- 外部有效性与泛化范围。

领域加权：
- **AI/CS**：train/test contamination、baseline tuning、公平计算预算、多 seed、OOD、benchmark saturation、成本与复现。
- **生医/临床**：随机化、盲法、样本量、终点、混杂、批次效应、选择偏差、临床意义。
- **观察性研究**：混杂控制、反向因果、测量误差、模型设定与稳健性。

- **理论论文**：定义、假设、证明步骤、定理适用范围与反例；不套用多 seed 或临床试验要求。
- **综述论文**：检索范围、纳入排除标准、来源覆盖、综合方式和结论边界；按叙述综述/系统综述区别要求，不编造实验。

## 外部证据增强
若 `external_context` 有可靠来源，再检查：
- 后续工作是否稳定复现论文核心结论；
- 后续 benchmark/Survey 是否指出评价协议缺陷；
- 是否有人发现失效场景、成本瓶颈或数据偏差；
- 后续方法主要修改了哪里，这是否反向暴露原方法弱点；
- 相反结果是否来自不同人群/数据/设定，避免假冲突。

所有这些写入 `externally_supported_concerns`，并绑定 `source_ledger` id；不得把外部批评伪装成作者自述。

## 输出
按 `Strengths / Major concerns / Minor concerns / Externally supported concerns / Uncertain due to missing information / How to improve` 组织。每个问题写：**问题是什么 → 证据位置/外部来源 → 为什么影响结论 → 如何改进**。

写入 Context 的 `method_critique`。若判断改变 Claim 支持度，按 Context 合并规则修订关联条目与依赖摘要，记录变更原因；原文作者主张不随评价改变。

## 边界
- 不为了挑刺强行制造问题；证据不足标 `[不确定]`。
- 不重复 Claim–Evidence 表，除非方法学问题改变其支持度。
- 不重复执行外部搜索；缺什么就回到 `paper-context-research` 补什么。
