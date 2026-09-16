# Paper Reader Workflow

日常只调用 `paper-reader`，按问题选择能力，并共享一份带版本和覆盖范围的 Paper Context。

## 阅读深度与保存独立

- `quick`：structure，标明已读范围，不做外部研究。
- `teach`：必要结构 → teacher；具体前置知识缺口交给 context research。
- `deep`：structure → teacher → evidence；具体外部问题按需补 context。
- `critique`：必要结构 → evidence → critic；创新性、后续复现等外部问题按需补 context。
- `context`：只回答所需外部脉络问题。
- `archive`：note 保存已有结果和缺口，不自动补研究；可以叠加到任意阅读深度。
- `full` / 明确要求完整学习档案：structure → teacher → evidence → context → critic → note；各阶段按论文类型、实际材料和用户目的执行。

## 复用与修订

1. 核对论文身份、版本和材料质量。
2. 用 `stage_status` 的 scope/status/remaining 判断是否覆盖当前问题；旧 `completed_stages` 不能代表全文已读。
3. `paper_internal` 与 `external_context` 分开；关键结论绑定原文位置或来源 id。
4. 外部搜索统一调度，稳定结果复用，时效性问题刷新；以问题解决程度决定停止，不凑文献数量。
5. 新版本或新证据影响已有结论时，记录原因并更新关联判断、解释和笔记，保留用户注释。
6. 图表按 `references/figure-handling.md` 实际查看，归档时选择性保存，记录图号、页码、版本、图注与 Claim 关联。
7. 最终输出去重；普通笔记紧凑，完整档案按需展开。

## 典型续跑

```text
“解释式（4）” → teaching scope: equation-4
“继续讲全文方法” → 复用式（4），补其余方法
“最新 benchmark 结果如何” → 定向搜索并记录截至日期
“保存刚才的内容” → 直接保存已有结果和缺口
“这是 v3” → 检查版本差异，重验受影响内容
```
