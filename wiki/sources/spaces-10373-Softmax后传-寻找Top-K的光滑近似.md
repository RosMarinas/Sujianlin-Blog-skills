---
type: article_summary
title: Softmax后传：寻找Top-K的光滑近似
article_id: 10373
source_url: "https://spaces.ac.cn/archives/10373"
date: 2024-09-19
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
series: []
topics:
  - [[概率分布构建]]
concepts:
  - [[可微Top-K算子]]
methods:
  - [[二分法求解待定阈值]]
  - [[stop_gradient自定义反向传播]]
evidence_spans:
  - ev::10373::问题描述
  - ev::10373::作为梯度
  - ev::10373::作为梯度
  - ev::10373::待定常数
  - ev::10373::解析求解
  - ev::10373::通用结果
  - ev::10373::二者兼之
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-09-19-Softmax后传-寻找Top-K的光滑近似.md
source_ids:
  - 10373
status: draft
updated: 2026-06-11
---

# Softmax后传：寻找Top-K的光滑近似

## 文章核心问题

寻找离散Top-K算子的连续光滑近似（可微Top-K算子），并解决反向传播求导、参数估计以及数值计算稳定性的难题。

## 主要结论

- **问题描述**: Top-k算子可以用最大k分量和的梯度表达：T_k(x) = grad(sum_{i in Omega_k} x_i)。
- **作为梯度**: 利用logsumexp近似最大k分量和，对其求梯度得到GradTopK公式，满足单调、不变和趋近性。
- **作为梯度**: GradTopK的分子分母可以通过递归计算，但在k较大或方差较大时存在数值溢出（log 0）问题。
- **待定常数**: ThreTopK公式通过待定常数lambda保证分量和为k，类似于Sparsemax。
- **解析求解**: 对于f(x) = min(1, e^x)，ThreTopK存在解析解，且在k=1时退化为Softmax，但非处处光滑。
- **通用结果**: 对于f(x) = sigmoid(x)，需要二分法或牛顿法数值求解lambda，并通过隐式微分自定义反向传播。
- **二者兼之**: 设计分段S型函数可使ThreTopK全局光滑且能解析求解lambda，且在k=1时退化为Softmax。

