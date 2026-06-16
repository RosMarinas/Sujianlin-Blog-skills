---
type: example
title: spaces-11619-QB最优分配推导
aliases: []
article_id: '11619'
article: '[[MoE环游记：6. 最优分配促均衡]]'
section: 线性规划
claim: Top-k MoE 负载均衡可以写成约束分配问题，并通过对偶变量得到分位数偏置。
notation_mapping:
  same_as_standard: true
steps:
- 定义二值分配变量 `x_ij`。
- 添加每 Token 激活 `k` 个 Expert 和每 Expert 激活 `mk/n` 次的约束。
- 松弛为线性规划并交换 max-min。
- 固定一组对偶变量，另一组变量的最优值由排序分位数给出。
used_concepts:
- '[[Quantile Balancing]]'
- '[[MoE负载均衡]]'
used_formulas:
- '[[QB分位数偏置公式]]'
used_methods:
- '[[用分位数求解负载均衡偏置]]'
- '[[用对偶偏置改写路由约束]]'
problem_pattern: '[[将路由选择转化为约束分配问题]]'
source_span: ev::11619::线性规划
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-02-22-MoE环游记-6-最优分配促均衡.md
source_ids:
- '11619'
status: stable
updated: '2026-06-12'
---

# spaces-11619-QB最优分配推导

## 问题

源文“线性规划”把 Top-k MoE 的负载均衡写成严格约束分配问题：每个 Token 选 $k$ 个 Expert，每个 Expert 被激活 $mk/n$ 次，并使总 Router 分数最大。

## 推导

原始问题是
$$
\max_{x_{i,j}\in\{0,1\}}\sum_{i,j}x_{i,j}s_{i,j}
\quad\text{s.t.}\quad \sum_jx_{i,j}=k,\quad \sum_ix_{i,j}=\frac{mk}{n}.
$$
源文先松弛为 $x_{i,j}\in[0,1]$，再引入拉格朗日乘子 $\alpha_i,\beta_j$，把约束问题改写为 max-min 形式。交换极大极小后，对 $x_{i,j}$ 的最大化给出阈值规则：当 $s_{i,j}-\alpha_i-\beta_j>0$ 时取 1，否则取 0。随后固定 $\beta$ 求 $\alpha$，问题分解为排序后的分位点选择；固定 $\alpha$ 求 $\beta$ 同理。最终只需保留 $\boldsymbol{\beta}^*$，推理时选择 $\boldsymbol{s}_i-\boldsymbol{\beta}^*$ 的 Top-k。

## 方法与证据

本例体现“整数分配松弛、对偶化、分位数交替最小化”的方法。证据锚点为 `ev::11619::线性规划`，源文还给出 Quantile Balancing 的迭代算法，说明 $\boldsymbol{\alpha}$ 是中间变量而 $\boldsymbol{\beta}$ 是固定大小的推理偏置。
