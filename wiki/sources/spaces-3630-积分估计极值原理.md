---
type: article_summary
title: 积分估计的极值原理——变分原理的初级版本
article_id: "3630"
source_url: https://spaces.ac.cn/archives/3630
date: 2016-02-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-02-15-积分估计的极值原理-变分原理的初级版本.md
series: []
topics:
  - 采样与估计
  - 变分法
concepts:
  - Jensen's inequality
  - variational principle
  - integral estimation
  - Laplace method
methods:
  - 积分估计的极值原理
problem_patterns: []
evidence_spans:
  - "3630::从高斯型积分出发"
  - "3630::我的总结"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-02-15-积分估计的极值原理-变分原理的初级版本.md
source_ids:
  - "3630"
status: draft
updated: 2026-06-10
---

## 文章核心问题

用极值原理（Jensen不等式）估计难以解析计算的积分，作为变分原理的有限维前奏。

## 主要结论

- 对积分 $I(\epsilon)=\int_{-\infty}^{\infty} e^{-x^2-\epsilon x^4}dx$，引入自由参数 $p$，用高斯积分 $\sqrt{\pi/p}$ 作为近似
- 使用Jensen不等式得到下界，通过最大化下界确定最优 $p$
- 该估计同时提供了下界和解析近似

## 推导结构

1. 将积分改写为权重 $e^{-px^2}$ 下的期望形式
2. 用Jensen不等式将期望提到指数外：$\langle e^{h(x)}\rangle \geq e^{\langle h(x)\rangle}$
3. 求 $\langle h(x)\rangle$ 解析形式，得到 $p$ 的函数下界
4. 最大化下界得到最优 $p$ 的方程

## 关键公式

$$I(\epsilon) = \sqrt{\frac{\pi}{p}} \left\langle e^{(p-1)x^2-\epsilon x^4} \right\rangle_{p}$$

$$I(\epsilon) \geq \sqrt{\frac{\pi}{p}}\exp\left[\frac{2(p-1)p-3\epsilon}{4p^2}\right]$$

$$p_* = \frac{1}{2}(\sqrt{12\epsilon+1}+1)$$

## 体现的方法

- 积分估计极值原理：用Jensen不等式构造可调参数的积分下界，通过变分优化获得最佳估计

## 所属系列位置

单篇，可视为"变分原理的初级版本"。

## 与其他文章的关系

与11390的Jensen上界证明在技术上相通（都使用Jensen不等式和指数凸性），是本批次中"估计/采样代替精确计算"的又一实例。

## 原文证据锚点

- 方法核心：从高斯型积分出发节
- 优缺点总结：我的总结节
