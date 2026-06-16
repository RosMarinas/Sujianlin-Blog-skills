---
type: concept
definition: Johnson-Lindenstrauss引理：嵌入n个向量到低维空间时，只需要 O(log n) 维就能近似保持向量间的距离关系。具体地，n个向量约需要
  8 log n 维空间。
aliases:
- Johnson-Lindenstrauss Lemma
- JL Lemma
- Dimension Reduction Bound
status: draft
updated: '2026-06-12'
title: JL引理
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


# JL引理

Johnson-Lindenstrauss引理：嵌入n个向量到低维空间时，只需要 O(log n) 维就能近似保持向量间的距离关系。具体地，n个向量约需要 8 log n 维空间。

## 在注意力机制中的应用

- 解释Q、K投影维度的选择：n=512时 8 log n ≈ 50，接近BERT的key_size=64
- 说明多头注意力的必要性：用多个低维头替代单个高维头
- 联系熵不变性Attention：理想投影维度 d_n = λ log n，固定d后用 d_n/d 补偿

## 相关概念

- [[熵不变性]]
- [[共享Embedding]]
- [[词向量模长ICF解释]]
- [[注意力机制]]