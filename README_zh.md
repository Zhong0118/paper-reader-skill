# Paper Reader Skill

一个专门用于**真正读懂论文、讲解方法与公式、分析证据、补齐相关研究脉络、批判方法学并沉淀长期笔记**的 Agent Skill。

对外只有一个入口：`paper-reader`。

> **最推荐的用法：**在支持 Skill 显式调用的宿主里输入 `/paper-reader <mode>`；不想记模式也没关系，直接 `/paper-reader 你的需求`，或者直接用自然语言说需求即可。

---

## 30 秒上手

安装完成后，你可以这样用：

```text
/paper-reader quick
```

快速看懂论文。

```text
/paper-reader deep
```

深入精读，自动补一层轻量相关研究脉络。

```text
/paper-reader internal
```

只读这篇论文本身，不使用外部资料。

```text
/paper-reader teach 重点讲 Method 3.2 和式（4）
```

只讲你没懂的方法、公式或概念。

```text
/paper-reader context 查当时的 SOTA、作者前作和后续研究
```

专门查论文外部学术位置。

```text
/paper-reader critique
```

检查 Claim–Evidence、实验设计、偏差、统计、复现和后续批评。

```text
/paper-reader note learning
```

整理成适合长期复习的知识库 / Obsidian 笔记。

```text
/paper-reader full
```

从头到尾吃透，并生成完整学习档案。

---

## 一定要写 `/paper-reader` 吗？

**不一定。**

Paper Reader 有两种调用方式。

### 方式 A：显式调用（推荐）

```text
/paper-reader deep 帮我把这篇论文真正讲懂
```

优点是意图最明确，尤其适合你同时安装很多 Skill 的情况。

### 方式 B：自然语言自动触发

```text
帮我深入精读这篇论文，把方法和公式讲懂。
```

如果当前 Agent 已经加载 `paper-reader`，它会根据语义自动判断应该走哪个模式。

### 关于 Slash Command

本仓库本质上仍是 **Agent Skill**，不是绑定某个宿主的私有 Slash Command 插件。

因此：

- 支持把已安装 Skill 暴露为 slash / 显式 invocation 的宿主：推荐 `/paper-reader ...`；
- 不支持自定义 slash command 的宿主：使用宿主的 Skill 选择方式，或直接自然语言调用；
- 本 Skill 不为了实现 `/paper-reader` 而绑定 Claude Code、DSH、Codex 任一家的专有目录格式。

也就是说，`/paper-reader` 是**推荐显式调用语义**，具体 UI/命令是否原生出现取决于宿主。

---

# 模式到底有几种？

用户层面只需要记 **8 个主模式**：

| 模式 | 什么时候用 | 默认行为 |
|---|---|---|
| `quick` | 我只想快速知道这篇讲什么 | 论文结构/核心贡献/主要结果 |
| `deep` | 我想真正精读这篇 | 结构 → 教学 → Claim–Evidence → light context |
| `internal` | 我只想读这篇，不要外部文献 | deep，但 `context_depth=none` |
| `teach` | 某个公式/方法/概念没懂 | 聚焦解释指定难点 |
| `context` | 我想查 SOTA、benchmark、作者前作、后续论文 | targeted 外部研究 |
| `critique` | 我想知道论文靠不靠谱、有什么不足 | 证据审查 + 方法学批判 + 必要外部验证 |
| `note` | 我要保存/整理笔记 | `compact / learning / full` 三个子模式 |
| `full` | 我要从头吃透并完整归档 | 六阶段完整流程 |

如果只输入：

```text
/paper-reader
```

或者：

```text
/paper-reader 帮我看看这篇论文值不值得继续读
```

会根据后面的自然语言自动选模式。

---

# Note 的 3 个子模式

## 1. Compact Note

```text
/paper-reader note compact
```

适合：

```text
把刚才内容保存一下。
```

特点：

- 只保存已有分析；
- 不为了笔记模板重新搜索；
- 不自动补 critique；
- 不自动补没读过的方法；
- 明确保留“未读 / 未评估 / 未解决”。

---

## 2. Standard Learning Note

```text
/paper-reader note
```

或：

```text
/paper-reader note learning
```

这是**推荐的日常知识库模式**。

适合：

```text
整理成以后复习用的 Obsidian 论文笔记。
```

通常包含：

- Paper Card；
- Five-Minute Recall；
- Research Question & Motivation；
- Method；
- 核心公式与前置知识；
- Experiments & Evidence；
- Claim–Evidence；
- What It Proves / Does Not Prove；
- Strengths & Limitations；
- light Research Context；
- Related Paper Comparison；
- Learning Notes；
- Further Reading；
- Sources。

必要且允许时，会补少量真正有价值的：

- 核心前置工作；
- 当前论文相对已有工作的变化；
- 代表性 follow-up；
- Survey / Review；
- 特别重要的作者前作或 benchmark 背景。

---

## 3. Full Learning Record

有两种方式。

### 只把现有分析整理成 Full 格式

```text
/paper-reader note full
```

它只使用当前已经核验的 Paper Context。

缺什么就标什么，**不会为了填满 Full 模板自动跑完六阶段**。

### 真正从头完整吃透

```text
/paper-reader full
```

执行：

```text
paper-structure
→ paper-teacher
→ paper-evidence-review
→ full paper-context-research
→ paper-method-critic
→ Full Learning Record
```

这两个命令不要混淆：

```text
note full = 完整格式
full      = 完整工作流 + 完整格式
```

---

# 不想记模式怎么办？

完全可以。

下面这些自然语言都会自动路由。

```text
帮我快速看看这篇论文讲了什么。
```

