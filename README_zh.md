# Paper Reader Skill

一个专门用于**真正读懂论文、讲解论文、分析证据、补齐相关文献脉络、批判方法学并沉淀长期笔记**的 Agent Skill。

它对外只有一个入口：`paper-reader`。你不需要记六个内部模块，更不用手动一个个调用。

## 它和普通论文总结 Skill 的区别

普通总结通常是：

```text
PDF → 背景 → 方法 → 实验 → 结论
```

Paper Reader 的目标是：

```text
目标论文
  ↓
结构理解
  ↓
老师模式讲懂方法/公式/知识点
  ↓
Claim ↔ Evidence：作者到底证明了什么
  ↓
Web / 学术检索：把论文放回研究脉络
  ↓
方法学与后续证据压力测试
  ↓
完整论文学习档案 / 知识库 Note
```

## 六个内部能力

| 内部 capability | 负责什么 |
|---|---|
| `paper-structure` | 研究问题、论文骨架、方法、贡献、实验、结果 |
| `paper-teacher` | 概念、公式、机制、方法教学 |
| `paper-evidence-review` | Claim ↔ Evidence，判断作者自己的证据够不够 |
| `paper-context-research` | SOTA、benchmark、作者前作、前置/竞争/后续工作、Survey、外部局限与相反证据 |
| `paper-method-critic` | 实验设计、偏差、混杂、统计、泛化、复现，并吸收外部文献证据 |
| `paper-note` | 汇总成完整 Markdown / Obsidian 论文学习档案 |

六个模块共享同一个 Paper Context，因此不是把 PDF 从头读六遍。

## 你平时怎么用

不用命令，直接自然语言：

```text
帮我快速看懂这篇论文。
```
→ 只做结构理解。

```text
帮我精读这篇论文，真正给我讲懂。
```
→ 结构 → 教学 → Claim–Evidence → 必要的相关文献脉络。

```text
重点给我讲 Method 3.2 和式 (4)，为什么要这么设计？
```
→ 直接进入老师模式，只补必要上下文。

```text
这篇论文到底创新在哪？作者是不是说过头了？
```
→ 内部证据审查 + 外部文献定位 + 方法学批判。

```text
帮我查一下这篇论文相关的 SOTA、benchmark、作者前作、后续工作和 survey。
```
→ 只跑 paper-centered context research，不重新总结全文。

```text
把我们前面所有内容整理成一份以后能复习的 Obsidian 笔记。
```
→ 复用已有 Context，补必要外部资料，然后生成完整 Note。

```text
从头到尾把这篇论文吃透，并做成完整学习档案。
```
→ 六阶段全流程。

## 外部文献检索

这一版**会主动做相关文献检索**，但它不是你的通用 Research Agent。

它的原则是：**以当前论文为中心，只搜索理解这篇论文所需的一圈高价值文献。**

默认关注：

- 论文发表当时的 SOTA；
- 截至当前检索日期的代表性 SOTA/进展；
- benchmark 是什么、是否有已知缺陷；
- 作者/课题组直接相关前作；
- 关键前置论文；
- 同期竞争路线；
- 后续继承、改进、替代工作；
- 后续复现失败、方法局限、不同结论；
- 1–2 篇高质量 Survey/Review；
- 官方代码、数据集、项目页。

关键点是：

```text
论文内部事实          external literature
     ↓                       ↓
paper_internal        external_context
     └─────────┬─────────────┘
               ↓
       最终综合，但来源不混淆
```

因此后续论文说“这个方法有缺陷”，不会被写成“原作者自己承认了这个缺陷”。

## 最终 Note 有多完整

最终的 `paper-note` 默认可以包含：

1. 论文卡片；
2. 5 分钟快速回忆；
3. 研究问题、背景与核心假设；
4. 方法整体框架；
5. 关键知识点与核心公式；
6. 实验设计与关键结果；
7. Claim–Evidence Matrix；
8. 方法学、作者局限和外部验证局限；
9. “真正证明了什么 / 没证明什么”；
10. 技术发展脉络；
11. 作者自己的研究路线；
12. 同期竞争与相关论文对比表；
13. 当时与当前 SOTA；
14. Benchmark 现状；
15. 后续工作与外部评价；
16. Survey / Review；
17. “先读 → 再读 → 深入读”的推荐阅读路径；
18. 用户自己的笔记与疑问；
19. Socratic Questions；
20. Glossary；
21. Related Papers / Source Ledger。

因此它更接近“**论文 + 老师讲义 + 审稿记录 + Related Work + 长期学习笔记**”，而不是一页摘要。

## 安装

### 从 GitHub 用 skills CLI

发布到你自己的 GitHub 后：

```bash
npx skills add https://github.com/<你的GitHub用户名>/paper-reader-skill --skill paper-reader
```

### 安装到所有 Agent 共用目录

```bash
git clone https://github.com/<你的GitHub用户名>/paper-reader-skill.git
cd paper-reader-skill
chmod +x install.sh
./install.sh ~/.agents/skills
```

最终全局只暴露：

```text
~/.agents/skills/
└── paper-reader/
```

六个 capability 都藏在 `paper-reader` 内部，不会和最外层入口抢触发。

## 发布到你自己的 GitHub

本仓库已经按 GitHub 项目整理好。解压后：

```bash
cd paper-reader-skill

gh repo create paper-reader-skill \
  --public \
  --source=. \
  --remote=origin \
  --push
```

也可以直接运行：

```bash
./publish.sh paper-reader-skill public
```

如果你想先换名字，直接改仓库目录/README 再创建即可。

## 验证

```bash
python3 tests/validate_skills.py
```

GitHub Actions 也会自动运行相同校验。

## 来源与许可证

这套 Skill 是重新设计和编写的工作流，没有直接把 5 个上游 SKILL.md 打包进来。设计参考和许可证说明见 [`ATTRIBUTION.md`](ATTRIBUTION.md)。

MIT License。
