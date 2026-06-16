---
type: article_summary
title: 低秩近似之路（三）：CR
article_id: "10427"
source_url: https://spaces.ac.cn/archives/10427
date: 2024-10-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-10-11-低秩近似之路-三-CR.md
source_html: null
series:
  - "[[低秩近似之路]]"
topics:
  - "[[低秩近似]]"
concepts:
  - "[[CR近似]]"
methods:
  - "[[将矩阵近似问题化为骨架选择问题]]"
problem_patterns:
  - "[[在误差最优与结构可解释之间选择低秩近似]]"
evidence_spans:
  - ev::10427::问题背景
  - ev::10427::初步近似
  - ev::10427::采样视角
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-10-11-低秩近似之路-三-CR.md
source_ids:
  - "10427"
status: draft
updated: 2026-06-09
---

## 文章核心问题

在矩阵乘法 `M=XY` 已知的场景中，怎样只选择 `X` 的若干列和 `Y` 的对应行来构造可解释、可加速的低秩近似。

## 主要结论

CR 近似把 `XY` 写成若干外积之和后选择其中一部分保留。精确选择是困难的，模长乘积排序可以作为 baseline；若允许对角重标定，可以用采样视角得到按 `||x_i||||y_i||` 加权采样的近似。

## 推导结构

文章先说明结构约束来自可解释性和非线性处理需求，然后把 `XY` 展开为外积和，转化为选择向量子集的问题。接着从采样期望和方差角度推导最优采样分布，最后讨论更高复杂度的元组贪心和对角系数优化。

## 关键公式

- `argmin_S ||X_{[:,S]}Y_{[S,:]}-XY||_F^2`
- `XY=sum_i x_i y_i^T`
- `p_i^* proportional ||vec(x_i y_i^T)|| = ||x_i||||y_i||`

## 体现的方法

CR 体现了从无约束最优近似转向结构化骨架选择的思路：牺牲部分误差最优性，换取列/行来源清晰和乘法复杂度降低。

## 所属系列位置

这是 [[低秩近似之路]] 的第三篇，是从 SVD 无约束最优转向结构化近似的第一步。

## 与其他文章的关系

- 使用 [[低秩近似之路（一）：伪逆]] 中的最小二乘思路。
- 与 [[低秩近似之路（四）：ID]]、[[低秩近似之路（五）：CUR]] 共同构成“选择原矩阵局部骨架”的路线。

## 原文证据锚点

- `问题背景`：定义选择矩阵约束下的 CR 近似。
- `初步近似`：把 CR 转化为外积向量子集选择。
- `采样视角`：推导按外积模长采样的分布。
