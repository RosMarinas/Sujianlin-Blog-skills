---

type: formula
title: SVD等效前向梯度公式
aliases: []
latex: \sigma_i \leadsto \operatorname{sg}(\boldsymbol{u}_i)^{\top}\boldsymbol{W}\operatorname{sg}(\boldsymbol{v}_i)
symbol_meanings:
  W: 原矩阵
  sg: stop_gradient
  u_i/v_i: 奇异向量
standard_notation:
  sg: stop_gradient
  W: 原矩阵
  u_i/v_i: 奇异向量
conditions:
- 用于自动求导实现中替换前向表达而不改变前向值。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
- '10878'
derived_from: []
implies: []
appears_in:
- - - SVD的导数
evidence_spans:
- ev::10878::梯度一
status: draft
updated: "2026-06-14"
---

# SVD等效前向梯度公式


## 概述

（待补充）

## 公式

```tex
\sigma_i \leadsto \operatorname{sg}(\boldsymbol{u}_i)^{\top}\boldsymbol{W}\operatorname{sg}(\boldsymbol{v}_i)
```

## 详情描述

在深度学习的自动求导框架中，直接实现矩阵奇异值分解（SVD）的底层反向传播逻辑较为复杂。该公式提供了一种优雅的等效前向计算替代方法，能够利用现有的自动求导引擎正确计算奇异值 $\sigma_i$ 对原始矩阵 $\boldsymbol{W}$ 的偏导数。其中，$\operatorname{sg}$ 表示 `stop_gradient`（停止梯度回传）操作，确保梯度只流向 $\boldsymbol{W}$，而不对奇异向量进行反向传播。

**数学推导过程**：
假设 $\boldsymbol{W}$ 是满秩且奇异值两两不等的 $n \times n$ 矩阵，其SVD可以表示为 $\boldsymbol{W} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^{\top}$。对该等式两边同时求微分，可得：
$$
d\boldsymbol{W} = (d\boldsymbol{U})\boldsymbol{\Sigma}\boldsymbol{V}^{\top} + \boldsymbol{U}(d\boldsymbol{\Sigma})\boldsymbol{V}^{\top} + \boldsymbol{U}\boldsymbol{\Sigma}(d\boldsymbol{V})^{\top}
$$
在等式两端分别左乘 $\boldsymbol{U}^{\top}$ 并右乘 $\boldsymbol{V}$，化简得到：
$$
\boldsymbol{U}^{\top}(d\boldsymbol{W})\boldsymbol{V} = \boldsymbol{U}^{\top}(d\boldsymbol{U})\boldsymbol{\Sigma} + d\boldsymbol{\Sigma} + \boldsymbol{\Sigma}(d\boldsymbol{V})^{\top}\boldsymbol{V}
$$
利用正交矩阵的性质（$\boldsymbol{U}^{\top}\boldsymbol{U} = \boldsymbol{I}$ 和 $\boldsymbol{V}^{\top}\boldsymbol{V} = \boldsymbol{I}$），对其进行微分可知，$(d\boldsymbol{U})^{\top}\boldsymbol{U} + \boldsymbol{U}^{\top}(d\boldsymbol{U}) = \boldsymbol{0}$。这表明 $\boldsymbol{U}^{\top}(d\boldsymbol{U})$ 与 $(d\boldsymbol{V})^{\top}\boldsymbol{V}$ 均为反对称矩阵，因此它们的对角线元素必然全为零。

考虑到 $\boldsymbol{\Sigma}$ 与 $d\boldsymbol{\Sigma}$ 都是对角矩阵，我们可以使用单位阵 $\boldsymbol{I}$ 与 Hadamard 积（按元素相乘，符号为 $\otimes$）来提取等式两边的对角线部分：
$$
d\boldsymbol{\Sigma} = \boldsymbol{I}\otimes(\boldsymbol{U}^{\top}(d\boldsymbol{W})\boldsymbol{V})
$$
将其转化为标量形式，对于第 $i$ 个奇异值有 $d\sigma_i = \boldsymbol{u}_i^{\top}(d\boldsymbol{W})\boldsymbol{v}_i$。该微元表达式等价于梯度 $\frac{\partial \sigma_i}{\partial \boldsymbol{W}} = \boldsymbol{u}_i \boldsymbol{v}_i^{\top}$。

在模型的前向传播中，采用 $\operatorname{sg}(\boldsymbol{u}_i)^{\top}\boldsymbol{W}\operatorname{sg}(\boldsymbol{v}_i)$ 来代替原有的 $\sigma_i$。在数值上，这并不会改变前向传播的结果，但在反向求导时，借助于链式法则引擎，可以直接正确还原出 $d\sigma_i = \boldsymbol{u}_i^{\top}(d\boldsymbol{W})\boldsymbol{v}_i$ 的导数行为，巧妙绕过了针对SVD进行复杂的定制化算子开发。

## 证据

- `ev::10878::梯度一`
