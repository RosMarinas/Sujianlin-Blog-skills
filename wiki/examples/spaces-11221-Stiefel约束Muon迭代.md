---
type: example
title: spaces-11221-Stiefel约束Muon迭代
aliases: []
article_id: '11221'
article:
- - 流形上的最速下降：3. Muon + Stiefel
section: 方程变换
claim: Stiefel-Muon 的约束方向可写成切空间方程加待定矩阵求解。
notation_mapping:
  W: boldsymbol{W}
  Phi: boldsymbol{Phi}
  X: boldsymbol{X}
steps:
- 写出 Stiefel 正交约束
- 一阶展开得到切空间条件
- 引入待定矩阵 X 修正梯度
- 通过迭代求满足条件的 msign 方向
used_concepts:
- - - Stiefel流形约束
- - - 切空间投影
used_formulas:
- - - Stiefel切空间条件公式
used_methods:
- - - 用切空间投影改写约束最速下降
problem_pattern:
- - 把约束优化器更新转化为切空间或对偶变量问题
source_span: ev::11221::方程变换
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-08-08-流形上的最速下降-3-Muon-Stiefel.md
source_ids:
- '11221'
status: stable
updated: '2026-06-12'
---

# spaces-11221-Stiefel约束Muon迭代

## 所在文章

[[流形上的最速下降：3. Muon + Stiefel]]

## 原始问题

Stiefel-Muon 的约束方向可写成切空间方程加待定矩阵求解。

## 推导步骤

1. 写出 Stiefel 正交约束
2. 一阶展开得到切空间条件
3. 引入待定矩阵 X 修正梯度
4. 通过迭代求满足条件的 msign 方向

## 证据锚点

- `ev::11221::方程变换`