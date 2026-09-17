---
name: paper-compare
description: Use when the user wants to compare multiple supplied academic papers, compare papers in a folder or collection, build a normalized evidence-backed comparison matrix, or synthesize agreements, differences, mechanisms, methods, outcomes, limitations, and research evolution across a defined paper set.
---

# Paper Compare

## 目标

围绕**用户已经给定的一组论文**做可追溯的横向比较与综合。

不是：

- 把每篇论文各写一遍摘要；
- 把整个领域重新搜索一遍；
- 默认对文件夹中每篇执行 full workflow。

先读：

- `references/collection-protocol.md`
- `references/paper-context.md`

按需消费已有单篇 Paper Context。

## 输入类型

支持：

1. 当前会话中明确的多篇论文；
2. 用户指定的论文文件列表；
3. 一个包含多篇论文的文件夹；
4. 已存在的 collection；
5. 当前论文 + 用户点名的其他论文。

若只有一篇论文且用户没有比较意图，不进入本阶段。

## Step 1: 定义集合

建立或复用 `collection_id`。

优先确认：

- collection 的研究问题；
- 用户明确的比较维度；
- 论文集合范围；
- 是否要求所有论文都纳入；
- 是否允许外部资料。

不需要为了开始比较让用户手工逐篇命名；可以从可访问文件建立 manifest。

## Step 2: Inventory / Manifest

对文件夹或较多论文：

1. 列出文件；
2. 识别每篇论文身份；
3. 检查是否已有 Paper Context；
4. 尽可能提取 metadata / abstract；
5. 标记 coverage 与初步相关性。

禁止 inventory 阶段直接 `full × N`。

## Step 3: 选择比较 axes

优先级：

1. 用户明确给的 axes；
2. 用户问题天然要求的 axes；
3. 根据论文类型推导的最小充分 axes。

示例：

用户要比较生物材料论文：

```text
材料类型
关键材料特性
巨噬细胞如何感知/响应
表型/通路变化
对骨再生的影响
证据类型
局限
```

用户要比较 AI 方法论文：

```text
task
core idea
architecture
training data
benchmark
metric
compute
ablation
robustness
limitations
```

不要为了“专业”机械生成与问题无关的列。

## Step 4: 复用单篇 Context，补最小缺口

每篇论文：

```text
已有 Context
   ↓
当前 axes 是否被覆盖？
   ├─ 是 → 直接复用
   └─ 否 → 只补缺失字段所需的原文范围
```

如果某篇完全没读过：

- 先建立最小 structure；
- 再只深入当前比较所需字段；
- 除非用户明确要求，不自动 deep/full。

补读产生的新单篇知识写回该论文 Context，并按 Note Sync 规则决定是否同步其 Note。

## Step 5: Normalize

将各篇信息归一到同一 axes。

每个关键 cell 要区分：

- reported
- derived
- not_reported
- not_assessed
- not_accessible
- not_applicable
- uncertain

不能把 `not_assessed` 当成 `not_reported`。

涉及数字/排名时先判断是否：

- 同数据集；
- 同人群；
- 同指标；
- 同实验协议；
- 同计算预算；
- 同时间点。

不公平可比时明确写“不可直接横比”。

## Step 6: Comparison Matrix

输出 `comparison.md`：

```markdown
# <Collection> Comparison

## Comparison question

## Paper coverage

## Axes

## Matrix

## Key contrasts

## Evidence gaps
```

矩阵不是结束；它只是 synthesis 的证据底座。

## Step 7: Synthesis

输出 `synthesis.md`：

### Agreements
多篇论文一致支持什么？

### Differences
真正差异来自：

- 方法；
- 材料；
- 人群/数据；
- benchmark；
- 处理条件；
- 测量指标；
- 时间点；
- 假设。

### Mechanistic chain
如果问题涉及机制，优先重建：

```text
input / material property
→ sensing
→ intracellular pathway
→ phenotype
→ downstream outcome
```

并逐篇指出链条证据覆盖到哪里。

### Contradictions
结果相反时先检查设定差异，不把“不同条件下不同结果”误写成真正冲突。

### Research evolution
有时间顺序时说明：

```text
predecessor
→ current papers
→ later refinements
```

### Open questions
当前 collection 仍回答不了什么？

## 外部搜索边界

Compare 默认比较**用户给定集合**。

只有用户要求：

- 补 SOTA；
- 找缺失竞争论文；
- 验证集合是否代表领域；
- 找 Survey；
- 查后续复现；

才调用 `paper-context-research`。

不要把 compare 自动扩展成无边界 literature review。

## Note / Context 边界

- collection comparison 写入 collection 文件；
- 不把所有比较内容塞回单篇 Note；
- 只有明确影响某篇论文理解的 cross-paper 结论，才写回该论文 Context；
- 用户自己的 collection 笔记必须保留；
- collection 更新做增量 row/column/synthesis patch，不全量重写。

## 输出给用户

默认先给：

1. 一句话总体结论；
2. 规范化比较表；
3. 3–7 个最重要差异；
4. 一致/冲突机制；
5. coverage / 证据缺口；
6. 如已持久化，给 comparison/synthesis 位置。

不要输出一串互不关联的逐篇摘要。
