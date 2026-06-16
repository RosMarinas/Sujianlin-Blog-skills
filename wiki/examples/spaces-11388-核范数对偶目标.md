---
type: example
title: spaces-11388-核范数对偶目标
aliases: []
article_id: '11388'
article:
- - 流形上的最速下降：5. 对偶梯度下降
section: 对偶目标
claim: 待定系数约束方程可作为核范数目标的梯度，用对偶梯度下降求解。
notation_mapping:
  G: boldsymbol{G}
  Theta: boldsymbol{Theta}
  lambda: lambda
  msign: msign
steps:
- 利用核范数梯度等于 msign
- 对 lambda 求导得到约束残差
- 最小化核范数目标使残差趋零
- 把 lambda 缓存在训练循环中同步更新
used_concepts:
- - - 核范数对偶目标
- - - 谱球面约束
- - - Stiefel流形约束
used_formulas:
- - - 核范数对偶目标公式
used_methods:
- - - 用对偶目标求解约束更新系数
problem_pattern:
- - 把约束优化器更新转化为切空间或对偶变量问题
source_span: ev::11388::对偶目标
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-11-03-流形上的最速下降-5-对偶梯度下降.md
source_ids:
- '11388'
status: stable
updated: '2026-06-12'
---

# spaces-11388-核范数对偶目标

## 所在文章

[[流形上的最速下降：5. 对偶梯度下降]]

## 原始问题

待定系数约束方程可作为核范数目标的梯度，用对偶梯度下降求解。

## 推导步骤

1. 利用核范数梯度等于 msign
2. 对 lambda 求导得到约束残差
3. 最小化核范数目标使残差趋零
4. 把 lambda 缓存在训练循环中同步更新

## 证据锚点

- `ev::11388::对偶目标`