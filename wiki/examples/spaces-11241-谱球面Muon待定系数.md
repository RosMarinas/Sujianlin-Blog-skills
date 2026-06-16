---
type: example
title: spaces-11241-谱球面Muon待定系数
aliases: []
article_id: '11241'
article:
- - 流形上的最速下降：4. Muon + 谱球面
section: 待定系数
claim: 谱球面-Muon 把保持谱范数的约束转成一个标量待定系数方程。
notation_mapping:
  G: boldsymbol{G}
  Theta: boldsymbol{Theta}
  lambda: lambda
  Phi: boldsymbol{Phi}
steps:
- 写出谱范数保持约束
- 用最大奇异向量给出一阶条件
- 把方向写为 msign(G + lambda Theta)
- 通过迭代求 lambda
used_concepts:
- - - 谱球面约束
- - - 流形最速下降
used_formulas:
- - - 核范数对偶目标公式
used_methods:
- - - 用切空间投影改写约束最速下降
problem_pattern:
- - 把约束优化器更新转化为切空间或对偶变量问题
source_span: ev::11241::待定系数
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-08-21-流形上的最速下降-4-Muon-谱球面.md
source_ids:
- '11241'
status: stable
updated: '2026-06-12'
---

# spaces-11241-谱球面Muon待定系数

## 所在文章

[[流形上的最速下降：4. Muon + 谱球面]]

## 原始问题

谱球面-Muon 把保持谱范数的约束转成一个标量待定系数方程。

## 推导步骤

1. 写出谱范数保持约束
2. 用最大奇异向量给出一阶条件
3. 把方向写为 msign(G + lambda Theta)
4. 通过迭代求 lambda

## 证据锚点

- `ev::11241::待定系数`