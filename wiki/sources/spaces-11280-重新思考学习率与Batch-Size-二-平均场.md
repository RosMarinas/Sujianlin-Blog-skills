---
type: article_summary
title: "重新思考学习率与Batch Size（二）：平均场"
article_id: "11280"
source_url: "https://spaces.ac.cn/archives/11280"
date: "2025-09-10"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11280/page.html"
series:
  - "[[重新思考学习率与Batch Size]]"
topics:
  - "[[SGD收敛与学习率调度]]"
concepts:
  - "[[平均场近似学习率分析]]"
  - "[[Surge现象]]"
formulas:
  - "[[SignSGD平均场学习率公式]]"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
problem_patterns:
  - "[[将优化器非线性更新转化为Batch Size尺度律问题]]"
evidence_spans:
  - "ev::11280::方法大意"
  - "ev::11280::计算过程"
  - "ev::11280::一般规律"
  - "ev::11280::广义近似"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-10-重新思考学习率与Batch-Size-二-平均场.md"
source_ids:
  - "11280"
status: draft
updated: "2026-06-10"
---

# 重新思考学习率与Batch Size（二）：平均场

## 文章核心问题

这篇文章讨论学习率与 Batch Size 的尺度关系，重点是把随机优化器更新量的统计量写成可分析的 Batch Size 函数。

## 主要结论

用平均场近似替代 SignSGD/SoftSignSGD 中复杂的分布积分，得到显式 Batch Size 依赖。

## 推导结构

1. 固定更新量或优化器近似。
2. 计算更新量的一阶矩与二阶矩。
3. 代回二阶损失近似，读出最优学习率与 Batch Size 的关系。

## 关键对象

- 概念：[[平均场近似学习率分析]], [[Surge现象]]
- 公式：[[SignSGD平均场学习率公式]]
- 方法：[[用平均场近似替代复杂期望计算]]
- 问题模式：[[将优化器非线性更新转化为Batch Size尺度律问题]]

## 原文证据锚点

- `ev::11280::方法大意`
- `ev::11280::计算过程`
- `ev::11280::一般规律`
- `ev::11280::广义近似`
