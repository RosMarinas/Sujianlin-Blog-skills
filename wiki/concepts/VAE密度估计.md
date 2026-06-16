---
type: concept
title: VAE密度估计
aliases:
- VAE as Density Estimator
- VAE密度估计视角
- 变分自编码器概率密度估计
definition: 将VAE视为一种概率密度估计工具，使用混合模型 $q_\theta(x) = \int q_\theta(x|z)q(z)dz$ 来拟合数据分布，通过重要性采样高效估计高维积分，直接从最大似然估计推导出VAE训练目标而无需ELBO。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-12-09-变分自编码器-八-估计样本概率密度.md
source_ids:
- '8791'
prerequisites:
- '[[变分自编码器]]'
- '[[混合模型]]'
- '[[重要性采样]]'
equivalent_forms: []
direct_consequences:
- '[[重要性加权自编码器]]'
related_formulas:
- '[[IWAE损失函数]]'
related_methods:
- '[[重要性加权估计]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::8791::混合模型
- ev::8791::重要采样
status: draft
updated: '2026-06-12'
---

## 定义

VAE密度估计视角是将变分自编码器重新理解为一种概率密度估计方法。其核心思想包含三个步骤：

1. **混合模型构造**：用 $q_\theta(x) = \int q_\theta(x|z)q(z)dz$ 作为待拟合的密度函数。其中 $q(z)$ 是简单先验（如标准正态分布），$q_\theta(x|z)$ 是以 $z$ 为条件的简单分布。这种混合模型具有万能近似能力（类似于高斯混合模型扩展到无限分量）。

2. **重要性采样估计**：直接估计 $\mathbb{E}_{z\sim q(z)}[q_\theta(x|z)]$ 在高维空间效率极低（维度灾难）。引入重要性分布 $p_\theta(z|x)$ 将采样空间从"漫无目的的 $q(z)$"缩小到"针对 $x$ 的 $p_\theta(z|x)$"：
   $$q_\theta(x) = \mathbb{E}_{z\sim p_\theta(z|x)}\left[q_\theta(x|z)\frac{q(z)}{p_\theta(z|x)}\right]$$

3. **最大似然训练**：直接将上述估计代入负对数似然目标：
   - $M=1$ 个重要性样本：$-\log q_\theta(x|z) - \log q(z) + \log p_\theta(z|x)$，即标准VAE。
   - $M>1$ 个重要性样本：$-\log(\frac{1}{M}\sum_i q_\theta(x|z_i)q(z_i)/p_\theta(z_i|x))$，即IWAE。

## 关键见解

- 在此视角下，后验 $p_\theta(z|x)$ 不再需要被解释为"真实后验的变分近似"，而是纯粹的重要性采样分布（proposal distribution）。
- 推导完全绕过了ELBO和变分推断的所有繁琐步骤。
- 该方法对 $q_\theta(x|z)$ 的方差有要求：方差应较小，保证只有少量 $z$ 能产生有意义的贡献，从而让重要性采样高效。