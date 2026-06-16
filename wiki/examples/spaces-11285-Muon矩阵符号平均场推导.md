---
type: example
title: spaces-11285-Muon矩阵符号平均场推导
aliases: null
article_id: '11285'
article: '[[重新思考学习率与Batch Size（三）：Muon]]'
section: 计算期望
claim: 把矩阵符号函数的期望近似为 G(E[G^T G])^{-1/2}，再抽出 Batch Size 标量依赖。
notation_mapping:
  same_as_standard: 'true'
steps:
- 选定随机更新量
- 计算或近似统计量
- 代回最优学习率公式
used_concepts:
- '[[平均场近似学习率分析]]'
- '[[矩阵符号函数]]'
used_formulas:
- '[[Muon平均场Batch缩放公式]]'
used_methods:
- '[[用平均场近似替代复杂期望计算]]'
problem_pattern: '[[将优化器非线性更新转化为Batch Size尺度律问题]]'
source_span: ev::11285::计算期望
evidence_spans:
- ev::11285::计算期望
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md
source_ids:
- '11285'
status: stable
updated: '2026-06-12'
---

# spaces-11285-Muon矩阵符号平均场推导

## 所在文章

[[重新思考学习率与Batch Size（三）：Muon]]

## 原始问题

把矩阵符号函数的期望近似为 G(E[G^T G])^{-1/2}，再抽出 Batch Size 标量依赖。

## 推导步骤

1. 选定随机更新量。
2. 用原文章节 `计算期望` 中的近似或恒等式计算统计量。
3. 代回最优学习率表达式，得到 Batch Size 依赖。

## 结论

该例子支撑 [[用平均场近似替代复杂期望计算]]。

## 证据锚点

- `ev::11285::计算期望`