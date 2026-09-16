---
name: paper-context-research
description: Use when a paper needs to be placed in its research context, including state of the art, benchmarks, author prior work, predecessors, competing methods, follow-up work, surveys, documented limitations, contradictory findings, or recommended related reading.
---

# Paper Context Research

## 目标
不是“再做一次泛化文献综述”，而是围绕**当前这篇论文**补齐它在真实学术脉络中的位置。只搜索与理解、比较、验证当前论文直接相关的内容。

先读 `references/paper-context.md`。优先使用已经存在的 `paper_internal`、`teaching` 与 `evidence_review` 来生成搜索问题；先检查 `research_queries` 和 `source_ledger`，已经查过且仍然新鲜的问题不要重复搜索。

## 可选检索方向
根据论文类型和用户目的选择必要项，不机械凑数：

1. **State of the art (SOTA)**：目标任务在论文发表当时和现在分别处于什么水平；注意区分不同数据集、指标、计算预算和设定，不能只抄排行榜。
2. **Benchmark**：论文使用的 benchmark 是否主流、评价什么、有哪些已知缺陷或后续修订。
3. **Authors' previous work / 作者前作**：作者或课题组是否有直接前置工作，这篇论文是延续、扩展还是转向。
4. **Predecessors / 前置工作**：当前方法真正建立在哪些关键思想、方法或数据资源之上。
5. **Competing work / 同期竞争**：同一时期解决同一问题的替代路线，比较核心假设与方法差异。
6. **Follow-up work / 后续工作**：谁继续使用、改进、替代或系统评估了这篇工作。
7. **Method limitations / 外部局限**：其他研究是否实证指出当前方法的失效场景、偏差、复现问题或成本问题。
8. **Contradictory findings / 相反证据**：是否存在不能复现、结论相反或对机制有不同解释的研究。
9. **Survey / Review**：寻找高质量综述帮助理解整个方向和术语体系。
10. **Code / Dataset / Project**：官方代码、数据集、项目页、benchmark 文档是否存在，作为方法与复现背景。

## 搜索策略

### A. 先用论文自身生成检索键
- 精确标题；
- 第一作者 + 核心方法名；
- 方法名 + task；
- task + benchmark + survey/review；
- 论文标题/方法名 + limitation / reproducibility / replication；
- 论文标题/方法名 + follow-up / improved / revisited；
- 作者名 + 论文发表前 3–5 年的直接相关工作。

### B. 来源优先级
优先：出版社/会议页、Crossref/DOI、arXiv、PubMed/PMC、Semantic Scholar/OpenAlex、官方 benchmark / dataset / project 页面、权威 Survey。

普通网页、博客、社交媒体只能作为发现线索；关键判断必须回到可核验学术来源。

### C. 时间边界
- 对“当时的 SOTA”以目标论文发表年份附近的资料为准。
- 对“当前 SOTA/后续进展”必须记录检索日期 `retrieved_at`，并明确这是**截至检索日**的状态。
- 后续论文不能用于证明作者当年的主张，只能用于说明后来如何评价该工作。

## 问题、预算与停止条件

先列当前阅读真正未解决的问题，再选择方向，不为补齐栏目而检索。
- 方法来源：查直接前置工作；创新性：查最相关同期工作。
- 当前是否值得使用：查后续评测、替代路线、可比设定及成本。
- 教学背景：只补所需前置概念；归档已有内容不触发新搜索。
- full/完整学习档案可以扩大覆盖，仍以相关性与证据缺口为准，不要求所有类别都有材料。

每个问题先做一轮定向检索，优先阅读最相关的一手来源；只有尚未解决的具体缺口才继续。证据足以回答问题、可用渠道已无法推进，或达到用户时间/范围限制时停止，记录已回答与未解决项。没有固定论文配额；“未找到反证”不等于“反证不存在”。

搜索记录包含问题、日期、时间范围/任务设定、来源与结果。已查且仍适用的结果复用；当前排名、后续工作等时效性问题按需刷新，不受“只搜一次”限制。

## 输出到 Paper Context
外部来源必须与目标论文内部证据分开记录。

更新 `external_context`、`research_queries` 与 `source_ledger`：
- 每个结论绑定 source id；
- SOTA 比较写清 task / dataset / metric / setting / year；
- Related paper 不只写标题，要写“它与当前论文的关系”；
- 需要进一步阅读时，`reading_path` 按“先读 → 再读 → 深入读”选择有明确用途的材料，不凑数量。

## 无 Web/Search 工具时
明确说明当前环境无法完成外部检索，只保留基于目标论文引用表可确认的内部关系；不得凭模型记忆伪造 SOTA、后续论文或作者前作。

## 边界
- 不替代通用 Research Agent，不从零做完整领域调研。
- 不找与当前论文无直接关系的 research idea。
- 不因外部资料更“新”就覆盖目标论文原始事实。
- 不把排行榜名次直接等同于“方法更好”；需要考虑设定、公平性和成本。
