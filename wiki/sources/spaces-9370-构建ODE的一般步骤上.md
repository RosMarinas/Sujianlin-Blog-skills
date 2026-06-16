---
type: article_summary
title: "生成扩散模型漫谈（十四）：构建ODE的一般步骤（上）"
article_id: "9370"
source_url: "https://spaces.ac.cn/archives/9370"
date: "2022-12-15"
category: "Big-Data"
source_markdown: "Data/Spaces_ac_cn/markdown/Big-Data/2022-12-15-生成扩散模型漫谈-十四-构建ODE的一般步骤-上.md"
series:
  - "[[生成扩散模型漫谈]]"
topics: []
concepts:
  - "[[无散度条件]]"
  - "[[格林函数方法]]"
  - "[[一般ODE构建框架]]"
methods:
  - "[[万有引力类比构造法]]"
problem_patterns: []
evidence_spans:
  - "ev::9370::基础结论"
  - "ev::9370::简化方程"
  - "ev::9370::格林函数"
  - "ev::9370::万有引力"
  - "ev::9370::时空分离"
  - "ev::9370::逆向构造"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-12-15-生成扩散模型漫谈-十四-构建ODE的一般步骤-上.md"
source_ids:
  - "9370"
status: draft
updated: "2026-06-09"
---

# 生成扩散模型漫谈（十四）：构建ODE的一般步骤（上）

## 文章核心问题

能否用数学系统地回答"什么样的力场适合构建ODE式生成扩散模型"？如何将第12篇的连续性方程和第13篇的PFGM统一到同一个理论框架下，并进一步开辟构造新ODE扩散模型的途径？

## 主要结论

1. 构造ODE扩散模型本质上是一个"松弛"问题：连续性方程是1个方程对 $d$ 个未知数，存在无穷多解。
2. 将连续性方程重新写为 $d+1$ 维散度为零的条件 $\nabla_{(t,\boldsymbol{x}_t)}\cdot\boldsymbol{u}=0$，其中 $\boldsymbol{u}=(p_t, \boldsymbol{f}_t p_t)$，这为使用格林函数方法铺平了道路。
3. 格林函数方法：先解决单个数据点 $\boldsymbol{x}_0$ 的"点源"问题，再通过积分叠加得到整个数据分布的解。
4. **各向同性解（引力解）**：假设 $d+1$ 维空间的完全各向同性，得到 $\boldsymbol{G} \propto (t, \boldsymbol{x}_t - \boldsymbol{x}_0) / (t^2 + \Vert\boldsymbol{x}_t - \boldsymbol{x}_0\Vert^2)^{(d+1)/2}$，这正是PFGM的引力场。其条件概率 $p_t(\boldsymbol{x}_t|\boldsymbol{x}_0) \propto t / (t^2 + \Vert\boldsymbol{x}_t - \boldsymbol{x}_0\Vert^2)^{(d+1)/2}$。
5. **时空分离解（高斯解）**：假设在 $\boldsymbol{x}_t$ 空间各向同性但时间独立，代入高斯条件概率后恢复标准高斯扩散ODE $\frac{d\boldsymbol{x}_t}{dt} = -\dot{\sigma}_t\sigma_t \nabla_{\boldsymbol{x}_t}\log p_t(\boldsymbol{x}_t)$。
6. 发现PFGM的训练采样方案（用正态分布构造比值）实际上精确地实现了各向同性格林函数的条件概率采样——这一"巧合"在原论文中未被指出。
7. 提出逆向构造法：直接构造累积概率函数 $\psi_t(r)$，通过微分得到 $\phi_t(r)$ 和 $\varphi_t(r)$，避免复杂积分。

## 推导结构

