---
type: article_summary
title: 生成扩散模型漫谈（八）：最优扩散方差估计（下）
article_id: "9246"
source_url: https://spaces.ac.cn/archives/9246
date: 2022-08-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-08-18-生成扩散模型漫谈-八-最优扩散方差估计-下.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[最优扩散方差]]"
methods:
  - "[[最优方差估计]]"
evidence_spans:
  - ev::9246::如何改进
  - ev::9246::最大似然
  - ev::9246::条件方差
  - ev::9246::两个阶段
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-08-18-生成扩散模型漫谈-八-最优扩散方差估计-下.md
source_ids:
  - "9246"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文介绍Extended-Analytic-DPM，它放松了上篇的完美均值假设，将最优方差估计推广到逐维度（对角协方差）和逐输入（条件方差）的情形，并提出了两阶段训练方案。

## 核心问题

上篇（Analytic-DPM）有三个主要限制：（1）假设各维度方差相同（各向同性标量）；（2）方差与$\boldsymbol{x}_t$无关（无条件）；（3）假设$\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t)$精确等于真实后验均值（完美均值假设）。如何放松这些假设，得到更一般、更精确的方差估计？

## 关键结论

- 在完美均值假设下，可以直接将标量方差推广为逐维度向量方差（对角协方差）：$\bar{\boldsymbol{\sigma}}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}(\boldsymbol{1}_d - \mathbb{E}[\boldsymbol{\epsilon}_{\boldsymbol{\theta}}^2(\boldsymbol{x}_t, t)])$。
- 在非完美均值假设下，最大似然估计给出$\bar{\sigma}_t^2 = \frac{1}{d}\mathbb{E}[\|\boldsymbol{x}_0 - \bar{\boldsymbol{\mu}}(\boldsymbol{x}_t)\|^2]$，等价于$\frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2 d}\mathbb{E}[\|\boldsymbol{\varepsilon} - \boldsymbol{\epsilon}_{\boldsymbol{\theta}}\|^2]$，无需均值精确性假设。
- NPR-DPM方案通过MSE训练一个网络$\boldsymbol{g}(\boldsymbol{x}_t)$来预测$(\boldsymbol{\varepsilon} - \boldsymbol{\epsilon}_{\boldsymbol{\theta}})^2$，实现条件（逐输入）方差学习。
- 两阶段训练（先固定方差训练均值模型，再冻结均值模型训练方差模型）避免了方差变化对均值学习的干扰，降低了成本并提高了稳定性。
- 令人惊讶的实验结果：基于完美均值假设的SN-DPM方案反而优于处理非完美均值的NPR-DPM方案，说明完美均值假设与实际情况足够接近。

## 核心推导

文章从上篇结果出发，逐层放松假设。首先，将标量方差推广到对角向量，直接取$\boldsymbol{\Sigma}_t$的对角线：$\bar{\boldsymbol{\sigma}}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}(\boldsymbol{1}_d - \mathbb{E}[\boldsymbol{\epsilon}_{\boldsymbol{\theta}}^2])$。其次，放弃完美均值假设，从负对数似然$\mathbb{E}[-\log\mathcal{N}(\boldsymbol{x}_0;\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t),\bar{\sigma}_t^2\boldsymbol{I})]$出发求导，得到$\bar{\sigma}_t^2 = \frac{1}{d}\mathbb{E}[\|\boldsymbol{x}_0 - \bar{\boldsymbol{\mu}}(\boldsymbol{x}_t)\|^2]$，该式无需$\bar{\boldsymbol{\mu}}$等于真实均值。最后，对条件方差，利用$\mathbb{E}[\boldsymbol{x}] = \text{argmin}_{\boldsymbol{\mu}}\mathbb{E}[\|\boldsymbol{x} - \boldsymbol{\mu}\|^2]$的恒等式，将方差估计转化为对$(\boldsymbol{\varepsilon} - \boldsymbol{\epsilon}_{\boldsymbol{\theta}})^2$的MSE回归问题，得到NPR-DPM方案。

## 关键公式

**逐维度方差估计**（完美均值）：
$$\bar{\boldsymbol{\sigma}}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}\left(\boldsymbol{1}_d - \mathbb{E}_{\boldsymbol{x}_t\sim p(\boldsymbol{x}_t)}\left[ \boldsymbol{\epsilon}_{\boldsymbol{\theta}}^2(\boldsymbol{x}_t, t)\right]\right)$$

**最大似然方差估计**（非完美均值）：
$$\bar{\sigma}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2 d}\mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{\varepsilon}}\left[\left\Vert\boldsymbol{\varepsilon} - \boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\bar{\alpha}_t\boldsymbol{x}_0 + \bar{\beta}_t\boldsymbol{\varepsilon}, t)\right\Vert^2\right]$$

**条件方差**（NPR-DPM）：
$$\bar{\boldsymbol{\sigma}}_t^2(\boldsymbol{x}_t) = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}\mathop{\text{argmin}}_{\boldsymbol{g}(\boldsymbol{x}_t)}\mathbb{E}_{\boldsymbol{x}_t,\boldsymbol{x}_0}\left[\left\Vert\left(\boldsymbol{\epsilon}_t - \boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)\right)^2-\boldsymbol{g}(\boldsymbol{x}_t)\right\Vert^2\right]$$

## 实验或案例

本文未报告新实验。文中引用了原论文令人惊讶的结果：SN-DPM（完美均值假设）优于NPR-DPM（非完美均值）。作者对此进行了批判性分析，认为这动摇了原论文标题"Imperfect Mean"的核心动机。

## 系列定位

作为方差估计子系列的下篇，本文扩展了上篇的理论并放松了假设，完成了从各向同性标量到逐维度、逐条件方差的理论覆盖。虽被作者评价为"常规扩展"（相比上篇的"惊艳"），但两阶段训练范式对实际应用有重要价值。文章末尾的开放问题（MSE vs. 负对数似然的选择）和实验反直觉结果，为后续研究留下了空间。
