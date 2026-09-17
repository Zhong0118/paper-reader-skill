---
name: paper-note
description: Use when the user wants to persist, update, merge, or regenerate a durable Markdown or Obsidian-style learning record from an already-read paper and its Paper Context, including incremental synchronization as later questions add or revise knowledge.
---

# Paper Note

## 目标

把当前论文、教学解释、Claim–Evidence、方法学批判和相关论文脉络整理成以后真的会回来看的**论文学习档案 / 知识库记录**。

它不是：

- 摘要换皮；
- 每次追问后重新生成整份文件；
- 聊天记录按时间追加；
- 为了让模板完整而重新跑所有阶段。

先读 `references/paper-context.md`。

## Note 是 Context 的派生产物

Paper Context 是单篇论文长期状态源。

```text
user asks
   ↓
relevant capability updates Context
   ↓
context_revision +1 (substantive change)
   ↓
Note exists?
   ↓
note_sync policy
   ↓
incremental merge
```

因此用户连续追问一个概念、公式或机制时，Note 应逐渐完善对应知识节点，而不是覆盖整份旧 Note。

## Note Sync

### auto

默认。

如果：

- Note 已存在；
- Context 有实质更新；
- 当前环境可写文件；
- 更新与该 Note 的内容范围有关；

则同步受影响 managed sections。

自动同步**不能触发新的分析或研究**。

### on-demand

Context 正常更新，但 Note 只在用户明确：

```text
note
save
archive
整理笔记
```

时同步。

### off

不修改已有 Note。

## Merge 策略

同一个稳定节点：

```text
T1 / E1 / C1 / M1
```

后续出现新内容时：

1. 比较已有 Note managed region；
2. 去重；
3. 新信息合并；
4. 更准确解释替换旧模型解释；
5. 如果新证据推翻旧判断，修订对应结论；
6. 更新 `synced_context_revision`；
7. 在 `note_metadata.sync_log` 记录修改范围和原因。

禁止生成：

```text
补充：
再次补充：
补充 3：
```

式聊天堆叠。

## Managed / User Regions

新 Note 推荐：

```markdown
<!-- paper-reader:managed:start key="teaching.T1" -->
...
<!-- paper-reader:managed:end -->
```

用户区域：

```markdown
<!-- paper-reader:user:start -->
...
<!-- paper-reader:user:end -->
```

规则：

- managed region 可由 Paper Reader 增量维护；
- user region 永不自动改写；
- `我的笔记` / 用户观点默认视为 protected；
- 不认识来源的手工文本默认保留；
- 旧 Note 没有 markers 时做 section-aware merge，不整份覆盖；
- 用户明确“重新生成整份”时也必须迁移/保留用户内容。

## Compact Note

触发：

```text
保存一下
把刚才内容记下来
/paper-reader note compact
```

只保存已有结果。

建议：

1. 论文卡片；
2. 已读范围；
3. 快速回忆与研究问题；
4. 已讲解方法/公式；
5. 已核验 Claim–Evidence；
6. 已知局限；
7. 用户笔记/疑问；
8. 来源与未完成项。

不启动新检索或缺失阶段。

## Standard Learning Note

触发：

```text
整理成论文笔记
放进知识库
Obsidian
以后复习
/paper-reader note
/paper-reader note learning
```

这是默认长期知识库格式。

### 0. Paper Card
身份、作者、Venue、年份、DOI/arXiv、版本、代码/数据、阅读日期、实际范围。

### 1. Five-Minute Recall
一句话、研究问题、核心方法思想、重要贡献、关键结果、为什么值得记住。

### 2. Research Question & Motivation
问题、重要性、已有方法不足、核心假设。

### 3. Method
输入 → 处理 → 中间状态 → 输出；模块、公式、前置知识、直觉、易混点。

### 4. Experiments & Evidence
Dataset/Baseline/Metric/Control/Ablation 或理论证明条件；核心 Figure/Table 与 Claim–Evidence。

### 5. What It Proves / Does Not Prove
证据支持边界、未证明部分、过度外推风险。

### 6. Strengths & Limitations
作者自述、内部分析、外部验证分开。

### 7. Research Context
有价值且允许时呈现 light context。

### 8. Related Paper Comparison
只保留与本论文直接相关的关键对比；完整多论文矩阵放 Collection。

### 9. Learning Notes
模型易错点、用户笔记、用户疑问、未解决问题分开。

### 10. 推荐进一步阅读（Further Reading）
先读 → 再读 → 深入读，并说明为什么。

### 11. Sources
目标论文、相关论文、Survey、benchmark/project/dataset，外部判断回指 source_ledger。

## Full Learning Record

`/paper-reader note full`：

只用当前已核验 Context 生成 full 格式，缺项明确标记。

`/paper-reader full`：

由入口先调度完整单篇工作流，再生成 full 格式。

可按论文类型选择：

0. 论文卡片
1. 快速回忆
2. 研究问题与背景
3. 方法整体框架
4. 关键知识点与核心公式
5. 实验设计与关键结果
6. Claim–Evidence
7. 方法学与局限
8. 真正证明了什么 / 没证明什么
9. 技术发展脉络
10. 作者研究路线
11. 同期竞争与相关论文对比
12. 当时 / 当前 SOTA
13. Benchmark
14. 后续工作与外部评价
15. Survey / Review 与进一步阅读
16. 我的笔记
17. Socratic Questions
18. Glossary
19. Related Papers / Sources

不要求空栏目强行填满。

## Collection Links

如果该论文属于一个或多个 Collection，可以在 Note 添加轻量链接：

```markdown
## Cross-paper Links

- [[../../collections/<collection-id>/comparison]]
- [[../../collections/<collection-id>/synthesis]]
```

不要把整个 collection comparison 复制进单篇 Note。

只有跨论文发现直接改变了对本论文的：

- Claim 支持；
- 方法局限；
- novelty 定位；
- benchmark 理解；

才以明确 `[跨论文比较]` 标记增量合并对应章节。

## 图表归档

按 `references/figure-handling.md`。

已有图像资产复用；只有实际核验过的图才作为证据。保存后验证文件、链接、图号、版本和图注。

## 写作与同步要求

- 默认中文，术语首次出现保留英文；
- 数字、公式、实验结论保留论文位置；
- 外部判断保留 source id；
- 相同知识点只保留一个最佳整合版本；
- 用户内容不可静默删除；
- Note 成功更新后同步 `note_metadata`；
- 无法写文件时标 Note stale/blocked，不声称已更新；
- note_sync 只持久化已有知识，不触发额外研究。
