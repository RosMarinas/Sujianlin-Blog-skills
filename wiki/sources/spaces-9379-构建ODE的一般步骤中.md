---
type: article_summary
title: "生成扩散模型漫谈（十五）：构建ODE的一般步骤（中）"
article_id: "9379"
source_url: "https://spaces.ac.cn/archives/9379"
date: "2022-12-22"
category: "Big-Data"
source_markdown: "Data/Spaces_ac_cn/markdown/Big-Data/2022-12-22-生成扩散模型漫谈-十五-构建ODE的一般步骤-中.md"
series:
  - "[[生成扩散模型漫谈]]"
topics: []
concepts:
  - "[[特征线法]]"
  - "[[一般ODE构建框架]]"
methods:
  - "[[特征线ODE构造法]]"
problem_patterns: []
evidence_spans:
  - "ev::9379::几何直观"
  - "ev::9379::特征线法"
  - "ev::9379::训练目标"
  - "ev::9379::直线轨迹"
  - "ev::9379::效果演示"
  - "ev::9379::一般推广"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2022-12-22-生成扩散模型漫谈-十五-构建ODE的一般步骤-中.md"
source_ids:
  - "9379"
status: draft
updated: "2026-06-09"
---

# 生成扩散模型漫谈（十五）：构建ODE的一般步骤（中）

## 文章核心问题

能否用更直观、更强大的方法——一阶偏微分方程的特征线法——来构造ODE扩散模型？能否同时保证初值条件（轨迹经过数据点）和终值条件（先验分布简单可采样），并允许任意简单分布作为先验？

## 主要结论

1. "轨迹优先"设计思路：直接设计单点轨迹 $\boldsymbol{\varphi}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = \boldsymbol{x}_T$（如直线），自动满足初值条件（轨迹经过 $\boldsymbol{x}_0$），然后通过微分得到力场 $\boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0)$。
2. 特征线法可以同时保证初值和终值条件：沿ODE轨迹将连续性方程转化为常微分方程，得到 $p_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = p_T(\boldsymbol{x}_T) \exp(\int_t^T \nabla\cdot\boldsymbol{f}_s ds)$，代入终值条件即可确定格林函数。
3. 无条件力场是条件力场的后验期望：$\boldsymbol{f}_t(\boldsymbol{x}_t) = \mathbb{E}_{\boldsymbol{x}_0\sim p_t(\boldsymbol{x}_0|\boldsymbol{x}_t)}[\boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0)]$，训练目标为条件流匹配（Conditional Flow Matching），与Flow Matching论文（Lipman et al., 2022）一致。
4. 该方法允许任意简单分布作为先验分布 $p_T(\boldsymbol{x}_T)$，不限于高斯分布。这是通过特征线法同时满足初值和终值条件的能力带来的。
5. 直线轨迹假设已足够：即使单点轨迹是直线，多点生成的聚合轨迹也会变成复杂曲线。更复杂的单点轨迹假设会导致不必要的训练不稳定。

## 推导结构

1. **回顾**：重述第14篇的连续性方程、$d+1$ 维散度为零形式和格林函数方法。
2. **几何直观**：直接设计轨迹簇 $\boldsymbol{\varphi}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = \boldsymbol{x}_T$，通过对时间求导得到 $\boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0)$。这自动保证初值条件——所有轨迹都经过 $\boldsymbol{x}_0$。
3. **特征线法**：沿特征线（ODE轨迹）将连续性方程改写为全微分形式 $\frac{d}{dt}p_t = -p_t \nabla\cdot\boldsymbol{f}_t$，解为 $p_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = p_T(\boldsymbol{x}_T) \exp(\int_t^T \nabla\cdot\boldsymbol{f}_s ds)$。代入终值条件 $p_T(\boldsymbol{x}_T)$ 即完全确定格林函数。
4. **训练目标**：无条件力场 $\boldsymbol{f}_t(\boldsymbol{x}_t)$ 是条件力场的后验期望，通过最小二乘恒等式得到条件流匹配目标。
5. **直线轨迹例子**：$\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t\boldsymbol{x}_1$，得到 $\boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = (\boldsymbol{x}_t - \boldsymbol{x}_0)/t$ 和 $p_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = p_1(\boldsymbol{x}_1)/t^d$。
6. **一般化**：扩展到 $\boldsymbol{x}_t = \boldsymbol{\mu}_t(\boldsymbol{x}_0) + \sigma_t \boldsymbol{x}_1$，恢复Flow Matching的一般公式。
7. **复杂度论证**：通过1D可视化演示直线单点轨迹产生弯曲聚合轨迹，论证复杂单点轨迹假设的不必要性。

