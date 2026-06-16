---
title: 去噪自编码器最优解
type: formula
status: draft
standard_notation: 去噪自编码器最优解
updated: '2026-06-14'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
latex: r(\boldsymbol{x}+\boldsymbol{\varepsilon}) = \arg\min_r \mathbb{E}[\|r(\boldsymbol{x}+\boldsymbol{\varepsilon}) - \boldsymbol{x}\|^2] = \boldsymbol{x} + \sigma^2 \nabla_{\boldsymbol{x}} \log \tilde{p}(\boldsymbol{x})
symbol_meanings:
  r: 去噪函数
  \boldsymbol{x}: 原始数据样本
  \boldsymbol{\varepsilon}: 高斯噪声 $\mathcal{N}(0, \sigma^2\boldsymbol{I})$
  \tilde{p}: 加噪后的数据分布
  \sigma^2: 噪声方差
conditions: （待从源文章提取）
appears_in:
- （待从源文章提取）
---

# 去噪自编码器最优解


## 概述

（待补充）

## Optimal Denoiser
若 x ~ p(x), ε ~ N(0, σ²I), 则:
r(x+ε) = argmin_r E[||r(x+ε) - x||²] = x + σ² ∇_x log p̃(x)

其中 p̃ = p * u 为加噪分布。

## Score Function Connection
∇_x log p̃(x) = (r(x) - x) / σ²

## Related Methods
- [[methods/denoising-score-matching]]
- [[sources/spaces-7038-去噪自编码器]]