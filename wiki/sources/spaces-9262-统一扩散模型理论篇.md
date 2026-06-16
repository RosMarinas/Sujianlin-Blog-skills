---
type: article_summary
title: 生成扩散模型漫谈（十）：统一扩散模型（理论篇）
article_id: "9262"
source_url: https://spaces.ac.cn/archives/9262
date: 2022-09-14
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-09-14-生成扩散模型漫谈-十-统一扩散模型-理论篇.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[统一扩散模型]]"
  - "[[边缘一致性]]"
  - "[[冷扩散]]"
methods:
  - "[[估计-校正分解]]"
evidence_spans:
  - ev::9262::前向过程
  - ev::9262::反向过程
  - ev::9262::训练目标
  - ev::9262::条件概率
  - ev::9262::思考分析
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-09-14-生成扩散模型漫谈-十-统一扩散模型-理论篇.md
source_ids:
  - "9262"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文提出统一扩散模型（UDM）理论框架，将前向过程抽象为任意确定性变换$\boldsymbol{x}_t = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon})$，将反向过程分解为"预估-修正"两步，建立了包含DDPM、DDIM、SDE和ODE为特例的最一般扩散模型框架。

## 核心问题

现有扩散模型都处理连续型数据、基于高斯加噪前向过程、离散或连续时间但互不统一。能否构建一个突破这些限制的统一理论框架——不限数据类型（连续/离散），不限前向过程（加噪/模糊/遮掩/删减），不限时间类型（离散/连续），且能包含所有已有结果为特例？

## 关键结论

- UDM框架的核心是将前向过程写为$\boldsymbol{x}_t = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon})$，其中$\boldsymbol{\mathcal{F}}_t$是任意确定性的"破坏"函数，$t$控制信息破坏进度，$\boldsymbol{\varepsilon}\sim q(\boldsymbol{\varepsilon})$是标准分布的随机变量。这统一了所有加噪、模糊、遮掩等前向过程。
- 反向过程恒等于分解式$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t) = \int p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0)p(\boldsymbol{x}_0|\boldsymbol{x}_t) d\boldsymbol{x}_0$，自然构成"预估-修正"两步采样：先估$\boldsymbol{x}_0$，再修正到$\boldsymbol{x}_{t-1}$。
- $p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0)$的设计必须满足边缘一致性约束$\int p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0)p(\boldsymbol{x}_t|\boldsymbol{x}_0)d\boldsymbol{x}_t = p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_0)$。利用$\boldsymbol{\mathcal{F}}_t$关于$\boldsymbol{\varepsilon}$的可逆性，可以用推断噪声替代随机噪声，得到更好的设计方案。
- UDM从数学上区分了扩散模型的"自由"（前向变换$\boldsymbol{\mathcal{F}}_t$的设计）与"约束"（概率恒等式和边缘一致性条件），为设计新扩散模型提供了方法论指导。

## 核心推导

框架分三步构建。前向过程：直接定义$\boldsymbol{x}_t = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon})$，其中$\boldsymbol{\mathcal{F}}_t$可为任意"渐进破坏"变换，$\boldsymbol{\varepsilon}$描述随机性。反向过程：利用概率恒等式$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t) = \int p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0)p(\boldsymbol{x}_0|\boldsymbol{x}_t)d\boldsymbol{x}_0$将生成分解为"预估"和"修正"两步。训练目标：对连续数据用高斯近似$q(\boldsymbol{x}_0|\boldsymbol{x}_t) = \mathcal{N}(\boldsymbol{x}_0;\boldsymbol{\mathcal{G}}_t(\boldsymbol{x}_t),\bar{\sigma}_t^2\boldsymbol{I})$最小化交叉熵；对离散数据用自回归/非自回归序列模型。条件概率设计：边缘一致性条件为约束，最简方案$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0) = p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_0)$可行但误差累积。更好的方案利用$\boldsymbol{\mathcal{F}}_t$关于$\boldsymbol{\varepsilon}$的可逆性：从$\boldsymbol{x}_t$和$\boldsymbol{x}_0$推断出$\boldsymbol{\varepsilon}$，代入$\boldsymbol{\mathcal{F}}_{t-1}$使$\boldsymbol{x}_{t-1}$同时依赖$\boldsymbol{x}_t$和$\boldsymbol{x}_0$。对高斯噪声还可引入随机插值参数$\tilde{\sigma}_t$。

## 关键公式

**UDM前向过程**（重参数化形式）：
$$\boldsymbol{x}_t = \boldsymbol{\mathcal{F}}_t(\boldsymbol{x}_0,\boldsymbol{\varepsilon}),\quad \boldsymbol{\varepsilon} \sim q(\boldsymbol{\varepsilon})$$

**反向过程分解**：
$$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t) = \int p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t, \boldsymbol{x}_0) p(\boldsymbol{x}_0|\boldsymbol{x}_t) d\boldsymbol{x}_0$$

**边缘一致性约束**：
$$\int p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t, \boldsymbol{x}_0)p(\boldsymbol{x}_t|\boldsymbol{x}_0) d\boldsymbol{x}_t = p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_0)$$

**基于逆变换的$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t,\boldsymbol{x}_0)$设计**：
$$p(\boldsymbol{x}_{t-1}|\boldsymbol{x}_t, \boldsymbol{x}_0) = \delta\big(\boldsymbol{x}_{t-1} - \boldsymbol{\mathcal{F}}_{t-1}(\boldsymbol{x}_0,\boldsymbol{\mathcal{F}}_t^{-1}(\boldsymbol{x}_0,\boldsymbol{x}_t))\big)$$

**随机插补版本**（高斯噪声情形）：
$$\boldsymbol{x}_{t-1} = \boldsymbol{\mathcal{F}}_{t-1}(\boldsymbol{x}_0,\sqrt{1 - \tilde{\sigma}_t^2}\boldsymbol{\mathcal{F}}_t^{-1}(\boldsymbol{x}_0,\boldsymbol{x}_t) + \tilde{\sigma}_t \boldsymbol{\varepsilon})$$

## 实验或案例

本文为纯理论框架构建，未提供实验。文章明确表示具体例子和新结果将在下一篇（第十一篇）中给出。

## 系列定位

作为扩散模型系列前十篇的理论顶峰（第10篇），UDM框架以前面九篇文章的全部成果为基础，抽象出扩散模型的本质数学结构。它提出了"设计自由 vs. 数学约束"的元理论视角，为超越高斯加噪、连续数据的扩散模型设计开辟了道路。"预估-修正"视角则为不同扩散模型框架（DDPM、DDIM、SDE、ODE）提供了统一的解释。本文是系列的承上启下之作，承诺在第十一篇进行具体推导和验证。
