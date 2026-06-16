---
type: concept
title: CUR分解
aliases:
- CUR
- CUR decomposition
definition: CUR分解同时选择原矩阵的若干列和若干行，并用中间矩阵连接它们来近似原矩阵。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md
source_ids:
- '10662'
prerequisites:
- '[[伪逆]]'
- '[[插值分解]]'
equivalent_forms: []
direct_consequences: []
related_formulas:
- '[[CUR中间矩阵伪逆公式]]'
related_methods:
- '[[将矩阵近似问题化为骨架选择问题]]'
series:
- '[[低秩近似之路]]'
evidence_spans:
- ev::10662::基本定义
- ev::10662::U的选择
status: stable
updated: '2026-06-12'
---

## 核心定义

CUR 近似形如 `C U R`，其中 `C=M_{[:,S1]}`，`R=M_{[S2,:]}` 都来自原矩阵。它比只选列的 ID 更对称，也更接近保留原矩阵可解释结构的目标。

## 中间矩阵

给定 `C` 和 `R` 后，理论最优中间矩阵为 `C^\dagger M R^\dagger`。另一种直观选择是公共子矩阵 `M_{[S2,S1]}` 的伪逆，此时近似可以解释为用选中行列重建未选中的块。

## 选择问题

CUR 的核心难点仍是行列选择。文章列出模长、随机采样、列驱 QR、杠杆分数、DEIM 等方案。