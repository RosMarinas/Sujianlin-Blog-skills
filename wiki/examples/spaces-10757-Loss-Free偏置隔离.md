---
type: example
title: spaces-10757-Loss-Free偏置隔离
aliases: []
article_id: '10757'
article: '[[MoE环游记：3. 换个思路来分配]]'
section: 一脉相承
claim: Loss-Free 通过只优化偏置项来隔离负载均衡和 LM Loss 的参数更新。
notation_mapping:
  same_as_standard: true
steps:
- 保留 Router 原始分数作为 Expert 门控。
- 在路由排序中加入偏置 `b`。
- 根据负载统计更新 `b`。
- 让 LM Loss 继续优化主模型参数。
used_concepts:
- '[[Loss-Free偏置]]'
used_formulas:
- '[[Loss-Free偏置更新]]'
used_methods:
- '[[用对偶偏置改写路由约束]]'
problem_pattern: '[[将路由选择转化为约束分配问题]]'
source_span: ev::10757::一脉相承
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
source_ids:
- '10757'
status: stable
updated: '2026-06-12'
---

# spaces-10757-Loss-Free偏置隔离

## 问题

源文“一脉相承”一节解释 Loss-Free 的核心并不是字面上的“没有 Aux Loss”，而是把负载均衡所需的更新从 LM Loss 的主模型参数中隔离出来。

## 推导

Loss-Free 在 Router 打分中引入偏置 $\boldsymbol{b}$：
$$
\boldsymbol{y}=\sum_{i\in\mathrm{argtop}_k\boldsymbol{\rho}+\boldsymbol{b}}\rho_i\boldsymbol{e}_i.
$$
源文指出，$\boldsymbol{b}$ 只改变 Expert 排序，真正乘到 Expert 输出上的仍是 $\rho_i$，因此它不直接参与模型计算。负载统计 $\boldsymbol{F}$ 高于目标 $\boldsymbol{Q}$ 的 Expert 降低偏置，低于目标的 Expert 增大偏置；这样 Aux Loss 的作用被限制在新引入的偏置项上，而 LM Loss 继续优化其余参数。

## 方法与证据

这个例子体现“用额外排序偏置承担约束修正，把均衡目标和主任务参数更新隔离”的方法。证据锚点为 `ev::10757::一脉相承`，源文明确说 Loss-Free 的本质创新是“一个偏置项足以达到负载均衡”，从而让负载均衡和模型能力两不误。
