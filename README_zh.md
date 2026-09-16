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
| `paper-note` | Compact / Learning / Full 三级长期笔记 |

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
→ 结构 → 教学 → Claim–Evidence → 默认 light 学术脉络。

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
→ Standard Learning Note；复用已有分析，必要且允许时补轻量学术脉络。

```text
从头到尾把这篇论文吃透，并做成完整学习档案。
```
→ 六阶段全流程。

## 外部文献检索

深入精读默认补 light context：关键前置工作、当前论文改变了什么、代表性 follow-up 和领域 Survey。明确问题使用 targeted；完整档案使用 full；“只读论文，不查外部资料”使用 none。深度精读不会自动扩展成大型文献综述。

它的原则是：**以当前论文为中心，只搜索理解这篇论文所需的一圈高价值文献。**

可按问题选择：

- 论文发表当时的 SOTA；
- 截至当前检索日期的代表性 SOTA/进展；
- benchmark 是什么、是否有已知缺陷；
- 作者/课题组直接相关前作；
- 关键前置论文；
- 同期竞争路线；
- 后续继承、改进、替代工作；
- 后续复现失败、方法局限、不同结论；
- 相关 Survey/Review；
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

## 阅读模式

- 快速看看：论文骨架。
- 深入精读：内部理解、方法讲解、Claim–Evidence 和轻量领域脉络。
- 只读论文、不查外部：只做内部精读。
- 完整吃透并归档：六阶段完整工作流，按材料与论文类型选择内容。

## 三种笔记

| 你怎么说 | 产物 |
|---|---|
| “保存一下 / 把刚才内容记下来” | Compact Note，只保存已有成果，不新增分析或检索 |
| “整理成论文笔记 / 放知识库 / Obsidian / 以后复习用” | Standard Learning Note，必要且允许时补有用的 light context |
| “完整学习档案 / 从头吃透并归档” | Full Learning Record，六阶段工作流 |

Learning Note 组织论文身份、快速回忆、方法与公式、证据、局限、技术脉络、核心相关论文对比、后续工作、Survey、阅读路径、用户疑问和来源。它优先复用已有内部分析，未读部分明确标为缺口，不为了模板假装已完成精读。

“只保存刚才内容到 Obsidian”仍是 compact。禁止外部资料时不补外部内容；工具受限或没有可靠材料时保留缺口。full 按价值展开，不要求每一章都有内容。

## 增量阅读与版本

Context 按阶段记录 scope、status、remaining 和来源版本。讲过式（4）只代表该公式已覆盖；继续精读时补其他方法。旧版论文更新后，重验受影响的图表、结论及关联笔记，保留用户注释。外部检索以问题为单位记录结果，稳定结论复用，当前进展按需刷新，不凑文献数量。

## 图表怎么处理

读图与存图分开：解释依赖图片时必须实际查看；归档优先保存核心架构/流程图及支撑关键结论的结果图，次要图片保留定位即可。

每张选中的图记录图号、页码、论文版本、来源、图注及关联 Claim，放在对应解释旁。PDF 矢量图可通过渲染页面后裁剪保存，不能假设提取内嵌位图就完整。交付前检查图像清晰完整、链接有效；只有图注可读时明确标注，不猜测箭头或数值。模型重绘与原图分开标识。详见 [图表规则](skills/paper-reader/references/figure-handling.md)。

## 安装

### 从 GitHub 用 skills CLI

发布到你自己的 GitHub 后：

```bash
npx skills add https://github.com/Zhong0118/paper-reader-skill --skill paper-reader
```

### 安装到所有 Agent 共用目录

```bash
git clone https://github.com/Zhong0118/paper-reader-skill.git
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
