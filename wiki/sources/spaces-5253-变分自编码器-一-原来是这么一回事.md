---
type: article_summary
title: "变分自编码器（一）：原来是这么一回事"
article_id: "5253"
source_url: https://spaces.ac.cn/archives/5253
date: 2018-03-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-03-18-变分自编码器-一-原来是这么一回事.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[变分自编码器]]"
  - "[[后验分布假设]]"
  - "[[重参数化技巧 (VAE中的)]]"
methods:
  - "[[高斯噪声正则化]]"
evidence_spans:
  - ev::5253::VAE初现
  - ev::5253::分布标准化
  - ev::5253::重参数技巧
  - ev::5253::本质是什么
  - ev::5253::条件VAE
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-03-18-变分自编码器-一-原来是这么一回事.md
source_ids:
  - "5253"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文从直觉出发，将VAE解释为在普通自编码器的编码结果上添加高斯噪声并施加KL正则化的模型，核心洞见是VAE假设每个样本的后验分布 $p(Z|X_k)$ 为正态分布，而非先验 $p(Z)$ 为正态分布，纠正了常见教程中的误解。

## 核心问题

变分自编码器（VAE）究竟是什么？它和普通自编码器有何本质区别？为什么需要KL散度作为额外的损失项？VAE的"变分"从何而来？能否利用标签信息实现条件生成？

## 关键结论

- VAE的核心假设是每个样本 $X_k$ 的后验分布 $p(Z|X_k)$ 为正态分布（专属正态分布），而非先验分布 $p(Z)$ 为正态分布。先验 $p(Z)$ 的正态性是通过对所有后验分布施加标准化后自然导出的推论。
- KL散度正则化迫使每个后验分布向标准正态分布对齐，从而使得边缘先验 $p(Z)$ 成为标准正态分布，保证生成能力。
- VAE本质上就是在自编码器编码结果上添加高斯噪声，KL loss充当对编码结果的正则项——迫使编码结果均值为0。
- 重构loss（希望无噪声）与KL loss（希望有高斯噪声）天然相互对抗，其动态平衡机制类似GAN内部的对抗过程。
- 高斯分布是VAE中KL散度计算的必然选择，因为均匀分布会在 $p(x)\neq0$ 且 $q(x)=0$ 的区域导致KL散度无穷大。
- 通过修改KL loss可以将标签信息融入VAE中（CVAE），使同一类样本的后验分布指向类专属均值 $\mu^Y$ 而非零均值。

## 核心推导

**KL散度闭式推导**（一元情况）：从KL散度定义出发
$$KL(\mathcal{N}(\mu,\sigma^2)\|\mathcal{N}(0,1)) = \int \frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/2\sigma^2} \left(\log \frac{e^{-(x-\mu)^2/2\sigma^2}/\sqrt{2\pi\sigma^2}}{e^{-x^2/2}/\sqrt{2\pi}}\right)dx$$

将log内项展开为 $-\log\sigma^2 + x^2 - (x-\mu)^2/\sigma^2$（乘以1/2因子），积分分解为三项：
1. $-\log\sigma^2$ 乘概率密度积分 = $-\log\sigma^2$
2. 正态分布二阶矩 $\mathbb{E}[x^2] = \mu^2 + \sigma^2$
3. $-\mathbb{E}[(x-\mu)^2]/\sigma^2 = -1$

求和得 $\frac{1}{2}(-\log\sigma^2 + \mu^2 + \sigma^2 - 1)$。

**重参数化技巧**：从 $\mathcal{N}(\mu,\sigma^2)$ 中采样 $Z$ 等价于从 $\mathcal{N}(0,I)$ 中采样 $\varepsilon$ 后计算 $Z = \mu + \varepsilon \times \sigma$，使采样操作可导。

## 关键公式

- $(2)$: $p(Z) = \sum_X p(Z|X)p(X) = \mathcal{N}(0,I)$ —— 所有后验趋向标准正态时，边缘先验即标准正态
- $(4)$: $\mathcal{L}_{\mu,\sigma^2} = \frac{1}{2} \sum_{i=1}^d (\mu_{(i)}^2 + \sigma_{(i)}^2 - \log \sigma_{(i)}^2 - 1)$ —— 多元高斯与标准正态的KL散度闭式
- $(6)$: $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-(z-\mu)^2/2\sigma^2}dz = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{z-\mu}{\sigma})^2}d(\frac{z-\mu}{\sigma})$ —— 重参数化变换
- $(8)$: $\mathcal{L}_{\mu,\sigma^2} = \frac{1}{2} \sum_{i=1}^d [(\mu_{(i)}-\mu^Y_{(i)})^2 + \sigma_{(i)}^2 - \log \sigma_{(i)}^2 - 1]$ —— CVAE类条件KL损失

## 实验或案例

无定量实验。展示了一个简单的CVAE生成效果：控制生成数字9的多种样式，并观察数字9向7过渡的定性结果，验证了条件VAE的基本有效性。

## 系列定位

本文是系列的奠基之作，以最直观的方式解释VAE的基本结构，刻意规避复杂的贝叶斯理论框架。核心贡献是：(1) 纠正了"VAE假设 $p(Z)$ 是正态分布"的常见误解；(2) 从KL散度闭式推导给出了标准VAE损失函数；(3) 引入重参数化技巧解决梯度流问题；(4) 将VAE解释为"自编码器 + 高斯噪声 + KL正则化"的直观模型。后续文章在此基础上从贝叶斯视角做严格推导，并进一步解释VAE为何有效。
