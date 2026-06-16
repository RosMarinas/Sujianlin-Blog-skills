---
type: concept
title: 重参数化技巧 (VAE中的)
aliases:
- Reparameterization Trick
- 重参数技巧
definition: 将从正态分布 $\mathcal{N}(\mu,\sigma^2)$ 中采样的非可微操作转化为从标准正态分布 $\mathcal{N}(0,I)$
  中采样后通过可微变换 $Z = \mu + \varepsilon \times \sigma$ 获得样本，使得梯度可以流过采样操作并更新 $\mu$ 和 $\sigma$
  参数。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-03-18-变分自编码器-一-原来是这么一回事.md
- Data/Spaces_ac_cn/markdown/Big-Data/2018-04-03-变分自编码器-三-这样做为什么能成.md
source_ids:
- '5253'
- '5383'
prerequisites: []
equivalent_forms: []
direct_consequences:
- VAE编码器可训练的基石
related_formulas: []
related_methods:
- '[[VAE联合分布最小化]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::5253::重参数技巧
- ev::5383::重参之神
status: draft
updated: '2026-06-12'
---

# 重参数化技巧 (Reparameterization Trick)

**重参数化技巧**是VAE训练中的关键使能技术，解决了"采样操作不可导"的核心障碍。

## 数学原理

标准正态分布的微分形式为 $\frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}\varepsilon^2}d\varepsilon$。从 $\mathcal{N}(\mu,\sigma^2)$ 中采样 $z$ 等价于：

$$\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(z-\mu)^2}{2\sigma^2}}dz = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{z-\mu}{\sigma})^2}d(\frac{z-\mu}{\sigma})$$

因此采样的随机性来自固定的标准正态噪声 $\varepsilon\sim\mathcal{N}(0,1)$，模型输出的 $z$ 通过可微变换获得：

$$z = \mu + \varepsilon \times \sigma$$

## 在VAE中的作用

如果没有重参数化技巧，采样操作在计算图中是一个"黑箱"——输出的样本值 $z$ 看起来像常向量，其梯度 $\partial z/\partial\mu$ 和 $\partial z/\partial\sigma$ 为零，编码器参数无法更新。重参数化将随机性外化到输入噪声 $\varepsilon$，使 $\mu$ 和 $\sigma$ 的梯度路径显式化，是VAE训练的关键使能技术。

## 与扩散模型中重参数化技巧的区别

在扩散模型中，"重参数化技巧"通常指将生成模型 $\mu(x_t)$ 参数化为从 $x_t$ 中减去预测噪声的形式（噪声预测参数化）。VAE中的重参数化技巧形式更简洁，核心是从参数分布采样转为从固定分布采样后做确定性变换。