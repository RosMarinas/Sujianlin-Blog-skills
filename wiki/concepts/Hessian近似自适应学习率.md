---
type: concept
title: Hessian近似自适应学习率
aliases:
- Hessian Approximation for Adaptive Optimizers
definition: 将自适应学习率优化器（如 Adam/RMSprop）中梯度平方的滑动平均项，解释为对损失函数 Hessian 矩阵二阶项（对角元素）的长期平均近似估计的理论模型。
standard_notation: \boldsymbol{\mathcal{H}}_t \approx \eta_t^{-1} \text{diag}(\sqrt{\hat{\boldsymbol{v}}_t}
  + \epsilon)
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-11-29-从Hessian近似看自适应学习率优化器.md
source_ids:
- '10588'
related_formulas:
- '[[Hessian期望近似公式]]'
status: draft
null_evidence_reason: Initial compilation draft with updated schema
updated: '2026-06-12'
---

## 概述

在深度学习的一阶优化算法中，自适应学习率优化器（如 Adam）被广泛使用。本概念提供了一个将此类算法视为二阶牛顿法近似的全新物理解释：即认为梯度平方的二阶矩滑动平均项 $\hat{\boldsymbol{v}}_t$ 在长期演化下收敛于最优点附近时，其期望值逼近于 Hessian 矩阵的平方的对角分量。

## 核心要点

1. **牛顿法对应**：牛顿法形式为 $\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \boldsymbol{\mathcal{H}}_t^{-1}\boldsymbol{g}_t$。自适应优化器相当于采用对角 Hessian 近似：$\boldsymbol{\mathcal{H}}_t \approx \eta_t^{-1}\text{diag}(\sqrt{\hat{\boldsymbol{v}}_t})$。
2. **期望与根号关系**：
   - 瞬时 Gauss-Newton 近似给出的关系为 $\boldsymbol{g}\boldsymbol{g}^\top \approx \sigma^2 \boldsymbol{\mathcal{H}}$。
   - 自适应滑动平均在长期时空平均下的演化关系为 $\mathbb{E}[\boldsymbol{g}\boldsymbol{g}^\top] \approx \sigma^2 \boldsymbol{\mathcal{H}}^2$。这解释了为何优化器分母中需要对滑动平均项求平方根（差了一个根号）。
3. **AdaBelief 的扩展**：当参数未收敛到最优点附近时，用协方差代替二阶矩，对应了 AdaBelief 的 Hessian 解释。