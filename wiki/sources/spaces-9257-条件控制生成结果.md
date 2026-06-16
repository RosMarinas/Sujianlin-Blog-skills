---
type: article_summary
title: 生成扩散模型漫谈（九）：条件控制生成结果
article_id: "9257"
source_url: https://spaces.ac.cn/archives/9257
date: 2022-08-30
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-08-30-生成扩散模型漫谈-九-条件控制生成结果.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[条件生成控制]]"
  - "[[分类器引导]]"
  - "[[无分类器引导]]"
methods: []
evidence_spans:
  - ev::9257::技术分析
  - ev::9257::近似分布
  - ev::9257::梯度缩放
  - ev::9257::相似控制
  - ev::9257::连续情形
  - ev::9257::无分类器
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-08-30-生成扩散模型漫谈-九-条件控制生成结果.md
source_ids:
  - "9257"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文系统地介绍了扩散模型条件生成的两大主流范式——Classifier-Guidance（事后修改）和Classifier-Free（事前训练）——的理论推导、实施细节和统一视角。

## 核心问题

如何让扩散模型根据条件信号（类别标签、文本描述、图像等）控制生成结果？如何在无需重新训练的条件下复用已训练的无条件模型？两种主流方法各自的数学基础、适用场景和内在联系是什么？

## 关键结论

- Classifier-Guidance的核心结果是将反向过程的均值从$\boldsymbol{\mu}(\boldsymbol{x}_t)$修正为$\boldsymbol{\mu}(\boldsymbol{x}_t) + \sigma_t^2\nabla_{\boldsymbol{x}_t}\log p(\boldsymbol{y}|\boldsymbol{x}_t)$，通过泰勒展开条件对数概率即可推导此结果，其中$\sigma_t^2$前的系数来自反向方差。
- 缩放参数$\gamma$控制条件强度，但原论文的"温度缩放"解释不完全正确——当$\gamma \neq 1$时，归一化因子$Z(\boldsymbol{x}_t)$依赖于$\boldsymbol{x}_t$，梯度不能简单乘以$\gamma$。正确理解是直接定义$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{y}) \propto p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t)e^{\gamma\cdot\text{sim}(\boldsymbol{x}_{t-1},\boldsymbol{y})}$。
- 在SDE/ODE框架下，条件生成等价于将score函数替换为$\nabla\log p_t(\boldsymbol{x}|\boldsymbol{y}) = \nabla\log p_t(\boldsymbol{x}) + \nabla\log p_t(\boldsymbol{y}|\boldsymbol{x})$，适用于任意反向方差（包括DDIM的零方差情形）。
- Classifier-Free通过训练$\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,\boldsymbol{y},t)$实现条件控制，用$(1+w)\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,\boldsymbol{y},t) - w\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)$控制引导强度，无条件模型通过空输入$\boldsymbol{\phi}$获得。

## 核心推导

对于Classifier-Guidance：从贝叶斯公式$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{y}) \propto p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t)p(\boldsymbol{y}|\boldsymbol{x}_{t-1})$出发，泰勒展开$\log p(\boldsymbol{y}|\boldsymbol{x}_{t-1})$在$\boldsymbol{x}_t$附近至一阶，代入$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t) = \mathcal{N}(\boldsymbol{x}_{t-1};\boldsymbol{\mu}(\boldsymbol{x}_t),\sigma_t^2\boldsymbol{I})$的表达式，配方后即得均值修正$\boldsymbol{\mu}(\boldsymbol{x}_t) + \sigma_t^2\nabla_{\boldsymbol{x}_t}\log p(\boldsymbol{y}|\boldsymbol{x}_t)$。

对于SDE推广：从第六篇的一般反向SDE $d\boldsymbol{x} = (\boldsymbol{f}_t - \frac{1}{2}(g_t^2 + \sigma_t^2)\nabla\log p_t(\boldsymbol{x}))dt + \sigma_t d\boldsymbol{w}$出发，将$\nabla\log p_t(\boldsymbol{x})$替换为$\nabla\log p_t(\boldsymbol{x}) + \nabla\log p_t(\boldsymbol{y}|\boldsymbol{x})$。代入$\boldsymbol{\epsilon}$参数化后，相当于用$\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t) - \bar{\beta}_t\nabla\log p_t(\boldsymbol{y}|\boldsymbol{x})$替换$\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)$，适用于所有反向方差。

对于Classifier-Free：直接训练条件噪声预测模型，引导强度通过$(1+w)\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,\boldsymbol{y},t) - w\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)$实现。

## 关键公式

**Classifier-Guidance采样公式**：
$$\boldsymbol{x}_{t-1} = \boldsymbol{\mu}(\boldsymbol{x}_t) + \sigma_t^2 \nabla_{\boldsymbol{x}_t} \log p(\boldsymbol{y}|\boldsymbol{x}_t) + \sigma_t\boldsymbol{\varepsilon}$$

**含缩放参数的采样**：
$$\boldsymbol{x}_{t-1} = \boldsymbol{\mu}(\boldsymbol{x}_t) + \sigma_t^2 \gamma \nabla_{\boldsymbol{x}_t} \log p(\boldsymbol{y}|\boldsymbol{x}_t) + \sigma_t\boldsymbol{\varepsilon}$$

**SDE框架下的条件score**：
$$\nabla_{\boldsymbol{x}}\log p_t(\boldsymbol{x}|\boldsymbol{y}) = \nabla_{\boldsymbol{x}}\log p_t(\boldsymbol{x}) + \nabla_{\boldsymbol{x}}\log p_t(\boldsymbol{y}|\boldsymbol{x})$$

**Classifier-Free引导**：
$$\tilde{\boldsymbol{\epsilon}}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, \boldsymbol{y}, t) = (1 + w)\boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, \boldsymbol{y}, t) - w \boldsymbol{\epsilon}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t)$$

## 实验或案例

本文为理论综述，未直接报告新实验。但引用了大量外部工作：（1）Dhariwal & Nichol 2021的Classifier-Guidance原始实验，展示其超越GAN的生成质量；（2）DALL-E 2和Imagen基于Classifier-Free的方案；（3）Liu et al. 2021的语义扩散引导方案，用余弦相似度替代分类器实现多模态控制。

## 系列定位

作为系列第九篇，本文是对扩散模型理论应用的重要拓展。它将前六篇建立的基础理论（DDPM、DDIM、SDE、ODE框架）延伸到了条件生成这一实际关键场景。本文特别建立了条件生成与SDE/ODE框架的统一联系，将第八篇之前的所有理论成果串联到了生成控制的应用层面，为理解DALL-E 2、Imagen等前沿模型提供了理论准备。
