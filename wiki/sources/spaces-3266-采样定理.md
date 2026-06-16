---
type: article_summary
title: 采样定理：有限个点构建出整个函数
article_id: "3266"
source_url: https://spaces.ac.cn/archives/3266
date: 2015-04-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2015-04-16-采样定理-有限个点构建出整个函数.md
series: []
topics:
  - 采样与估计
  - 信号处理
concepts:
  - Nyquist-Shannon sampling theorem
  - Fourier transform
  - bandlimited function
  - sinc interpolation
methods:
  - 采样定理重建
problem_patterns: []
evidence_spans:
  - "3266::采样定理：有限个点构建出整个函数"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2015-04-16-采样定理-有限个点构建出整个函数.md
source_ids:
  - "3266"
status: draft
updated: 2026-06-10
---

## 文章核心问题

为什么有限个采样点可以完整恢复一个连续信号？Nyquist-Shannon采样定理的推导。

## 主要结论

- 带限函数（频域支撑在 $[-W,W]$ 内）可以被离散采样完全重建
- 重建公式：$f(t)=\sum_{n=-\infty}^{+\infty} f(\frac{n\pi}{W})\frac{\sin(n\pi-Wt)}{n\pi-Wt}$
- sinc插值：每个采样点用sinc函数加权叠加即可恢复原函数

## 推导结构

1. 傅里叶变换将时域信号映射到频域
2. 若信号带限（$F(\omega)=0$ for $|\omega|>W$），将 $F(\omega)$ 展开为傅里叶级数
3. 代入逆变换并交换求和与积分，得到sinc插值公式
4. 系数正好是采样点处的函数值 $f(n\pi/W)$

## 关键公式

$$F(\omega)=\int_{-\infty}^{+\infty}f(t)e^{i\omega t}dt,\quad f(t)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}F(\omega)e^{-i\omega t}d\omega$$

$$f(t)=\sum_{n=-\infty}^{+\infty}f\left(\frac{n\pi}{W}\right)\frac{\sin(n\pi-Wt)}{n\pi-Wt}$$

## 体现的方法

- 采样定理重建：带限函数的离散采样与连续重建

## 所属系列位置

单篇独立文章。

## 与其他文章的关系

采样定理是本批次中"采样"主题的基础理论之一，与采样作为估计手段的核心思想一致。

## 原文证据锚点

- 完整推导：全文
