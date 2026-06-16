---
type: article_summary
title: 生成扩散模型漫谈（七）：最优扩散方差估计（上）
article_id: "9245"
source_url: https://spaces.ac.cn/archives/9245
date: 2022-08-12
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-08-12-生成扩散模型漫谈-七-最优扩散方差估计-上.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[最优扩散方差]]"
methods:
  - "[[最优方差估计]]"
evidence_spans:
  - ev::9245::不确定性
  - ev::9245::方差估计1
  - ev::9245::方差估计2
  - ev::9245::实验结果
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-08-12-生成扩散模型漫谈-七-最优扩散方差估计-上.md
source_ids:
  - "9245"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文在DDIM框架下，通过考虑$\boldsymbol{x}_0$预测的不确定性，推导了反向过程最优方差的解析表达式（Analytic-DPM），给出了无需重新训练的即用型方差修正公式。

## 核心问题

扩散模型反向（生成）过程的方差应该如何选择？DDPM提供了两种启发式选择，DDIM将方差视为可调超参数（甚至允许零方差），SDE篇认为前后方差应在$\Delta t \to 0$时匹配——但所有这些都没有给出确定的最优答案。能否导出一个解析的、不依赖额外训练的最优方差公式？

## 关键结论

- 反向过程的最优方差应为$\sigma_t^2 + \gamma_t^2\bar{\sigma}_t^2$，其中$\sigma_t$是DDIM的标准差参数，$\bar{\sigma}_t^2$是$p(\boldsymbol{x}_0|\boldsymbol{x}_t)$的方差，$\gamma_t = \bar{\alpha}_{t-1} - \bar{\alpha}_t\sqrt{\bar{\beta}_{t-1}^2 - \sigma_t^2}/\bar{\beta}_t$。
- DDIM将$\boldsymbol{x}_0$预测视为确定的点估计忽略了内在不确定性——即使$\sigma_t=0$，修正项$\gamma_t^2\bar{\sigma}_t^2$也不为零，这解释了为什么DDPM（非零方差）通常优于DDIM（零方差）。
- 方差$\bar{\sigma}_t^2$可解析估计：$\bar{\sigma}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}\left(1 - \frac{1}{d}\mathbb{E}[\|\boldsymbol{\epsilon}_{\boldsymbol{\theta}}\|^2]\right) \leq \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}$，由已训练好的噪声预测网络$\boldsymbol{\epsilon}_{\boldsymbol{\theta}}$计算期望即可，无需重新训练。
- 当扩散步数较少时（如10步），Analytic-DPM修正显著提升生成质量，图像更真实但会增加少许噪点。

## 核心推导

文章从DDIM的一般解$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0) = \mathcal{N}(\boldsymbol{x}_{t-1}; \frac{\sqrt{\bar{\beta}_{t-1}^2 - \sigma_t^2}}{\bar{\beta}_t} \boldsymbol{x}_t + \gamma_t \boldsymbol{x}_0, \sigma_t^2 \boldsymbol{I})$出发。关键洞察是：DDIM将$\boldsymbol{x}_0$视为确定值$\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t)$，但正确的贝叶斯处理应边际化$p(\boldsymbol{x}_0|\boldsymbol{x}_t)$。将$p(\boldsymbol{x}_0|\boldsymbol{x}_t)$近似为高斯分布$\mathcal{N}(\boldsymbol{x}_0;\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t),\bar{\sigma}_t^2\boldsymbol{I})$并代入积分，得到$\boldsymbol{x}_{t-1}$的有效方差为$\sigma_t^2 + \gamma_t^2\bar{\sigma}_t^2$。

接下来估计$\bar{\sigma}_t^2$。作者给出两种方法：方法一利用协方差平移不变性，用参考常向量$\boldsymbol{\mu}_0$将协方差分解为数据方差与预测误差的差，得到$\bar{\sigma}_t^2 = \frac{1}{d}\mathbb{E}[\|\boldsymbol{x}_0 - \boldsymbol{\mu}_0\|^2] - \frac{1}{d}\mathbb{E}[\|\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t) - \boldsymbol{\mu}_0\|^2]$。方法二（原论文结果）代入$\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t)$的$\boldsymbol{\epsilon}_{\boldsymbol{\theta}}$参数化，利用$p(\boldsymbol{x}_t|\boldsymbol{x}_0)$的协方差为$\bar{\beta}_t^2\boldsymbol{I}$，推导出$\bar{\sigma}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}(1 - \frac{1}{d}\mathbb{E}[\|\boldsymbol{\epsilon}_{\boldsymbol{\theta}}\|^2])$。

## 关键公式

**最优反向方差**：
$$\text{Variance} = \sigma_t^2 + \gamma_t^2\bar{\sigma}_t^2, \quad \gamma_t = \bar{\alpha}_{t-1} - \frac{\bar{\alpha}_t\sqrt{\bar{\beta}_{t-1}^2 - \sigma_t^2}}{\bar{\beta}_t}$$

**Analytic-DPM方差估计**（原论文形式）：
$$\bar{\sigma}_t^2 = \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}\left(1 - \frac{1}{d}\mathbb{E}_{\boldsymbol{x}_t\sim p(\boldsymbol{x}_t)}\left[ \Vert\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)\Vert^2\right]\right) \leq \frac{\bar{\beta}_t^2}{\bar{\alpha}_t^2}$$

**作者给出的方差估计**：
$$\bar{\sigma}_t^2 = \frac{1}{d}\mathbb{E}_{\boldsymbol{x}_0}[\|\boldsymbol{x}_0 - \boldsymbol{\mu}_0\|^2] - \frac{1}{d}\mathbb{E}_{\boldsymbol{x}_t}[\|\bar{\boldsymbol{\mu}}(\boldsymbol{x}_t) - \boldsymbol{\mu}_0\|^2]$$

## 实验或案例

作者在Keras-DDPM实现（10扩散步）上验证：DDPM生成结果过度光滑（"重度磨皮"效果），Analytic-DDPM结果更真实但带额外噪点，评价指标上Analytic-DDPM更优。原论文实验显示，Analytic-DPM在少步数场景下有显著提升。

## 系列定位

作为系列第七篇，本文回答了前序文章共同留下的开放问题：反向方差如何选择。它基于第四篇（DDIM）的框架，给出第一个解析最优方差解，在实际性能上填补了理论到应用的空白。本文也为第八篇（下篇）奠定了完美均值假设的基础，第八篇将在此基础上弱化此假设，扩展到更一般的情形。
