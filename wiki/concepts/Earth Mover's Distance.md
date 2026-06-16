---
type: concept
title: Earth Mover's Distance
aliases:
- 推土机距离
- Wasserstein距离
- EMD
- Wasserstein distance
definition: 两个概率分布之间最优传输成本的最小值，通过线性规划求解运输方案。
standard_notation: $\mathcal{C}[p, \tau] = \inf_{\gamma \in \Pi[p, \tau]} \sum_{i,j}
  \gamma_{i,j} c_{i,j}$
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
- Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
source_ids:
- '7388'
- '9797'
prerequisites:
- - - concept::最优传输理论
related_formulas:
- - - formula::Wasserstein距离公式
related_methods:
- - - method::WMD文本相似度计算
- - - method::WRD文本相似度计算
- - - method::EMO损失函数
status: deprecated
replaced_by: '[[concept::Wasserstein距离]]'
updated: '2026-06-12'
deprecation_reason: Merged into concept::Wasserstein距离 as part of Pass A node boundary
  repair.
---

# Earth Mover's Distance

Wasserstein距离（又称推土机距离/EMD）度量两个概率分布之间的差异，通过求解线性规划找到从分布 $p$ 到 $q$ 的最优传输方案 $\gamma_{i,j}$，最小化 $\sum_{i,j} \gamma_{i,j} d_{i,j}$。在NLP中用于文本向量序列相似度比较（WMD/WRD）和损失函数设计（EMO）。