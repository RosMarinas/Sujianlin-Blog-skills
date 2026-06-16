---
type: formula
title: GELU函数及其近似公式
aliases:
- GELU function and approximations
standard_notation: GELU函数及其近似公式
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
source_ids:
- '7309'
evidence_spans: []
latex: \text{GELU}(x)=x\Phi(x)=\frac12 x\left[1+\text{erf}\left(\frac{x}{\sqrt{2}}\right)\right],\quad
  \Phi(x)=\int_{-\infty}^x\frac{e^{-t^2/2}}{\sqrt{2\pi}}dt
symbol_meanings:
  \text{GELU}(x): GELU 激活函数值
  x: 输入变量
  \Phi(x): 标准正态累积分布函数
  \text{erf}: 误差函数
  t: 积分哑变量
  \pi: 圆周率
conditions: （待从源文章提取）
appears_in:
- '7309'
---
## 概述

（待补充）



## GELU精确形式

$$
\text{GELU}(x)=x\Phi(x)=\frac12 x\left[1+\text{erf}\left(\frac{x}{\sqrt{2}}\right)\right],\quad \Phi(x)=\int_{-\infty}^x\frac{e^{-t^2/2}}{\sqrt{2\pi}}dt
$$

## Sigmoid近似

$$
\text{GELU}(x) \approx x\sigma(1.702x)
$$

通过 $\min_\lambda\max_x|\Phi(x)-\sigma(\lambda x)|$ 全局优化得到 $\lambda=1.702$。

## Tanh近似

$$
\text{GELU}(x) \approx \frac12 x\left[1+\tanh\left(\sqrt{\frac{2}{\pi}}(x+0.044715x^3)\right)\right]
$$

局部泰勒展开（匹配 $x=0$ 处前两阶）+ 全局 min-max 优化混合所得。

## 所属系列

[[激活函数理论]]