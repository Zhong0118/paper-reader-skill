---
name: paper-reader
description: Use when the user wants to read, understand, explain, critique, contextualize, compare, study, or archive academic papers, including methods, equations, evidence, related work, SOTA, benchmarks, limitations, cross-paper comparisons, or durable research notes.
---

# Paper Reader

## 定位

这是论文学习的**唯一公开入口（唯一入口）**。用户不需要记内部 capability 名称。根据问题自动选择阶段，并通过 Paper Context / Collection Context 串联；**不要重复已经可靠完成的分析、检索或笔记内容**。

先读 `references/paper-context.md`。涉及多篇论文、文件夹或横向比较时，再读 `references/collection-protocol.md`。涉及图表时按需读 `references/figure-handling.md`。

内部 capability：

- `capabilities/paper-structure.md`
- `capabilities/paper-teacher.md`
- `capabilities/paper-evidence-review.md`
- `capabilities/paper-context-research.md`
- `capabilities/paper-method-critic.md`
- `capabilities/paper-compare.md`
- `capabilities/paper-note.md`

不要一次性加载全部 capability；只读取当前路由需要的文件。

## Invocation / 调用语义

Paper Reader 同时支持**显式调用**与**自然语言自动路由**。

推荐显式语义：

```text
/paper-reader <mode> <request>
```

是否由宿主原生注册为 Slash Command 取决于宿主能力；本仓库仍是可移植的 Agent Skill，不绑定 Claude Code、DSH、Codex 等任一家的私有 command 目录。

不写 mode 也可以：

```text
/paper-reader 帮我深入精读这篇论文
```

也可以完全使用自然语言：

```text
帮我深入精读这篇论文。
```

模式名是路由标签，不是必须出现的关键词；没有显式 mode 时应理解语义，而不是机械字符串匹配。

### 显式 mode 优先级

显式 mode 优先于自动推断，但以下用户限制更高：

- 不联网；
- 不使用外部资料；
- 只保存已有内容；
- 指定论文/文件夹范围；
- 指定论文版本；
- 指定比较维度；
- 指定时间范围。

未知 mode 不报错退出；把 `/paper-reader` 后面的整段文本视为自然语言请求重新路由。

## 用户可见模式

用户层面有 **9 个主模式**：

| mode | 内部路由 | 用途 |
|---|---|---|
| `quick` | `quick` | 快速建立单篇论文骨架 |
| `deep` | `deep` | 深入精读 + light context |
| `internal` | `deep-internal` | 深入精读，但不使用外部资料 |
| `teach` | `teach` | 解释公式、方法、概念、机制 |
| `context` | `context` | SOTA、benchmark、作者前作、相关/后续工作、Survey |
| `critique` | `critique` | 证据 + 方法学 + 必要外部验证 |
| `compare` | `compare` | 多论文/文件夹横向比较与综合 |
| `note` | note 路由 | `compact / learning / full` |
| `full` | `full` | 单篇论文六阶段完整精读 + Full Learning Record |

### `note` 子模式

```text
/paper-reader note compact
```

只保存当前已有结果，不启动新分析或新检索。

```text
/paper-reader note
/paper-reader note learning
```

默认长期知识库模式。复用已有分析，并在有价值且允许时补 light context。

```text
/paper-reader note full
```

基于**当前已经核验的 Paper Context**生成 Full Learning Record 格式；缺失内容明确标记，不为了填模板自动跑完整六阶段。

注意：

```text
/paper-reader note full
```

和：

```text
/paper-reader full
```

不是一回事。前者是完整格式；后者是完整六阶段工作流 + 完整格式。

## 自动语义路由

没有显式 mode 时，按用户真正目的选择最小充分工作流。

| 用户目的 | 内部模式 | 目标 |
|---|---|---|
| “快速看看 / 这篇讲什么” | `quick` | structure |
| “只读懂这篇 / 不查外部” | `deep-internal` | structure → teacher → evidence |
| “精读 / 深入读懂” | `deep` | structure → teacher → evidence → light context |
| “这个公式/方法没懂” | `teach` | 必要 structure → teacher |
| “SOTA / 作者前作 / 后续研究” | `context` | targeted context |
| “靠谱吗 / 有什么不足” | `critique` | evidence → targeted context（按需）→ critic |
| “比较这几篇 / 比较这个文件夹 / 横向对比” | `compare` | collection → normalized comparison → synthesis |
| “保存一下” | `note compact` | 保存已有成果 |
| “知识库 / Obsidian / 以后复习” | `note learning` | 标准长期学习笔记 |
| “完整吃透并归档” | `full` | 单篇六阶段 + full note |

