# Collection Protocol

Collection 用于**多篇已给定论文、一个论文文件夹、或明确论文集合**的横向比较与综合。

它不是通用 Research Agent，也不是把几十篇论文合并成一个巨大 Paper Context。

## 核心原则

```text
one paper
→ one Paper Context
→ optional one or more Notes

many papers
→ many independent Paper Contexts
→ one Collection manifest
→ comparison
→ synthesis
```

每篇论文的事实、证据、版本、图表和 Note 仍然独立。

## 推荐目录

```text
.paper-reader/
├── papers/
│   ├── <paper-id-a>/
│   │   ├── context.md
│   │   ├── note.md
│   │   └── figures/
│   └── <paper-id-b>/
│       ├── context.md
│       ├── note.md
│       └── figures/
└── collections/
    └── <collection-id>/
        ├── manifest.md
        ├── comparison.md
        └── synthesis.md
```

兼容已有旧 Paper Context 路径，不强制立即迁移。

## Collection Manifest

`manifest.md` 至少记录：

```markdown
---
collection_id:
title:
root:
created_at:
updated_at:
question:
comparison_axes: []
---

| paper_id | file/source | title | year | type | coverage | note | relevance | remarks |
|---|---|---|---:|---|---|---|---|---|
```

`coverage` 推荐：

- `discovered`：只知道文件存在；
- `metadata`：标题/作者/年份/摘要等元信息；
- `structure`：已建立论文骨架；
- `deep`：已做内部深读及必要 context；
- `full`：单篇 full workflow 已有；
- `partial:<scope>`：只针对比较维度补读了部分内容。

不要因为论文进入 Collection 就把 coverage 标成 deep/full。

## 文件夹中论文很多时

不要默认：

```text
full × N
```

推荐三阶段：

### 1. Inventory

先扫描可访问文件，建立 manifest：

- 文件名；
- 论文身份；
- 年份；
- 摘要/关键词（可可靠读取时）；
- 论文类型；
- 是否已有 Paper Context；
- 初步相关性。

这一阶段不要求完整读论文。

### 2. Triage

根据用户问题/比较 axes 判断：

- 哪些论文与问题直接相关；
- 哪些只需要 metadata；
- 哪些需要 structure；
- 哪些需要针对某个字段定向补读；
- 哪些值得 deep/full。

如果用户明确“所有论文都要比较”，仍然可以全部进入矩阵，但必须透明标记不同 coverage。

### 3. Compare

只读取完成比较所必需的缺口。

例如比较：

```text
材料类型
材料特性
巨噬细胞感知机制
骨再生结果
```

某篇只缺“巨噬细胞感知机制”，优先回看该论文相应 Methods/Results/Figure，而不是重读全文。

## Comparison Axes

用户给出的维度优先。

例如：

```text
从材料类型、材料特性、如何影响巨噬细胞、对骨再生的影响四个方面比较
```

就直接成为 axes。

用户没给时，按研究问题推导**最小充分维度**，避免机械生成几十列。

常见 axes：

- research question
- material / intervention / dataset
- key mechanism
- method
- population / setting
- benchmark
- outcome
- evidence
- limitation
- novelty
- cost / compute
- reproducibility

## Comparison Cell 状态

不要把“没看到”写成“没有”。

比较单元应区分：

- `reported`：论文明确报告；
- `derived`：从多个已读位置可靠归纳；
- `not_reported`：已检查相应范围，论文未报告；
- `not_assessed`：还没读到足够范围；
- `not_accessible`：材料/图表不可访问；
- `not_applicable`：维度对该论文不适用；
- `uncertain`：证据冲突或质量不足。

矩阵正文可以简化显示，但底层判断必须遵守这些语义。

## Cross-paper Provenance

关键比较结论绑定：

```text
<paper-id>:C1
<paper-id>:Section 3.2
<paper-id>:Figure 4
<paper-id>:X2
```

不要只写：

> Paper A 更强

必须说明：

- 强在哪个维度；
- 基于什么设定；
- 哪些证据支持；
- 是否公平可比。

## Outputs

### comparison.md

主要是**规范化横向矩阵**。

推荐：

```markdown
# Comparison

## Question
...

## Axes
...

## Coverage
...

## Matrix
| Paper | Axis A | Axis B | Axis C |

## Key contrasts
...
```

### synthesis.md

主要是**跨论文综合**：

- 共同模式；
- 关键差异；
- 证据一致处；
- 矛盾结果；
- 可能原因；
- 研究演化；
- 哪些问题仍无法从当前集合回答。

`synthesis.md` 不能伪装成系统综述；它只代表当前 collection 和当前覆盖范围。

## 与单篇 Note 的边界

Collection 比较结果默认**不直接写入任一单篇 Note 主体**。

单篇 Note 可以增加轻量链接：

```markdown
## Cross-paper Links

- Collection: [[../../collections/<collection-id>/comparison]]
- Related synthesis: [[../../collections/<collection-id>/synthesis]]
```

只有当跨论文结论直接改变对该论文的理解/局限判断时，才把相应内容以明确 `[跨论文比较]` 形式增量写回该论文 Context/Note，并保留 collection 来源。

## Collection 更新

新增论文或某篇 Paper Context 发生实质变化时：

1. 更新 manifest coverage/revision；
2. 判断哪些 comparison cells 受影响；
3. 只更新受影响的行/列/结论；
4. synthesis 只重算依赖受影响证据的段落；
5. 保留用户手写 comparison notes。

不要每增加一篇论文就从头重做整个集合。
