---
type: formula
title: msign导数求解公式
aliases:
- msign Derivative Sylvester Equation Solution
latex: \boldsymbol{X} = -\frac{1}{2} \left[ \lim_{\epsilon\to 0} \text{mcsgn}\left(
  \begin{bmatrix} \boldsymbol{A} + \epsilon\boldsymbol{I} & -\boldsymbol{C} \\ \boldsymbol{0}
  & -\boldsymbol{B} - \epsilon\boldsymbol{I} \end{bmatrix} \right) \right]_{[:n, n:]}
symbol_meanings:
  \boldsymbol{X}: Sylvester 方程 $\boldsymbol{A}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} = \boldsymbol{C}$
standard_notation: \boldsymbol{X} = -\frac{1}{2} \left[ \text{mcsgn}\left( \begin{bmatrix}
  \boldsymbol{A} + \epsilon\boldsymbol{I} & -\boldsymbol{C} \\ \boldsymbol{0} & -\boldsymbol{B}
  - \epsilon\boldsymbol{I} \end{bmatrix} \right) \right]_{[:n, n:]}
conditions: 用于对前向传播包含 $\boldsymbol{O} = \text{msign}(\boldsymbol{M})$ 算子的网络进行高效反向传播。其中
  $\boldsymbol{M} \in \mathbb{R}^{n \times m}$。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-13-msign的导数.md
source_ids:
- '11025'
appears_in:
- '[[spaces-11025-msign的导数]]'
status: draft
null_evidence_reason: Initial compilation draft
updated: "2026-06-14"
---

## 概述

该公式给出了求解 $\text{msign}$ 反向传播梯度的关键步骤。根据迹技巧，$\text{msign}$ 算子的微分求解方程为：

$$\nabla_{\boldsymbol{M}}\mathcal{L} = \boldsymbol{X} - \boldsymbol{O}\boldsymbol{X}^\top\boldsymbol{O}$$

其中 $\boldsymbol{X}$ 满足 Sylvester 方程 $\boldsymbol{A}\boldsymbol{X} + \boldsymbol{X}\boldsymbol{B} = \boldsymbol{C}$。

该公式利用特征值符号函数 $\text{mcsgn}$ 在分块三角矩阵上的代数性质，将这一 Sylvester 方程的求解转化为对分块矩阵的 $\text{mcsgn}$ 计算。其右上角分块即为方程解 $\boldsymbol{X}$。该过程可以使用 GPU 友好的 Newton-Schulz 迭代进行，无需进行昂贵的奇异值分解（SVD），为端到端反向传播扫清了计算障碍。