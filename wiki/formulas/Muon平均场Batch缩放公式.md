---
type: formula
title: Muon平均场Batch缩放公式
aliases: null
latex: \eta^* \approx \frac{\eta_{max}}{\sqrt{1+\mathcal{B}_{simple}/B}}
symbol_meanings:
  eta_star: \eta^*
  noise_scale: \mathcal{B}_{simple}
standard_notation:
  eta_star: \eta^*
  batch_size: B
  noise_scale: \mathcal{B}_{simple}
conditions:
- 二阶损失近似有效
- 更新量统计量可由对应原文假设近似
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-09-15-重新思考学习率与Batch-Size-三-Muon.md
source_ids:
- '11285'
derived_from: null
implies: null
appears_in:
- '[[重新思考学习率与Batch Size（三）：Muon]]'
evidence_spans:
- ev::11285::相同规律
status: draft
updated: "2026-06-14"
---

# Muon平均场Batch缩放公式


## 概述

（待补充）

## 公式

```tex
\eta^* \approx \frac{\eta_{max}}{\sqrt{1+\mathcal{B}_{simple}/B}}
```

## 核心概念与假设

在探讨Muon优化器时，由于其主要特点是非Element-wise的更新规则，以往分析SGD的传统Element-wise计算方法不再适用。为了简化计算，采用了平均场方法，并引入了以下关键的数学设定：

- **参数矩阵与标量方差**：设损失函数为 $\mathcal{L}(\boldsymbol{W})$，其中参数矩阵 $\boldsymbol{W}\in\mathbb{R}^{n\times m}$（假设 $n\geq m$）。其真实梯度为 $\boldsymbol{G}$。当Batch Size为 $B$ 时，小批量梯度记为 $\tilde{\boldsymbol{G}}_B$，其均值仍为 $\boldsymbol{G}$。为避免讨论复杂的4阶张量协方差矩阵，将梯度的随机扰动简化为一个标量方差，此时小批量梯度的方差变为 $\sigma^2/B$。
- **Hessian矩阵的线性算子视角**：在对损失函数做二阶展开 $\mathcal{L}(\boldsymbol{W} - \eta\tilde{\boldsymbol{\Phi}}_B)$ 时，涉及到了Hessian矩阵 $\boldsymbol{H}$ 构成的二次型 $\mathop{\text{tr}}(\tilde{\boldsymbol{\Phi}}{}_B^{\top}\boldsymbol{H}\tilde{\boldsymbol{\Phi}}_B)$。为了简化，不再写出Hessian的高阶张量形式，而是将 $\boldsymbol{H}$ 视为一个输入和输出都是矩阵的线性算子。
- **近似牛顿法等价**：以 $\tilde{\boldsymbol{\Phi}}_B=\mathop{\text{msign}}(\tilde{\boldsymbol{G}}_B) = \tilde{\boldsymbol{G}}_B(\tilde{\boldsymbol{G}}{}_B^{\top}\tilde{\boldsymbol{G}}_B)^{-1/2}$ 作为更新量。从牛顿法的视角，这一特定的形式相当于隐式地假设了Hessian的逆为 $\boldsymbol{H}^{-1}\boldsymbol{X} = \eta_{\max}\boldsymbol{X}(\boldsymbol{G}^{\top}\boldsymbol{G})^{-1/2}$，从而对应的Hessian算子被近似为 $\boldsymbol{H}\boldsymbol{X} = \eta_{\max}^{-1}\boldsymbol{X}(\boldsymbol{G}^{\top}\boldsymbol{G})^{1/2}$。

## 作用

通过对二阶展开的近似公式两边求期望，即计算 $\mathbb{E}[\mathcal{L}(\boldsymbol{W} - \eta\tilde{\boldsymbol{\Phi}}_B)]$，结合上述特定的 Hessian 线性算子假设和矩阵梯度的统计特性推导可知，Muon 的学习率-Batch Size 尺度关系与 SignSGD 呈现出相同的规律。这意味着在扩大 Batch Size 时，Muon 的最优学习率衰减同样遵循上述公式。

## 证据

- `ev::11285::相同规律`
