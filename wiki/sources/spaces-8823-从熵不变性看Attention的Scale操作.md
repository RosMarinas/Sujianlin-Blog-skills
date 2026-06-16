---
type: article_summary
title: 从熵不变性看Attention的Scale操作
article_id: "8823"
source_url: https://spaces.ac.cn/archives/8823
date: 2021-12-21
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
  - "[[熵归一化与熵不变性]]"
concepts:
  - "[[熵不变性]]"
  - "[[Softmax]]"
methods:
  - "[[Attention-E熵不变性缩放]]"
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::8823::熵不变性定义
  - ev::8823::熵不变性缩放
  - ev::8823::长度外推实验
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
source_ids:
  - "8823"
status: draft
updated: 2026-06-11
---

# 从熵不变性看Attention的Scale操作

## 文章核心问题

从注意力分布熵对长度不敏感的要求重新推导Attention缩放因子，得到Attention-E长度外推方案。

## 主要结论

- 注意力分布的熵代表聚焦程度，长度增加时应尽量保持不变。
- 缩放因子乘以log n可抵消长度变化对softmax熵的影响，并改善长度外推。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[Attention-E熵不变性缩放]]

## 原文证据锚点

- `ev::8823::熵不变性定义`
- `ev::8823::熵不变性缩放`
- `ev::8823::长度外推实验`
