---
type: article_summary
title: 用狄拉克函数来构造非光滑函数的光滑近似
article_id: "8718"
source_url: https://spaces.ac.cn/archives/8718
date: 2021-10-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-10-10-用狄拉克函数来构造非光滑函数的光滑近似.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-10-10-用狄拉克函数来构造非光滑函数的光滑近似.md
source_ids:
  - "8718"
status: stable
updated: 2026-06-12
---

## 概述

本文介绍了一种利用狄拉克函数（Dirac delta）构造非光滑函数光滑近似的通用方法。核心思路是利用狄拉克函数的重要恒等式 $\int_{-\infty}^{\infty} f(y)\delta(x-y) dy = f(x)$，通过将 $\delta(x)$ 替换为其光滑近似 $\varphi(x)$，得到 $g(x) = \int_{-\infty}^{\infty} f(y)\varphi(x-y) dy$ 作为 $f(x)$ 的光滑近似。由于卷积核 $\varphi$ 是光滑的，$g(x)$ 自然也是光滑的。

作为应用示例，文章推导了ReLU函数 $\max(x,0)$ 的多种常见近似：
1. 用sigmoid导数的极限形式 $\delta(x) = \lim_{t\to\infty} \frac{e^{tx}t}{(1+e^{tx})^2}$，推导出SoftPlus激活函数 $\log(1+e^{tx})/t$。
2. 用高斯核 $\delta(x) = \lim_{\sigma\to 0} \frac{e^{-x^2/2\sigma^2}}{\sqrt{2\pi}\sigma}$，推导出含 $\text{erf}$ 的GELU型近似。
3. 利用 $\max(x,0) = x\theta(x)$ 以及sigmoid作为阶跃函数近似，得到Swish激活函数 $x\sigma(tx)$ 和GELU激活函数。

文章还以此方法推导了下取整函数 $[x]$ 的光滑近似。

## 关键数学公式

- **狄拉克光滑近似卷积通式**：$g(x) = \int_{-\infty}^{\infty} f(y)\varphi(x-y) dy$
- **SoftPlus（从Dirac推导）**：$\max(x,0) \approx \frac{\log(1+e^{tx})}{t}$
- **GELU（从Dirac推导）**：$\max(x,0) \approx \frac{1}{2}\left[x + x\,\text{erf}\left(\frac{x}{\sqrt{2}\sigma}\right)\right]$
