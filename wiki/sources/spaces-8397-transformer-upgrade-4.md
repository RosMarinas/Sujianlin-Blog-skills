---
type: article_summary
title: "Transformer升级之路：4、二维位置的旋转式位置编码"
article_id: "8397"
source_url: https://spaces.ac.cn/archives/8397
date: 2021-05-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-05-10-Transformer升级之路-4-二维位置的旋转式位置编码.md
series: [Transformer升级之路]
topics: [位置编码, 二维RoPE, 视觉Transformer]
concepts: [2D RoPE, Matrix Exponential]
methods: [Matrix Exponential for RoPE]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-05-10-Transformer升级之路-4-二维位置的旋转式位置编码.md
source_ids:
  - "8397"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：4、二维位置的旋转式位置编码

## 文章核心问题
如何将RoPE从一维序列扩展到二维空间（如图像）？满足"相对性"和"可逆性"的二维RoPE的封闭形式是什么？

## 主要结论
- 二维RoPE不能用简单的四元数乘法来优雅解决，因为四元数乘法不满足交换律。
- 利用矩阵指数 $e^{\boldsymbol{A}}$ 可以将乘法转换为加法，完美契合位置编码中要求的加法性（相对位置）。
- 最终的2D RoPE解将不同维度的旋转分块对角化，使得每一维（$x$ 和 $y$）独立旋转，从而维持了可逆性和相对性。

## 推导结构
从满足"相对性"和"可逆性"条件出发，分别尝试了四元数乘法和矩阵指数法。四元数方法因不满足交换律而失败。利用矩阵指数法，通过求解矩阵指数方程证明了满足条件的二维RoPE可以表达为分块对角矩阵。

## 关键公式
- 相对性条件: $\boldsymbol{R}_{m,n}^{\top}\boldsymbol{R}_{m',n'} = \boldsymbol{R}_{m-m',n-n'}$
- 矩阵指数解: $\boldsymbol{R}_{m,n} = \exp(m\boldsymbol{A} + n\boldsymbol{B})$
- 2D RoPE分块对角形式: $\boldsymbol{R}_{m,n} = \begin{bmatrix} \boldsymbol{R}_m & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{R}_n \end{bmatrix}$

## 体现的方法
- 利用矩阵指数 $e^{\boldsymbol{A}}$ 将乘法转换为加法
- 分块对角化维持可逆性和相对性

## 所属系列位置
Transformer升级之路系列第4篇，将RoPE从一维扩展到二维。

## 与其他文章的关系
本文在第2篇RoPE的基础上将其推广到二维空间，使得RoPE可以应用于Vision Transformer等处理图像的任务。同时，矩阵指数方法的使用也为第6篇中RoPE的完备性分析提供了数学工具。

## 原文证据锚点
- 四元数乘法因不满足交换律无法用于二维RoPE
- 矩阵指数法推导二维RoPE的解
- 2D RoPE的分块对角化形式
