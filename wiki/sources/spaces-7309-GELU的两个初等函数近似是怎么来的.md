---
type: article_summary
title: GELU的两个初等函数近似是怎么来的
article_id: "7309"
source_url: https://spaces.ac.cn/archives/7309
date: 2020-03-26
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
source_ids:
  - "7309"
status: stable
updated: 2026-06-12
---

## 概述

本文探讨了高斯误差线性单元（GELU）激活函数的数学定义及其两个经典的初等函数近似形式的来源与推导过程。GELU精确定义为 $\text{GELU}(x) = x \Phi(x)$，其中 $\Phi(x)$ 是标准正态分布的累积分布函数（CDF）。为了在计算中规避误差函数 $\text{erf}(x)$ 的非初等计算开销，原论文提出了两个逼近形式。本文重现了这两个近似系数的计算原理：
1. **Logistic 逼近（Sigmoid 近似）**：
   $$ \Phi(x) \approx \sigma(\lambda x) $$
   利用全局 minimax 误差优化 $\min_{\lambda} \max_x |\Phi(x) - \sigma(\lambda x)|$，解得最优系数 $\lambda \approx 1.702$。
2. **双曲正切逼近（Tanh 近似）**：
   $$ \text{erf}(z) \approx \tanh(a z + b z^3) $$
   在 $z = 0$ 处进行局部一阶泰勒展开对齐，确定 $a = \sqrt{2/\pi}$。在此基础上，通过数值计算求解全局 minimax 误差优化问题，确定三次方项系数 $b \approx 0.035677$。折算到 $\text{GELU}(x)$ 的标准形式，得到 $x^3$ 项前系数为 $0.044715$。

## 关键数学公式

- **精确形式**： $\text{GELU}(x) = x \Phi(x) = \frac{1}{2} x \left[1 + \text{erf}\left(\frac{x}{\sqrt{2}}\right)\right]$
- **Sigmoid近似**： $\text{GELU}(x) \approx x \sigma(1.702 x)$
- **Tanh近似**： $\text{GELU}(x) \approx \frac{1}{2} x \left[1 + \tanh\left(\sqrt{\frac{2}{\pi}}\left(x + 0.044715 x^3\right)\right)\right]$
