---
title: Wasserstein距离对偶形式
type: formula
status: draft
standard_notation: Wasserstein距离对偶形式
updated: '2026-06-14'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
latex: \mathcal{C}[p,q] = \inf_{\gamma \in \Pi[p,q]} \iint \gamma(x,y) c(x,y) \, dx \, dy
symbol_meanings:
  \mathcal{C}[p,q]: 最优传输代价
  \gamma: 联合分布（运输方案）
  \Pi[p,q]: 所有以 $p,q$ 为边缘分布的联合分布集合
  c(x,y): 运输成本函数
  p, q: 边缘概率分布
conditions:
- p 与 q 为具有有限运输代价的概率分布，Pi[p,q] 表示以二者为边缘分布的耦合集合。
- 成本函数 c(x,y) 非负且满足最优传输对偶所需的可测/下半连续等正则条件。
- WGAN 形式对应一阶 Wasserstein 距离，此时对偶函数 f 需要满足 1-Lipschitz 约束。
appears_in:
- （待从源文章提取）
---

# Wasserstein距离对偶形式


## 概述

（待补充）

## Primal Form (Optimal Transport)
C[p,q] = inf_{γ∈Π[p,q]} ∬ γ(x,y) c(x,y) dx dy

## Dual Form
C[p,q] = max_{f,g} { ∫ [p(x)f(x) + q(x)g(x)] dx | f(x) + g(y) ≤ c(x,y) }

## WGAN Form (c(x,y) = ||x-y||)
W₁[p,q] = max_{f, ||f||_L ≤ 1} E_{x~p}[f(x)] - E_{x~q}[f(x)]

## Variables
- γ: 联合分布（运输方案）
- c: 成本函数
- f,g: 对偶变量（Kantorovich势）
- ||·||_L: Lipschitz常数

## Related Sources
- [[sources/spaces-6280-Wasserstein-WGAN]]