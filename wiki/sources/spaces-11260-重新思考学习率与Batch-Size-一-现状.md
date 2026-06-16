---
type: article_summary
title: "重新思考学习率与Batch Size（一）：现状"
article_id: "11260"
source_url: "https://spaces.ac.cn/archives/11260"
date: "2025-09-01"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11260/page.html"
series:
  - "[[重新思考学习率与Batch Size]]"
topics:
  - "[[SGD收敛与学习率调度]]"
concepts:
  - "[[学习率-Batch Size尺度律]]"
  - "[[噪声尺度]]"
formulas:
  - "[[二阶近似最优学习率公式]]"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
problem_patterns:
  - "[[将优化器非线性更新转化为Batch Size尺度律问题]]"
evidence_spans:
  - "ev::11260::方法大意"
  - "ev::11260::热身练习"
  - "ev::11260::数据效率"
  - "ev::11260::困难分析"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-01-重新思考学习率与Batch-Size-一-现状.md"
source_ids:
  - "11260"
status: draft
updated: "2026-06-10"
---

# 重新思考学习率与Batch Size（一）：现状

## 文章核心问题

这篇文章讨论学习率与 Batch Size 的尺度关系，重点是把随机优化器更新量的统计量写成可分析的 Batch Size 函数。

## 主要结论

建立二阶近似框架，把最优学习率写成更新量一阶矩和二阶矩的函数，并回顾 SGD 的 Batch Size 尺度律。

## 推导结构

1. 固定更新量或优化器近似。
2. 计算更新量的一阶矩与二阶矩。
3. 代回二阶损失近似，读出最优学习率与 Batch Size 的关系。

## 关键对象

- 概念：[[学习率-Batch Size尺度律]], [[噪声尺度]]
- 公式：[[二阶近似最优学习率公式]]
- 方法：[[用平均场近似替代复杂期望计算]]
- 问题模式：[[将优化器非线性更新转化为Batch Size尺度律问题]]

## 原文证据锚点

- `ev::11260::方法大意`
- `ev::11260::热身练习`
- `ev::11260::数据效率`
- `ev::11260::困难分析`
