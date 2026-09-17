# Paper Context Protocol

所有单篇论文阶段共享一份 Paper Context，目标是：

- 按论文身份、版本与覆盖范围复用可靠结果；
- 按当前问题增量更新；
- 为持续 Note 同步提供稳定的事实源；
- 在多论文比较中作为单篇论文的独立证据节点。

推荐路径：

```text
.paper-reader/papers/<paper-id>/context.md
```

兼容旧版：

```text
.paper-reader/<paper-id>/context.md
```

`paper-id` 优先使用 `first-author-year-short-title`。匹配论文身份优先 DOI/arXiv ID；缺失时核对标题、作者、年份和来源版本。禁止仅凭文件名判定同一论文。

## Context 结构

首次只填当前需要的区块，不要求生成空白全表。

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
source_version:
source_hash:
source_quality: good|degraded|poor
retrieved_at:

# 单调递增。只有出现实质性 Context 新增/修订时 +1。
context_revision: 0

# 外部研究实际覆盖类型。
context_depth: none # none | light | targeted | full

# 最近实际生成/同步的笔记深度。
note_depth: none # none | compact | learning | full

# 已存在 Note 的同步策略。
note_sync: auto # auto | on-demand | off

stage_status: {}
---

## source_map
- 实际读取的 Section/Figure/Table/Page、版本、读取方式和局部质量

## figures
- 按 references/figure-handling.md 记录关键图表

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
  scope:
  outcome:

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
- path:
  depth:
  generated_at:
  last_synced_at:
  source_version:
  synced_context_revision:
  managed_sections: []
  status: current|stale|blocked
  sync_log: []
```

## 来源标签

- `[论文原文]`：目标论文明确表达或直接展示。
- `[模型归纳]`：从论文多个位置综合。
- `[模型解释]`：教学解释、类比或机制说明。
- `[外部文献]`：其他论文、Survey、benchmark 或权威项目资料。
- `[后续研究]`：时间上晚于目标论文。
- `[不确定]`：证据不足或来源质量不足。

## 稳定 ID

为了让 Note 增量同步和多论文比较更可靠，重要知识节点尽量使用稳定 ID：

- Claim：`C1`, `C2`, ...
- Teaching concept：`T1`, `T2`, ...
- Equation：`E1`, `E2`, ...
- Method node：`M1`, `M2`, ...
- Figure：沿用论文 Figure/Table 标识或稳定本地 `fig-*`
- External source：`X1`, `X2`, ...

稳定 ID 的目标不是制造复杂数据库，而是避免同一个知识点在多轮追问中被当成多个不同条目。

已有旧 Context 没有 ID 时按需补，不要求一次性重构全部历史内容。

## context_revision

`context_revision` 是单篇 Context 的**实质内容版本号**。

以下情况递增：

- 新增重要概念、公式解释或机制；
- 新增/修订 Claim–Evidence；
- 新增关键 Figure 解读；
- 新增方法学判断；
- 新增相关论文或外部证据；
- 纠正旧结论；
- 用户明确写入需要长期保留的个人笔记/疑问；
- 论文版本变化导致依赖内容重新核验。

以下情况通常不递增：

- 纯格式调整；
- 只改时间戳；
- 同义重述但没有新增知识；
- “好的 / 再简单说一遍”且最终没有形成新的可复用解释。

revision 只表示 Context 有新实质内容，不表示“全文完成”。

## Note Sync

### 模式

`note_sync`：

- `auto`：默认。已有 Note 且出现与 Note 有关的实质 Context 更新时，自动做局部同步。
- `on-demand`：只有用户明确 `note/save/archive` 时同步。
- `off`：不修改已有 Note。

### 自动同步不等于自动研究

Note Sync 只把**已经核验并写入 Context 的内容**合并进 Note。

禁止因为：

```text
note_sync=auto
```

就自动启动：

- 全文重读；
- 新外部检索；
- 新 critique；
- 新 comparison。

分析/研究由当前用户请求决定，Note Sync 只是持久化层。

### managed region

新生成 Note 推荐给模型管理区域加标记：

```markdown
<!-- paper-reader:managed:start key="teaching.T1" -->
...模型维护的内容...
<!-- paper-reader:managed:end -->
```

用户区域推荐：

```markdown
<!-- paper-reader:user:start -->
...用户自己的笔记...
<!-- paper-reader:user:end -->
```

规则：

1. auto sync 优先只改对应 `managed` 区域；
2. `user` 区域永不自动改写；
3. 未知来源的手工文本默认保留；
4. 旧 Note 没有 markers 时按标题/稳定 ID 做 section-aware merge，不能整份覆盖；
5. 第一次成功同步旧 Note 后可为可管理区域补 markers；
6. 用户明确要求“完全重建/重新生成”时才允许整份重写，但仍必须保留或迁移用户内容。

### Merge，而不是 Append

同一稳定知识节点后续变丰富时：

```text
existing node
   ↓
new context
   ↓
deduplicate
   ↓
merge / revise
```

不要产生：

```text
补充：
再次补充：
进一步补充：
```

纠错时更新 managed 内容，并在 `note_metadata.sync_log` 记录：

- revision；
- 修改的 section/key；
- 原因；
- 日期。

不要求把每次修订历史都堆在用户可见 Note 正文。

### Stale Note

若：

```text
note_metadata.synced_context_revision < context_revision
```

则 Note 至少可能 stale。

`auto` 且可写时应同步；不能写时标 `status: stale|blocked`，不得声称已经同步。

## Research / Note Depth

`context_depth`：

- none
- light
- targeted
- full

它描述实际执行的外部研究类型，不是严格全序。targeted 可在一个问题上比 full 更深入。

`note_depth`：

- none
- compact
- learning
- full

记录最近实际生成/同步的笔记类型。不同深度的历史 Note 可以同时存在；生成 compact 不删除 learning/full。

路由里的 depth 是本次目标，不能在任务开始时直接写成“已完成”。

## 阶段状态与版本更新

```yaml
stage_status:
  teacher:
    status: partial # partial | complete | blocked
    scope: [E1]
    source_version: arxiv-v2
    remaining: [method-overview]
    updated_at: 2026-09-17
```

- `complete` 只表示 scope 内完成；
- 新问题超出 scope 就增量补；
- 旧 `completed_stages` 只兼容，不代表全文覆盖；
- 论文版本变化只重验受影响内容；
- 保留用户笔记和无关可靠结果；
- “当前 SOTA”等时效性外部事实独立检查 retrieved_at。

## 合并规则

- 各 capability 主要更新自己的区块；
- `paper_internal` 与 `external_context` 永远分开；
- 关键数字、公式、Claim 和证据保留 Section/Figure/Table/Page；
- `research_queries` 防止重复搜索；
- `source_ledger` 是外部事实来源账本；
- critic 改变 Claim 支持度时记录原因并让依赖 Note 进入待同步状态；
- 多论文比较只引用本 Context，不把别篇论文内容直接写进这里，除非是明确的 external/cross-paper reference；
- Collection 级综合写入 collection 文件，不侵入单篇 Context 的主体事实。
