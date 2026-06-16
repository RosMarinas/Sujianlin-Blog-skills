---
type: formula
title: EFLA递归更新公式
latex: \boldsymbol{S}_t = \boldsymbol{S}_t-1 \left(\boldsymbol{I} - \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{k}_t\boldsymbol{k}_t^{\top}\right)
  + \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{v}_t
  \boldsymbol{k}_t^{\top}
symbol_meanings:
  S_t: 线性注意力机制在 t 时刻的状态累加器矩阵
  k_t: 输入 Key 向量
  v_t: 输入 Value 向量
  eta_t: 时变更新步长（学习率）
standard_notation:
  state_matrix: \boldsymbol{S}_t
  key_vector: \boldsymbol{k}_t
  value_vector: \boldsymbol{v}_t
conditions: 转移矩阵特征值由指数函数保证天然在 (0, 1] 区间，避免大特征值累乘数值发散
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-23-为什么DeltaNet要加L2-Normalize.md
source_ids:
- 11486
appears_in:
- - - spaces-11486-DeltaNet的L2-Normalize解释
status: draft
updated: '2026-06-14'
---

## 概述

EFLA (Error-Free Linear Attention) 提出了一种基于连续时间动力学（Continuous-Time Dynamics）精确解的全新视角，从解析解展开式中自然导出了对 Key 的模长归一化项，从理论基础上严谨地佐证了 L2 归一化的必要性。

在标准的 DeltaNet 离散更新格式中，状态累加器的转移矩阵为 $\boldsymbol{I} - \eta_t \boldsymbol{k}_t\boldsymbol{k}_t^{\top}$。该矩阵有一个特征值为 $1 - \eta_t\|\boldsymbol{k}_t\|^2$，其余特征值均为 1。由于不同时间步的转移矩阵在递归过程中需要连乘，为避免数值爆炸，必须满足约束 $-1 \leq 1 - \eta_t\|\boldsymbol{k}_t\|^2 \leq 1$。常规的做法是强制给 $\boldsymbol{k}_t$ 加上 L2 Normalize，并对学习率 $\eta_t$ 使用 Sigmoid 激活函数来满足此约束边界。

相比之下，EFLA 通过连续动力学的精确解析解引入了指数项 $e^{-\eta_t\|\boldsymbol{k}_t\|^2}$。在其改进的更新公式中，转移矩阵变为 $\boldsymbol{I} - \frac{1 - e^{-\eta_t\|\boldsymbol{k}_t\|^2}}{\|\boldsymbol{k}_t\|^2}\boldsymbol{k}_t\boldsymbol{k}_t^{\top}$。此时矩阵的关键特征值由指数函数保证，天然落在 $(0, 1]$ 这一安全区间内。这种精确解形式不仅从根本上避免了由大负特征值累乘导致的数值发散问题（实现“Error-Free”），并且公式中自然浮现的分母 $\|\boldsymbol{k}_t\|^2$ 直接证明了对 Key 向量进行 L2 归一化不仅是一种有效的工程Trick，更是连续时间演化下的数学必然。
