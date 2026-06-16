---
type: formula
title: RMSNorm雅可比矩阵公式
latex: \nabla_{\boldsymbol{x}} \boldsymbol{y} = \frac{1}{\|\boldsymbol{x}\|_{RMS}}\left(\boldsymbol{I}
  - \frac{\boldsymbol{y}\boldsymbol{y}^{\top}}{d}\right)
symbol_meanings:
  x: 输入特征向量
  y: 标准化输出特征向量，且 y = \sqrt{d} x / \|x\|
  d: 特征维度
  I: 单位矩阵
standard_notation:
  jacobian_matrix: \nabla_x y
  rms_norm: \|x\|_{RMS}
conditions: 输入向量 x 必须为非零向量
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-02-通过梯度近似寻找Normalization的替代品.md
source_ids:
- 10831
appears_in:
- - - spaces-10831-寻找Normalization替代品
status: draft
updated: '2026-06-14'
---

## 概述

该公式精确刻画了 RMS Norm (Root Mean Square Normalization) 层中特征的反向传播梯度流。在深度学习中，RMS Norm 的核心运算为 $\boldsymbol{y} = \frac{\boldsymbol{x}}{\Vert\boldsymbol{x}\Vert_{RMS}} = \sqrt{d}\times \frac{\boldsymbol{x}}{\Vert\boldsymbol{x}\Vert}$，其中 $\Vert\boldsymbol{x}\Vert = \sqrt{\sum_{i=1}^d x_i^2}$。

通过引入微小扰动进行泰勒展开，求 $\boldsymbol{x} / \Vert\boldsymbol{x}\Vert_{RMS}$ 的梯度可转化为求 $\boldsymbol{x} / \Vert\boldsymbol{x}\Vert$ 的梯度近似过程：
$$
\frac{\boldsymbol{x}+\Delta\boldsymbol{x}}{\Vert\boldsymbol{x}+\Delta\boldsymbol{x}\Vert} = \frac{\boldsymbol{x}}{\Vert\boldsymbol{x}+\Delta\boldsymbol{x}\Vert} + \frac{\Delta\boldsymbol{x}}{\Vert\boldsymbol{x}+\Delta\boldsymbol{x}\Vert} \approx \frac{\boldsymbol{x}}{\Vert\boldsymbol{x}+\Delta\boldsymbol{x}\Vert} + \frac{\Delta\boldsymbol{x}}{\Vert\boldsymbol{x}\Vert}
$$

基于上述展开推导出的雅可比矩阵 $\nabla_{\boldsymbol{x}} \boldsymbol{y}$，其括号内的主体 $\left(\boldsymbol{I} - \frac{\boldsymbol{y}\boldsymbol{y}^{\top}}{d}\right)$ 具有深远的模型优化意义。对角阵 $\boldsymbol{I}$ 提供了基础的同维度比例映射，而非对角线项 $-\frac{y_i y_j}{d}$（或写为特征向量的外积形式）则实质性地引入了跨维度的强负反馈通道。这种全局的特征依赖运算极大地稳定了模型的前向传播，限制了特征在特定方向上的无界膨胀。

正因为 RMS Norm 的梯度天然包含了关联各个维度的调节效应，试图利用单纯的逐元素（element-wise）运算来替代归一化层往往面临极大挑战。例如近期研究中提出的 Dynamic Tanh ($\mathop{\text{DyT}}(\boldsymbol{x}) = \boldsymbol{\gamma} \odot \tanh(\alpha \boldsymbol{x}) + \boldsymbol{\beta}$) 算子，虽然在计算上免除了均值和方差等标量统计步骤，但同时也丢失了上述复杂的雅可比矩阵跨维度交互约束。梯度分析的数学关系深刻表明，缺失了 Normalization 层这种稳定、强效的跨维度误差反向调控，模型将会流失优化自由度，从而在复杂微调和泛化性能上难以实现完全对等的替代。
