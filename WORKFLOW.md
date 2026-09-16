# Paper Reader Workflow

## 唯一入口

日常只调用 `paper-reader`。它根据用户目的选择最小工作流，并按需加载内部 capability。

## 路由

- `quick`：`paper-structure`
- `teach`：必要结构 → `paper-teacher`
- `context`：必要结构 → `paper-context-research`
- `deep`：`paper-structure → paper-teacher → paper-evidence-review → paper-context-research`
- `critique`：必要结构 → `paper-evidence-review → paper-context-research → paper-method-critic`
- `archive`：复用已有 Context → 缺外部脉络才补 `paper-context-research` → `paper-note`
- `full`：`paper-structure → paper-teacher → paper-evidence-review → paper-context-research → paper-method-critic → paper-note`

## 去重原则

1. 同一论文只有一份 Paper Context。
2. `paper_internal` 与 `external_context` 分开。
3. 一个阶段完成后写入 `completed_stages`。
4. 后续阶段读取前序结果，不重复生成完整摘要。
5. 外部搜索统一由 `paper-context-research` 管理，并记录 `research_queries`，避免重复搜索。
6. 原文只在缺失、冲突、低质量或需要精确定位时按需回看。
7. 最终回答整体去重，不能把六份阶段报告原样拼在一起。

## 典型续跑

```text
“先帮我精读”
structure → teacher → evidence → context

“这个 benchmark 后来是不是有问题？”
复用 Context → context-research（只补 benchmark）

“那从方法学上再挑一下”
直接接 method-critic

“整理成长期笔记”
直接接 paper-note
```
