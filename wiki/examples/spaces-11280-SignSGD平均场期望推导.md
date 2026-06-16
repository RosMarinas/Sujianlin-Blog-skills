---
type: example
title: spaces-11280-SignSGD平均场期望推导
aliases: null
article_id: '11280'
article: '[[重新思考学习率与Batch Size（二）：平均场]]'
section: 方法大意
claim: 平均场把 E[sign(g)] 近似为 E[g]/sqrt(E[g^2])。
notation_mapping:
  same_as_standard: 'true'
steps:
- 选定随机更新量
- 计算或近似统计量
- 代回最优学习率公式
used_concepts:
- '[[平均场近似学习率分析]]'
used_formulas:
- '[[SignSGD平均场学习率公式]]'
used_methods:
- '[[用平均场近似替代复杂期望计算]]'
problem_pattern: '[[将优化器非线性更新转化为Batch Size尺度律问题]]'
source_span: ev::11280::方法大意
evidence_spans:
- ev::11280::方法大意
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md
source_ids:
- '11280'
status: stable
updated: '2026-06-12'
---

# spaces-11280-SignSGD平均场期望推导

## 所在文章

[[重新思考学习率与Batch Size（二）：平均场]]

## 原始问题

平均场把 E[sign(g)] 近似为 E[g]/sqrt(E[g^2])。

## 推导步骤

1. 选定随机更新量。
2. 用原文章节 `方法大意` 中的近似或恒等式计算统计量。
3. 代回最优学习率表达式，得到 Batch Size 依赖。

## 结论

该例子支撑 [[用平均场近似替代复杂期望计算]]。

## 证据锚点

- `ev::11280::方法大意`