→ `quick`

```text
帮我深入精读这篇论文，把方法和公式真正讲懂。
```

→ `deep`

```text
只分析这篇论文，不要查外部资料。
```

→ `internal`

```text
式（4）为什么这么写？每个符号是什么意思？
```

→ `teach`

```text
它真的是首创吗？当时 SOTA 是谁？
```

→ `context`

```text
这篇论文有哪些硬伤？实验设计靠谱吗？
```

→ `critique`

```text
把刚才内容保存一下。
```

→ `note compact`

```text
整理成以后复习的 Obsidian 论文笔记。
```

→ `note learning`

```text
从头到尾吃透并做成完整学习档案。
```

→ `full`

模式名是**可选的显式控制方式**，不是必须出现的关键词。

---

# 显式模式和自然语言冲突时听谁的？

显式 mode 优先，例如：

```text
/paper-reader quick 给我看看这篇论文
```

明确走 `quick`。

但用户限制优先级更高，例如：

```text
/paper-reader deep 只分析论文内部，不要外部资料
```

虽然指定 `deep`，但必须遵守“不使用外部资料”，所以实际相当于 `internal`。

同理：

```text
/paper-reader note learning 只把刚才内容存下来，不要新增分析
```

应降为 compact 行为。

---

# 它和普通论文总结 Skill 有什么区别？

普通总结通常是：

```text
PDF
→ 背景
→ 方法
→ 实验
→ 结论
```

Paper Reader 的目标是：

```text
目标论文
  ↓
结构理解
  ↓
老师模式讲懂方法 / 公式 / 知识点
  ↓
Claim ↔ Evidence：作者到底证明了什么
  ↓
Web / 学术检索：把论文放回研究脉络
  ↓
方法学与后续证据压力测试
  ↓
长期知识库 Note
```

---

# 六个内部能力

你不需要手动调用它们。

| capability | 负责什么 |
|---|---|
| `paper-structure` | 研究问题、论文骨架、贡献、实验、结果 |
| `paper-teacher` | 概念、公式、机制、方法教学 |
| `paper-evidence-review` | Claim ↔ Evidence，判断作者自己的证据够不够 |
| `paper-context-research` | SOTA、benchmark、作者前作、前置/竞争/后续工作、Survey、外部局限 |
| `paper-method-critic` | 实验设计、偏差、混杂、统计、泛化、复现 |
| `paper-note` | Compact / Learning / Full 三级长期笔记 |

六个模块共享同一份 Paper Context，不会把 PDF 从头读六遍。

---

# 外部文献检索

研究深度分成：

```text
none
light
targeted
full
```

### none

不使用论文外资料。

### light

`deep` 默认使用。

只补理解当前论文最重要的一圈：

- 核心前置思想；
- 当前论文改变了什么；
- 少量代表性 follow-up；
- Survey/Review；
- 必要时作者前作 / benchmark。

### targeted

围绕一个明确问题深挖，例如：

- 是不是首创；
- 当时 SOTA；
- 当前 SOTA；
- 作者前作；
- benchmark 缺陷；
- 复现失败；
- 某项 limitation 是否被后续证实。

### full

完整学习档案使用。

根据论文类型选择性建立：

- predecessors；
- author previous work；
- competing work；
- publication-time SOTA；
- current representative progress；
- benchmark context；
- follow-up；
- external limitations；
- contradictory findings；
- Survey；
- code / dataset / project；
- reading path。

没有固定论文数量配额。

完成标准是：

> 当前问题是否已经被足够可靠的证据回答。

---

# 内部事实和外部研究不会混在一起

```text
论文内部事实          external literature
     ↓                       ↓
paper_internal        external_context
     └─────────┬─────────────┘
               ↓
       最终综合，但来源不混淆
```

因此：

> 后续论文认为某方法有缺陷

不会被写成：

> 原论文自己承认了这个缺陷。

---

# 增量阅读与版本

Paper Context 按阶段记录：

```text
status
scope
remaining
source_version
updated_at
```

所以：

```text
“式（4）已经讲懂”
```

不等于：

```text
“整篇 Method 已经读完”
```

如果论文：

```text
arXiv v2 → v3
```

只重验受影响的：

- Figure；
- Claim；
- 实验结果；
- 解释；
- Note。

不从头全部重跑，并保留用户笔记。

---

# 图表处理

解释依赖图表时必须实际查看。

区分：

```text
verified
caption_only
unreadable
```

归档时优先保存：

- 核心方法图；
- 流程/架构图；
- 支撑关键 Claim 的结果图；
- 关键消融图。

保存后检查：

- 图片是否完整；
- 裁剪是否正确；
- Markdown 链接是否有效；
- Figure 编号是否对应；
- 论文版本是否对应。

模型重绘和论文原图必须分开标识。

---

# 安装

## skills CLI

```bash
npx skills add https://github.com/Zhong0118/paper-reader-skill --skill paper-reader
```

## 共用 Skills 目录

```bash
git clone https://github.com/Zhong0118/paper-reader-skill.git
cd paper-reader-skill
chmod +x install.sh
./install.sh ~/.agents/skills
```

最终只暴露：

```text
~/.agents/skills/
└── paper-reader/
```

内部六个 capability 不会和入口抢触发。

---

# 验证

```bash
python3 tests/validate_skills.py
```

GitHub Actions 也会自动执行相同校验。

---

# 来源与许可证

这套 Skill 是重新设计和编写的工作流，没有直接把上游 5 个 `SKILL.md` 打包进来。

设计参考和许可证说明见：

```text
ATTRIBUTION.md
```

MIT License。
