---
type: article_summary
title: 用狄拉克函数来构造非光滑函数的光滑近似
article_id: "8718"
source_url: https://spaces.ac.cn/archives/8718
date: 2021-10-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-10-10-用狄拉克函数来构造非光滑函数的光滑近似.md
series: []
topics:
  - 函数逼近论
  - 激活函数
concepts:
  - 狄拉克函数
  - 光滑近似
  - ReLU
  - GELU
  - Swish
  - SoftPlus
methods:
  - 狄拉克函数光滑近似法
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-10-10-用狄拉克函数来构造非光滑函数的光滑近似.md
source_ids:
  - "8718"
status: draft
updated: 2026-06-10
---

## 总结

本文介绍一种通用方法：用狄拉克函数的光滑近似来构造任意非光滑函数（有可数个间断点）的光滑近似。核心恒等式 $f(x)=\int f(y)\delta(x-y)dy$ 将光滑近似问题转化为找 $\delta(x)$ 的光滑近似。作为应用导出ReLU的各种常见光滑近似（SoftPlus, Swish, GELU）以及取整函数的光滑近似。

## 关键思想

- 狄拉克函数核心性质：$\int_{-\infty}^{\infty} f(x)\delta(x)dx = f(0)$
- 光滑近似构造：$g(x)=\int f(y)\varphi(x-y)dy$，$\varphi\approx\delta$ 光滑
- 常用的 $\delta$ 近似：正态分布钟形曲线 $\frac{e^{-x^2/2\sigma^2}}{\sqrt{2\pi}\sigma}$ 或 sigmoid的导数 $\frac{e^{tx}t}{(1+e^{tx})^2}$
- ReLU近似：$\max(x,0)=\int_0^\infty \delta(x-y)y\,dy$ 代入不同 $\delta$ 近似得 SoftPlus/Swish/GELU

## 所属系列

[[函数逼近论]] — [[激活函数理论]]