## 关键公式

- **轨迹函数**: $\boldsymbol{\varphi}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = \boldsymbol{x}_T$
- **条件力场**: $\boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = -(\partial\boldsymbol{\varphi}_t/\partial\boldsymbol{x}_t)^{-1} \partial\boldsymbol{\varphi}_t/\partial t$
- **特征线解**: $p_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = p_T(\boldsymbol{x}_T) \exp(\int_t^T \nabla_{\boldsymbol{x}_s}\cdot \boldsymbol{f}_s(\boldsymbol{x}_s|\boldsymbol{x}_0) ds)$
- **无条件力场**: $\boldsymbol{f}_t(\boldsymbol{x}_t) = \mathbb{E}_{\boldsymbol{x}_0\sim p_t(\boldsymbol{x}_0|\boldsymbol{x}_t)}[\boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0)]$
- **条件流匹配目标**: $\mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_t \sim p_t(\boldsymbol{x}_t|\boldsymbol{x}_0)p_0(\boldsymbol{x}_0)}\left[\left\Vert \boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t) - \boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0)\right\Vert^2\right]$
- **直线轨迹**: $\boldsymbol{x}_t = (1-t)\boldsymbol{x}_0 + t\boldsymbol{x}_1,\quad \boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = (\boldsymbol{x}_t - \boldsymbol{x}_0)/t$
- **一般线性扩散**: $\boldsymbol{x}_t = \boldsymbol{\mu}_t(\boldsymbol{x}_0) + \sigma_t \boldsymbol{x}_1,\quad \boldsymbol{f}_t(\boldsymbol{x}_t|\boldsymbol{x}_0) = \dot{\boldsymbol{\mu}}_t(\boldsymbol{x}_0) + \frac{\dot{\sigma}_t}{\sigma_t}(\boldsymbol{x}_t - \boldsymbol{\mu}_t(\boldsymbol{x}_0))$

## 实验或案例

提供了一个1D数值演示（使用Python + scipy.integrate.odeint）：在4个数据点（位置0.5、0.5、1.2、1.7）和均匀先验 $U[0,2]$ 的设定下，即使单点轨迹是直线，聚合后的ODE轨迹也呈现弯曲，直观演示了"简单单点轨迹→复杂聚合轨迹"的涌现现象。

## 所属系列位置

本文是系列第15篇（中），是第14篇（上）的直接续篇和深化。它用特征线法改进了第14篇的格林函数方法，提供了更直观、更强大的ODE构造框架，并自然导出与Flow Matching等价的训练目标。这是整个ODE构造理论的"升级版"，后续可能还有第16篇（下）。

## 与其他文章的关系

- continues: [[生成扩散模型漫谈（十四）：构建ODE的一般步骤（上）]]
- builds_on: [[生成扩散模型漫谈（十二）：“硬刚”扩散ODE]]（评论区@gaohuazuo的见解启发了本文）
- belongs_to: [[生成扩散模型漫谈]]
- references: Flow Matching (Lipman et al., 2022)

## 原文证据锚点

- `ev::9379::几何直观`
- `ev::9379::特征线法`
- `ev::9379::训练目标`
- `ev::9379::直线轨迹`
- `ev::9379::效果演示`
- `ev::9379::一般推广`
