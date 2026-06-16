---
type: article_summary
title: "生成扩散模型漫谈（十三）：从万有引力到扩散模型"
article_id: "9305"
source_url: "https://spaces.ac.cn/archives/9305"
date: "2022-10-18"
category: "Big-Data"
source_markdown: "Data/Spaces_ac_cn/markdown/Big-Data/2022-10-18-生成扩散模型漫谈-十三-从万有引力到扩散模型.md"
series:
  - "[[生成扩散模型漫谈]]"
topics: []
concepts:
  - "[[泊松流生成模型]]"
  - "[[万有引力类比]]"
  - "[[无散度条件]]"
methods:
  - "[[万有引力类比构造法]]"
problem_patterns: []
evidence_spans:
  - "ev::9305::万有引力"
  - "ev::9305::沿场线走"
  - "ev::9305::模式坍缩"
  - "ev::9305::增加一维"
  - "ev::9305::豁然开朗"
  - "ev::9305::场的训练"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-10-18-生成扩散模型漫谈-十三-从万有引力到扩散模型.md"
source_ids:
  - "9305"
status: draft
updated: "2026-06-09"
---

# 生成扩散模型漫谈（十三）：从万有引力到扩散模型

## 文章核心问题

能否利用万有引力定律——将数据点视为引力源、将生成过程视为沿引力场线运动——来构造一种全新的ODE式扩散模型？这种模型能否摆脱传统扩散模型对高斯假设的依赖？

## 主要结论

1. PFGM（泊松流生成模型）将数据点视为 $d+1$ 维空间中的引力源，生成过程沿着引力场线从远处运动到 $t=0$ 平面上的数据点。这是一个完全不同于传统高斯扩散模型的框架。
2. 在纯 $d$ 维空间中，引力场的各向同性会导致模式坍缩（部分引力源相互抵消，使得对应数据点无法生成）。这是连续分布假设下的必然结果。
3. 增加一维（$d \to d+1$）神奇地解决了模式坍缩问题：二维的"圆"在三维空间中不再是各向同性的，破坏了抵消条件，同时提供了清晰的终止信号（$t=0$）。
4. PFGM 不依赖高斯扰动核，而是基于泊松方程（万有引力定律的数学基础）来构造生成 ODE，突破了以往扩散模型的高斯假设局限。
5. 在 $t=T$ 平面上的先验分布为 $p_{prior}(\boldsymbol{x}) \propto (\Vert\boldsymbol{x}\Vert^2 + T^2)^{-(d+1)/2}$，可通过球坐标逆累积函数法采样。

## 推导结构

1. **万有引力场**：从牛顿万有引力定律出发，推广到 $d$ 维空间，引力场是泊松方程格林函数的梯度。
2. **场线生成**：观察发现大部分场线从远处出发终止于引力源，提出"沿场线从远处运动到数据点"的生成思想。
3. **等效质心**：远处任意多源引力场近似于质心单源引力场，保证各向同性和均匀球面采样。
4. **模式坍缩问题**：各向同性分布会在内部产生场抵消，导致某些数据点无法被生成。
5. **增加一维**：将数据从 $\mathbb{R}^d$ 提升到 $\mathbb{R}^{d+1}$，放在 $t=0$ 平面上，打破各向同性条件。
6. **场线ODE**：$d+1$ 维引力场 $\boldsymbol{F}=(\boldsymbol{F}_{\boldsymbol{x}},\boldsymbol{F}_t)$，生成 ODE 为 $\frac{d\boldsymbol{x}}{dt} = \boldsymbol{F}_{\boldsymbol{x}}/\boldsymbol{F}_t$。
7. **先验分布**：将 $d+1$ 维球面上的均匀分布通过几何相似投影到 $t=T$ 平面，推导出先验分布形式。
8. **训练目标**：利用 $\mathbb{E}[\boldsymbol{x}] = \arg\min \mathbb{E}[\Vert\boldsymbol{x} - \boldsymbol{\mu}\Vert^2]$ 的恒等式，构造回归训练目标来学习引力场。

## 关键公式

- **$d$ 维引力场（单源）**: $\boldsymbol{F}(\boldsymbol{x}) = -\frac{1}{S_d(1)}\frac{\boldsymbol{x} - \boldsymbol{y}}{\Vert \boldsymbol{x} - \boldsymbol{y}\Vert^d}$
- **$d+1$ 维引力场（多源）**: $\boldsymbol{F}(\boldsymbol{x}, t) = -\frac{1}{S_{d+1}(1)}\int\frac{(\boldsymbol{x} - \boldsymbol{x}_0, t)}{(\Vert\boldsymbol{x} - \boldsymbol{x}_0\Vert^2 + t^2)^{(d+1)/2}}\tilde{p}(\boldsymbol{x}_0) d\boldsymbol{x}_0$
- **生成ODE**: $\frac{d\boldsymbol{x}}{dt} = \frac{\boldsymbol{F}_{\boldsymbol{x}}}{\boldsymbol{F}_t}$
- **先验分布**: $p_{prior}(\boldsymbol{x}) \propto \frac{1}{(\Vert\boldsymbol{x}\Vert^2 + T^2)^{(d+1)/2}}$
- **径向先验**: $p_{prior}(r) \propto r^{d-1}(r^2 + T^2)^{-(d+1)/2}$
- **训练目标**: $\mathbb{E}_{\boldsymbol{x}_0\sim \tilde{p}(\boldsymbol{x}_0)}\left[\left\Vert\boldsymbol{s}_{\boldsymbol{\theta}}(\boldsymbol{x}, t) + \frac{(\boldsymbol{x} - \boldsymbol{x}_0, t)}{(\Vert\boldsymbol{x} - \boldsymbol{x}_0\Vert^2 + t^2)^{(d+1)/2}}\right\Vert^2\right]$

## 实验或案例

本文为理论介绍，未提供原始实验。引用PFGM原论文的实验结果：PFGM在FID/IS等指标上优于基线扩散模型，生成速度更快，对超参数和模型架构有更好的鲁棒性。该论文被NeurIPS 2022接收。

## 所属系列位置

本文是系列第13篇，引入了一个全新的物理类比框架（万有引力/PFGM），打破了此前高斯扩散的范式。它直接为第14篇（一般ODE构建框架中的各向同性解）提供了具体案例，同时也推动第14、15篇去构建更一般的ODE生成模型理论。

## 与其他文章的关系

- builds_on: [[生成扩散模型漫谈（十二）：“硬刚”扩散ODE]]（连续性方程为理解PFGM提供了背景）
- precedes: [[生成扩散模型漫谈（十四）：构建ODE的一般步骤（上）]]
- belongs_to: [[生成扩散模型漫谈]]
- references: PFGM论文（NeurIPS 2022）

## 原文证据锚点

- `ev::9305::万有引力`
- `ev::9305::沿场线走`
- `ev::9305::模式坍缩`
- `ev::9305::增加一维`
- `ev::9305::豁然开朗`
- `ev::9305::场的训练`
