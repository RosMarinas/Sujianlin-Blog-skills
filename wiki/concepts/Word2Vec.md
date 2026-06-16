---
type: concept
title: Word2Vec
aliases:
- Word2Vec tool
- Word representations in vector space
definition: 一种高效获取词向量的分布式表示学习工具，核心包含CBOW与Skip-Gram两种训练架构，以及Hierarchical Softmax与Negative
  Sampling两种提速手段。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
source_ids:
- '4299'
prerequisites: []
evidence_spans:
- ev::4299::训练提速
status: stable
updated: '2026-06-12'
---

# Word2Vec

Word2Vec 是 Google 出品的高效率获取词向量的工具。它能够将词汇映射到低维连续向量空间，保留丰富的语义和语法关系。

## 核心架构
Word2Vec 由两种训练架构和两种提速手段排列组合而成：
- **CBOW (Continuous Bag-of-Words)**：利用上下文词预测中心词。
- **Skip-Gram**：利用中心词预测上下文词。
- **Hierarchical Softmax (层次Softmax)**：使用 Huffman 树降低分类复杂度。
- **Negative Sampling (负采样)**：使用二分类近似多分类。