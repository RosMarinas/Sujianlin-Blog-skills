---
type: article_summary
title: 低秩近似之路（四）：ID
article_id: "10501"
source_url: https://spaces.ac.cn/archives/10501
date: 2024-10-30
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-10-30-低秩近似之路-四-ID.md
source_html: null
series:
  - "[[低秩近似之路]]"
topics:
  - "[[低秩近似]]"
concepts:
  - "[[插值分解]]"
methods:
  - "[[将矩阵近似问题化为骨架选择问题]]"
problem_patterns:
  - "[[在误差最优与结构可解释之间选择低秩近似]]"
evidence_spans:
  - ev::10501::基本定义
  - ev::10501::列驱QR
  - ev::10501::随机求解
  - ev::10501::提高精度
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-10-30-低秩近似之路-四-ID.md
source_ids:
  - "10501"
status: draft
updated: 2026-06-09
---

## 文章核心问题

当直接给定矩阵 `M` 时，怎样选出若干原矩阵列作为骨架，用它们的线性组合逼近整个矩阵。

## 主要结论

ID 近似形如 `M_{[:,S]}Z`。固定列集合 `S` 后，最优 `Z` 由伪逆给出；难点是列子集选择，这本质上是 NP-Hard 的离散优化问题。列驱 QR 是标准确定性近似，随机投影或随机列采样可以降低复杂度。

## 推导结构

文章先把 ID 放在伪逆、SVD、CR 之后说明其结构约束，再解释“选择列作为基向量”的几何意义。之后从 QR 分解解释投影，再给出列驱 QR 的贪心选择过程，最后讨论随机算法和高精度列选择的取舍。

## 关键公式

- `argmin_{S,Z} ||M_{[:,S]}Z-M||_F^2`
- `Z^*=C^\dagger M`
- `M Pi approx Q_{[:,:r]}R_{[:r,:]} = CZ`

## 体现的方法

ID 是“骨架列 + 最优系数”的典型结构化低秩近似，将问题集中到列子集选择。

## 所属系列位置

这是 [[低秩近似之路]] 的第四篇，从 `XY` 乘积场景的 CR 转向直接矩阵的列骨架近似。

## 与其他文章的关系

- 依赖 [[低秩近似之路（一）：伪逆]] 固定骨架后的系数求解。
- 与 [[低秩近似之路（五）：CUR]] 形成一侧骨架到双侧骨架的递进。

## 原文证据锚点

- `基本定义`：定义 ID 和列选择难点。
- `列驱QR`：给出列驱 QR 到 ID 的构造。
- `随机求解` 与 `提高精度`：说明随机列采样、QR baseline 和精度-复杂度权衡。
