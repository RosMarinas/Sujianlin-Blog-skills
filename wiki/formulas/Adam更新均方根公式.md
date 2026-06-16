---
type: formula
title: Adam更新均方根公式
aliases:
- Update RMS Formula
latex: \|\boldsymbol{u}_t\|_{RMS} \approx \sqrt{\frac{\|\boldsymbol{\mu}\|^2/\|\boldsymbol{\sigma}\|^2
  + \frac{1 - \beta_1}{1 + \beta_1}}{\|\boldsymbol{\mu}\|^2/\|\boldsymbol{\sigma}\|^2
  + 1}}
symbol_meanings:
  \beta: 二阶矩衰减系数 / 动量系数
  \boldsymbol{\mu}: boldsymbol{\mu} 参数
  \boldsymbol{\sigma}: boldsymbol{\sigma} 参数
  \boldsymbol{u}: boldsymbol{u} 参数
  t: 时间步 / 自变量
standard_notation: \|\boldsymbol{u}_t\|_{RMS} \approx \sqrt{\frac{\text{SNR} + \frac{1-\beta_1}{1+\beta_1}}{\text{SNR}
  + 1}} \quad \text{where} \quad \text{SNR} = \frac{\|\boldsymbol{\mu}\|^2}{\|\boldsymbol{\sigma}\|^2}
conditions: 模型训练进入正式稳态时刻 $t \to \infty$，且二阶矩平滑超参数 $\beta_2 \geq 0.9$，梯度在统计上可被近似建模为独立同分布。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
source_ids:
- '11267'
appears_in:
- '[[spaces-11267-为什么Adam的Update-RMS是0-2]]'
status: draft
null_evidence_reason: Initial compilation draft
updated: "2026-06-14"
---

## 概述

该公式给出了 Adam/AdamW 优化器更新均方根（Update RMS）的理论近似解析解。它将 Update RMS 与动量超参数 $\beta_1$ 和当前状态下的梯度信噪比（SNR）联系在一起。

当信噪比极低（纯噪声，$\boldsymbol{\mu} = \boldsymbol{0}$）时，公式简化为：

$$\|\boldsymbol{u}_t\|_{RMS} \approx \sqrt{\frac{1 - \beta_1}{1 + \beta_1}}$$

这解释了为什么在 $\beta_1 = 0.9$ 的常规设置下，Adam 的 Update RMS 会稳定在 $\sqrt{0.1/1.9} \approx 0.2294$（即约 0.2）附近。