---
type: article_summary
title: 生成扩散模型漫谈（二十九）：用DDPM来离散编码
article_id: "10711"
source_url: https://spaces.ac.cn/archives/10711
date: 2025-02-14
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2025-02-14-生成扩散模型漫谈-二十九-用DDPM来离散编码.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[离散扩散自编码器]]"
  - "[[低维流形假设]]"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-02-14-生成扩散模型漫谈-二十九-用DDPM来离散编码.md
source_ids:
  - "10711"
status: draft
updated: 2026-06-09
---

# 生成扩散模型漫谈（二十九）：用DDPM来离散编码

## 一句话总结

本文介绍DDCM（Denoising Diffusion Codebook Models, arXiv:2502.01189），将DDPM采样中的高斯噪声限制在一个预采样的有限Codebook上，结合条件生成思路，免训练地将预训练DDPM转化为类似VQ-VAE的离散自编码器。

## 核心问题

能否在不额外训练的情况下，将预训练好的DDPM变成一个离散编码器？能否让DDPM像VQVAE一样将图像编码为离散ID序列并重构？

## 关键结论

1. 将DDPM每步的噪声$\boldsymbol{\varepsilon}_t$限制在有限Codebook$\mathcal{C}_t$上（$K=64$即可几乎无损），生成质量基本不变。
2. 通过条件生成视角，提出argmax编码规则$\boldsymbol{\varepsilon}_t = \text{argmax}_{\boldsymbol{\varepsilon}\in\mathcal{C}_t} \boldsymbol{\varepsilon}\cdot(\boldsymbol{x}_0 - \bar{\boldsymbol{\mu}}(\boldsymbol{x}_t))$，将图像编码为$T$个离散ID。
3. 重要性采样修正：为避免$K\to\infty$时退化为确定性变换，应使用Softmax加权采样而非简单argmax。
4. DDCM编码天然是1D序列（长度$T$），比VQ/FSQ的2D编码更便于自回归建模。

## 核心推导

### 从DDPM条件后验出发
$$
p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t, \boldsymbol{x}_0) = \mathcal{N}\left(\boldsymbol{x}_{t-1}; \frac{\alpha_t\bar{\beta}_{t-1}^2}{\bar{\beta}_t^2}\boldsymbol{x}_t + \frac{\bar{\alpha}_{t-1}\beta_t^2}{\bar{\beta}_t^2}\boldsymbol{x}_0, \frac{\bar{\beta}_{t-1}^2\beta_t^2}{\bar{\beta}_t^2}\boldsymbol{I}\right)
$$

将其均值分解为无条件DDPM均值$\boldsymbol{\mu}(\boldsymbol{x}_t)$加修正项$\frac{\bar{\alpha}_{t-1}\beta_t^2}{\bar{\beta}_t^2}(\boldsymbol{x}_0 - \bar{\boldsymbol{\mu}}(\boldsymbol{x}_t))$。

### 编码规则推导
修正项需要由Codebook噪声补偿，得到最小化问题：在等模长假设下简化为argmax内积。

### 重要性采样修正
为了满足$\lim_{K\to\infty}$ DDCM = DDPM，应使用Softmax概率采样而非argmax。

## 关键公式

| 公式 | 含义 |
|------|------|
| $\boldsymbol{x}_{t-1} = \boldsymbol{\mu}(\boldsymbol{x}_t) + \sigma_t \boldsymbol{\varepsilon}_t,\quad \boldsymbol{\varepsilon}_t \sim \mathcal{C}_t$ | DDCM采样（有限Codebook） |
| $\boldsymbol{\varepsilon}_t = \text{argmax}_{\boldsymbol{\varepsilon}\in\mathcal{C}_t} \boldsymbol{\varepsilon}\cdot(\boldsymbol{x}_0 - \bar{\boldsymbol{\mu}}(\boldsymbol{x}_t))$ | 编码选择规则 |
| $p(\boldsymbol{\varepsilon})\propto \exp\left(-\frac{1}{2}\|\boldsymbol{\varepsilon} - \frac{\bar{\alpha}_{t-1}\beta_t^2}{\bar{\beta}_t^2\sigma_t}(\boldsymbol{x}_0 - \bar{\boldsymbol{\mu}}(\boldsymbol{x}_t))\|^2\right)$ | 重要性采样分布 |
| $\boldsymbol{\varepsilon}_t = \text{argmax}_{\boldsymbol{\varepsilon}\in\mathcal{C}_t} \boldsymbol{\varepsilon}\cdot\nabla_{\boldsymbol{x}_t} \log p(\boldsymbol{y}|\boldsymbol{x}_t)$ | Classifier-Guidance扩展 |

## 实验或案例

- $K=64$时FID基本追平连续DDPM
- 即使$K=2$质量损失也很小（但每步Codebook必须独立）
- 作者在个人模型上复现了相近效果
- 参考实现：https://github.com/bojone/Keras-DDPM/blob/main/ddcm.py

## 系列定位

本文是系列中从加速生成切换到离散编码的独辟蹊径之作。文章31（JiT）引用DDCM中"噪声不可压缩"的实验经验，作为"数据在低维流形上"论据的支持。
