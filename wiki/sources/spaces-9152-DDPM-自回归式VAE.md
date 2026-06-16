---
type: article_summary
title: "生成扩散模型漫谈（二）：DDPM = 自回归式VAE"
article_id: "9152"
source_url: https://spaces.ac.cn/archives/9152
date: 2022-07-06
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-07-06-生成扩散模型漫谈-二-DDPM-自回归式VAE.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[DDPM]]"
  - "[[前向扩散过程]]"
  - "[[反向去噪过程]]"
  - "[[方差保持约束]]"
  - "[[累积信号率]]"
  - "[[噪声预测网络]]"
  - "[[重参数化技巧]]"
methods:
  - "[[方差消减技术]]"
evidence_spans:
  - ev::9152::联合散度
  - ev::9152::分而治之
  - ev::9152::超参设置
  - ev::9152::参考实现
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-07-06-生成扩散模型漫谈-二-DDPM-自回归式VAE.md
source_ids:
  - "9152"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文从变分自编码器（VAE）的视角重新推导DDPM，将其理解为编码和解码均分解为T步的自回归式VAE，通过最小化联合分布KL散度得到与第一篇相同的损失函数，并提供了Keras实现指南与实战经验。

## 核心问题

如何将DDPM置于更广阔的生成模型谱系中进行理解？DDPM与传统VAE之间有何深层联系？DDPM在实践中需要哪些实现技巧？

## 关键结论

- DDPM本质上是一个VAE：其多步编码-解码过程恰好是VAE框架的推广，以联合分布KL散度 $KL(p\|q)$ 为优化目标。
- 多步分解用简单正态分布建模微小变化，类似于分段线性函数逼近复杂曲线，理论上可以突破单步VAE的拟合能力限制。
- DDPM没有编码能力：前向分布 $p(x_T|x_0)$ 收敛到与 $x_0$ 无关的标准正态分布（要求 $\bar{\alpha}_T \approx 0$），因此DDPM是纯生成模型，不适合表示学习。
- DDPM可视为极度简化的NVAE：NVAE使用非马尔可夫递归隐变量，DDPM使用马尔可夫链和参数共享。
- 实践中，损失函数必须用欧氏距离平方而非MSE，归一化需用Instance/Layer/Group Norm而非Batch Norm。

## 核心推导

文章首先定义编码分布 $p$ 和生成分布 $q$ 的联合分布，优化目标为 $KL(p\|q)$。由于 $p$ 不含可训练参数，KL最小化等价于最大化 $-\int p \log q$。利用马尔可夫性质将 $\log q$ 分解为 $\sum \log q(x_{t-1}|x_t)$，逐项分析。对于第 $t$ 项，积分消去无关变量后简化为 $-\int p(x_t|x_{t-1})p(x_{t-1}|x_0)\tilde{p}(x_0)\log q(x_{t-1}|x_t) dx_0 dx_{t-1} dx_t$。代入正态分布的具体形式并执行与第一篇相同的参数化 $\mu(x_t) = \frac{1}{\alpha_t}(x_t - \beta_t \epsilon_\theta(x_t, t))$ 和方差消减换元，得到带系数的损失函数 $\frac{\beta_t^4}{\bar{\beta}_t^2 \alpha_t^2 \sigma_t^2} \|\varepsilon - \frac{\bar{\beta}_t}{\beta_t} \epsilon_\theta(\bar{\alpha}_t x_0 + \bar{\beta}_t \varepsilon, t)\|^2$。实验发现去掉系数效果更好，最终与第一篇一致。

## 关键公式

**联合分布KL散度优化目标：**
$$KL(p\|q) = \int p(x_T|x_{T-1})\cdots p(x_1|x_0) \tilde{p}(x_0) \log \frac{p(\cdots) \tilde{p}(x_0)}{q(\cdots) q(x_T)} dx_0\cdots dx_T$$

**前向转移（固定，不可学习）：**
$$p(x_t|x_{t-1}) = \mathcal{N}(x_t; \alpha_t x_{t-1}, \beta_t^2 I)$$

**逆向转移（可学习）：**
$$q(x_{t-1}|x_t) = \mathcal{N}(x_{t-1}; \mu(x_t), \sigma_t^2 I)$$

**经VAE推导的损失函数（带系数，式41）：**
$$\frac{\beta_t^4}{\bar{\beta}_t^2 \alpha_t^2 \sigma_t^2} \mathbb{E}_{\varepsilon, x_0} \left[\left\| \varepsilon - \frac{\bar{\beta}_t}{\beta_t} \epsilon_\theta(\bar{\alpha}_t x_0 + \bar{\beta}_t \varepsilon, t) \right\|^2\right]$$

**$\sigma_t$的两种理论候选：**
- 单样本情形：$\sigma_t = \frac{\bar{\beta}_{t-1}}{\bar{\beta}_t}\beta_t$
- 标准正态数据情形：$\sigma_t = \beta_t$

## 实验或案例

作者在CelebA HQ(128×128)上训练，单张24GB RTX 3090，batch_size=64，简化U-Net。半天可见初步效果，三天后生成效果清晰。关键实验发现：(1) 欧氏距离平方与MSE的差异会导致训练崩溃；(2) Batch Norm在DDPM中失败而Instance/Layer/Group Norm有效；(3) U-Net可大幅简化；(4) 可训练的Embedding层与Sinusoidal编码效果相当；(5) LAMB优化器（lr=$10^{-3}$）适用性良好。

## 系列定位

本文是系列第二篇，在首篇直观类比的基础上提供了更严格的理论基础，将DDPM纳入VAE的生成模型谱系。核心贡献是：(1) 建立了DDPM与经典VAE和NVAE之间的桥梁；(2) 提供了实用实现指南，使读者能自行训练DDPM；(3) 明确指出了DDPM作为纯生成模型（无编码能力）的本质。为第三篇贝叶斯视角提供了对照。
