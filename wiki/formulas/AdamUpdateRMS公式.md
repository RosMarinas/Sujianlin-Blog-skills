---
title: Adam Update RMS渐近公式
type: formula
standard_notation: Adam Update RMS渐近公式
tags:
- Adam
- Update RMS
- 平均场
- SNR
status: draft
updated: '2026-06-14'
source_ids:
- '11267'
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
latex: \|\boldsymbol{u}_t\|_{RMS} \approx \sqrt{\frac{1 - \beta_1}{1 + \beta_1}}
symbol_meanings:
  \|\boldsymbol{u}_t\|_{RMS}: Adam 更新向量的 RMS 范数
  \beta_1: Adam 一阶动量衰减系数（默认 0.9）
conditions: （待从源文章提取）
appears_in:
- '11267'
---
# Adam Update RMS渐近公式


## 概述

（待补充）

## 平均场近似
E[u_t^2] ~ (mu^2 + (1-beta1)/(1+beta1)*sigma^2) / (mu^2 + sigma^2)

## RMS
||u_t||_RMS ~ sqrt((||mu||^2/||sigma||^2 + (1-beta1)/(1+beta1)) / (||mu||^2/||sigma||^2 + 1))

## 纯噪声近似(mu=0)
||u_t||_RMS ~ sqrt((1-beta1)/(1+beta1))，代入beta1=0.9得0.2294