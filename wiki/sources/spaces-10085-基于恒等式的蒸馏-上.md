---
type: article_summary
title: 生成扩散模型漫谈（二十五）：基于恒等式的蒸馏（上）
article_id: "10085"
source_url: https://spaces.ac.cn/archives/10085
date: 2024-05-01
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-05-01-生成扩散模型漫谈-二十五-基于恒等式的蒸馏-上.md
series: [生成扩散模型漫谈]
concepts: [基于恒等式的蒸馏, Fisher散度]
methods: [恒等式蒸馏法]
evidence_spans:
  - 10085-重现江湖
  - 10085-初级形式
  - 10085-点睛之笔
  - 10085-恒等变换
  - 10085-其他细节
  - 10085-延伸思考
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-05-01-生成扩散模型漫谈-二十五-基于恒等式的蒸馏-上.md
source_ids:
  - "10085"
status: draft
updated: 2026-06-09
---

## 一句话总结

SiD（Score identity Distillation）通过恒等变换将扩散模型的蒸馏损失重新表述，消除了对不精确的学生去噪模型 $\boldsymbol{\psi}^*$ 的过度依赖，实现了一种无需真实数据、无需教师模型迭代采样的单步生成模型蒸馏方案。

## 核心问题

传统的扩散模型蒸馏需要大量从教师模型采样的数据对，耗时且费力。能否在不依赖教师模型迭代采样、也不使用原始训练数据的情况下，将多步扩散模型蒸馏为单步生成器？

## 关键结论

1. 若学生生成器 $\boldsymbol{g}_{\boldsymbol{\theta}}$ 产生的数据分布与真实分布相近，则在其数据上训练的扩散模型 $\boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}$ 应与教师模型 $\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}$ 相近——这是SiD的思想基础。
2. 朴素的交替训练（类似GAN）存在两个根本困难：最优性gap（无法将 $\boldsymbol{\psi}$ 训练到最优再更新 $\boldsymbol{\theta}$）和梯度gap（忽略 $\boldsymbol{\psi}^*(\boldsymbol{\theta})$ 对 $\boldsymbol{\theta}$ 的依赖）。
3. 恒等变换 $\mathbb{E}[\langle\boldsymbol{f}, \boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}\rangle] = \mathbb{E}[\langle\boldsymbol{f}, \boldsymbol{\varepsilon}\rangle]$ 将损失从 $\mathcal{L}_1 = \|\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*} - \boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}\|^2$ 变为 $\mathcal{L}_2 = \langle\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*} - \boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}, \boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*} - \boldsymbol{\varepsilon}\rangle$，显著降低了对 $\boldsymbol{\psi}^*$ 的依赖。
4. SiD的最终损失为 $\mathcal{L}_2 - \lambda\mathcal{L}_1$，$\lambda \approx 1$ 最优。

## 核心推导

从最优解 $\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}(\boldsymbol{x}_t, t) = -\bar{\beta}_t\nabla_{\boldsymbol{x}_t}\log p(\boldsymbol{x}_t)$ 和 $\boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}(\boldsymbol{x}_t^{(g)}, t) = -\bar{\beta}_t\nabla_{\boldsymbol{x}_t^{(g)}}\log p_{\boldsymbol{\theta}}(\boldsymbol{x}_t^{(g)})$ 出发，展开 $\|\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*} - \boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}\|^2$。利用恒等式 $\nabla_{\boldsymbol{x}_t}\log p(\boldsymbol{x}_t) = \mathbb{E}_{\boldsymbol{x}_0\sim p(\boldsymbol{x}_0|\boldsymbol{x}_t)}[\nabla_{\boldsymbol{x}_t}\log p(\boldsymbol{x}_t|\boldsymbol{x}_0)]$，将包含 $\boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}$ 的项转化为对 $\boldsymbol{\varepsilon}$ 的期望，最终得到 $\mathcal{L}_2$。

## 关键公式

教师模型训练目标：
$$\boldsymbol{\varphi}^* = \mathop{\text{argmin}}_{\boldsymbol{\varphi}} \mathbb{E}_{\boldsymbol{x}_0\sim \tilde{p}(\boldsymbol{x}_0),\boldsymbol{\varepsilon}}\left[\|\boldsymbol{\epsilon}_{\boldsymbol{\varphi}}(\bar{\alpha}_t\boldsymbol{x}_0 + \bar{\beta}_t\boldsymbol{\varepsilon}, t) - \boldsymbol{\varepsilon}\|^2\right]$$

学生去噪模型训练目标（仅用学生数据）：
$$\boldsymbol{\psi}^* = \mathop{\text{argmin}}_{\boldsymbol{\psi}} \mathbb{E}_{\boldsymbol{z},\boldsymbol{\varepsilon}}\left[\|\boldsymbol{\epsilon}_{\boldsymbol{\psi}}(\bar{\alpha}_t\boldsymbol{g}_{\boldsymbol{\theta}}(\boldsymbol{z}) + \bar{\beta}_t\boldsymbol{\varepsilon}, t) - \boldsymbol{\varepsilon}\|^2\right]$$

恒等变换后的生成器损失：
$$\mathcal{L}_2 = \mathbb{E}_{\boldsymbol{z},\boldsymbol{\varepsilon}}\left[\left\langle\boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}(\boldsymbol{x}_t^{(g)}, t) - \boldsymbol{\epsilon}_{\boldsymbol{\psi}^*}(\boldsymbol{x}_t^{(g)}, t), \boldsymbol{\epsilon}_{\boldsymbol{\varphi}^*}(\boldsymbol{x}_t^{(g)}, t) - \boldsymbol{\varepsilon}\right\rangle\right]$$

最终损失：$\mathcal{L} = \mathcal{L}_2 - \lambda\mathcal{L}_1$

## 实验或案例

- $\mathcal{L}_1$ 单独使用（无恒等变换）完全无法训练出有意义的结果。
- $\mathcal{L}_2$ 单独使用即可成功训练；$\mathcal{L}_2 - \lambda\mathcal{L}_1$ 效果更优。
- $\lambda \approx 1$ 最优；$\lambda > 1.5$ 导致训练崩溃。
- 显存需求约为教师模型的2倍（需同时维护3个模型），建议未来用LoRA降低。

## 系列定位

作为系列第25篇，本文与第26篇（下篇）共同构成"基于恒等式的蒸馏"主题。SiD的思想可追溯到DDE（去噪自编码器作为生成模型），但在扩散模型时代被重新发掘并改进。它代表了扩散模型加速的第三条路径：不改进ODE求解器（第21篇），不调整模型结构（第24篇），而是通过蒸馏将多步模型压缩为单步。
