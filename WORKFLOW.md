# Paper Reader Workflow

日常只调用 `paper-reader`，按问题选择能力，并共享一份带版本和覆盖范围的 Paper Context。

## Main Modes

| 模式 | 工作流 | 本次研究目标 | 笔记目标 |
|---|---|---|---|
| quick | structure | none | none |
| deep-internal | structure → teacher → evidence | none | none |
| deep | structure → teacher → evidence → light context | light | none |
| teach | necessary structure → teacher，按知识缺口补 context | none / targeted | none |
| context | targeted context | targeted | none |
| critique | necessary structure → evidence → targeted context when required → critic | targeted 按需 | none |
| archive-compact | existing context → compact note | 不新增 | compact |
| archive-learning | existing analysis → useful light context → learning note | light（有价值且允许时） | learning |
| full | structure → teacher → evidence → full context → critic → full note | full | full |

## Context Depth

none = 不做外部研究；light = 理解论文所需的最小学术脉络；targeted = 明确问题深挖；full = 较全面的论文中心型研究地图。targeted 与 full 不构成严格等级。已有 full 不阻止新问题研究，也不能代替当前 SOTA 的时效性刷新。

## Note Depth

none = 不生成笔记；compact = 只保存已有成果；learning = 标准知识库笔记；full = 完整学习档案。显式“只保存刚才内容”优先于 Obsidian 等格式词。learning 内部分析缺失时保留未读/未评估项，不自动补跑全部阶段。

路由深度表示目标，Context 字段在实际执行/生成后更新。外部资料被禁止时不检索或引用外部缓存；仅禁止联网时可复用注明日期的本地来源。材料或工具受限时标记缺口，不以深度标签宣称完成。

## 复用与修订

1. 核对论文身份、版本和材料质量。
2. 用 `stage_status` 的 scope/status/remaining 判断是否覆盖当前问题；旧 `completed_stages` 不能代表全文已读。
3. `paper_internal` 与 `external_context` 分开；关键结论绑定原文位置或来源 id。
4. 外部搜索统一调度，稳定结果复用，时效性问题刷新；以问题解决程度决定停止，不凑文献数量。
5. 新版本或新证据影响已有结论时，记录原因并更新关联判断、解释和笔记，保留用户注释。
6. 图表按 `references/figure-handling.md` 实际查看，归档时选择性保存，记录图号、页码、版本、图注与 Claim 关联。
7. 最终输出去重；compact 紧凑保存、learning 用于长期复习、full 按需展开。

## 典型续跑

```text
“解释式（4）” → teaching scope: equation-4
“继续讲全文方法” → 复用式（4），补其余方法
“最新 benchmark 结果如何” → 定向搜索并记录截至日期
“保存刚才的内容” → 直接保存已有结果和缺口
“这是 v3” → 检查版本差异，重验受影响内容
```
