---
name: paper-reader
description: Use when the user wants to read, understand, explain, critique, contextualize, study, compare, or archive an academic paper, including methods, equations, evidence, related work, SOTA, benchmarks, limitations, or durable research notes.
---

# Paper Reader

## 定位

这是论文阅读的**唯一入口**。用户不需要记内部 capability 名称。根据问题自动选择阶段，并通过同一份 Paper Context 串联；**不要重复已经可靠完成的分析或搜索**。

本文及内部模块中的 `references/`、`capabilities/` 路径均相对本 skill 根目录。先读 `references/paper-context.md`，但不要一次性加载全部 capability。只在确定需要某阶段时读取对应文件：

- `capabilities/paper-structure.md`
- `capabilities/paper-teacher.md`
- `capabilities/paper-evidence-review.md`
- `capabilities/paper-context-research.md`
- `capabilities/paper-method-critic.md`
- `capabilities/paper-note.md`

## Invocation / 调用语义

Paper Reader 同时支持**显式调用**与**自然语言自动路由**。

### 显式调用（推荐）

在宿主支持通过 Skill 名称进行 slash / 显式 invocation 时，推荐使用：

```text
/paper-reader <mode> <request>
```

例如：

```text
/paper-reader quick 帮我快速看懂这篇论文
/paper-reader deep 把这篇论文深入讲懂
/paper-reader internal 只分析论文本身，不查外部资料
/paper-reader teach 重点讲 Method 3.2 和式（4）
/paper-reader context 查它当时的 SOTA、作者前作和后续工作
/paper-reader critique 看看这篇论文有什么硬伤
/paper-reader note learning 整理成长期 Obsidian 笔记
/paper-reader full 从头到尾吃透并做成完整学习档案
```

`/paper-reader` 是本 Skill 的**推荐显式调用语义**。是否由宿主原生注册为 Slash Command 取决于宿主能力；本仓库不绑定 Claude Code、DSH、Codex 等任一宿主的私有 command 格式。

如果宿主没有把 Agent Skill 暴露为 slash command，应使用该宿主的 Skill 选择方式，或直接用自然语言调用；路由语义保持一致。

### 不写 mode 也可以

```text
/paper-reader 帮我深入精读这篇论文，并看看它后续发展得怎么样
```

此时根据剩余自然语言自动判断模式。

用户也可以完全不写 `/paper-reader`，直接说：

```text
帮我深入精读这篇论文。
```

只要宿主已经加载本 Skill，也按相同语义自动路由。

### 显式 mode 优先级

如果用户显式写了 mode，优先服从 mode；但以下限制优先级更高：

- “不要联网”
- “不要使用外部资料”
- “只保存已有内容”
- 用户指定的阅读范围、论文版本、时间范围

例如：

```text
/paper-reader deep 只分析论文本身，不要查外部资料
```

应执行内部 deep reading，`context_depth=none`，不能因为 `deep` 默认 light context 而违反用户限制。

### 未知 mode

如果 `/paper-reader` 后的第一个词不是已知 mode，不报错退出；把后续整句视为自然语言请求并自动路由。

## 用户可见模式

用户只需要理解下面 8 个主模式：

| 显式 mode | 内部路由 | 用途 |
|---|---|---|
| `quick` | `quick` | 快速建立论文骨架 |
| `deep` | `deep` | 深入精读 + light context |
| `internal` | `deep-internal` | 深入精读，但不使用外部资料 |
| `teach` | `teach` | 专门解释公式、方法、概念、机制 |
| `context` | `context` | 专门查 SOTA、benchmark、作者前作、相关/后续工作、Survey |
| `critique` | `critique` | 证据 + 方法学 + 必要外部验证 |
| `note` | note 路由 | 保存/整理笔记，支持 `compact / learning / full` |
| `full` | `full` | 六阶段完整精读 + Full Learning Record |

### `note` 子模式

```text
/paper-reader note compact
```

只保存当前已有结果，不启动新研究。

```text
/paper-reader note learning
```

默认长期知识库模式；复用已有分析，并在有价值且允许时补 light context。

```text
/paper-reader note full
```

基于**当前已经核验的 Paper Context**生成 Full Learning Record 格式。缺失内容明确标记，不为了填满模板自动跑完整六阶段。

注意：

```text
/paper-reader note full
```

和：

```text
/paper-reader full
```

不是一回事。

前者是“完整格式的笔记”；后者是“完整六阶段阅读 + 完整格式笔记”。

单独：

```text
/paper-reader note
```

默认等价于 `note learning`。

## 自动语义路由

没有显式 mode 时，优先根据用户自然语言意图判断，不要求出现 `quick`、`deep`、`full` 等关键词。

