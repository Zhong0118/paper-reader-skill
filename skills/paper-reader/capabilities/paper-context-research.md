---
name: paper-context-research
description: Use when a paper needs to be placed in its research context, including state of the art, benchmarks, author prior work, predecessors, competing methods, follow-up work, surveys, documented limitations, contradictory findings, or recommended related reading.
---

# Paper Context Research

## 目标
不是“再做一次泛化文献综述”，而是围绕**当前这篇论文**补齐它在真实学术脉络中的位置。只搜索与理解、比较、验证当前论文直接相关的内容。

先读 `references/paper-context.md`。优先使用已经存在的 `paper_internal`、`teaching` 与 `evidence_review` 来生成搜索问题；先检查 `research_queries` 和 `source_ledger`，已经查过且仍然新鲜的问题不要重复搜索。

## 必查方向
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

## 搜索预算
默认 deep/full 模式保留高相关结果，而不是无限扩张：
- 1–2 篇高质量 Survey/Review；
- 2–4 篇关键前置工作；
- 1–3 篇作者直接前作（存在才保留）；
- 2–4 篇同期/竞争工作；
- 2–4 篇代表性后续工作；
- 1–3 篇真正提供局限、复现失败或不同结论的文献（存在才保留）。

如果某类没有可靠结果，写“未找到足够可靠证据”，不要凑数。

## 输出到 Paper Context
外部来源必须与目标论文内部证据分开记录。

更新 `external_context`、`research_queries` 与 `source_ledger`：
- 每个结论绑定 source id；
- SOTA 比较写清 task / dataset / metric / setting / year；
- Related paper 不只写标题，要写“它与当前论文的关系”；
- `reading_path` 按“先读 → 再读 → 深入读”给 5–10 篇最值得继续学习的材料。

## 无 Web/Search 工具时
明确说明当前环境无法完成外部检索，只保留基于目标论文引用表可确认的内部关系；不得凭模型记忆伪造 SOTA、后续论文或作者前作。

## 边界
- 不替代通用 Research Agent，不从零做完整领域调研。
- 不找与当前论文无直接关系的 research idea。
- 不因外部资料更“新”就覆盖目标论文原始事实。
- 不把排行榜名次直接等同于“方法更好”；需要考虑设定、公平性和成本。
