---
name: paper-note
description: Use when the user wants to turn an already-read paper and its related research context into a durable Markdown or Obsidian-style learning record for long-term study, comparison, review, and reuse.
---

# Paper Note

## 目标
把当前论文、教学解释、Claim–Evidence、方法学批判和相关论文脉络整理成一份以后真的会回来看的**论文学习档案 / 知识库记录**。它不是摘要换皮，也不是第六次重新分析全文。

## Paper Context 复用规则
先读 `references/paper-context.md`。只要存在匹配 Context，就以它为主材料：不得为了“让笔记更完整”重新跑已经完成的阶段。若用户要求完整学习档案而 `external_context` 明显为空，先补一次 `paper-context-research`；若 Web 不可用，明确缺口而不是编造相关论文。

## 默认 Markdown 结构

### 0. 论文卡片
标题、作者、机构、Venue、年份、DOI/arXiv、代码、数据集、论文类型、阅读日期。

### 1. 快速回忆
- 一句话讲清；
- 它解决什么问题；
- 3 个最重要贡献；
- 最重要结果；
- 为什么值得记住。

### 2. 研究问题与背景
研究问题、动机、已有方法为什么不够、作者核心假设。

### 3. 方法整体框架
输入 → 核心操作 → 中间状态 → 输出；复杂方法按模块拆解。

### 4. 关键知识点与核心公式
吸收 `teaching`：概念定义、前置知识、核心公式、符号解释、直觉解释、公式在方法链中的作用、易混点。

### 5. 实验设计与关键结果
Dataset / Baseline / Metric / Control / Ablation；关键 Figure/Table 的结果，以及“说明了什么 / 没说明什么”。

### 6. Claim–Evidence
保留最关键的 Claim–Evidence 矩阵、最强证据、薄弱证据和 overclaim。

### 7. 方法学与局限
作者自述局限、内部分析发现、外部文献验证的局限必须分栏；保留复现、偏差、统计、泛化等问题。

### 8. 这篇论文真正证明了什么 / 没证明什么
用短句划清结论边界。

### 9. 技术发展脉络
按时间写关键前置工作 → 当前论文 → 代表性 follow-up，并说明每一跳“改变了什么”。

### 10. 作者研究路线
作者/课题组直接相关前作与当前论文的继承关系；不存在可靠前作就明确写无充分证据。

### 11. 同期竞争与相关论文对比
至少对最相关的若干篇做表格：

| Paper | Year | Core idea | Setting/Benchmark | 与当前论文关系 | 优势 | 局限 |
|---|---:|---|---|---|---|---|

### 12. 当前 SOTA
区分“论文发表当时”与“截至 `retrieved_at` 的当前状态”。写清 dataset / metric / setting / compute；不能只写排行榜名次。

### 13. Benchmark 现状
论文用了哪些 Benchmark、它们测什么、已知缺陷、是否存在后续修订/替代 benchmark。

### 14. 后续工作与外部评价
谁继承、改进、替代、复现或质疑了这篇论文；重要判断绑定 `source_ledger`。

### 15. Survey / Review 与推荐进一步阅读
给出“先读 → 再读 → 深入读”的阅读路径；每篇写一句为什么读，而不是只列标题。

### 16. 我的笔记
只保留用户自己的观点、灵感和疑问；没有就留空，不替用户编造。

### 17. Socratic Questions
给 3–8 个能检查是否真正理解的问题，覆盖研究问题、方法机制、证据和局限。

### 18. Glossary
术语中英文、简明定义、在本文中的具体含义。

### 19. Related Papers / Sources
按 `source_ledger` 输出完整相关论文清单及 DOI/URL（如果有）。

## 写作要求
- 默认中文，术语首次出现保留英文原名。
- 以复习、复现、比较和长期学习为导向，不写成“背景很长、方法很短”的摘要。
- 数字、公式、实验结论保留论文位置；外部判断保留 source id。
- 去重：相同内容只出现一次，后续章节用交叉引用而不是重新解释。
- 重要对比宁可少而准确，不机械凑论文数量。
- 用户明确要求保存时写为 `.md`；Obsidian 使用标准 Markdown/Wikilink，不绑定特定 Vault。

## 边界
- 不把外部资料当目标论文自身证据。
- 不自动找 research idea 或代写论文正文；“我的笔记”保持用户主导。
- 不生成 HTML/PPT，除非用户另行要求。
