---
type: example
title: spaces-9889-极简线性Attention稀疏度下限推导
article_id: 9889
article: |
  [spaces-9889-注意力机制真的可以“集中注意力”吗](wiki/sources/spaces-9889-注意力机制真的可以“集中注意力”吗.md)
section: 极简线性
claim: 极简线性Attention的注意力权重稀疏度存在较高的理论下限无法实现极端集中的聚焦
notation_mapping:
  S_a: Sparsity metric value
  gamma: Standard deviation scaled query norm
  beta: Mean scaled query norm
steps:
  - 假定特征维度 $d$ 较大，Key 向量服从各向同性的高斯分布：$\boldsymbol{k}\sim\mathcal{N}(\boldsymbol{\mu},\sigma^2\boldsymbol{I})$。
  - 对于不使用激活函数 $f=\text{identical}$ 的极简线性 Attention，写出稀疏度公式 $S(\boldsymbol{a})$ 的高斯积分表示。
  - 使用数学软件（如 Mathematica）计算关于标量高斯分布特征的一维积分，得出精确闭式解：$S(\boldsymbol{a}) = \frac{\sqrt{2/\pi}\gamma e^{-\beta^2/(2\gamma^2)} + \beta \text{erf}(\beta/(\sqrt{2}\gamma))}{\sqrt{\beta^2+\gamma^2}}$。
  - 对其取相对于特征值 $\beta$ 和 $\gamma$ 的变化范围进行绘图，可以看出稀疏度函数值始终处于 $[0.6, 1.0]$ 范围。
  - 这证明了由于线性点积的极高非稀疏性，其无论参数如何缩放都无法让注意力权重聚焦到单个 token，导致处理长程信息时容易引起信息的过度平滑和均值化。
used_concepts:
  - [attention_sparsity](wiki/concepts/attention_sparsity.md)
source_span: ev::9889::linear_sparsity_proof
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
source_ids:
  - 9889
status: draft
updated: 2026-06-12
---

# spaces-9889-极简线性Attention稀疏度下限推导

## Claim
极简线性Attention的注意力权重稀疏度存在较高的理论下限无法实现极端集中的聚焦

## Section
极简线性

## Notation Mapping
- $S_a$: Sparsity metric value
- $\gamma$: Standard deviation scaled query norm
- $\beta$: Mean scaled query norm

## Steps
1. 假定特征维度 $d$ 较大，Key 向量服从各向同性的高斯分布：$\boldsymbol{k}\sim\mathcal{N}(\boldsymbol{\mu},\sigma^2\boldsymbol{I})$。
2. 对于不使用激活函数 $f=\text{identical}$ 的极简线性 Attention，写出稀疏度公式 $S(\boldsymbol{a})$ 的高斯积分表示。
3. 使用数学软件（如 Mathematica）计算关于标量高斯分布特征的一维积分，得出精确闭式解：$S(\boldsymbol{a}) = \frac{\sqrt{2/\pi}\gamma e^{-\beta^2/(2\gamma^2)} + \beta \text{erf}(\beta/(\sqrt{2}\gamma))}{\sqrt{\beta^2+\gamma^2}}$。
4. 对其取相对于特征值 $\beta$ 和 $\gamma$ 的变化范围进行绘图，可以看出稀疏度函数值始终处于 $[0.6, 1.0]$ 范围。
5. 这证明了由于线性点积的极高非稀疏性，其无论参数如何缩放都无法让注意力权重聚焦到单个 token，导致处理长程信息时容易引起信息的过度平滑和均值化。