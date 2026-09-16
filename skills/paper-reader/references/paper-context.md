# Paper Context Protocol

所有阶段共享一份 Paper Context，目标是**论文只建立一次内部理解，外部研究只做一次定向检索，后续阶段直接复用**。推荐路径：`.paper-reader/<paper-id>/context.md`。`paper-id` 优先使用 `first-author-year-short-title`；未知时使用 PDF 文件名。禁止把 Context 复用到另一篇论文。

## 最小结构

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
source_quality: good|degraded|poor
retrieved_at:
completed_stages: []
---

## source_map
- internal sections / figures / tables / pages actually read

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

## 合并规则

- 每个 capability 只更新自己的区块；保留其他区块原样。
- `paper_internal` 与 `external_context` 永远分开。后续论文的观点不能被写成“原论文承认”。
- 已有可靠结果优先于重复读取；只有缺失、矛盾、低质量或需要精确证据定位时才回看原文。
- 外部检索优先记录 DOI / arXiv / 官方项目页 / 出版社页 / 学术数据库入口；博客和二手解读只能作辅助线索。
- 所有论文事实尽量保留 Section/Figure/Table/Page；外部事实尽量保留 source id（如 `X3`）。
- `research_queries` 记录“搜过什么以及为什么”，避免不同阶段重复搜索同一问题。
- `source_ledger` 是外部事实的唯一来源账本。最终 Note 中的重要外部判断必须能回指这里。
- 用户未要求持久化时，可以只在当前会话维护等价 Context；跨轮次/跨 Agent 时优先落盘。
