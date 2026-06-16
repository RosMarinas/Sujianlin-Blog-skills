---
type: article_summary
title: 概率分布的熵归一化（Entropy Normalization）
article_id: "8829"
source_url: https://spaces.ac.cn/archives/8829
date: 2021-12-24
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-12-24-概率分布的熵归一化-Entropy-Normalization.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[熵归一化]]
  - [[Softmax]]
methods:
  - [[幂次变换熵归一化]]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-12-24-概率分布的熵归一化-Entropy-Normalization.md
source_ids:
  - "8829"
status: draft
updated: 2026-06-11
---

## 文章核心问题

是否存在类似L2 Normalization的操作，可以直接对概率分布进行变换，使得保持原始分布主要特性的同时，让它的熵为指定值？

## 主要结论

通过幂次变换 $p_i \to \tilde{p}_i = p_i^\gamma / \sum_i p_i^\gamma$ 可以将熵从0到$\log n$变换。通过牛顿迭代法可求解指定熵对应的$\gamma$。

## 推导结构

1. 幂次变换保持单调性且能覆盖所有熵值
2. 泰勒展开得到牛顿迭代公式
3. 潜在应用讨论（稀疏性控制等）

## 关键公式

$\mathcal{H}_\gamma = \log\sum_i p_i^\gamma - \frac{\gamma\sum_i p_i^\gamma \log p_i}{\sum_i p_i^\gamma}$

迭代公式：$\gamma \leftarrow 1 + \frac{\mathcal{H}^*-\mathcal{H}}{\mathcal{H}^2-\mathbb{E}[(\log p_i)^2]}$

## 体现的方法

幂次变换熵归一化、牛顿迭代法

## 所属系列位置

独立单篇，与Attention的Scale操作相关。

## 与其他文章的关系

与Softmax系列（如Sparsemax、Sparse Softmax）共同构成概率分布变换主题。

## 原文证据锚点

- 幂次变换定义
- 牛顿迭代求解
- 应用设想：稀疏性和采样
