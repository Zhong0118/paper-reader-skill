# Paper Reader Workflow

`paper-reader` 是唯一公开入口。v0.5 同时覆盖：

1. 单篇论文持续精读；
2. Note 增量同步；
3. 多论文 Collection / Compare。

## Invocation

```text
/paper-reader <mode> <request>
```

也支持自然语言自动路由。

## Modes

| mode | workflow |
|---|---|
| quick | structure |
| internal | structure → teacher → evidence |
| deep | structure → teacher → evidence → light context |
| teach | necessary structure → teacher |
| context | targeted context |
| critique | evidence → targeted context if needed → critic |
| compare | collection inventory → normalized compare → synthesis |
| note compact | persist current results only |
| note learning | standard learning note |
| note full | full-format note from current verified Context |
| full | single-paper six-stage workflow → full note |

## Single-paper state

推荐：

```text
.paper-reader/papers/<paper-id>/
├── context.md
├── note.md
└── figures/
```

Paper Context 用：

```text
context_revision
context_depth
note_depth
note_sync
stage_status
```

### Context revision

实质内容新增/修订：

```text
context_revision += 1
```

### Note sync

```text
auto
on-demand
off
```

auto：

```text
Context changed
→ locate affected managed sections
→ deduplicate
→ merge/revise
→ preserve user regions
→ update synced_context_revision
```

Note sync 本身不启动新的阅读/检索。

## Collection state

```text
.paper-reader/collections/<collection-id>/
├── manifest.md
├── comparison.md
└── synthesis.md
```

### Large folder

```text
inventory
→ metadata/abstract triage
→ choose axes
→ decide per-paper coverage
→ targeted backfill
→ compare
→ synthesize
```

禁止默认 `full × N`。

### Comparison

用户 axes 优先。

没有 axes 时，按问题推导最小充分维度。

所有关键比较单元区分：

```text
reported
derived
not_reported
not_assessed
not_accessible
not_applicable
uncertain
```

### Incremental collection update

新增论文或单篇 Context 更新：

```text
update manifest
→ detect affected rows/cells
→ update comparison
→ patch dependent synthesis
```

不要重做整个 collection。

## note full vs full

```text
/paper-reader note full
```

= 现有 Context → Full Learning Record 格式。

```text
/paper-reader full
```

= 单篇完整六阶段 → Full Learning Record。

## Compare boundary

`compare` 比较用户给定集合。

需要 SOTA / Survey / 补领域缺失论文时，才按用户意图调用 context research。

Compare 不自动变成通用 Research Agent。

## Typical flows

```text
/paper-reader teach 式（4）
→ update teaching
→ context_revision +1
→ existing auto-sync Note updates the equation section

/paper-reader compare 比较这个文件夹的材料类型、巨噬细胞机制和骨再生结果
→ inventory
→ axes
→ targeted backfill
→ comparison.md
→ synthesis.md

新增一篇 PDF
→ manifest add
→ read only needed axes
→ patch one row
→ update dependent synthesis
```
