---
type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: Weiszfeld迭代法
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2026-03-31-中位数-Median-简介.md
source_ids:
  - 11693
method_summary: 通过不动点迭代计算方式，为无解析解的高维几何中位数（Fermat点）提供高效的近似数值求解算法。
typical_structure: |
  1. 设定一个初始中心点 $\boldsymbol{\mu}_0$（例如可以取所有数据点的算术平均值）。
  2. 计算所有样本点 $\boldsymbol{x}_i$ 到当前中心点 $\boldsymbol{\mu}_t$ 的欧氏距离 $\Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2$。
  3. 以距离的倒数 $1 / \Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2$ 作为权重，对所有数据点进行加权平均，计算得到下一个迭代点：
     $$ \boldsymbol{\mu}_{t+1} = \frac{\sum_{i=1}^n \boldsymbol{x}_i / \Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2}{\sum_{i=1}^n 1 / \Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2} $$
  4. 检查 $\Vert\boldsymbol{\mu}_{t+1} - \boldsymbol{\mu}_t\Vert$ 是否小于收敛阈值。若未收敛则重复步骤 2-3。
applicability: 适用于高维空间中需要抵御异常值（Outliers）干扰的中心点估计问题，如求解几何中位数（Geometric Median）或费马点（Fermat Point）。
evidence_spans:
  - ev::11693::"很遗憾，中位向量没有解析解，我们通常是基于如下Weiszfeld迭代来计算...将$\boldsymbol{\mu}_t$代入右端记为$\boldsymbol{\mu}_{t+1}$，即得不动点迭代法"
examples:
  - [[article::11693]]
status: stable
updated: 2026-06-13
---

# Weiszfeld迭代法

## 适用问题

在多维/高维空间中，当我们希望找到一组点集最具代表性的中心时，简单的算术平均值（Mean）由于优化目标是 $\sum \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2^2$，极易受到极端异常值的影响（崩溃点极低）。而优化目标为 $\sum \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2$ 的几何中位数（Geometric Median，亦称费马点）虽然抗干扰能力极强，但该优化问题在 $n \geq 3$ 时没有封闭形式的代数解析解，无法直接计算得出，需要一种高效的数值迭代逼近算法。

## 核心变换

将“求解导数为零的非线性超越方程”变换为“距离反比加权的不动点迭代”。通过令目标函数 $f(\boldsymbol{\mu}) = \sum \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2$ 的梯度等于零，代数整理后构造出一个显式的迭代更新格式，从而用一系列反复的加权平均操作代替复杂的梯度下降或黑盒数值优化。

## 典型步骤

1. **初始化**：选择一个起始猜测值 $\boldsymbol{\mu}_0$，通常直接使用均值 $\frac{1}{n}\sum \boldsymbol{x}_i$。
2. **计算距离倒数**：对每个数据点 $\boldsymbol{x}_i$，计算它与当前估计中心 $\boldsymbol{\mu}_t$ 之间的欧氏距离的倒数 $w_i^{(t)} = \frac{1}{\Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2}$。
3. **加权更新**：以 $w_i^{(t)}$ 作为归一化权重，计算所有点的新加权质心，作为下一步的估计值：
   $$
   \boldsymbol{\mu}_{t+1} = \frac{\sum_{i=1}^n w_i^{(t)} \boldsymbol{x}_i}{\sum_{i=1}^n w_i^{(t)}}
   $$
4. **收敛判定**：比较 $\boldsymbol{\mu}_{t+1}$ 与 $\boldsymbol{\mu}_t$ 的差值，如果足够小则停止，否则继续循环。

## 直觉

为什么是“距离越近，权重越大”？算术平均由于用的是平方距离，离得远的异常点产生的“拉力”（导数）非常大，因此均值会被异常点生生拽过去。而在几何中位数的导数方程中，每个点对中心施加的拉力大小其实是固定的（方向朝向自己，大小为单位向量）。如果强行要把这种等拉力写成类似“加权平均”的形式，那么原本离得远的异常点，为了保持它的绝对拉力不变，它对应的乘积权重就必须非常小；离得近的正常点，权重反而必须很大。这就是为什么 Weiszfeld 迭代中，距离倒数天然成为了加权因子的直观原因——它通过自动给远处的异常点降权，实现了稳健的中心估计。

## 边界

- **重合奇点问题**：如果某一次迭代估计 $\boldsymbol{\mu}_t$ 恰好落在了某个数据点 $\boldsymbol{x}_i$ 上，那么 $\Vert\boldsymbol{x}_i - \boldsymbol{\mu}_t\Vert_2 = 0$，此时公式的分母会出现除零错误。实际编程中通常在距离上加一个小常数 $\epsilon$ （如 $1e-8$）来防止数值溢出。
- **广义 $L_p$ 范数的非凸性**：Weiszfeld 迭代实际上是求解更广义最小化问题 $\sum \Vert\boldsymbol{x}_i - \boldsymbol{\mu}\Vert_2^{\alpha}$ 当 $\alpha=1$ 时的特例。如果 $\alpha < 1$，目标函数变得高度非凸，简单的迭代可能只会收敛到局部极小值。

## 例子

假设我们要在地图上为 4 个城市（A, B, C, D，其中 D 是一个离得很远的偏僻乡村）建立一个物流中心，使得物流中心到这 4 个城市的直线距离之和最短。如果用均值，物流中心会被严重拉向 D 村；如果使用 Weiszfeld 迭代，我们先把中心暂定在均值处，然后每一步中，由于 A, B, C 抱团距离新中心较近，它们的权重 $1/d$ 被急剧放大，而 D 的权重越来越小。经过几次迭代后，物流中心会稳稳地收敛回 A, B, C 的密集区域，甚至直接落在其中一个城市里。

## 证据

- ev::11693::"高维空间的平均值概念很容易推广...至于中位向量（几何中位数/费马点），没有解析解，我们通常是基于如下Weiszfeld迭代来计算...代入$\alpha=1$即得Weiszfeld迭代"
- ev::11693::"均值带来的损失是$(x_i - \mu)^2$，而中位数则是$|x_i - \mu|$...所以均值会更偏向于异常值，这样才能尽可能降低损失"
