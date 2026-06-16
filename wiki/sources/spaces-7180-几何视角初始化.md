---
type: article_summary
title: 从几何视角来理解模型参数的初始化策略
article_id: "7180"
source_url: https://spaces.ac.cn/archives/7180
date: 2020-01-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-01-16-从几何视角来理解模型参数的初始化策略.md
series: []
topics:
  - 深度学习理论
  - 高维几何
concepts:
  - 高维随机向量正交性
  - Xavier初始化
  - 正交矩阵
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-01-16-从几何视角来理解模型参数的初始化策略.md
source_ids:
  - "7180"
status: draft
updated: 2026-06-10
---

## 总结

本文从高维几何视角解释Xavier初始化：高维空间中任意两个随机向量几乎垂直，因此从 $\mathcal{N}(0,1/n)$ 采样的 $n\times n$ 矩阵接近正交矩阵。正交矩阵保持向量模长不变，从而初始化时输出与输入保持相同尺度。相比传统概率统计推导更直观。

## 关键思想

- 推论1：高维空间中的任意两个随机向量几乎都是垂直的
- 推论2：从 $\mathcal{N}(0,1/n)$ 采样 $n^2$ 个数组成的矩阵接近正交矩阵
- 推论3：任意均值为0、方差为 $1/n$ 的分布采样的 $n\times n$ 矩阵都接近正交矩阵
- 正交矩阵 $\boldsymbol{W}^\top\boldsymbol{W}=\boldsymbol{I}$ 保持模长：$\|\boldsymbol{Wx}\|=\|\boldsymbol{x}\|$
- Xavier初始化方差 $\frac{2}{fan_{in}+fan_{out}}$ 是前向/反向传播的折中
- ReLU对应Kaiming初始化方差 $2/fan_{in}$

## 所属系列

[[深度学习理论]] — [[高维几何]]