如果请求同时包含多篇论文和“完整比较”，优先进入 `compare`，再按比较所需范围对各论文做增量补读；不要把 `full × N` 当默认策略。

## 单篇论文调度

1. **按覆盖范围复用。** 核对论文身份、版本、已读范围和当前问题；可靠部分复用，缺失部分增量补充。
2. **外部检索统一调度。** `paper-context-research` 负责论文外学术脉络；稳定结果复用，时效性问题刷新。
3. **阶段只做自己的职责。** 不为了完整而重复摘要、解释或搜索。
4. **按需回看原文。** 只回看缺失、冲突、证据定位不足或版本变化影响的 Section/Figure/Table/Page。
5. **内部/外部严格分层。** `[论文原文]`、`[模型归纳]`、`[模型解释]`、`[外部文献]`、`[后续研究]`、`[不确定]` 不混用。
6. **研究有深度。** quick/internal 为 none，deep 默认 light，明确外部问题为 targeted，full 为 full。
7. **笔记有深度。** compact / learning / full 与阅读深度独立。
8. **显式调用不绕过证据规则。** 缺材料时记录 blocked/remaining，不能伪造“完整完成”。

## Note 持续增量同步

Paper Context 是单篇论文的事实与学习状态源。已有 Note 时，后续实质性学习应**增量合并**到 Note，而不是整份覆盖或机械追加聊天记录。

按 `references/paper-context.md` 的 `context_revision` 与 `note_sync` 执行：

- Context 出现实质新增/修订时递增 `context_revision`；
- 已存在 Note 且 `note_sync=auto` 时，若当前环境可持久化，更新受影响的 managed section；
- `note_sync=on-demand` 时，只在用户显式 `note/save/archive` 时同步；
- `note_sync=off` 时，不修改已有 Note；
- Note 更新只消费已经核验的 Context，**不会因为自动同步而触发新的全文阅读或外部研究**；
- 相同知识点优先 merge / revise / deduplicate，不创建“补充1、补充2、再补充”式重复段落；
- 用户手写内容、用户观点和无法确认来源的手工修改必须保留。

例如用户连续追问某个公式或机制，`teaching` 会逐渐变丰富；已有 Learning Note 应把对应章节逐步完善，而不是删掉旧笔记重新生成。

## 多论文 / Collection 调度

涉及多个 PDF、一个文献文件夹、显式论文列表或横向比较时，读取 `references/collection-protocol.md` 和 `capabilities/paper-compare.md`。

原则：

1. **每篇论文仍有独立 Paper Context / Note。** 禁止把几十篇论文塞进一个巨大单篇 Context。
2. **先 inventory，再决定阅读深度。** 文件夹很大时先做 manifest / metadata / abstract-level triage；不要默认 `full × N`。
3. **比较先定义 axes。** 用户给的比较维度优先；否则按问题和论文类型推导最小充分维度。
4. **Compare 消费已有 Context。** 某篇缺比较字段时只补该字段所需章节，不重读全部论文。
5. **并排摘要不等于比较。** 输出规范化矩阵，再做跨论文 synthesis。
6. **覆盖差异透明。** `not reported`、`not assessed`、`not accessible` 与真正的“没有”必须区分。
7. **Collection 结果单独保存。** comparison/synthesis 不直接塞回某一篇论文 Note；单篇 Note 只可保留 collection 链接或与本论文直接相关的 cross-paper note。
8. **比较证据可回溯。** 每个关键比较结论绑定 paper_id + Section/Figure/Table/Page 或外部 source id。

## 执行与持久化

单篇推荐：

```text
.paper-reader/papers/<paper-id>/
├── context.md
├── note.md
└── figures/
```

为兼容旧版，也可读取：

```text
.paper-reader/<paper-id>/context.md
```

多篇集合推荐：

```text
.paper-reader/collections/<collection-id>/
├── manifest.md
├── comparison.md
└── synthesis.md
```

若用户只在当前对话阅读，可维护等价的会话状态，不强制落盘。

## 默认回答行为

- `quick`：论文骨架，不做外部搜索。
- `internal`：内部理解、教学、Claim–Evidence，不使用外部资料。
- `deep`：内部精读 + light context。
- `teach`：聚焦难点，按需补背景。
- `context`：targeted research。
- `critique`：证据、方法学和必要外部验证分层。
- `compare`：先建立/复用 collection manifest，再做规范化比较和综合。
- `note compact`：只保存已有成果。
- `note learning`：标准长期学习笔记。
- `note full`：用现有 Context 渲染 full 格式。
- `full`：单篇完整六阶段 + Full Learning Record。
