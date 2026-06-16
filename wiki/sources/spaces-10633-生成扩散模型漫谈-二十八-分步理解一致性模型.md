---
type: article_summary
title: 生成扩散模型漫谈（二十八）：分步理解一致性模型
article_id: "10633"
source_url: https://spaces.ac.cn/archives/10633
date: 2024-12-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-12-18-生成扩散模型漫谈-二十八-分步理解一致性模型.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[一致性模型]]"
  - "[[自一致性损失]]"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-12-18-生成扩散模型漫谈-二十八-分步理解一致性模型.md
source_ids:
  - "10633"
status: draft
updated: 2026-06-09
---

# 生成扩散模型漫谈（二十八）：分步理解一致性模型

## 一句话总结

本文通过逐步解构ReFlow训练流程，从可微分的"预测目标替换"出发，推导出Consistency Models（一致性模型）的Consistency Training（CT）和Consistency Distillation（CD）目标，为CM提供了从ReFlow出发的直观理解路径。

## 核心问题

一致性模型（Consistency Models）能够实现1-2步快速生成，但其训练目标看起来像实践中的Trick——依赖EMA和stop_gradient，缺乏从ReFlow等基础知识出发的直观推导。如何从第一性原理理解CM的工作机制？

## 关键结论

1. 一致性训练（CT）优化的是单步生成误差的上界，通过最小化相邻时间步间$\boldsymbol{f}_\theta$输出的差异，间接实现正确的$\boldsymbol{x}_0,\boldsymbol{x}_1$配对。
2. "预测目标替换"（用$\boldsymbol{f}_{\theta_{k-1}^*}(\boldsymbol{x}_{t_{k-1}}, t_{k-1})$替代$\boldsymbol{x}_0$作为第$k$步目标）能减少轨迹交叉（trajectory crossing）问题。
3. EMA权重可近似视为"超前解"$\theta^*$，从而允许用单一模型参数实现序列化训练目标。
4. 一致性蒸馏（CD）将教师模型替换为预训练扩散模型的单步预测，比ReFlow蒸馏更高效（无需完整采样轨迹）。

## 核心推导

### 从ReFlow出发
设定$\boldsymbol{x}_0$为数据，$\boldsymbol{x}_1$为噪声，轨迹$\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t\boldsymbol{x}_1$。定义数据预测函数$\boldsymbol{f}_\theta(\boldsymbol{x}_t, t) = \boldsymbol{x}_t - t\boldsymbol{v}_\theta(\boldsymbol{x}_t, t)$，满足$\boldsymbol{f}_\theta(\boldsymbol{x}_0, 0) = \boldsymbol{x}_0$。

### 序列化训练目标
将$[0,1]$等分为$n$份，$t_k = k/n$，逐步将预测目标从$\boldsymbol{x}_0$替换为上一步模型的输出：
$$\boldsymbol{\theta}_k^* = \text{argmin}_\theta \mathbb{E}[\tilde{w}(t_k)\|\boldsymbol{f}_\theta(\boldsymbol{x}_{t_k}, t_k) - \boldsymbol{f}_{\theta_{k-1}^*}(\boldsymbol{x}_{t_{k-1}}, t_{k-1})\|^2]$$

### 统一参数+EMA
所有$\theta_k^*$共享参数后，用EMA$\bar{\theta}$作为目标：
$$\boldsymbol{\theta}^* = \text{argmin}_\theta \mathbb{E}[ \tilde{w}(t_k)\|\boldsymbol{f}_\theta(\boldsymbol{x}_{t_k}, t_k) - \boldsymbol{f}_{\bar{\theta}}(\boldsymbol{x}_{t_{k-1}}, t_{k-1})\|^2]$$

这就是CT目标。CD则把$\boldsymbol{f}_{\bar{\theta}}(\boldsymbol{x}_{t_{k-1}}, t_{k-1})$换成教师模型单步预测的输出。

## 关键公式

| 公式 | 含义 |
|------|------|
| $\boldsymbol{f}_\theta(\boldsymbol{x}_t, t) = \boldsymbol{x}_t - t\boldsymbol{v}_\theta(\boldsymbol{x}_t, t)$ | 数据预测函数 |
| $\|\boldsymbol{f}_{\theta^*}(\boldsymbol{x}_1, 1) - \boldsymbol{x}_0\| \leq \sum_{k=1}^n \|\boldsymbol{f}_{\theta^*}(\boldsymbol{x}_{t_k}, t_k) - \boldsymbol{f}_{\theta^*}(\boldsymbol{x}_{t_{k-1}}, t_{k-1})\|$ | 单步生成误差上界 |
| $\boldsymbol{x}_0 = \boldsymbol{f}_{\theta^*}(\boldsymbol{x}_1, 1)$ | 单步生成公式 |
| $\boldsymbol{x}_0 = \boldsymbol{f}_{\theta^*}(\boldsymbol{x}_1, 1)$ 及其多步噪声增强采样 | 多步改进采样 |

## 实验或案例

本文为教学性文章，无新实验。原始CM论文在CIFAR-10和ImageNet上证明了CT/CD在1-2 NFE下达到竞争性生成质量。

## 系列定位

本文承前（Shortcut Model, 文章27）启后（MeanFlow, 文章30），为理解一致性模型提供了从ReFlow出发的渐进推导。sCM在后续文章30中被证明是MeanFlow在$r=0$时的特例。
