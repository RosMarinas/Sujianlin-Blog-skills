---
type: concept
title: CR近似
aliases:
- Column-Row Approximation
definition: CR近似是在矩阵乘法 `XY` 中选择 `X` 的部分列和 `Y` 的对应行，用这些外积项近似完整乘积。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-10-11-低秩近似之路-三-CR.md
source_ids:
- '10427'
prerequisites:
- '[[伪逆]]'
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods:
- '[[将矩阵近似问题化为骨架选择问题]]'
series:
- '[[低秩近似之路]]'
evidence_spans:
- ev::10427::问题背景
- ev::10427::采样视角
status: stable
updated: '2026-06-12'
---

## 核心定义

给定 `M=XY`，CR 近似选择索引集 `S`，使用 `X_{[:,S]}Y_{[S,:]}` 近似 `XY`。

## 选择原则

文章给出两个层次：固定选择数量时，模长乘积最大的外积项是一个 baseline；允许重标定并从采样视角分析时，最优采样概率正比于 `||x_i||||y_i||`。

## 与其他概念的关系

CR 是从 SVD 无约束最优转向结构化近似的第一步。它要求源矩阵本身来自乘法 `XY`，而 [[插值分解]] 则面向直接给出的矩阵。