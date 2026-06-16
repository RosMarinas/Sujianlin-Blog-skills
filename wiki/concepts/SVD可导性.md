---
type: concept
title: SVD可导性
aliases: []
definition: 在非零奇异值两两不等等条件下，SVD 的奇异值和奇异向量可对原矩阵求微分。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
- '10878'
related_methods:
- - - 用等效前向表达保留SVD梯度
series: []
evidence_spans:
- ev::10878::推导基础
- ev::10878::一般结果
status: draft
updated: '2026-06-12'
---

# SVD可导性

## 定义

在非零奇异值两两不等等条件下，SVD 的奇异值和奇异向量可对原矩阵求微分。

## 激活场景

源文研究的是把 SVD 嵌入可微模型时如何写出导函数。它先假设 $\boldsymbol{W}$ 是满秩 $n\times n$ 矩阵，且全体奇异值两两不等，写成 $\boldsymbol{W}=\boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^{\top}$，再对两边求微分并左乘 $\boldsymbol{U}^{\top}$、右乘 $\boldsymbol{V}$，得到后续推导的核心等式。

## 关键关系

该概念连接奇异值微分、奇异向量微分和自动求导实现。源文说明 $\boldsymbol{U}^{\top}d\boldsymbol{U}$ 与 $(d\boldsymbol{V})^{\top}\boldsymbol{V}$ 是反对称矩阵；对角部分给出 $d\sigma_i=\boldsymbol{u}_i^{\top}(d\boldsymbol{W})\boldsymbol{v}_i$，非对角部分则需用奇异值差构造矩阵 $\boldsymbol{F}_{i,j}=1/(\sigma_j^2-\sigma_i^2)$。因此奇异值相等时会出现分母退化，这就是 frontmatter 定义中强调“两两不等”的原因。

## 证据

- `ev::10878::推导基础`
- `ev::10878::一般结果`
