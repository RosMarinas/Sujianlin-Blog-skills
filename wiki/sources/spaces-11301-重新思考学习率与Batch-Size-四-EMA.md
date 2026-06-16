---
type: article_summary
title: "重新思考学习率与Batch Size（四）：EMA"
article_id: "11301"
source_url: "https://spaces.ac.cn/archives/11301"
date: "2025-09-22"
category: "Mathematics"
source_markdown: "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
source_html: "Data/Spaces_ac_cn/raw/articles/11301/page.html"
series:
  - "[[重新思考学习率与Batch Size]]"
topics:
  - "[[SGD收敛与学习率调度]]"
concepts:
  - "[[EMA等效批量放大]]"
  - "[[Surge现象]]"
formulas:
  - "[[EMA等效Batch Size公式]]"
methods:
  - "[[用等效Batch Size解释动量降噪]]"
problem_patterns:
  - "[[将优化器非线性更新转化为Batch Size尺度律问题]]"
evidence_spans:
  - "ev::11301::放大批量"
  - "ev::11301::符号动量"
  - "ev::11301::双重滑动"
  - "ev::11301::一般分析"
sources:
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-09-22-重新思考学习率与Batch-Size-四-EMA.md"
source_ids:
  - "11301"
status: draft
updated: "2026-06-10"
---

# 重新思考学习率与Batch Size（四）：EMA

## 文章核心问题

这篇文章讨论学习率与 Batch Size 的尺度关系，重点是把随机优化器更新量的统计量写成可分析的 Batch Size 函数。

## 主要结论

分析动量/EMA 对优化器尺度律的影响，得出动量约等于放大有效 Batch Size。

## 推导结构

1. 固定更新量或优化器近似。
2. 计算更新量的一阶矩与二阶矩。
3. 代回二阶损失近似，读出最优学习率与 Batch Size 的关系。

## 关键对象

- 概念：[[EMA等效批量放大]], [[Surge现象]]
- 公式：[[EMA等效Batch Size公式]]
- 方法：[[用等效Batch Size解释动量降噪]]
- 问题模式：[[将优化器非线性更新转化为Batch Size尺度律问题]]

## 原文证据锚点

- `ev::11301::放大批量`
- `ev::11301::符号动量`
- `ev::11301::双重滑动`
- `ev::11301::一般分析`
