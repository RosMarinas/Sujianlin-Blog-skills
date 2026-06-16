---
type: concept
title: "Johnson-Lindenstrauss引理"
aliases: ["JL引理", "JL Lemma"]
definition: "说明高维空间中的 $N$ 个向量可以通过随机线性投影降维至 O(log N) 维，且使得任意两点间相对欧氏距离的误差保证被控制在一个较小范围内的定理。"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-06-28-维度灾难-之Hubness现象浅析.md"
source_ids: ["8679", "8706"]
evidence_spans: []
status: draft
null_evidence_reason: "Concept created via batch script, detailed evidence span defered."
updated: "2026-06-12"
---

# Johnson-Lindenstrauss引理

## 定义
说明高维空间中的 $N$ 个向量可以通过随机线性投影降维至 O(log N) 维，且使得任意两点间相对欧氏距离的误差保证被控制在一个较小范围内的定理。

## 关键性质
JL引理给出了一个存在性保证：对于任意 $N$ 个点的集合和任意误差 $\epsilon \in (0, 1)$，存在一个从 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的线性映射，其中 $m = O(\epsilon^{-2} \log N)$，使得降维后所有点对距离的变化不超过 $(1 \pm \epsilon)$ 倍。随机高斯投影矩阵以高概率满足此性质。JL引理在理论上是许多近似最近邻搜索、随机投影降维和注意力头大小分析的理论基础，其维度下界 $n > 8.33 \log N$ 是苏剑林博客中多次讨论的实用经验公式。
