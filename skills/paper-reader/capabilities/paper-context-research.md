---
name: paper-context-research
description: Use when a paper needs to be placed in its research context, including state of the art, benchmarks, author prior work, predecessors, competing methods, follow-up work, surveys, documented limitations, contradictory findings, or recommended related reading.
---

# Paper Context Research

## 目标
不是“再做一次泛化文献综述”，而是围绕**当前这篇论文**补齐它在真实学术脉络中的位置。只搜索与理解、比较、验证当前论文直接相关的内容。

先读 `references/paper-context.md`。优先使用已经存在的 `paper_internal`、`teaching` 与 `evidence_review` 来生成搜索问题；先检查 `research_queries` 和 `source_ledger`，已经查过且仍然新鲜的问题不要重复搜索。

## Research Depth

按入口指定的研究目标执行；先复用已核验且仍适用的材料，再补缺口。深度不以文献数量衡量。

### none

不启动论文外检索。quick、deep-internal 或用户明确禁止外部资料时使用；此时不加载本能力也可直接结束。目标论文引用表只能说明作者引用了什么，不能冒充已独立核验的外部研究。

### light

默认 deep 的轻量学术脉络，也用于有价值且允许外部研究的 Learning Note。至少尝试回答：最关键直接前置思想是什么、当前工作相对最近相关工作改变了什么、是否有帮助理解发展的代表性 follow-up、是否有适合作领域地图的 Survey/Review。

按论文类型选择性补 benchmark 演化及重要缺陷、直接作者前作或重要失败/替代验证。已有可靠回答可复用；没有适用材料或可靠结果时记录缺口，不凑论文。足以帮助理解当前论文时停止，不扩展为全面 SOTA 扫描。

### targeted

围绕明确问题定向研究，例如首创性、发表时或当前 SOTA、作者前作、复现失败、benchmark 缺陷或特定局限。可以比 full 在单问题上更深入；已有 full 不能作为跳过新问题的理由。

### full

服务完整学习档案，按论文类型与实际价值选择前置工作、作者前作、竞争路线、发表时 SOTA、当前代表性进展、benchmark、后续工作、外部局限、相反证据、Survey、官方代码/数据/项目和阅读路径。强调研究地图的广度，不是系统综述，不要求每类有文献。

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
- 教学背景：只补所需前置概念；compact 归档不触发新搜索，learning 按 light 补有价值的脉络。
- full/完整学习档案可以扩大覆盖，仍以相关性与证据缺口为准，不要求所有类别都有材料。

每个问题先做一轮定向检索，优先阅读最相关的一手来源；只有尚未解决的具体缺口才继续。证据足以回答问题、可用渠道已无法推进，或达到用户时间/范围限制时停止，记录已回答与未解决项。没有固定论文配额；“未找到反证”不等于“反证不存在”。

搜索记录包含问题、日期、时间范围/任务设定、来源与结果。已查且仍适用的结果复用；当前排名、后续工作等时效性问题按需刷新，不受“只搜一次”限制。

## 输出到 Paper Context
外部来源必须与目标论文内部证据分开记录。

更新 `external_context`、`research_queries` 与 `source_ledger`，按协议记录实际 context_depth 和阶段覆盖/缺口：
- 每个结论绑定 source id；
- SOTA 比较写清 task / dataset / metric / setting / year；
- Related paper 不只写标题，要写“它与当前论文的关系”；
- 需要进一步阅读时，`reading_path` 按“先读 → 再读 → 深入读”选择有明确用途的材料，不凑数量。

## 无 Web/Search 工具时
明确说明当前环境无法新增在线检索。用户未禁止外部资料时，可复用已核验且适用的本地/缓存外部来源，注明日期；不能把过时缓存称为当前状态。没有可用外部材料时，仅保留目标论文引用表可确认的内部关系。将尚需在线验证的问题记录为 blocked/remaining；不得凭模型记忆伪造 SOTA、后续论文或作者前作。

## 边界
- 不替代通用 Research Agent，不从零做完整领域调研。
- 不找与当前论文无直接关系的 research idea。
- 不因外部资料更“新”就覆盖目标论文原始事实。
- 不把排行榜名次直接等同于“方法更好”；需要考虑设定、公平性和成本。
