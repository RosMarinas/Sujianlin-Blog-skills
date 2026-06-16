---
type: series
title: SVD分解
aliases:
  - SVD representation series
article_ids:
  - "4208"
  - "4216"
  - "4233"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-01-15-SVD分解-一-自编码器与人工智能.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-01-26-SVD分解-二-为什么SVD意味着聚类.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-02-23-SVD分解-三-连Word2Vec都只不过是个SVD.md
source_ids:
  - "4208"
  - "4216"
  - "4233"
series_goal: 用 SVD 统一解释线性自编码器、聚类语义和词向量模型结构。
entry_roles:
  4208: 把 SVD 和无激活线性自编码器视为同一种压缩重建结构，并用聚类解释泛化。
  4216: 把矩阵分解解释为行类、列类和类间关系的概率分解。
  4233: 把词向量、词袋模型、CBOW 和线性自编码器/SVD 的结构关系放在同一矩阵视角下比较。
key_concepts:
  - [[奇异值分解]]
  - [[线性自编码器-SVD等价]]
  - [[矩阵分解聚类解释]]
key_methods:
  - [[用矩阵分解重写表示学习结构]]
reading_paths:
  - [[SVD矩阵分解阅读路径]]
status: draft
updated: 2026-06-10
---

# SVD分解

## 系列核心问题

这个早期系列不是严密的 SVD 定理证明，而是把 SVD 当作表示学习的认知透镜：矩阵分解、线性自编码器、聚类语义和词向量结构可以互相改写。

## 文章顺序

1. `4208` [[SVD分解(一)：自编码器与人工智能]]
2. `4216` [[SVD分解(二)：为什么SVD意味着聚类？]]
3. `4233` [[SVD分解(三)：连Word2Vec都只不过是个SVD？]]
