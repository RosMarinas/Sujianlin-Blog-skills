---
type: article_summary
title: 生成扩散模型漫谈（十七）：构建ODE的一般步骤（下）
article_id: "9497"
source_url: https://spaces.ac.cn/archives/9497
date: 2023-02-23
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-02-23-生成扩散模型漫谈-十七-构建ODE的一般步骤-下.md
series:
  - "[[生成扩散模型漫谈]]"
concepts:
  - "[[矫流]]"
methods:
  - "[[矫流构造法]]"
evidence_spans:
  - ev::9497::直观结果
  - ev::9497::简单例子
  - ev::9497::证明过程
  - ev::9497::读后感受
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-02-23-生成扩散模型漫谈-十七-构建ODE的一般步骤-下.md
source_ids:
  - "9497"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文介绍了Rectified Flow（矫流），这是目前已知的最简单的构建ODE式扩散模型的方法：只需两步——(1) 选择一个插值轨迹，(2) 用神经网络学习该轨迹对时间的导数。

## 核心问题

在前两篇文章（第14篇"上"和第15篇"中"）中，作者已探索了两种构建ODE式扩散模型的框架，但都较为复杂。能否存在一种更加简单、直观、几乎"降维打击"式的构建方法？

## 关键结论

1. **两步构建法**：任何满足边界条件的连续插值轨迹$\boldsymbol{\varphi}_t$都可用来构造扩散ODE：第一步定义插值$\boldsymbol{x}_t = \boldsymbol{\varphi}_t(\boldsymbol{x}_0,\boldsymbol{x}_T)$，第二步学习速度场$\boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t,t)$逼近$\partial \boldsymbol{\varphi}_t/\partial t$。
2. **最优解为条件期望**：学习目标的最优解是$\boldsymbol{v}^*(\boldsymbol{x}_t, t) = \mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\partial \boldsymbol{\varphi}_t/\partial t]$，这由条件期望的MSE最优性给出。
3. **正确性证明**：最优解满足基本推进方程$\mathbb{E}_{\boldsymbol{x}_{t+\Delta t}}[\phi(\boldsymbol{x}_{t+\Delta t})] = \mathbb{E}_{\boldsymbol{x}_t}[\phi(\boldsymbol{x}_t + \boldsymbol{v}^*\Delta t)]$，从而确保ODE正确实现了分布变换。
4. **极简性的极限**：作者认为这是目前能想到的最简单构造，难以想象还有更简化的空间。

## 核心推导

证明的核心思路是使用"测试函数法"验证最优解满足连续性方程：

1. 从插值轨迹出发，对任意测试函数$\phi$写出$\mathbb{E}_{\boldsymbol{x}_{t+\Delta t}}[\phi(\boldsymbol{x}_{t+\Delta t})] = \mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_T}[\phi(\boldsymbol{\varphi}_{t+\Delta t})]$。
2. 泰勒展开到一阶：$\boldsymbol{\varphi}_{t+\Delta t} = \boldsymbol{\varphi}_t + \Delta t\,\partial\boldsymbol{\varphi}_t/\partial t + O(\Delta t^2)$。
3. 假设$\boldsymbol{\varphi}_t$对$\boldsymbol{x}_T$可逆，将$\partial\boldsymbol{\varphi}_t/\partial t$重新参数化为$\boldsymbol{x}_0,\boldsymbol{x}_t$的函数。
4. 通过边缘化技巧将期望从$(\boldsymbol{x}_0,\boldsymbol{x}_t)$空间转移到$\boldsymbol{x}_t$空间，利用条件期望$\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\partial \boldsymbol{\varphi}_t/\partial t]$。
5. 重新合并泰勒展开项获得$\mathbb{E}_{\boldsymbol{x}_t}[\phi(\boldsymbol{x}_t + \Delta t\,\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\partial \boldsymbol{\varphi}_t/\partial t])]$。
6. 由此读出ODE的漂移项必须为$\mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}[\partial \boldsymbol{\varphi}_t/\partial t]$，而最小二乘目标正好学习此条件期望。

## 关键公式

**一般插值轨迹**：
$$\boldsymbol{x}_t = \boldsymbol{\varphi}_t(\boldsymbol{x}_0, \boldsymbol{x}_T)$$
边界条件：$\boldsymbol{x}_0 = \boldsymbol{\varphi}_0(\boldsymbol{x}_0, \boldsymbol{x}_T)$，$\boldsymbol{x}_T = \boldsymbol{\varphi}_T(\boldsymbol{x}_0, \boldsymbol{x}_T)$

**学习目标**：
$$\mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_T}\left[\left\Vert \boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t) - \frac{\partial \boldsymbol{\varphi}_t(\boldsymbol{x}_0, \boldsymbol{x}_T)}{\partial t}\right\Vert^2\right]$$

**线性插值（Rectified Flow）**：
$$\boldsymbol{x}_t = (\boldsymbol{x}_1 - \boldsymbol{x}_0)t + \boldsymbol{x}_0$$
$$\frac{\partial \boldsymbol{\varphi}_t}{\partial t} = \boldsymbol{x}_1 - \boldsymbol{x}_0$$
$$\text{目标：}\mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_t}\left[\left\Vert \boldsymbol{v}_{\boldsymbol{\theta}}(\boldsymbol{x}_t, t) - \frac{\boldsymbol{x}_t - \boldsymbol{x}_0}{t}\right\Vert^2\right]$$

**最优解**：
$$\boldsymbol{v}^*(\boldsymbol{x}_t, t) = \mathbb{E}_{\boldsymbol{x}_0|\boldsymbol{x}_t}\left[\frac{\partial \boldsymbol{\varphi}_t}{\partial t}\right] = \mathop{\text{argmin}}_{\boldsymbol{v}} \mathbb{E}_{\boldsymbol{x}_0,\boldsymbol{x}_T}\left[\Vert \boldsymbol{v}(\boldsymbol{x}_t, t) - \partial \boldsymbol{\varphi}_t/\partial t\Vert^2\right]$$

## 实验或案例

本文为纯方法论介绍，没有实验验证。文中以线性插值（即Rectified Flow本身）作为简单例子展示了两步构建法的具体应用，指出该结果与第15篇"中"的"直线轨迹"例子完全一致。

## 系列定位

本文是"构建ODE的一般步骤"三部曲的最终篇（前两篇为第14篇"上"和第15篇"中"），提供了一个在简洁性上远超前两篇的构造方案。作者认为这种方法已经简单到难以进一步简化的程度。更重要的是，Rectified Flow的极简形式为后续第20篇（从ReFlow到WGAN-GP）奠定了关键基础。
