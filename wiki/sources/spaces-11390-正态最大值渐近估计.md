---
type: article_summary
title: n个正态随机数的最大值的渐近估计
article_id: "11390"
source_url: https://spaces.ac.cn/archives/11390
date: 2025-11-06
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-11-06-n个正态随机数的最大值的渐近估计.md
series: []
topics:
  - 采样与估计
  - 极值统计
concepts:
  - order statistics
  - Laplace Approximation
  - inverse transform sampling
  - extreme value distribution
methods:
  - Jensen-Exponential bounds for maxima estimation
  - Laplace approximation for maxima
  - Inverse-transform sampling estimation
problem_patterns: []
evidence_spans:
  - "11390::先看结论"
  - "11390::快速上界"
  - "11390::拉普拉斯"
  - "11390::逆变采样"
  - "11390::应用例子"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-11-06-n个正态随机数的最大值的渐近估计.md
source_ids:
  - "11390"
status: draft
updated: 2026-06-10
---

## 文章核心问题

估计 $n$ 个独立标准正态随机数 $z_1,\dots,z_n\sim\mathcal{N}(0,1)$ 的最大值 $z_{\max}=\max\{z_1,\dots,z_n\}$ 的数学期望 $\mathbb{E}[z_{\max}]$ 的渐近行为。

## 主要结论

基本渐近结果：$\mathbb{E}[z_{\max}] \sim \sqrt{2\log n}$，更精确的近似为 $\mathbb{E}[z_{\max}] \sim \sqrt{2\log\frac{n}{\sqrt{2\pi}}}$。并用该结果估计了低精度Attention中重复最大值的出现概率。

## 推导结构

给出三种证明方法：
1. **Jensen+指数上界**：利用 $\exp$ 的凸性、Jensen不等式和$\sum$替代$\max$，得到 $\mathbb{E}[z_{\max}] \leq \sqrt{2\log n}$，且该上界恰好是渐近精确的。
2. **拉普拉斯近似**：先求 $z_{\max}$ 的CDF $[\Phi(z)]^n$ 和PDF，再用拉普拉斯近似（在模式点 $z_*$ 处展开）得到渐近估计。
3. **逆变采样**：利用 $\Phi(z_{\max})$ 是均匀分布最大值，通过 $\Phi^{-1}$ 映射回正态尺度。

## 关键公式

$$\mathbb{E}[z_{\max}] \leq \frac{\log n}{t} + \frac{t}{2} \quad \text{(优化后)} \quad \mathbb{E}[z_{\max}] \leq \sqrt{2\log n}$$

$$p_{\max}(z) = n[\Phi(z)]^{n-1} p(z),\quad p(z)=\frac{e^{-z^2/2}}{\sqrt{2\pi}}$$

$$\Phi(z) \sim 1 - \frac{e^{-z^2/2}}{z\sqrt{2\pi}}$$

## 体现的方法

- 方法：通过Jensen+指数上界估计极值期望
- 方法：拉普拉斯近似估计最大值分布
- 方法：逆变换采样思想估计期望

## 所属系列位置

单篇，不属于现有系列。

## 与其他文章的关系

应用链接到低精度Attention（文章11371）。估计方法本身是极值统计和采样理论的通用工具。

## 原文证据锚点

- 主要结论：先看结论节
- Jensen上界证明：快速上界节
- 拉普拉斯近似：拉普拉斯节、近似求解节
- 逆变换采样：逆变采样节
- 应用：应用例子节
