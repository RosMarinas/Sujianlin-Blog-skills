---
type: concept
title: GlobalPointer
aliases: []
definition: 一种统一处理嵌套和非嵌套命名实体识别/抽取式阅读理解任务的输出结构。将首尾位置组合视为一个整体进行分类，训练和推理行为一致，速度快且效果与CRF相当。
standard_notation: 
prerequisites: 序列标注、阅读理解
sources: Data/Spaces_ac_cn/markdown/... (详见具体文章)
source_ids:
  - 5542
  - 5597
  - 6877
  - 6915
  - 6920
  - 6933
  - 7196
  - 7259
  - 7500
  - 7718
  - 7809
  - 7912
  - 8128
  - 8209
  - 8739
  - 9059
evidence_spans: []
null_evidence_reason: 概念提取自多篇文章，暂未绑定具体证据跨度
status: draft
updated: 2026-06-12
---

# GlobalPointer

一种统一处理嵌套和非嵌套命名实体识别/抽取式阅读理解任务的输出结构。将首尾位置组合视为一个整体进行分类，训练和推理行为一致，速度快且效果与CRF相当。

## 相关文章

本批次中涉及该概念的多篇文章请参见各文章摘要页面。

GlobalPointer将NER任务中的每个实体视作(start, end)组合的全局分类问题。相比CRF，GlobalPointer不需要动态规划解码，直接对所有可能的span打分，训练和推理行为一致。在嵌套NER场景中优势更明显。
