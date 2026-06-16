---
type: article_summary
title: "对角+低秩三角阵的高效求逆方法"
article_id: "11072"
source_url: https://spaces.ac.cn/archives/11072
date: 2025-07-01
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-07-01-对角-低秩-三角阵的高效求逆方法.md
source_html: null
series:
  - "[[线性注意力简史]]"
topics:
  - "[[矩阵计算]]"
concepts:
  - "[[下三角矩阵]]"
  - "[[对角+低秩结构]]"
  - "[[Woodbury恒等式]]"
  - "[[分块矩阵求逆]]"
methods:
  - "[[用缓存变量实现三角低秩矩阵的线性递归求逆]]"
  - "[[用分块递归加速结构化矩阵求逆]]"
problem_patterns: []
evidence_spans:
  - ev::11072::基本结果
  - ev::11072::低秩结构
  - ev::11072::乘法计算
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-07-01-对角-低秩-三角阵的高效求逆方法.md
source_ids:
  - "11072"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何高效计算形如$T = \Lambda + QK^\top \odot M^-$的对角+低秩三角矩阵的逆矩阵，使得计算复杂度从$O(n^3)$降低到$O(n^2)$。

## 主要结论

1. 利用下三角矩阵的分块求逆公式和$QK^\top$的低秩结构，通过缓存$K_{[:l]}^\top T_{[:l,:l]}^{-1}$递归变量，将每一步迭代复杂度从$O(l^2)$降到$O(l)$，总复杂度$O(n^2)$。
2. 对于任意$V\in\mathbb{R}^{n\times d}$，计算$T^{-1}V$只需$O(n)$复杂度（比$T^{-1}$本身的$O(n^2)$更低），通过缓存$K_{[:l]}^\top(T^{-1}V)_{[:l]}$实现。
3. 递归算法可以自然推广到chunk格式，进一步提高计算效率。

## 推导结构

基本结果（分块三角矩阵求逆公式，引入Woodbury恒等式作为背景）→ 低秩结构（利用$Q_{[l:l+1]}K_{[:l]}^\top$的低秩性，引入缓存变量实现$O(l)$迭代）→ 乘法计算（推广到$T^{-1}V$计算，进一步降为$O(n)$总复杂度）。

## 关键公式

- 目标矩阵：$T = \Lambda + QK^\top\odot M^-$，其中$M^-$是严格下三角掩码
- 分块求逆：$\begin{bmatrix}A & 0 \\ C & B\end{bmatrix}^{-1} = \begin{bmatrix}A^{-1} & 0 \\ -B^{-1}CA^{-1} & B^{-1}\end{bmatrix}$
- 递归求逆：$T_{[:l+1,:l+1]}^{-1} = \begin{bmatrix}T_{[:l,:l]}^{-1} & 0 \\ -T_{[l:l+1,l:l+1]}^{-1}Q_{[l:l+1]}K_{[:l]}^\top T_{[:l,:l]}^{-1} & T_{[l:l+1,l:l+1]}^{-1}\end{bmatrix}$

## 体现的方法

- **用缓存变量实现三角低秩矩阵的线性递归求逆**：利用$QK^\top$的低秩结构，引入缓存变量$K_{[:l]}^\top T_{[:l,:l]}^{-1}$使每步复杂度与$l$无关。
- **用分块递归加速结构化矩阵求逆**：利用下三角矩阵的分块求逆恒等式，将整体求逆转化为逐步递归。

## 所属系列位置

与[[series::线性注意力简史]]相关，该求逆方法是DeltaNet线性注意力并行计算的核心。

## 与其他文章的关系

- 被[[spaces-11563-DeltaNet的核心逆矩阵的元素总是在-1-1-内]]引用，其中利用了本文的下三角矩阵对角性质。
- 背景是DeltaNet中出现的$(I+KK^\top\odot M^-)^{-1}$逆矩阵计算。

## 原文证据锚点

- `ev::11072::基本结果`：问题定义、分块三角矩阵求逆恒等式。
- `ev::11072::低秩结构`：利用低秩结构引入缓存变量的$O(n^2)$递归算法和代码实现。
- `ev::11072::乘法计算`：$T^{-1}V$的$O(n)$算法推导和代码实现。
