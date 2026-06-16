---
type: example
title: 平面仿射坐标转换实例
aliases: []
article_id: '1768'
article: '[[spaces-1768-新理解矩阵2-矩阵是什么]]'
section: 几何理解
claim: 矩阵 A 的列向量作为基向量，可以将仿射坐标系下的点坐标变换到直角坐标系中。
notation_mapping:
  A: 仿射坐标系基矩阵，在原文中为 A = [ [3, 2], [1, 3] ]
  x: 仿射坐标系下的向量坐标，在原文中为 x = [2, 2]^T
  y: 直角坐标系下的测量结果，在原文中为 y = [10, 8]^T
steps:
- 构造 2x2 仿射基矩阵 A = [ [3, 2], [1, 3] ]
- 给定仿射坐标下的向量 x = [2, 2]^T
- 执行矩阵乘积计算 y = Ax = [3*2 + 2*2, 1*2 + 3*2]^T = [10, 8]^T
- 验证该点在旧直角坐标系下的投影长度确实为 10 和 8，这与几何绘图完全吻合
used_concepts:
- '[[仿射坐标系]]'
- '[[矩阵]]'
used_formulas: []
used_methods:
- '[[用矩阵表示仿射坐标变换]]'
source_span: ev::1768::几何理解
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2012-10-31-新理解矩阵2-矩阵是什么.md
source_ids:
- '1768'
status: draft
updated: '2026-06-12'
---

# 平面仿射坐标转换实例

## 算例背景
原文第34-40行，提供了一个在平面仿射坐标系下的二维坐标映射计算。用以直观验证矩阵-向量乘法代表坐标变换这一几何本质。

## 映射计算
计算过程如下：
$$
\begin{pmatrix}3 & 2 \\ 1 & 3\end{pmatrix} \begin{pmatrix}2 \\ 2\end{pmatrix} = \begin{pmatrix}3 \times 2 + 2 \times 2 \\ 1 \times 2 + 3 \times 2\end{pmatrix} = \begin{pmatrix}10 \\ 8\end{pmatrix}
$$