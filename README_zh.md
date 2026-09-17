# Paper Reader Skill

一个用于**真正读懂论文、持续学习单篇论文、横向比较多篇文献，并把知识沉淀成可持续更新 Note** 的 Agent Skill。

> 推荐显式调用：`/paper-reader <mode>`  
> 也支持 `/paper-reader 你的自然语言需求`，以及完全自然语言自动路由。

---

## 30 秒上手

```text
/paper-reader quick
```
快速看懂一篇论文。

```text
/paper-reader deep
```
深入精读 + light 学术脉络。

```text
/paper-reader internal
```
只读论文本身，不使用外部资料。

```text
/paper-reader teach 重点讲式（4）
```
专门讲公式、方法、机制或概念。

```text
/paper-reader context 查作者前作、SOTA 和后续研究
```
定向查外部学术位置。

```text
/paper-reader critique
```
证据审查 + 方法学批判。

```text
/paper-reader compare 比较这个文件夹里的论文
```
建立 Collection，做真正的规范化横向比较。

```text
/paper-reader note learning
```
整理/更新长期知识库 Note。

```text
/paper-reader full
```
单篇论文完整六阶段精读并归档。

---

# 9 个主模式

| mode | 用途 |
|---|---|
| `quick` | 快速建立论文骨架 |
| `deep` | 深入精读 + light context |
| `internal` | 深入精读，但不使用外部资料 |
| `teach` | 公式、方法、概念、机制教学 |
| `context` | SOTA、benchmark、作者前作、相关/后续研究、Survey |
| `critique` | Claim–Evidence + 方法学 + 必要外部验证 |
| `compare` | 多论文 / 文件夹横向比较与综合 |
| `note` | compact / learning / full 笔记 |
| `full` | 单篇六阶段完整精读 + Full Learning Record |

不记模式也没关系：

```text
/paper-reader 帮我比较这五篇论文里材料刚度如何影响巨噬细胞
```

会自动路由到 compare。

---

# Note 会不会随着我继续问而更新？

**会。v0.5 开始把它作为正式协议。**

Paper Context 是事实源，Note 是派生产物。

```text
你继续问某个知识点
        ↓
teacher / evidence / critic 更新 Context
        ↓
context_revision +1
        ↓
已有 Note？
        ↓
note_sync
        ↓
增量合并对应章节
```

默认：

```yaml
note_sync: auto
```

也支持：

```text
auto
on-demand
off
```

### auto

已有 Note 时，出现实质性新知识就同步对应章节。

### on-demand

Context 一直更新，但只有你说：

```text
保存
更新笔记
note
```

时才写 Note。

### off

不自动改已有 Note。

---

## 更新是“合并”，不是“覆盖”

例如 Note 原来只有：

```markdown
### YAP/TAZ

材料刚度会影响 YAP/TAZ。
```

后来你连续追问 integrin、FAK、RhoA/ROCK、actin tension、YAP 核转位。

最终应该把原章节完善成：

```text
ECM stiffness
→ Integrin
→ FAK
→ RhoA/ROCK
→ Actin tension
→ YAP/TAZ nuclear translocation
→ downstream transcription
```

并补：

- 本文证据；
- 机制解释；
- 易混点；
- 论文真正证明到哪里；
- 尚未证明什么。

不会变成：

```text
补充1
补充2
再次补充
```

也不会把旧 Note 整份删掉重新写。

---

## 用户自己的笔记会被保护

Paper Reader 推荐用 managed region：

```markdown
<!-- paper-reader:managed:start key="teaching.T1" -->
模型维护内容
<!-- paper-reader:managed:end -->
```

用户区域：

```markdown
<!-- paper-reader:user:start -->
我的理解……
<!-- paper-reader:user:end -->
```

规则：

- managed 可以增量更新；
- user 永不自动覆盖；
- `我的笔记` 默认保护；
- 不认识来源的手工文本默认保留；
- 旧 Note 没有 marker 也不能整份覆盖。

---

# 多篇文献 / 文件夹怎么办？

v0.5 新增 Collection 层。

不是：

```text
20 篇 PDF
→ 一个巨大 context.md
```

而是：

```text
每篇论文
→ 独立 Context
→ 独立 Note

多篇论文
→ Collection
→ manifest
→ comparison
→ synthesis
```

