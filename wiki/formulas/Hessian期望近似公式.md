---
type: formula
title: Hessian期望近似公式
aliases:
- Hessian Expectation Approximation Formula
latex: \mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\boldsymbol{g}_{\boldsymbol{\theta}}^\top]
  \approx \sigma^2 \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*} \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}^\top
symbol_meanings:
  E: E
  H: H
  \boldsymbol{\mathcal{H}: boldsymbol{\mathcal{H}
  \boldsymbol{\theta}: boldsymbol{\theta} 参数
  \boldsymbol{g}: boldsymbol{g} 参数
  \mathbb{E}: 期望
  \sigma: 标准差 / 二阶矩
  g: 函数 / 梯度
standard_notation: \mathbb{E}[\boldsymbol{g}\boldsymbol{g}^\top] \approx \sigma^2
  \boldsymbol{\mathcal{H}}^2
conditions: 模型训练进入最优点附近收敛打转的平稳阶段，偏离误差 $\boldsymbol{\theta} - \boldsymbol{\theta}^*$
  服从各向同性高斯分布 $\mathcal{N}(\boldsymbol{0}, \sigma^2 \boldsymbol{I})$，最优点梯度 $\boldsymbol{g}_{\boldsymbol{\theta}^*}
  = \boldsymbol{0}$。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-11-29-从Hessian近似看自适应学习率优化器.md
source_ids:
- '10588'
appears_in:
- '[[spaces-10588-从Hessian近似看自适应学习率优化器]]'
status: draft
null_evidence_reason: Initial compilation draft
updated: "2026-06-14"
---

## 概述

该公式将梯度外积的长期平均（即二阶矩期望值）与 Hessian 矩阵的平方联系起来。这为自适应学习率优化器（如 Adam/RMSprop）的分母（梯度平方滑动平均再开根号，即 $\sqrt{\hat{\boldsymbol{v}}_t}$）提供了解释：

如果假设 Hessian 矩阵是对角矩阵，则有：

$$\boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*} \approx \frac{1}{\sigma} \text{diag}\left(\sqrt{\mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\odot\boldsymbol{g}_{\boldsymbol{\theta}}]}\right)$$

这就是为什么梯度平方的均值开平方能够近似表示对角 Hessian 的原因。它与瞬时 Gauss-Newton 近似相比，由于包含了长期的时间平均（抵消了部分随机扰动），因而多了一个根号。