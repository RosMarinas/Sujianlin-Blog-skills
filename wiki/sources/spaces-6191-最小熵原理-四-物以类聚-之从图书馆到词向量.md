---
type: article_summary
title: 最小熵原理（四）："物以类聚"之从图书馆到词向量
article_id: "6191"
source_url: https://spaces.ac.cn/archives/6191
date: 2018-12-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-12-02-最小熵原理-四-物以类聚-之从图书馆到词向量.md
series:
  - [[最小熵原理]]
topics:
  - [[最小熵原理]]
  - [[互信息词向量]]
concepts:
  - [[最小熵原理]]
  - [[互信息词向量]]
  - [[点互信息PMI]]
methods:
  - [[用互信息内积构造词向量几何]]
evidence_spans:
  - ev::6191::图书馆成本模型
  - ev::6191::最小熵等于最大似然
  - ev::6191::Word2Vec推导
  - ev::6191::t-SNE联系
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-02-最小熵原理-四-物以类聚-之从图书馆到词向量.md
source_ids:
  - "6191"
status: draft
updated: 2026-06-10
null_evidence_reason: "Fourth article connecting cost minimization to word vectors; evidence spans to be formalized."
---

# 最小熵原理（四）："物以类聚"之从图书馆到词向量

## 文章核心问题

如何用最小成本（最小熵）原理统一理解词向量（Word2Vec）、t-SNE降维和图书馆排书规划？

## 主要结论

词向量、Word2Vec和t-SNE都可以从同一个最小成本模型导出：将对象编码为向量位置，使共现/相似对象在向量空间中靠近，从而降低访问/传输成本。Skip Gram模型的优化目标等价于最小化 $- \sum p(i,j)\log q(j|i)$，这既是最大似然也是最小熵。图书馆排书、词向量训练、t-SNE降维共享同一数学结构。

## 推导结构

1. 图书馆排书成本模型：$S = \sum p(i,j)[\|\boldsymbol{v}_i\| + \|\boldsymbol{v}_i - \boldsymbol{v}_j\|]$
2. 约束优化：去约束后，成本函数化为条件概率的交叉熵
3. 一般化：$f(\boldsymbol{v}_i,\boldsymbol{v}_j) = -\log(e^{\langle\boldsymbol{v}_i,\boldsymbol{v}_j\rangle}/Z_i)$
4. 对应Word2Vec的Skip Gram模型
5. 推广到t-SNE：换用不同的距离度量（t分布替代高斯）

## 关键公式

$$
S = -\sum_{i,j} p(i)p(j|i)\log\frac{e^{\langle\boldsymbol{v}_i,\boldsymbol{v}_j\rangle}}{Z_i} = -\sum_{i,j} p(i,j)\log q(j|i)
$$

此即Word2Vec Skip Gram的优化目标，也是最小熵（=最大似然）。

## 体现的方法

- [[用互信息内积构造词向量几何]] — 文章4从成本最小化角度重新推导了该方法，与现有"更别致的词向量模型"系列的理解互补
- [[用矩阵分解重写表示学习结构]] — 共享表示学习与矩阵拟合的生成动作

## 所属系列位置

系列第四篇，第三个具体应用——词向量的最小熵解释。

## 与其他文章的关系

- 为[[最小熵原理（六）]]的词向量维度选择提供了理论模型基础
- 与[[更别致的词向量模型]]系列紧密相关，提供了成本最小化视角
- 与[[SVD分解（三）：连Word2Vec都只不过是个SVD？]]连接
- 方法上重用[[用互信息内积构造词向量几何]]，用新的图书馆类比补充理解

## 原文证据锚点

- `ev::6191::图书馆成本模型` — 图书馆排书问题的数学建模
- `ev::6191::最小熵等于最大似然` — 从成本最小化导出最大似然/最小熵等价
- `ev::6191::Word2Vec推导` — Word2Vec的Skip Gram模型从最小熵导出
- `ev::6191::t-SNE联系` — t-SNE与Word2Vec的共有数学结构
