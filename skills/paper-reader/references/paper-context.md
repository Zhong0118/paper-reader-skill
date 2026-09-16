# Paper Context Protocol

所有阶段共享一份 Paper Context，目标是**按论文版本与覆盖范围复用可靠结果，按当前问题增量更新**。推荐路径：`.paper-reader/<paper-id>/context.md`。`paper-id` 优先使用 `first-author-year-short-title`；未知时使用 PDF 文件名。目录名只用于可读性；匹配身份优先 DOI/arXiv ID，缺失时核对标题、作者与年份。禁止仅凭文件名判定同一论文，禁止把 Context 复用到另一篇论文。

## Context 结构

首次只填身份、材料覆盖与当前阶段所需区块；下列章节为可用字段，不要求生成空白全表。

```markdown
---
paper_id:
title:
authors:
year:
venue:
doi:
arxiv_id:
source:
paper_type:
source_version: # 如 arxiv-v2；未知时明确 unknown
source_hash: # 本地文件可用时记录，用于检测材料变化
source_quality: good|degraded|poor
retrieved_at:
stage_status: {} # 按下文记录范围；completed_stages 仅用于兼容旧记录
context_depth: none # none | light | targeted | full
note_depth: none # none | compact | learning | full
---

## source_map
- 实际读取的 Section/Figure/Table/Page、来源版本、读取方式及局部质量；区分摘要、全文和补充材料

## figures
- 按 references/figure-handling.md 记录实际查看或保存的关键图表

## paper_internal
### research_question
### motivation
### claims
### contributions
### method_backbone
### experiments
### results
### author_limitations

## teaching
### concepts
### equations
### mechanisms
### confusing_points

## evidence_review
### claim_evidence
### strongest_evidence
### evidence_gaps
### overclaims

## external_context
### field_position
### sota
### benchmarks
### author_previous_work
### predecessors
### competing_work
### follow_up
### surveys
### external_limitations
### contradictory_findings
### code_datasets_projects
### reading_path

## method_critique
### strengths
### major_concerns
### minor_concerns
### uncertainty
### externally_supported_concerns

## research_queries
- query:
  purpose:
  date:
  scope: # 时间范围、任务和设定
  outcome: # 已回答的问题、来源 id、未解决的问题

## source_ledger
- id: X1
  type: paper|survey|benchmark|project|documentation|other
  title:
  authors:
  year:
  venue:
  doi:
  url:
  retrieved_at:
  supports:
  notes:

## open_questions

## note_metadata
```

## 来源标签

- `[论文原文]`：当前目标论文明确表达或直接展示的事实。
- `[模型归纳]`：从目标论文多个位置综合出来的解释。
- `[模型解释]`：用于教学的解释、类比或机制说明。
- `[外部文献]`：来自其他论文、Survey、benchmark 页面或权威项目资料。
- `[后续研究]`：时间上晚于目标论文，用于说明后续验证、改进、质疑或 SOTA 演进。
- `[不确定]`：证据不足或来源质量不足。

## Research / Note Depth

`context_depth` 描述实际已执行的外部研究类型：none（尚无外部研究）、light（最小学术脉络）、targeted（明确问题的定向研究）、full（较全面的论文中心型研究）。deep 默认请求 light；明确的 SOTA/创新性等问题请求 targeted；完整学习档案请求 full。

这些值不是完成度或严格等级。targeted 可以在单一问题上比 full 更深入；新一轮 targeted 后可记录 targeted，但保留已有 full 的内容与历史覆盖。实际可复用范围始终由 stage_status.scope、research_queries 和 source_ledger 判断，时效性结论检查 retrieved_at。

`note_depth` 描述最近实际生成的笔记类型：none（尚无笔记）、compact（保存现有成果）、learning（标准长期知识库笔记）、full（完整学习档案）。在 note_metadata 记录各笔记路径、深度、版本与生成日期；生成 compact 不删除已有 learning/full 笔记。升级笔记深度复用已有成果。

路由表里的 depth 是本次目标，不可在开始任务时直接覆盖实际字段。研究实际执行后更新 context_depth；部分完成或受阻由 stage_status.status/remaining 记录，不能仅凭 depth 宣称任务完成。没有新研究时保留已有 context_depth；笔记实际生成后才更新 note_depth。旧 Context 缺字段时先从已有内容恢复，无法确认时暂不填该深度字段，在 stage_status/remaining 记录待核验，不新增枚举值，也不据此重跑全部阶段。

用户禁止外部资料时，本次目标为 none，不查询或引用外部缓存来补答案；已有外部记录保留但不混入本次结果。仅禁止联网时可使用已有本地或缓存来源并说明日期，不刷新在线信息。Web 不可用时记录受阻，不把计划的 light/full 当作已完成研究。

## 阶段状态与版本更新

每个已执行阶段记录实际覆盖，而非“曾运行过”：

```yaml
stage_status:
  teacher:
    status: partial # partial / complete / blocked
    scope: [equation-4]
    source_version: arxiv-v2
    remaining: [method-overview, training-objective]
    updated_at: 2026-09-17
```

- `complete` 只表示 scope 内完成，不代表全文完成；新问题超出 scope 时补充。未运行阶段可省略；缺全文、图像或工具而无法完成时记录 blocked 和具体缺口。
- 旧 Context 只有 `completed_stages` 时，从实际内容与 source_map 恢复范围；无法确认的部分视为待核验，不重跑已有可靠内容。
- 版本/文件变化后先定位差异：标记受影响的 Claim、图表、解释、支持度、外部比较和笔记为待核验，验证后更新；未能定位差异时不得把旧结论当作新版已核验事实。保留旧来源版本和用户笔记，不把不同版本的图号、结果混用。
- 外部来源的时效性独立于论文版本：已核实的稳定定义可复用，“当前 SOTA”等结论按用户请求刷新并标检索日期。

## 合并规则

- 各 capability 主要更新自己的区块；共享 source_map、figures 和状态可按实际读取补充。critic 若发现影响支持度的问题，可修订关联 evidence_review 条目，记录旧判断、新判断、原因与证据位置，并将依赖解释/笔记标为待更新。保留无关内容及用户注释。
- `paper_internal` 与 `external_context` 永远分开。后续论文的观点不能被写成“原论文承认”。
- 已有可靠结果优先于重复读取；只有缺失、矛盾、低质量或需要精确证据定位时才回看原文。
- 外部检索优先记录 DOI / arXiv / 官方项目页 / 出版社页 / 学术数据库入口；博客和二手解读只能作辅助线索。
- 关键数字、公式、作者贡献与证据判断必须保留可用的 Section/Figure/Table/Page；无法定位时标记缺口。外部关键判断绑定 source id（如 `X3`）。Claim 可使用 C1 等稳定 id，供图表与修订关联。
- `research_queries` 记录“搜过什么以及为什么”，避免不同阶段重复搜索同一问题。
- `source_ledger` 是外部事实的唯一来源账本。最终 Note 中的重要外部判断必须能回指这里。
- 用户未要求持久化时，可以只在当前会话维护等价 Context；跨轮次/跨 Agent 时优先落盘。
