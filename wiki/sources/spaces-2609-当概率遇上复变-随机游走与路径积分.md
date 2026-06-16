---
type: article_summary
title: 当概率遇上复变：随机游走与路径积分
article_id: "2609"
source_url: https://spaces.ac.cn/archives/2609
date: 2014-06-04
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2014-06-04-当概率遇上复变-随机游走与路径积分.md
series:
  - "[[当概率遇上复变]]"
topics:
  - "[[解析概率]]"
concepts:
  - "[[路径积分]]"
methods:
  - "[[用路径积分表示随机过程转移概率]]"
problem_patterns: []
evidence_spans:
  - ev::2609::路径积分思想
  - ev::2609::随机游走路径积分
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2014-06-04-当概率遇上复变-随机游走与路径积分.md
source_ids:
  - "2609"
status: draft
updated: 2026-06-11
---

# 当概率遇上复变：随机游走与路径积分

## 文章核心问题
引入费曼路径积分思想，构建随机游走的路径积分描述方式，展示如何将离散路径转移概率的连乘积在连续极限下写成路径作用量的指数积分形式。

## 主要结论
1. 路径积分不同于只关注终点概率密度的传统方法，它考虑的是事件沿着某条具体路径发生的概率，并将所有可能路径的概率进行积分测度累加。
2. 粒子在划分的极小时间间隔 $\Delta t$ 内，由位置 $x_i$ 转移到 $x_{i+1}$ 的概率满足正态分布。
3. 粒子沿特定连续路径 $x(t)$ 运动的概率密度，在 $\Delta t \to 0$ 时正比于以速度速度平方 $\dot{x}^2$ 为核心的积分指数：$\exp\left(-\int \frac{\dot{x}^2}{2\alpha} dt\right)$。
4. 粒子的总转移概率可以写为全部路径积分之和，即：
   $\frac{1}{\sqrt{2\pi\alpha t}} \exp\left(-\frac{(x_n-x_0)^2}{2\alpha t}\right) = \int \exp\left(-\int \frac{\dot{x}^2}{2\alpha} dt\right) \mathcal{D}x(t)$。

## 推导结构
1. 引入探讨：辨析随机游走与高斯正态分布谁更本质，引出更深刻的描述方式——路径积分。
2. 路径积分思想：介绍费曼在量子力学中首创的路径积分，说明其直观思想（把所有路径概率相加）及在现代物理学中的中心地位。
3. 路径概率推导：将总时间 $t$ 划分为 $n$ 份，利用高斯概率密度核写出经过一系列中间点 $x_1, \dots, x_{n-1}$ 的联合概率密度连乘形式。
4. 连续极限：将连乘积放到指数中，取 $\Delta t \to 0$，把差分项 $\frac{(x_{i+1}-x_i)^2}{\Delta t^2} \Delta t$ 转化为速度导数积分 $\int \dot{x}^2 dt$。
5. 转移概率总和：将联合概率对所有中间位置积分，写成作用量路径积分 $\int \exp(-S) \mathcal{D}x(t)$ 形式。

## 关键公式
- 单步高斯核：$\frac{1}{\sqrt{2\pi\alpha \Delta t}} \exp\left(-\frac{(x_{i+1}-x_i)^2}{2\alpha \Delta t}\right)$
- 极小步长差分乘积：$\exp\left(-\sum \frac{(x_{i+1}-x_i)^2}{2\alpha \Delta t}\right)$
- 路径作用量指数：$\exp\left(-\int\frac{\dot{x}^2}{2\alpha}dt\right)$
- 路径积分表示式：$\int \exp\left(-\int\frac{\dot{x}^2}{2\alpha}dt\right)\mathcal{D}x(t)$

## 体现的方法
- [[用路径积分表示随机过程转移概率]]

## 所属系列位置
- [[当概率遇上复变]] 系列第 3 篇，为随机游走提供路径积分/作用量物理图景。

## 与其他文章的关系
- 使用第二篇导出的高斯单步转移密度作为推导的出发点；与相似矩阵（矩阵力学）形成量子力学三种等价表达形式的互补认知（薛定谔波动力学、海森堡矩阵力学、费曼路径积分）。

## 原文证据锚点
- `ev::2609::路径积分思想`: 原文第18行至第27行，介绍费曼路径积分的核心思想及其在物理学中的重要地位。
- `ev::2609::随机游走路径积分`: 原文第28行至第52行，通过细分时间步和高斯转移密度连乘，推导出随机游走的路径积分表示与连续作用量公式。
