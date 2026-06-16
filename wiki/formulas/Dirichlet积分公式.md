---
type: formula
title: Dirichlet积分公式
aliases:
  - sin_x/x积分公式
status: draft
updated: 2026-06-13
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-03-24-费曼积分法-5-欧拉数学的传承.md
source_ids:
  - "1629"
  - "1942"
latex: "\\int_0^\\infty \\frac{\\sin x}{x}dx = \\frac{\\pi}{2}"
symbol_meanings:
  "sin x/x": 被积函数，在x=0处有可去奇点
  "π/2": 积分值
standard_notation: "Dirichlet integral = π/2"
conditions: "积分收敛于广义Riemann积分意义下（条件收敛）"
appears_in:
  - article::1629
  - article::1942
  - proposition::Dirichlet积分求值
---

# Dirichlet积分公式


## 概述

（待补充）

## 详细说明

Dirichlet积分∫₀^∞ sin x/x dx = π/2是数学分析中最重要的条件收敛广义积分之一。该积分不能通过常规的Newton-Leibniz公式直接计算，需借助含参积分技巧。费曼积分法通过引入指数衰减因子e^{-ax}构造含参积分，利用Leibniz法则求导后积分还原，优雅地得到结果。该结果在傅里叶分析、信号处理中有广泛应用。

该积分在傅里叶分析、信号处理和数论中都有重要地位，是许多复杂积分推导的基础。