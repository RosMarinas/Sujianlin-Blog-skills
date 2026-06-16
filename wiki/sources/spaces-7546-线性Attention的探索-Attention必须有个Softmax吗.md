---
type: article_summary
title: 线性Attention的探索：Attention必须有个Softmax吗？
article_id: "7546"
source_url: https://spaces.ac.cn/archives/7546
date: 2020-07-04
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
concepts:
  - "[[线性化Attention]]"
  - "[[Linear Attention]]"
methods:
  - "[[用结构约束线性化Attention计算]]"
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::7546::结合律线性化
  - ev::7546::一般化Attention
  - ev::7546::双重Softmax
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
source_ids:
  - "7546"
status: draft
updated: 2026-06-11
---

# 线性Attention的探索：Attention必须有个Softmax吗？

## 文章核心问题

系统解释线性Attention：用非负相似度、核函数、双重softmax等形式恢复结合律，把复杂度降到线性。

## 主要结论

- Softmax阻断QK^T V的结合律，是标准Attention二次复杂度的关键来源。
- 只要相似度非负且可分解，就能把Attention写成可线性计算的加权平均。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- [[用结构约束线性化Attention计算]]

## 原文证据锚点

- `ev::7546::结合律线性化`
- `ev::7546::一般化Attention`
- `ev::7546::双重Softmax`
