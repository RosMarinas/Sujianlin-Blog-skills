---
type: concept
title: 积分梯度
definition: "一种深度网络归因解释方法，通过沿基准输入到目标输入的直线路径对梯度进行积分来分配特征重要性。"
sources:
  - wiki/sources/spaces-7533-积分梯度.md
source_ids:
  - "7533"
aliases: [Integrated Gradients, IG, 积分梯度法]
tags: [visualization, interpretability, attribution, saliency]
related_methods: [归因方法]
related_sources: [spaces-7533-积分梯度]
status: draft
updated: 2026-06-12
---
## Definition

积分梯度（Integrated Gradients）是一种神经网络可视化/归因方法，由 Sundararajan et al. (2017) 提出。它通过沿输入 $x$ 到参照背景 $\bar{x}$ 的路径对梯度进行积分，来度量输入各分量对模型决策的重要性。

## Motivation

朴素梯度法 $|\nabla_x F(x)|_i$ 存在缺陷：梯度可被"操控"（对抗训练推动 $\|\nabla_x F(x)\|^2 \to 0$），且在饱和区（如ReLU负半轴）梯度为0。积分梯度通过路径积分解决了这一问题。

## Mathematical Formulation

设 $\gamma(\alpha): [0,1] \to \mathbb{R}^n$ 为连接 $x$ 和 $\bar{x}$ 的路径，$\gamma(0)=x, \gamma(1)=\bar{x}$，则积分恒等式：

$$
F(\bar{x}) - F(x) = \sum_i \int_0^1 [\nabla_\gamma F(\gamma(\alpha))]_i [\gamma'(\alpha)]_i d\alpha
$$

取直线路径 $\gamma(\alpha) = (1-\alpha)x + \alpha\bar{x}$，重要性度量：

$$
\text{IG}_i(x) = \left| [\bar{x} - x]_i \int_0^1 \nabla_\gamma F(\gamma(\alpha))|_{\gamma(\alpha) = (1-\alpha)x + \alpha\bar{x}} d\alpha \right|
$$

相比于朴素梯度 $|\nabla_x F(x)|_i$，积分梯度使用路径上所有点的梯度平均，不受单点梯度为零的限制。

## Discrete Approximation

实际计算中采用离散近似：
$$
\text{IG}_i(x) \approx \left| \left[ \frac{1}{n}\sum_{k=1}^n \nabla_\gamma F(\gamma(\alpha))|_{\alpha=k/n} \right]_i [\bar{x} - x]_i \right|
$$

## Applications

- CV任务：精确定位图像中的重要像素区域
- NLP任务：识别对分类决策关键的词语/Token
- 模型调试：发现模型的决策偏差（如情感分类中的"负面检测"倾向）

## References

- 苏剑林. "积分梯度：一种新颖的神经网络可视化方法". 科学空间, 2020. [spaces-7533]
- Sundararajan et al., "Axiomatic Attribution for Deep Networks", ICML 2017.
