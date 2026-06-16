---
title: f散度及其对偶形式
type: formula
status: draft
standard_notation: f散度及其对偶形式
updated: '2026-06-14'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
latex: D_f(P\|Q) = \int q(x) f\left(\frac{p(x)}{q(x)}\right) dx
symbol_meanings:
  D_f(P\|Q): $f$-散度
  P, Q: 概率分布
  p(x): 分布 $P$ 的概率密度函数
  q(x): 分布 $Q$ 的概率密度函数
  f: 凸函数且 $f(1)=0$
conditions: （待从源文章提取）
appears_in:
- （待从源文章提取）
---

# f散度及其对偶形式


## 概述

（待补充）

## Definition
D_f(P||Q) = ∫ q(x) f(p(x)/q(x)) dx

## Fenchel Conjugate
f(u) = max_t { t u - g(t) }
g(t) = -f(ξ) + f'(ξ)ξ, where t = f'(ξ)

## f-GAN Form
min_G max_T E_{x~p}[T(x)] - E_{x~G(z)}[g(T(x))]

## Variables
- P, Q: 概率分布
- f: 凸函数, f(1)=0
- g: f的Fenchel共轭
- T: 判别器网络
- G: 生成器网络

## Related Sources
- [[sources/spaces-6016-f-GAN]]