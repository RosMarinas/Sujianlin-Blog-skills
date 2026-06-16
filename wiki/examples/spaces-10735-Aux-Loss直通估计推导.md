---
type: example
title: spaces-10735-Aux-Loss直通估计推导
aliases: []
article_id: '10735'
article: '[[MoE环游记：2. 不患寡而患不均]]'
section: 直通估计
claim: 经典 Aux Loss 可由 STE 可导化的负载均衡目标推出等效梯度。
notation_mapping:
  same_as_standard: true
steps:
- 定义目标均匀分布 `Q` 和实际负载分布 `F`。
- 写出直观目标 `1/2||F-Q||^2`。
- 用 `P + sg[F-P]` 替换不可导的 `F`。
- 展开梯度，得到与 `F·P` 相同的梯度。
used_concepts:
- '[[Aux Loss负载均衡]]'
- '[[MoE负载均衡]]'
used_formulas:
- '[[Aux Loss负载均衡公式]]'
used_methods: []
problem_pattern: '[[将路由选择转化为约束分配问题]]'
source_span: ev::10735::直通估计
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
source_ids:
- '10735'
status: stable
updated: '2026-06-12'
---

# spaces-10735-Aux-Loss直通估计推导

## 问题

源文“直通估计”一节要解释经典 MoE Aux Loss 为什么能促进负载均衡。负载分布 $\boldsymbol{F}$ 来自 Top-k 路由，不可导；$\boldsymbol{P}$ 是由归一化打分平均得到的光滑近似。

## 推导

均衡目标先写成
$$
\mathcal{L}_{aux}=\frac12\Vert\boldsymbol{F}-\boldsymbol{Q}\Vert^2,\qquad \boldsymbol{Q}=(1/n,\ldots,1/n).
$$
由于 $\boldsymbol{F}$ 不可导，源文用 STE 把实现目标改成
$$
\frac12\Vert\boldsymbol{P}+\mathrm{sg}[\boldsymbol{F}-\boldsymbol{P}]-\boldsymbol{Q}\Vert^2.
$$
求梯度时 stop_gradient 使前向值仍为 $\boldsymbol{F}$，反向路径走 $\boldsymbol{P}$，于是
$$
\nabla_{\boldsymbol{\theta}}\mathcal{L}_{aux}
=\sum_i(F_i-1/n)\nabla_{\boldsymbol{\theta}}P_i
=\nabla_{\boldsymbol{\theta}}\sum_iF_iP_i.
$$
这说明常见的 $\boldsymbol{F}\cdot\boldsymbol{P}$ 是等效梯度形式，而不是真正按数值越小越好的 Loss。

## 方法与证据

本例体现“用 STE 把不可导负载分布替换为可导近似，同时保持前向统计”的方法。证据锚点为 `ev::10735::直通估计`，源文还说明该套路可推广到熵式 Aux Loss 和非均匀目标分布。
