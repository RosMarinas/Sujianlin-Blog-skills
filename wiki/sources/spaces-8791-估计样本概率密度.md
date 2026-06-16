---
type: article_summary
title: "变分自编码器（八）：估计样本概率密度"
article_id: "8791"
source_url: https://spaces.ac.cn/archives/8791
date: 2021-12-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-12-09-变分自编码器-八-估计样本概率密度.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[VAE密度估计]]"
  - "[[重要性加权自编码器]]"
  - "[[变分自编码器]]"
methods:
  - "[[重要性加权估计]]"
evidence_spans:
  - ev::8791::混合模型
  - ev::8791::重要采样
  - ev::8791::训练目标
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-09-变分自编码器-八-估计样本概率密度.md
source_ids:
  - "8791"
status: draft
updated: 2026-06-09
---

## 一句话总结

从密度估计（最小化负对数似然）的视角出发，用混合模型 $q_\theta(x) = \int q_\theta(x|z)q(z)dz$ 作为万能密度近似器，用重要性采样解决高维积分估计的困难，单样本重要性采样退化为标准VAE，多样本重要性采样导出IWAE（Importance Weighted Autoencoder），全程无需ELBO。

## 核心问题

能否完全绕过变分推断和ELBO的推导，仅从密度估计（最大似然估计）出发，自然地推导出VAE的训练目标？

## 关键结论

1. 密度估计面临两个问题：（a）选择什么样的分布族 $q_\theta(x)$ 来拟合数据——混合模型 $q_\theta(x) = \int q_\theta(x|z)q(z)dz$ 具有万能近似能力；（b）如何高效估计积分——重要性采样解决高维空间中的采样效率问题。
2. 后验分布 $p_\theta(z|x)$ 在密度估计视角下不再是"真实后验的变分近似"，而纯粹是一个重要性采样分布（proposal distribution）。
3. 单样本重要性采样得标准VAE：$-\log q_\theta(x|z) - \log q(z) + \log p_\theta(z|x)$。
4. 多样本重要性采样得IWAE：$-\log(\frac{1}{M}\sum_{i=1}^M q_\theta(x|z_i)q(z_i)/p_\theta(z_i|x))$。
5. 解码器 $q_\theta(x|z)$ 的方差应控制得较小，使重要性采样分布 $p_\theta(z|x)$ 的方差也小，保证采样效率。

## 核心推导

1. 从MLE目标 $\min_\theta -\log q_\theta(x)$ 出发。
2. 将 $q_\theta(x)$ 表示为混合模型 $q_\theta(x) = \mathbb{E}_{z\sim q(z)}[q_\theta(x|z)]$。
3. 引入重要性分布 $p_\theta(z|x)$：$q_\theta(x) = \mathbb{E}_{z\sim p_\theta(z|x)}[q_\theta(x|z)q(z)/p_\theta(z|x)]$。
4. 单样本蒙特卡洛估计：$-\log(q_\theta(x|z)q(z)/p_\theta(z|x))$，即VAE。
5. $M$ 样本蒙特卡洛估计：$-\log(\frac{1}{M}\sum_{i=1}^M q_\theta(x|z_i)q(z_i)/p_\theta(z_i|x))$，即IWAE。

## 关键公式

$$\mathbb{E}_{x\sim \tilde{p}(x)}\left[-\log\left(\frac{1}{M}\sum_{i=1}^M q_\theta(x|z_i)\frac{q(z_i)}{p_\theta(z_i|x)}\right)\right],\quad z_1,\dots,z_M\sim p_\theta(z|x)$$

当 $M=1$ 时退化为标准VAE；$M>1$ 时为IWAE。

## 实验或案例

无。本文为纯粹的理论/方法论讨论，引用IWAE原论文（arXiv:1509.00519）的实验结果。

## 系列定位

本文是系列第8篇（也是最后一篇），将VAE的认知提升到了"元视角"——VAE不仅仅是一个生成模型或表示学习模型，本质上是一个密度估计器。这种视角统一了VAE和IWAE，绕过了ELBO的繁琐推导，揭示了VAE训练目标的最简来源。至此，本系列完成了从概率推导（1-3）到应用（4-5）到直觉（6-7）到元理论（8）的完整闭环。
