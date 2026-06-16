---
type: topic
title: SVD矩阵分解
aliases:
  - SVD representation and differentiation
scope: SVD 在表示学习解释、低维矩阵分解、聚类语义和可导矩阵层中的认知用法。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-01-15-SVD分解-一-自编码器与人工智能.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-01-26-SVD分解-二-为什么SVD意味着聚类.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-02-23-SVD分解-三-连Word2Vec都只不过是个SVD.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
  - "4208"
  - "4216"
  - "4233"
  - "10878"
series:
  - [[SVD分解]]
  - [[低秩近似之路]]
concepts:
  - [[奇异值分解]]
  - [[线性自编码器-SVD等价]]
  - [[矩阵分解聚类解释]]
  - [[SVD可导性]]
formulas:
  - [[线性自编码器矩阵分解公式]]
  - [[SVD奇异值微分公式]]
  - [[SVD等效前向梯度公式]]
propositions:
  - [[线性自编码器可视为SVD式低维重建]]
  - [[SVD分解具有聚类语义]]
  - [[SVD可导需要非零奇异值互异]]
methods:
  - [[用矩阵分解重写表示学习结构]]
  - [[用等效前向表达保留SVD梯度]]
problem_patterns:
  - [[把表示学习模型改写为矩阵分解问题]]
reading_paths:
  - [[SVD矩阵分解阅读路径]]
status: draft
updated: 2026-06-10
---

# SVD矩阵分解

## 主题边界

本主题把早期 SVD 表示学习解释与后来的低秩近似/SVD 求导连接起来。它不替代 [[低秩近似]] 主题中的误差最优定理，而是补充“为什么 SVD 是一种表示学习结构”的认知层。
