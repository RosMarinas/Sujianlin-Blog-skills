---
type: article_summary
title: 低秩近似之路（五）：CUR
article_id: "10662"
source_url: https://spaces.ac.cn/archives/10662
date: 2025-01-12
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md
source_html: null
series:
  - "[[低秩近似之路]]"
topics:
  - "[[低秩近似]]"
concepts:
  - "[[CUR分解]]"
  - "[[杠杆分数]]"
  - "[[DEIM]]"
methods:
  - "[[将矩阵近似问题化为骨架选择问题]]"
problem_patterns:
  - "[[在误差最优与结构可解释之间选择低秩近似]]"
evidence_spans:
  - ev::10662::基本定义
  - ev::10662::U的选择
  - ev::10662::杠杆分数
  - ev::10662::DEIM法
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md
source_ids:
  - "10662"
status: draft
updated: 2026-06-09
---

## 文章核心问题

怎样同时选取原矩阵的若干行与列作为骨架，构造比 ID 更对称、更可解释的低秩近似。

## 主要结论

CUR 分解形如 `C U R`，其中 `C` 和 `R` 直接来自原矩阵的列和行。给定行列后，理论最优 `U` 可由 `C^\dagger M R^\dagger` 给出；常见直观选择是公共子矩阵的伪逆。行列选择可沿用 CR/ID 的模长、采样、列驱 QR，也可使用杠杆分数和 DEIM。

## 推导结构

文章先把 CUR 与 ID、SVD 对比，明确其左右骨架来自原矩阵。随后讨论 `U` 的两个选择：最小二乘最优解和公共子矩阵伪逆。最后集中于行列选择，给出已有选择策略、杠杆分数和 DEIM 贪心法。

## 关键公式

- `argmin_{S1,S2,U} ||M_{[:,S1]} U M_{[S2,:]}-M||_F^2`
- `U^*=C^\dagger M R^\dagger`
- `U=M_{[S2,S1]}^\dagger`
- `H=V_{[:,:gamma]}V_{[:,:gamma]}^T`

## 体现的方法

CUR 将结构化低秩近似推进到双侧骨架选择：用真实行列保留可解释性，用中间矩阵承担重构复杂度。

## 所属系列位置

这是 [[低秩近似之路]] 的第五篇，从 ID 的单侧列骨架扩展为同时选择行和列的骨架近似。

## 与其他文章的关系

- 使用 [[低秩近似之路（一）：伪逆]] 求给定骨架后的中间矩阵。
- 延续 [[低秩近似之路（四）：ID]] 的骨架思想。
- 将 [[低秩近似之路（二）：SVD]] 的奇异向量用于杠杆分数和 DEIM 的选择依据。

## 原文证据锚点

- `基本定义`：定义 CUR 与 SVD/ID 对比。
- `U的选择`：给出 `U` 的伪逆公式和公共子矩阵解释。
- `杠杆分数` 与 `DEIM法`：给出两种行列选择方法。
