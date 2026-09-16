# Paper Reader Workflow

日常只调用 `paper-reader`。内部六个 capability 共享一份带版本和覆盖范围的 Paper Context。

## Invocation

推荐显式语法：

```text
/paper-reader <mode> <request>
```

如果宿主不提供原生 slash Skill invocation，则使用宿主的 Skill 选择方式或自然语言；本仓库不绑定宿主私有 command 格式。

不指定 mode：

```text
/paper-reader 帮我深入精读这篇论文
```

→ 根据语义自动路由。

## User-facing modes

| 用户 mode | 内部模式/工作流 | 本次研究目标 | 笔记目标 |
|---|---|---|---|
| quick | structure | none | none |
| internal | deep-internal: structure → teacher → evidence | none | none |
| deep | structure → teacher → evidence → light context | light | none |
| teach | necessary structure → teacher；按知识缺口补 context | none / targeted | none |
| context | targeted context | targeted | none |
| critique | necessary structure → evidence → targeted context when required → critic | targeted 按需 | none |
| note compact | existing context → compact note | 不新增 | compact |
| note / note learning | existing analysis → useful light context → learning note | light（有价值且允许时） | learning |
| note full | existing verified context → full-format note | 不强制新增 | full |
| full | structure → teacher → evidence → full context → critic → full note | full | full |

## Important distinction

```text
/paper-reader note full
```

只把**当前已经核验的 Context**整理成 Full Learning Record 格式。

```text
/paper-reader full
```

会先执行完整六阶段，再生成 Full Learning Record。

## Explicit mode precedence

显式 mode 优先于自动语义判断，但以下用户限制更高：

1. 不使用外部资料；
2. 不联网；
3. 只保存已有内容；
4. 指定论文版本/范围；
5. 指定时间范围。

例：

```text
/paper-reader deep 不要使用外部资料
```

→ internal behavior。

```text
/paper-reader note learning 只保存已有内容
```

→ compact behavior。

## Unknown mode

若 `/paper-reader` 后第一个词不是已知 mode，不作为错误处理；将整段后续文本按自然语言自动路由。

## Context Depth

```text
none
light
targeted
full
```

- none：不做外部研究；
- light：理解论文所需的最小学术脉络；
- targeted：明确问题深挖；
- full：较全面的论文中心型研究地图。

targeted 与 full 不构成严格等级。已有 full 不阻止新问题研究，也不能代替当前 SOTA 的时效性刷新。

## Note Depth

```text
compact
learning
full
```

- compact：只保存已有成果；
- learning：标准知识库笔记；
- full：完整格式档案。

note depth 和 reading depth 是两回事。

## Reuse and revision

1. 核对论文身份、版本和材料质量。
2. 用 `stage_status.scope/status/remaining` 判断是否覆盖当前问题。
3. `paper_internal` 与 `external_context` 分开。
4. 稳定外部结果复用；当前 SOTA 等时效性问题刷新。
5. 新版本只重验受影响内容。
6. 图表按 `references/figure-handling.md` 实际查看和选择性归档。
7. 最终输出去重。

## Typical continuation

```text
/paper-reader teach 式（4）
→ teaching scope: equation-4

/paper-reader teach 继续讲完整方法
→ 复用式（4），补剩余方法

/paper-reader context 最新 benchmark 结果如何
→ targeted refresh

/paper-reader note compact
→ 保存现有成果

/paper-reader note learning
→ 标准长期笔记

/paper-reader full
→ 完整六阶段
```
