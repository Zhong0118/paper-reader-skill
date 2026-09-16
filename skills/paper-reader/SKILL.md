---
name: paper-reader
description: Use when the user wants to read, understand, explain, critique, contextualize, study, compare, or archive an academic paper, including methods, equations, evidence, related work, SOTA, benchmarks, limitations, or durable research notes.
---

# Paper Reader

## 定位
这是论文阅读的**唯一入口**。用户不需要记内部模块名。根据问题自动选择阶段，并通过同一份 Paper Context 串联；**不要重复已经可靠完成的分析或搜索**。

先读 `references/paper-context.md`，但不要一次性加载全部 capability。只在确定需要某阶段时读取对应文件：
- `capabilities/paper-structure.md`
- `capabilities/paper-teacher.md`
- `capabilities/paper-evidence-review.md`
- `capabilities/paper-context-research.md`
- `capabilities/paper-method-critic.md`
- `capabilities/paper-note.md`

## 自动路由
优先根据用户自然语言判断，不要求用户输入命令。

| 用户目的 | 模式 | 阶段 |
|---|---|---|
| “快速看看 / 这篇讲什么 / 20 分钟看懂” | `quick` | `paper-structure` |
| “精读 / 帮我真正读懂 / 分析这篇” | `deep` | `paper-structure → paper-teacher → paper-evidence-review → paper-context-research` |
| “这个公式/方法/概念没懂” | `teach` | 必要的 `paper-structure → paper-teacher`；需要领域背景时再定向 `paper-context-research` |
| “靠谱吗 / 创新真实吗 / 有什么不足 / 挑刺” | `critique` | 必要的 `paper-structure → paper-evidence-review → paper-context-research → paper-method-critic` |
| “相关工作 / SOTA / benchmark / 作者前作 / 后续研究 / survey” | `context` | 必要结构 → `paper-context-research` |
| “整理成笔记 / 放知识库 / Obsidian” | `archive` | 复用已有结果；缺外部脉络时补 `paper-context-research` → `paper-note` |
| “完整精读 / 全流程 / 从头读透并整理” | `full` | 六阶段依次执行 |

用户明确指定模式时服从；否则选择**能满足问题的最小工作流**。

## 调度规则
1. **内部理解只建立一次。** 没有 Context 时由第一个需要的阶段建立；已有匹配 Context 时直接复用。
2. **外部检索只集中做一次。** `paper-context-research` 负责 SOTA、benchmark、作者前作、前置/竞争/后续工作、Survey、外部局限和相反证据；其他阶段优先消费它的结果，不重复搜索。
3. **阶段只做自己的职责。** 后一阶段不得为了“完整”重复前一阶段的摘要、结构或分析。
4. **按需回看原文。** Context 缺失、冲突、证据定位不足或 source quality 低时，只回看必要 Section/Figure/Table/Page；不要无脑重新通读全文。
5. **按需加载 capability。** 未被路由到的 capability 不读取，以减少 token。
6. **内部/外部严格分层。** `[论文原文]`、`[模型归纳]`、`[模型解释]`、`[外部文献]`、`[后续研究]`、`[不确定]` 不得混用。
7. **外部检索要可追溯。** 关键外部判断进入 `source_ledger`，记录 DOI/URL/年份/检索日期；Web 不可用时明确限制，不得凭记忆补齐。
8. **中途追问可续跑。** 用户从 deep 继续说“再挑刺”，直接从已有 Context 接 critic；说“再看看后续研究”，只补 context；说“存成笔记”，接 note，不从头开始。

## 执行
每次先确定：当前论文身份、已有 `completed_stages`、用户当前目的、已有 `research_queries`。然后只执行缺失且必要的阶段。每完成一个阶段，将对应区块合并回 Context，并更新 `completed_stages`，不得覆盖其他阶段内容。

若当前环境支持持久化，Context 推荐保存在 `.paper-reader/<paper-id>/context.md`；若用户只是在当前对话阅读，可在会话内维护等价 Context，不强制落盘。

## 默认回答行为
- `quick`：短而结构化，不做外部检索。
- `deep`：搭骨架 → 讲难点 → 检查核心 Claim–Evidence → 补必要学术脉络，最终合并成一份连贯讲解。
- `teach`：直接回答难点；只在概念需要论文外背景时做小范围检索。
- `critique`：内部证据与外部文献分开呈现，区分“作者承认的局限”“分析发现的局限”“后续研究验证的局限”。
- `context`：只补外部学术位置，不重新讲整篇论文。
- `archive`：生成完整学习档案；必要时补缺失的外部脉络，但不无故重跑已完成阶段。
- `full`：六阶段都跑，最终呈现为一份去重后的统一结果，而不是六份报告拼接。
