---

type: concept
title: DDPM (去噪扩散概率模型)
aliases:
- Denoising Diffusion Probabilistic Model
definition: 一种生成模型，通过逐步加噪（前向扩散）和逐步去噪（反向生成）的过程，学习从随机噪声到数据样本的映射。DDPM将生成过程分解为T步马尔可夫链，每一步用简单正态分布建模微小变化，最终实现高质量的生成效果。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-06-13-生成扩散模型漫谈-一-DDPM-拆楼-建楼.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-07-06-生成扩散模型漫谈-二-DDPM-自回归式VAE.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-07-19-生成扩散模型漫谈-三-DDPM-贝叶斯-去噪.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-07-27-生成扩散模型漫谈-四-DDIM-高观点DDPM.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-08-03-生成扩散模型漫谈-五-一般框架之SDE篇.md
source_ids:
- '9119'
- '9152'
- '9164'
- '9181'
- '9209'
prerequisites:
- '[[前向扩散过程]]'
- '[[反向去噪过程]]'
- '[[方差保持约束]]'
- '[[累积信号率]]'
- '[[噪声预测网络]]'
equivalent_forms: []
direct_consequences:
- '[[DDIM]]'
related_formulas: []
related_methods:
- '[[方差消减技术]]'
series:
- '[[生成扩散模型漫谈]]'
evidence_spans:
- ev::9119::拆楼建楼
- ev::9152::联合散度
- ev::9164::去噪过程
status: draft
updated: '2026-06-12'
---
# DDPM (Denoising Diffusion Probabilistic Models)

## 定义
DDPM 是一种基于热力学非平衡态理论的生成扩散模型。它通过定义一个渐进的加噪前向过程和一个对应的去噪反向过程来学习复杂数据分布。

## 核心原理
- **前向加噪过程**：通过马尔可夫链向数据逐步注入高斯噪声，直到数据完全退化为标准正态分布：
  $$q(x_t | x_{t-1}) = \mathcal{N}(x_t; \sqrt{1-eta_t}x_{t-1}, eta_t I)$$
- **反向去噪过程**：利用神经网络预测每一步的噪声，从而逐步还原出清晰的图像。损失函数主要优化噪声预测网络与真实噪声之间的均方误差：
  $$\mathcal{L}_{\text{simple}} = \mathbb{E}_{t, x_0, \epsilon} \left[ \|\epsilon - \epsilon_\theta(x_t, t)\|^2 \right]$$
