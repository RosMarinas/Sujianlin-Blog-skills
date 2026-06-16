---

type: formula
title: SVD奇异值微分公式
aliases: []
latex: d\sigma_i=\boldsymbol{u}_i^{\top}(d\boldsymbol{W})\boldsymbol{v}_i
symbol_meanings:
  d\sigma_i: 第 i 个奇异值的一阶微分
  \boldsymbol{u}_i: 第 i 个左奇异向量
  d\boldsymbol{W}: 原矩阵 W 的微分
  \boldsymbol{v}_i: 第 i 个右奇异向量
standard_notation:
  sigma_i: 第 i 个奇异值
  u_i: 左奇异向量
  v_i: 右奇异向量
  dW: 矩阵微分
conditions:
- 在源文的满秩且奇异值两两不等推导下成立；一般条件见对应 proposition。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
- '10878'
derived_from: []
implies: []
appears_in:
- - - SVD的导数
evidence_spans:
- ev::10878::奇异值
status: draft
updated: '2026-06-14'
---


# SVD奇异值微分公式


## 概述

（待补充）

## 公式

```tex
d\sigma_i=\boldsymbol{u}_i^{\top}(d\boldsymbol{W})\boldsymbol{v}_i
```

## 符号与条件

$\boldsymbol{W}=\boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^{\top}$ 是 SVD，$\sigma_i$ 是第 $i$ 个奇异值，$\boldsymbol{u}_i$ 和 $\boldsymbol{v}_i$ 分别是对应的左右奇异向量，$d\boldsymbol{W}$ 是原矩阵的微分。源文推导时假设 $\boldsymbol{W}$ 满秩且奇异值两两不等；该条件使奇异向量微分中的奇异值差分母不退化。

## 用途

该公式来自对
$$
d\boldsymbol{W}=(d\boldsymbol{U})\boldsymbol{\Sigma}\boldsymbol{V}^{\top}
+\boldsymbol{U}(d\boldsymbol{\Sigma})\boldsymbol{V}^{\top}
+\boldsymbol{U}\boldsymbol{\Sigma}(d\boldsymbol{V})^{\top}
$$
左乘 $\boldsymbol{U}^{\top}$、右乘 $\boldsymbol{V}$ 后取对角部分。它直接给出奇异值对矩阵扰动的一阶响应，也是谱范数梯度在 $i=1$ 时的基础。

## 证据

- `ev::10878::奇异值`