1. 从连续性方程出发，将其改写为 $d+1$ 维散度为零的形式。
2. 引入边界格林函数 $\boldsymbol{G}(t,0;\boldsymbol{x}_t,\boldsymbol{x}_0)$，定义其在 $t=0$ 的初值条件为 $\delta(\boldsymbol{x}_t - \boldsymbol{x}_0)$。
3. 一般解为 $\boldsymbol{u} = \mathbb{E}_{\boldsymbol{x}_0}[\boldsymbol{G}]$，格林函数第一分量即为条件概率 $p_t(\boldsymbol{x}_t|\boldsymbol{x}_0)$。
4. **各向同性假设**：$\boldsymbol{G} = \varphi(R)(t, \boldsymbol{x}_t - \boldsymbol{x}_0)$，代入散度为零条件推导出 $\varphi(R) = C \times R^{-(d+1)}$，得到引力解。
5. 验证引力解的边界条件：证明 $\int \boldsymbol{G}_1 d\boldsymbol{x}_t$ 与 $t,\boldsymbol{x}_0$ 无关，且 $t\to 0^+$ 时退化为 $\delta$ 函数。
6. 证明PFGM采样中 $\Vert\boldsymbol{\varepsilon}_{\boldsymbol{x}}\Vert/|\varepsilon_t|$ 服从所需的 $p(r) \propto r^{d-1}/(1+r^2)^{(d+1)/2}$ 分布。
7. **时空分离假设**：$\boldsymbol{G}_1 = \phi_t(r)$，$\boldsymbol{G}_{>1} = \varphi_t(r)(\boldsymbol{x}_t - \boldsymbol{x}_0)$，代入得到 $\varphi_t(r) = -\frac{1}{r^d}\frac{\partial}{\partial t}\int \phi_t(r) r^{d-1} dr$。代入高斯分布恢复标准结果。
8. **逆向构造**：直接设计 $\psi_t(r)$，通过 $\phi_t(r) = \frac{1}{r^{d-1}}\partial_r\psi_t(r)$ 和 $\varphi_t(r) = -\frac{1}{r^d}\partial_t\psi_t(r)$ 得到解析解。

## 关键公式

- **连续性方程**: $\frac{\partial}{\partial t} p_t(\boldsymbol{x}_t) = - \nabla_{\boldsymbol{x}_t}\cdot\Big(\boldsymbol{f}_t(\boldsymbol{x}_t) p_t(\boldsymbol{x}_t)\Big)$
- **散度为零形式**: $\nabla_{(t,\boldsymbol{x}_t)}\cdot\boldsymbol{u}(t,\boldsymbol{x}_t)=0,\quad \boldsymbol{u} = (p_t, \boldsymbol{f}_t p_t)$
- **格林函数问题**: $\nabla_{(t,\boldsymbol{x}_t)}\cdot\boldsymbol{G}=0,\quad \boldsymbol{G}_1(0,0;\boldsymbol{x}_t,\boldsymbol{x}_0) = \delta(\boldsymbol{x}_t - \boldsymbol{x}_0)$
- **一般解**: $\boldsymbol{u}(t,\boldsymbol{x}_t) = \int \boldsymbol{G}(t,0;\boldsymbol{x}_t,\boldsymbol{x}_0)p_0(\boldsymbol{x}_0) d\boldsymbol{x}_0$
- **各向同性格林函数**: $\boldsymbol{G}(t,0;\boldsymbol{x}_t,\boldsymbol{x}_0) \propto \frac{(t, \boldsymbol{x}_t - \boldsymbol{x}_0)}{(t^2 + \Vert\boldsymbol{x}_t - \boldsymbol{x}_0\Vert^2)^{(d+1)/2}}$
- **时空分离解公式**: $\varphi_t(r) = -\frac{1}{r^d}\frac{\partial}{\partial t}\int \phi_t(r) r^{d-1} dr$
- **逆向构造**: $\phi_t(r) = \frac{1}{r^{d-1}}\frac{\partial}{\partial r}\psi_t(r),\quad \varphi_t(r) = -\frac{1}{r^d}\frac{\partial}{\partial t}\psi_t(r)$

## 实验或案例

本文为纯理论推导，未提供实验。引用PFGM的实验结果说明即使在数学等价的框架下，实际效果仍有差异（引力ODE优于高斯ODE）。

## 所属系列位置

本文是系列第14篇（上），首次建立了一个统一的ODE扩散模型"生产车间"框架。它将第12篇的连续性方程和第13篇的PFGM统一在同一数学结构下，证明了二者分别是不同对称性假设下的特解。第15篇（中）将在此基础上用特征线法提出更强的构造方法。

## 与其他文章的关系

- builds_on: [[生成扩散模型漫谈（十二）：“硬刚”扩散ODE]]（连续性方程）
- builds_on: [[生成扩散模型漫谈（十三）：从万有引力到扩散模型]]（引力解作为特例）
- precedes: [[生成扩散模型漫谈（十五）：构建ODE的一般步骤（中）]]
- belongs_to: [[生成扩散模型漫谈]]

## 原文证据锚点

- `ev::9370::基础结论`
- `ev::9370::简化方程`
- `ev::9370::格林函数`
- `ev::9370::万有引力`
- `ev::9370::时空分离`
- `ev::9370::逆向构造`
