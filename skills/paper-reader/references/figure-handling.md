# Figure Handling

图表是 structure、teacher、evidence-review 与 note 的共享材料。涉及图表解释、证据判断或图片归档时读取本文件。

## 读图与存图

- 解释依赖视觉信息时，实际查看相关图表，即使不保存。图注不等于图中内容；记录 `view_status: verified|caption_only|unreadable`。
- 归档时优先保存已用于讲解的核心架构/流程图，以及支撑主要 Claim 的结果/消融图。次要或重复图只保留定位；用户明确要求全量保存时按其范围处理。
- 只在会话阅读时可不落盘。保存请求下，图像不可用就记录来源定位与缺口，不声称文件已生成。

## 获取与核验

1. 确认论文版本、原图号与所需子图。优先使用可获取的官方完整原图，否则渲染 PDF 页面后裁剪。
2. 不假设“提取 PDF 内嵌位图”能得到完整图：流程图可能由矢量、文字和多张位图组成。核对箭头、标签、图例、坐标轴、单位、误差条及子图标记；必要时保留整页。
3. 保存后实际查看输出图片，确认清晰、完整、无错裁。图注可单独记录在笔记中，不必强行放入裁剪图。
4. 对结果图区分视觉趋势与精确数值。精确数值优先核对正文/表格；从图估读必须标明近似，不能给虚假精度。
5. 工具不支持查看、渲染失败或图像模糊时，记录 caption_only/unreadable 与原因，只解释可核验的文本。不得猜测箭头、数值或隐藏结构。

## 记录与文件

默认与笔记同目录保存 `figures/fig-02-method.png` 等有意义的文件名。Context 默认在 `.paper-reader/<paper-id>/context.md`；笔记可放同目录的 `note.md`，也可使用用户指定目录。跨版本图片使用版本子目录或文件名，避免覆盖旧版资产。

每个关键图表记录：

```yaml
figure_id: fig-02
source_version: arxiv-v2
source: # PDF 路径或来源 URL
pdf_page: 5 # 从 1 开始
printed_page: 4 # 无印刷页码可省略
panel: all
caption: # 原图注或明确标注的摘要
view_status: verified
kind: original_crop # original / original_crop / model_redraw
path: figures/fig-02-method.png # 未保存时省略；相对笔记目录
supports: [C1]
interpretation: # 图如何阅读，说明与未说明什么
```

原图保存来源与图注；模型重绘需标注“模型重绘/简化”，附依据与省略内容，不能冒充原图或作为新增实验结果。OCR 文本和重绘图不能代替原图核验。

## 笔记交付

把图贴在对应解释旁，附原图号、版本、来源与“如何读 / 支持到哪里”。使用相对笔记目录的 Markdown 图片链接；若笔记与 Context 分开保存，在 Context 记录笔记位置。移动笔记时同步移动资产并检查链接。交付前验证文件存在、链接可解析、图与图注对应；用户自己的注释保留。
