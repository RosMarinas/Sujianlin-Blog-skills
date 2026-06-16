---
type: article_summary
title: 生成扩散模型漫谈（十九）：作为扩散ODE的GAN
article_id: "9662"
source_url: https://spaces.ac.cn/archives/9662
date: 2023-06-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-06-24-生成扩散模型漫谈-十九-作为扩散ODE的GAN.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[扩散ODE与GAN等价]]"
  - "[[参数空间扩散]]"
  - "[[Wasserstein距离与得分匹配]]"
methods:
  - "[[Cauchy-Schwarz不等式放缩]]"
evidence_spans:
  - ev::9662::思路简介
  - ev::9662::梯度之流
  - ev::9662::判别估计
  - ev::9662::向前一步
  - ev::9662::点睛之笔
  - ev::9662::意义思考
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-06-24-生成扩散模型漫谈-十九-作为扩散ODE的GAN.md
source_ids:
  - "9662"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文基于Wasserstein梯度流理论，将GAN的交替训练过程重新诠释为参数空间中的扩散ODE——生成器的参数轨迹$\boldsymbol{\theta}_t$代替了扩散模型中的"时间"维度，判别器估计密度比，生成器执行梯度流一步前进。

## 核心问题

GAN和扩散模型表面上差异显著：GAN是单步直接生成，扩散模型是渐进式生成。能否找到一种理论框架将两者统一？特别是，GAN的实际训练过程（判别器和生成器交替更新）能否从扩散模型的视角得到合乎逻辑的解释？

## 关键结论

1. **GAN作为参数空间扩散ODE**：将生成器参数的历史轨迹$\boldsymbol{\theta}_0\to\boldsymbol{\theta}_1\to\cdots\to\boldsymbol{\theta}_T$视为扩散时间维度，则GAN的交替训练对应于参数空间中的扩散ODE。
2. **判别器估计密度比**：Vanilla GAN的最优判别器$D(\boldsymbol{x}) = \log(p(\boldsymbol{x})/q(\boldsymbol{x}))$恰好给出Wasserstein梯度流所需的密度比$\log r_t(\boldsymbol{x})$。
3. **生成器更新的两种形式**：显式对齐损失$\mathbb{E}[\|\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}) - \boldsymbol{g}_{\boldsymbol{\theta}_t}(\boldsymbol{z}) - \epsilon\nabla D\|^2]$与标准生成器损失$\mathbb{E}[-D(\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}))]$在单步优化下等价。
4. **训练过程一致的理论**：与GAN的经典证明（先完全优化判别器再优化生成器）不同，扩散ODE视角天然基于交替训练，与实际训练过程一致。
5. **解释生成器训练次数**：解释了为什么GAN的生成器不应训练太多步——仅当单步优化时两种损失等价。

## 核心推导

**从Wasserstein梯度流到GAN的推导链条**：

1. Wasserstein梯度流方程：$\frac{\partial q_t}{\partial t} = -\nabla\cdot(q_t \nabla\log\frac{p}{q_t})$，最小化KL$(q_t\|p)$。
2. 对应的样本空间ODE：$\frac{d\boldsymbol{x}}{dt} = \nabla\log\frac{p(\boldsymbol{x})}{q_t(\boldsymbol{x})}$。
3. Vanilla GAN的最优判别器$D(\boldsymbol{x}) = \log(p/q)$恰好给出$\log r_t$。
4. 欧拉前进一步：$\boldsymbol{x}_{t+1} = \boldsymbol{x}_t + \epsilon\nabla D(\boldsymbol{x}_t)$。
5. 对齐生成器：$\boldsymbol{\theta}_{t+1} = \mathop{\text{argmin}}_{\boldsymbol{\theta}} \mathbb{E}[\|\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}) - (\boldsymbol{g}_{\boldsymbol{\theta}_t}(\boldsymbol{z}) + \epsilon\nabla D(\boldsymbol{g}_{\boldsymbol{\theta}_t}(\boldsymbol{z})))\|^2]$。
6. 计算梯度得$\nabla_{\boldsymbol{\theta}_t} = -2\epsilon\nabla_{\boldsymbol{\theta}_t}D(\boldsymbol{g}_{\boldsymbol{\theta}_t}(\boldsymbol{z}))$，与标准生成器损失$-D(\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}))$的梯度只差常数倍。
7. 推广：任意单调递增函数$h$可替换$\log r_t$，得到MonoFlow框架。

## 关键公式

**Wasserstein梯度流方程**：
$$\frac{\partial q_t(\boldsymbol{x})}{\partial t} = -\nabla_{\boldsymbol{x}}\cdot\big(q_t(\boldsymbol{x})\nabla_{\boldsymbol{x}}\log r_t(\boldsymbol{x})\big)$$
其中$r_t(\boldsymbol{x}) = p(\boldsymbol{x})/q_t(\boldsymbol{x})$。

**对应的样本ODE**：
$$\frac{d\boldsymbol{x}}{dt} = \nabla_{\boldsymbol{x}}\log r_t(\boldsymbol{x})$$

**判别器最优解**：
$$D(\boldsymbol{x}) = \log\frac{p(\boldsymbol{x})}{q(\boldsymbol{x})}$$

**生成器显式对齐损失**：
$$\boldsymbol{\theta}_{t+1} = \mathop{\text{argmin}}_{\boldsymbol{\theta}}\mathbb{E}_{\boldsymbol{z}}\Big[\big\Vert \boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}) - \boldsymbol{g}_{\boldsymbol{\theta}_t}(\boldsymbol{z}) - \epsilon \nabla_{\boldsymbol{g}}D(\boldsymbol{g}_{\boldsymbol{\theta}_t}(\boldsymbol{z}))\big\Vert^2\Big]$$

**等价的标准生成器损失（单步优化）**：
$$\boldsymbol{\theta}_{t+1} = \mathop{\text{argmin}}_{\boldsymbol{\theta}}\mathbb{E}_{\boldsymbol{z}}[-D(\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}))]$$

**MonoFlow推广**：
$$\boldsymbol{\theta}_{t+1} = \mathop{\text{argmin}}_{\boldsymbol{\theta}}\mathbb{E}_{\boldsymbol{z}}[-h(D(\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z})))]$$
其中$h$是任意单调递增函数。

## 实验或案例

本文为纯理论推导，没有实验验证。作者在"意义思考"部分深入讨论了该视角的重要性：它提供了与GAN实际训练过程一致的理论解释，而GAN的经典推导（先封闭求解判别器再优化生成器）与交替训练过程不一致。

## 系列定位

本文是系列中将GAN与扩散模型统一的关键文章，与第20篇（从ReFlow到WGAN-GP）共同构成了统一化框架的完整图景。本文采用Wasserstein梯度流路径（较复杂），第20篇则采用ReFlow路径（较简单），两者从不同角度达成了相同的结论。此外，本文依赖于第16篇建立的理论基础和第9660篇"梯度流"的先行工作。
