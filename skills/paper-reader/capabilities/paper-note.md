---
name: paper-note
description: Use when the user wants to turn an already-read paper and its related research context into a durable Markdown or Obsidian-style learning record for long-term study, comparison, review, and reuse.
---

# Paper Note

## 目标
把当前论文、教学解释、Claim–Evidence、方法学批判和相关论文脉络整理成一份以后真的会回来看的**论文学习档案 / 知识库记录**。它不是摘要换皮，也不是第六次重新分析全文。

## Paper Context 复用规则
先读 `references/paper-context.md`。优先使用已有 Context，保存已读范围、可靠结论和未完成项。按 compact / learning / full 选择下面的笔记契约。compact 不补研究；learning 复用内部分析并在有价值且允许时补 light context；full 由入口调度六阶段。Learning Note 不自动等于完整精读：内部分析缺失时标明未读/未评估；用户同时要求读懂或补齐方法时才调度对应缺失阶段。材料或工具不足时保留缺口，不能用外部结果替代未读原文。

## Compact Note

“保存一下 / 把刚才内容记下来 / 简单存一下”默认 compact。只保存已有结果，不启动新检索、缺失阶段、critique 或 glossary。

1. 论文卡片：身份、版本、来源、阅读日期与已读范围。
2. 快速回忆与研究问题。
3. 方法、已讲解的难点与核心公式；有核验后的关键图则贴在解释旁。
4. 核心证据 / Claim–Evidence：只写已核验内容。
5. 局限：区分作者声明、分析发现和外部来源。
6. 我的笔记与疑问：用户观点与模型待解决问题分开。
7. 来源与未完成项。

缺少某部分时标注未读/未评估，不能为填充章节编造内容。根据已有材料合并或省略空章节。

## Standard Learning Note

“整理成论文笔记 / 放进知识库 / 做成 Obsidian 笔记 / 以后复习用”默认 learning。显式要求“只保存已有内容 / 不新增分析”时 compact 优先于 Obsidian 等格式词。

这是标准长期学习格式。复用已有 light 或更广但相关的研究覆盖；缺失且有价值时由 paper-context-research 补 light。禁止外部资料、工具受限或暂无可靠材料时，保留内部笔记与外部缺口，不强行满足栏目。

按实际材料组织以下部分；理论/综述论文改用证明或文献综合证据，不硬套实验项目。核心内部内容缺失时标题或卡片标明“部分阅读笔记”。

### 0. Paper Card
身份、作者、Venue、年份、DOI/arXiv、source version、已知 code/dataset、阅读日期、实际阅读范围。

### 1. Five-Minute Recall
一句话讲清论文、研究问题、核心方法思想、真正重要的贡献、关键结果及为什么值得记住。

### 2. Research Question & Motivation
作者要解决什么、为什么重要、已有方法为何不够、核心假设。

### 3. Method
输入 → 核心处理 → 中间状态 → 输出；整理模块及关系、最重要公式、前置知识、直觉解释与易混点。

### 4. Experiments & Evidence
按类型整理 Dataset/Baseline/Metric/Control/Ablation 或证明条件，核心 Figure/Table 与 Claim–Evidence。

### 5. What It Proves / Does Not Prove
有证据支持的结论、未证明部分与过度外推风险；未做 evidence review 时明确未评估。

### 6. Strengths & Limitations
区分作者自述局限、内部分析发现、外部研究验证的局限；不能为完整性虚构 critique。

### 7. Research Context
呈现有用的 light context：关键前置工作 → 当前论文改变了什么 → 代表性后续工作，以及领域 Survey。按价值加 benchmark、作者前作、竞争路线或当前发展。明确外部资料不可用或被排除的部分。

### 8. Related Paper Comparison
只比较已核验且真正重要的相关论文：

| Paper | Year | Core idea | 与本文关系 | 主要差异 | 为什么值得读 |
|---|---:|---|---|---|---|

### 9. Learning Notes
模型总结的易错知识点、用户自己的笔记、用户疑问和仍未解决问题分开记录；不把模型观点冒充用户观点。

### 10. Further Reading
先读 → 再读 → 深入读，按实际价值选择，说明每篇为什么值得读，不凑数量。

### 11. Sources
目标论文、相关论文、Survey、benchmark/project/dataset 页面；外部关键判断回指 source_ledger，保留未完成项。

## Full Learning Record


用户明确要求完整档案时使用以下菜单；按论文类型与实际材料选择章节，不要求填满。技术发展脉络、作者研究路线、同期竞争、当前 SOTA、Benchmark、后续工作、推荐进一步阅读、Glossary 等只在相关时展开。

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
有已核验的相关论文时做对比表：

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

## 图表归档

读取 `references/figure-handling.md`。默认选择已用于解释或支持核心结论的架构图、流程图、结果图，避免批量导出全篇图片。原图/裁剪与模型重绘明确区分。已有图像资产可复用；请求存图但尚未实际查看时，先核验所选图像，不触发额外文献研究。

保存笔记后验证图片文件存在、Markdown 链接能从笔记目录解析，图注/图号/来源版本正确。若没有可用提取或查看工具，保存定位与缺口，不声称已经保存或核验图片。

## 写作要求
- 生成后更新 note_depth、note_metadata 的笔记路径/版本/日期及 stage_status；缺口保留，深度标签不代表所有章节已完成。
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