| 用户目的 | 内部模式 | 目标 context_depth | 目标 note_depth | 阶段 |
|---|---|---|---|---|
| “快速看看 / 这篇讲什么 / 20 分钟看懂” | `quick` | none | none | `paper-structure` |
| “只读懂这篇 / 不查外部资料” | `deep-internal` | none | none | `paper-structure → paper-teacher → paper-evidence-review` |
| “精读 / 深入读懂 / 帮我真正学习这篇” | `deep` | light | none | structure → teacher → evidence → light context |
| “这个公式/方法/概念没懂” | `teach` | none，必要时 targeted | none | 必要 structure → teacher；知识缺口确实需要时补 context |
| “靠谱吗 / 有什么不足 / 挑刺” | `critique` | targeted 按需 | none | 必要 structure → evidence → targeted context（按需）→ critic |
| “创新真实吗 / 相关工作 / SOTA / benchmark / 作者前作 / 后续研究 / survey” | `context` | targeted | none | 必要结构 → `paper-context-research` |
| “保存一下 / 把刚才内容记下来” | `archive-compact` | 不新增 | compact | `paper-note` compact |
| “整理成论文笔记 / 放知识库 / Obsidian / 以后复习用” | `archive-learning` | light（有价值且允许时） | learning | 复用已有分析 → 补有用 light context → note learning |
| “完整精读 / 从头吃透并整理 / 完整学习档案” | `full` | full | full | 六阶段完整执行 |

模式名称是**路由标签，不是必须出现的关键词**。不能机械地用字符串匹配代替语义判断。

## 调度规则

1. **按覆盖范围复用。** 没有 Context 时建立；已有 Context 时核对论文身份、版本、已读范围及当前问题，可靠部分复用，缺失部分增量补充。
2. **外部检索统一调度、增量更新。** `paper-context-research` 负责 SOTA、benchmark、作者前作、前置/竞争/后续工作、Survey、外部局限和相反证据；其他阶段提出具体缺口并消费它的结果；稳定且已覆盖的问题不重复搜索，时效性问题按当前请求刷新。
3. **阶段只做自己的职责。** 后一阶段不得为了“完整”重复前一阶段的摘要、结构或分析。
4. **按需回看原文。** Context 缺失、冲突、证据定位不足或 source quality 低时，只回看必要 Section/Figure/Table/Page；不要无脑重新通读全文。
5. **按需加载 capability。** 未被路由到的 capability 不读取，以减少 token。
6. **内部/外部严格分层。** `[论文原文]`、`[模型归纳]`、`[模型解释]`、`[外部文献]`、`[后续研究]`、`[不确定]` 不得混用。
7. **外部检索要可追溯。** 关键外部判断进入 `source_ledger`，记录 DOI/URL/年份/检索日期；Web 不可用时明确限制，不得凭记忆补齐。
8. **中途追问可续跑。** 用户从 deep 继续说“再挑刺”，直接从已有 Context 接 critic；说“再看看后续研究”，只补 context；说“存成笔记”，按 note depth 接 note，不从头开始。
9. **研究有深度。** quick/internal 为 none，deep 默认 light，明确外部问题为 targeted，full 为 full；遵守外部资料与联网限制。
10. **笔记有深度。** 简单保存为 compact，知识库/论文笔记为 learning，完整档案为 full。learning 复用内部分析并保留缺口，不自动补跑全部内部阶段。
11. **覆盖优先于深度标签。** targeted 与 full 不构成严格等级，已有 full 不阻止新问题深挖；当前 SOTA 等时效性结论检查 retrieved_at。
12. **显式调用不绕过证据规则。** `/paper-reader full` 也不能在缺失全文、Web、图像或其他必要材料时伪造“完整完成”；必须记录 blocked/remaining。

## 执行

每次核对论文身份与 `source_version`、`stage_status` 的覆盖范围、用户当前目的、显式 mode（若有）及 `research_queries`。只执行缺失且必要的工作，按 `references/paper-context.md` 更新状态和依赖结论。`completed_stages` 仅兼容旧记录，不能替代覆盖检查。

涉及图表解释、图表证据或图片归档时，读取 `references/figure-handling.md`。读图与存图分开；图表是共享材料，不是必跑的第七阶段。

若当前环境支持持久化，Context 推荐保存在 `.paper-reader/<paper-id>/context.md`；若用户只是在当前对话阅读，可在会话内维护等价 Context，不强制落盘。

## 默认回答行为

- `quick`：论文骨架，不做外部搜索。
- `internal` / `deep-internal`：内部理解、教学与 Claim–Evidence，不使用外部研究。
- `deep`：内部精读后默认补 light context，合并成连贯讲解；受限时明确外部缺口。
- `teach`：直接解释难点，仅按具体知识缺口补 targeted 背景。
- `context`：围绕问题做 targeted research。
- `critique`：内部证据、方法学问题与必要外部验证分层呈现。
- `note compact`：只保存已有成果、来源与未完成项。
- `note learning`：标准长期学习笔记，按需确保有用的 light context。
- `note full`：用已有 Context 生成 Full Learning Record；不自动补齐所有缺失阶段。
- `full`：六阶段形成统一 Full Learning Record；限制或缺失材料导致未完成时明确记录。
