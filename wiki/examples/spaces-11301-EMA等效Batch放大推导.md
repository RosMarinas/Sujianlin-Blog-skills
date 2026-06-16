---
type: example
title: spaces-11301-EMA等效Batch放大推导
aliases: null
article_id: '11301'
article: '[[重新思考学习率与Batch Size（四）：EMA]]'
section: 放大批量
claim: 展开 EMA 权重并利用协方差可加性，得到动量等效 Batch Size 放大因子。
notation_mapping:
  same_as_standard: 'true'
steps:
- 选定随机更新量
- 计算或近似统计量
- 代回最优学习率公式
used_concepts:
- '[[EMA等效批量放大]]'
used_formulas:
- '[[EMA等效Batch Size公式]]'
used_methods:
- '[[用等效Batch Size解释动量降噪]]'
problem_pattern: '[[将优化器非线性更新转化为Batch Size尺度律问题]]'
source_span: ev::11301::放大批量
evidence_spans:
- ev::11301::放大批量
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md
source_ids:
- '11301'
status: stable
updated: '2026-06-12'
---

# spaces-11301-EMA等效Batch放大推导

## 所在文章

[[重新思考学习率与Batch Size（四）：EMA]]

## 原始问题

展开 EMA 权重并利用协方差可加性，得到动量等效 Batch Size 放大因子。

## 推导步骤

1. 选定随机更新量。
2. 用原文章节 `放大批量` 中的近似或恒等式计算统计量。
3. 代回最优学习率表达式，得到 Batch Size 依赖。

## 结论

该例子支撑 [[用等效Batch Size解释动量降噪]]。

## 证据锚点

- `ev::11301::放大批量`