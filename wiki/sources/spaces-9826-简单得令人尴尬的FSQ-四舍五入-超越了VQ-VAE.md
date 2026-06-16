---
type: article_summary
title: 简单得令人尴尬的FSQ：“四舍五入”超越了VQ-VAE
article_id: "9826"
source_url: https://spaces.ac.cn/archives/9826
date: 2023-10-31
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-10-31-简单得令人尴尬的FSQ-四舍五入-超越了VQ-VAE.md
series: []
topics:
  - "[[向量量化优化]]"
concepts:
  - "[[有限标量量化]]"
  - "[[向量量化]]"
  - "[[直通估计器]]"
methods:
  - "[[基于不完全采样的量化逼近]]"
problem_patterns: []
evidence_spans:
  - ev::9826::VQ-VAE公式
  - ev::9826::STE梯度设计
  - ev::9826::VQ-VAE辅助Loss
  - ev::9826::EMA优化编码表
  - ev::9826::FSQ量化与STE
  - ev::9826::FSQ与VQ对比实验
  - ev::9826::编码表坍缩分析
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-31-简单得令人尴尬的FSQ-四舍五入-超越了VQ-VAE.md
source_ids:
  - "9826"
status: draft
updated: 2026-06-12
---

# 简单得令人尴尬的FSQ：“四舍五入”超越了VQ-VAE

## 文章核心问题

如何用无显式编码表（Codebook）查找的四舍五入量化算子（Finite Scalar Quantization, FSQ）代替复杂的向量量化（Vector Quantization, VQ-VAE），以根治编码表坍缩（Codebook Collapse）与难以优化的问题。

## 主要结论

- **FSQ核心思想**：连续空间的编码向量经 Sigmoid 缩放至 $[0, 1]$ 范围，并乘以 $L-1$。直接使用四舍五入 $\text{Round}$ 操作得到离散的整数等级。
- **无需辅助Loss**：由于FSQ利用直通估计器（Straight-Through Estimator, STE）且不需要在多维空间中移动聚类中心，因此去掉了VQ-VAE复杂的辅助损失函数 $\beta\|e_k - \text{sg}[z]\|^2 + \gamma\|z - \text{sg}[e_k]\|^2$。
- **与VQ的维度和效果差异**：
  - VQ 将高维向量分类为 $K$ 个簇；FSQ 则将 $d$ 维隐空间向量中的每一维拆分成 $L$ 个等级，获得共 $L^d$ 个组合。
  - 在编码表规模 $K < 1000$ 时，VQ 效果优于 FSQ，因为低维 $d$ 会成为严重瓶颈；在 $K > 1000$ 且编码器/解码器足够复杂时，FSQ 的效果显著超越 VQ，能够充分且均衡地利用编码容量。
- **优缺点机制分析**：VQ-VAE 容易出现聚类中心的“赢者通吃”而导致坍缩，而 FSQ 没有显式的多中心聚类，直接在坐标轴维度量化，因此天然免疫编码表坍缩。

## 推导结构

1. **回顾 VQ-VAE**：详述量子化自编码器的重构与前向流程，突出 $\text{argmin}$ 计算的不可导性。
2. **分析直通估计（STE）**：解释如何利用 $\text{stop_gradient}$（$\text{sg}$）技巧构建前向使用量化向量、反向传导连续向量梯度的机制。
3. **解释辅助Loss的必要性**：剖析为什么 VQ-VAE 必须依赖辅助 Loss（包含阻断梯度的两部分）或指数滑动平均（EMA）来逼近聚类中心。
4. **引入 FSQ**：给出基于 Sigmoid 及 $\text{Round}$ 算子的多维标量分解量化公式，并以 $\text{sg}$ 构建其 STE 梯度。
5. **对比分析与思考**：通过分类器（VQ）与打分器（FSQ）的理论对比，指出神经网络拟合力对 FSQ 低维度的代偿作用，以及 VQ 在硬指派 $\text{argmin}$ 下“赢者通吃”导致坍缩的物理根源。

## 关键公式

- **VQ-VAE 状态与 Loss 公式**：
  $$
  \begin{aligned}
  z_q =&\, z + \text{sg}[e_k - z],\quad k = \mathop{\text{argmin}}_{i\in\{1,2,\cdots,K\}} \Vert z - e_i\Vert \\
  \mathcal{L} =&\, \Vert x - \hat{x}\Vert^2 + \beta\Vert e_k - \text{sg}[z]\Vert^2 + \gamma\Vert z - \text{sg}[e_k]\Vert^2
  \end{aligned}
  $$
- **FSQ 标量量化前向公式**：
  $$
  \text{FSQ}(t)\triangleq \text{Round}[(L-1)\sigma(t)]
  $$
- **FSQ 梯度直通估计 (STE) 恒等变形**：
  $$
  \text{FSQ}(z) = (L-1)\sigma(z) + \text{sg}\big[\text{Round}[(L-1)\sigma(z)] - (L-1)\sigma(z)\big]
  $$

## 体现的方法

- **基于不完全采样的量化逼近**：用均匀分级标量投影取代连续空间的距离搜索聚类。
- **直通梯度估计 (STE)**：利用数学上非严格的恒等代数替换，强制让不可导模块具备恒等式的后向传播通路。

## 所属系列位置

独立研究文章，属于向量量化与自编码器离散化机制的探讨。

## 与其他文章的关系

- 前置基础建立在 [VQ-VAE的简明介绍](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/向量量化.md) (6760) 与直通估计 (10489) 之上。
- 与 [Transformer-VQ](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Transformer-VQ.md) (9862) 中硬 VQ 机制造成的梯度次优估计和瓶颈问题相互印证。

## 原文证据锚点

- **ev::9826::VQ-VAE公式**: 第38-46行，详细给出了带有直通梯度的 VQ-VAE 前向重构与 Loss 计算方程。
- **ev::9826::STE梯度设计**: 第54-62行，推导了直通估计器（STE）的工作原理与自定义梯度技巧。
- **ev::9826::VQ-VAE辅助Loss**: 第66-78行，分析了辅助 Loss 中两项的物理意义与权重衰减机制。
- **ev::9826::EMA优化编码表**: 第80-84行，介绍了利用指数移动平均（EMA）在线更新聚类中心的代替方案。
- **ev::9826::FSQ量化与STE**: 第90-102行，给出了多维标量 FSQ 表达式与通过 stop_gradient 表达的 STE 计算恒等式。
- **ev::9826::FSQ与VQ对比实验**: 第107-118行，通过实验图像对比说明在不同编码表大小下两者的优劣曲线。
- **ev::9826::编码表坍缩分析**: 第122-130行，从 argmin 优化的“赢者通吃”特性深度剖析了聚类坍缩的几何根源，从而解释了 FSQ 成功的本质原因。
