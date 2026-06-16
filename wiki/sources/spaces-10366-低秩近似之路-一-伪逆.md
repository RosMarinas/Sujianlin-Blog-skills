---
type: article_summary
title: 低秩近似之路（一）：伪逆
article_id: "10366"
source_url: https://spaces.ac.cn/archives/10366
date: 2024-09-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-09-15-低秩近似之路-一-伪逆.md
source_html: null
series:
  - "[[低秩近似之路]]"
topics:
  - "[[低秩近似]]"
concepts:
  - "[[伪逆]]"
methods:
  - "[[将矩阵近似问题化为骨架选择问题]]"
problem_patterns: []
evidence_spans:
  - ev::10366::优化视角
  - ev::10366::基本结果
  - ev::10366::一般形式
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-09-15-低秩近似之路-一-伪逆.md
source_ids:
  - "10366"
status: draft
updated: 2026-06-09
---

## 文章核心问题

当矩阵方程 `AB=M` 中的 `A` 不可逆或不是方阵时，怎样用最小二乘意义上的近似逆继续求解。

## 主要结论

伪逆把精确逆矩阵推广为最小化 `||AB-M||_F^2` 的解析解。满秩时可写成 `(A^T A)^{-1}A^T`，秩不足时可用加正则再令正则趋零的极限定义，并通过谱分解稳定计算。

## 推导结构

文章先把不可解矩阵方程改写为 Frobenius 范数下的最小二乘问题，再补充 `F` 范数和 `F` 内积，随后对 `B` 和 `A` 求导得到基本解。最后用正则化极限和谱分解处理秩不足时的不唯一性与数值不稳定。

## 关键公式

- `argmin_B ||AB-M||_F^2`
- `A^\dagger=(A^T A)^{-1}A^T`
- `A^\dagger = lim_{\epsilon\to 0}(A^T A+\epsilon I)^{-1}A^T`

## 体现的方法

本文提供了后续 CR、ID、CUR 中反复使用的工具：当一个低秩近似结构的一侧已经确定时，用伪逆求另一侧的最优最小二乘解。

## 所属系列位置

这是 [[低秩近似之路]] 的第一篇，为后续 SVD 最优低秩近似和结构化分解中的系数求解提供基础。

## 与其他文章的关系

- [[低秩近似之路（二）：SVD]] 用 SVD 重新给出伪逆通解。
- [[低秩近似之路（三）：CR]]、[[低秩近似之路（四）：ID]] 和 [[低秩近似之路（五）：CUR]] 都在固定骨架后使用伪逆求最优中间系数。

## 原文证据锚点

- `优化视角`：把不可逆矩阵方程改写为最小二乘优化。
- `基本结果`：给出满秩伪逆公式。
- `一般形式` 与 `数值计算`：给出正则极限和谱分解计算。