推荐目录：

```text
.paper-reader/
├── papers/
│   ├── paper-a/
│   │   ├── context.md
│   │   ├── note.md
│   │   └── figures/
│   └── paper-b/
│       ├── context.md
│       ├── note.md
│       └── figures/
└── collections/
    └── macrophage-bone-regeneration/
        ├── manifest.md
        ├── comparison.md
        └── synthesis.md
```

---

# 文件夹里有几十篇 PDF 会全部 full 吗？

**不会。**

默认：

```text
Inventory
   ↓
Metadata / Abstract triage
   ↓
按比较问题筛选
   ↓
Structure / targeted backfill
   ↓
真正重要的少数论文才 deep/full
```

例如 40 篇：

```text
40 篇先进入 manifest
↓
根据问题判断相关性
↓
20 篇只需 metadata
10 篇 structure
7 篇定向补读
3 篇 deep
```

具体数量不是配额，只是示意。

---

# Compare 怎么用？

```text
/paper-reader compare
```

例如：

```text
/paper-reader compare
从材料类型、材料特性、如何影响巨噬细胞、对骨再生的影响四个方面比较这些论文
```

或：

```text
/paper-reader compare 比较这个文件夹里的文献
```

Paper Reader 会先建立 Collection Manifest，然后按统一 axes 比较。

---

## 真正比较，而不是并排摘要

错误：

```text
论文 A：……
论文 B：……
论文 C：……
```

正确：

| Paper | 材料类型 | 关键材料特性 | 巨噬细胞感知机制 | 表型/通路 | 骨再生结果 | 证据 |
|---|---|---|---|---|---|---|

然后再综合：

```text
共同规律
关键差异
真正冲突
不同结果可能来自什么条件
技术发展路线
当前集合还回答不了什么
```

---

## 某篇缺比较字段怎么办？

不会重新 full。

例如 P03 只缺：

```text
巨噬细胞感知机制
```

则只回看 P03 与这一字段相关的：

```text
Methods
Results
Figure
Supplement
```

补完 P03 Context 后继续比较。

---

## 比较结果保存在哪里？

```text
collections/<collection-id>/comparison.md
collections/<collection-id>/synthesis.md
```

不会把 10 篇论文的比较结果全部塞进某一篇 `note.md`。

单篇 Note 最多保留：

```markdown
## Cross-paper Links

- [[../../collections/.../comparison]]
- [[../../collections/.../synthesis]]
```

只有比较结果真正改变了对该论文的理解时，才把对应结论写回单篇 Context / Note。

---

# Compare 的数据覆盖状态

Paper Reader 会区分：

```text
reported
derived
not_reported
not_assessed
not_accessible
not_applicable
uncertain
```

所以：

> 没读到

不会被错误写成：

> 论文没有。

这是多论文比较里非常重要的一条。

---

# 单篇阅读模式

`deep` 默认：

```text
structure
→ teacher
→ evidence
→ light context
```

`internal`：

```text
structure
→ teacher
→ evidence
```

不使用外部资料。

`full`：

```text
structure
→ teacher
→ evidence
→ full context
→ critic
→ full note
```

---

# Note 三个档位

```text
/paper-reader note compact
```
只保存当前已有成果。

```text
/paper-reader note
/paper-reader note learning
```
默认知识库笔记。

```text
/paper-reader note full
```
只把当前已核验 Context 渲染成 Full 格式。

注意它不同于：

```text
/paper-reader full
```

后者会先跑完整单篇工作流。

---

# 内部能力

对外仍然只有一个 `paper-reader`。

内部现在是 7 个 capability：

```text
paper-structure
paper-teacher
paper-evidence-review
paper-context-research
paper-method-critic
paper-compare
paper-note
```

其中 `paper-compare` 只负责给定论文集合的比较，不替代通用 Research Agent。

---

# 安装

```bash
npx skills add https://github.com/Zhong0118/paper-reader-skill --skill paper-reader
```

或：

```bash
git clone https://github.com/Zhong0118/paper-reader-skill.git
cd paper-reader-skill
./install.sh ~/.agents/skills
```

最终只公开：

```text
paper-reader
```

---

# 验证

```bash
python3 tests/validate_skills.py
git diff --check
```

GitHub Actions 会自动运行 validator。
