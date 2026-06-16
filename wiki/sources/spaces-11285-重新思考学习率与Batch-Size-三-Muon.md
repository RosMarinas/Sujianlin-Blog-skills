---
type: article_summary
title: "重新思考学习率与Batch Size（三）：Muon"
article_id: "11285"
source_url: "https://spaces.ac.cn/archives/11285"
date: "2025-09-15"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11285/page.html"
series:
  - "[[重新思考学习率与Batch Size]]"
topics:
  - "[[SGD收敛与学习率调度]]"
concepts:
  - "[[平均场近似学习率分析]]"
  - "[[矩阵符号函数]]"
formulas:
  - "[[Muon平均场Batch缩放公式]]"
methods:
  - "[[用平均场近似替代复杂期望计算]]"
problem_patterns:
  - "[[将优化器非线性更新转化为Batch Size尺度律问题]]"
evidence_spans:
  - "ev::11285::基本记号"
  - "ev::11285::计算期望"
  - "ev::11285::相同规律"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md"
source_ids:
  - "11285"
status: draft
updated: "2026-06-10"
---

# 重新思考学习率与Batch Size（三）：Muon

## 文章核心问题

这篇文章讨论学习率与 Batch Size 的尺度关系，重点是把随机优化器更新量的统计量写成可分析的 Batch Size 函数。

## 主要结论

把平均场近似迁移到 Muon 的矩阵符号更新，说明其学习率-Batch Size 关系近似 SignSGD。

## 推导结构

1. 固定更新量或优化器近似。
2. 计算更新量的一阶矩与二阶矩。
3. 代回二阶损失近似，读出最优学习率与 Batch Size 的关系。

## 关键对象

- 概念：[[平均场近似学习率分析]], [[矩阵符号函数]]
- 公式：[[Muon平均场Batch缩放公式]]
- 方法：[[用平均场近似替代复杂期望计算]]
- 问题模式：[[将优化器非线性更新转化为Batch Size尺度律问题]]

## 原文证据锚点

- `ev::11285::基本记号`
- `ev::11285::计算期望`
- `ev::11285::相同规律`
