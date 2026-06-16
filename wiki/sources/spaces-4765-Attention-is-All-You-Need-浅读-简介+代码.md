---
type: article_summary
title: 《Attention is All You Need》浅读（简介+代码）
article_id: "4765"
source_url: https://spaces.ac.cn/archives/4765
date: 2018-01-06
category: 
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-01-06-Attention-is-All-You-Need-浅读-简介-代码.md
series:
  - "[[Attention归一化与线性化专题]]"
topics:
  - "[[Attention效率与归一化]]"
  - "[[Transformer架构]]"
concepts:
  - "[[Attention]]"
  - "[[Softmax]]"
  - "[[位置编码]]"
methods:
problem_patterns:
  - "[[把全量序列交互改写为结构化注意力计算问题]]"
evidence_spans:
  - ev::4765::Attention定义
  - ev::4765::MultiHead
  - ev::4765::复杂度
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-01-06-Attention-is-All-You-Need-浅读-简介-代码.md
source_ids:
  - "4765"
status: draft
updated: 2026-06-11
---

# 《Attention is All You Need》浅读（简介+代码）

## 文章核心问题

从序列编码角度解读Transformer的scaled dot-product attention、multi-head attention、位置编码和O(n^2)瓶颈。

## 主要结论

- Attention层通过QK相似度softmax加权V来一步获取全局关联。
- Self Attention的O(n^2)复杂度使restricted或结构化Attention成为后续研究重点。

## 推导结构

1. 从已有生成/注意力模型的瓶颈出发。
2. 把瓶颈改写为可优化的数学目标或结构约束。
3. 给出公式、训练目标或实现变体。
4. 通过实验、代码或理论解释说明适用边界。

## 体现的方法

- 本文主要作为概念和系列上下文支撑，不单独提升新的 method 节点。

## 原文证据锚点

- `ev::4765::Attention定义`
- `ev::4765::MultiHead`
- `ev::4765::复杂度`
