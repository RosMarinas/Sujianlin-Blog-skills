---
type: concept
title: MoE几何路由
aliases:
- geometric MoE routing
definition: 将 Dense FFN 分块为多个 Expert 向量之和，并把 MoE 路由解释为低成本预测向量模长后选择 Top-k 方向的近似求和过程。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-02-08-MoE环游记-1-从几何意义出发.md
source_ids:
- '10699'
prerequisites: []
equivalent_forms:
- '[[MoE基本路由公式]]'
direct_consequences:
- '[[Loss-Free通过偏置隔离均衡优化]]'
related_formulas:
- '[[MoE基本路由公式]]'
related_methods:
- '[[从计算节省目标重写模型结构]]'
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::10699::问题定义
- ev::10699::MoE初现
status: stable
updated: '2026-06-12'
---

# MoE几何路由

## 定义

[[MoE几何路由]] 把 Expert 选择解释为近似 Dense FFN 输出的几何问题：先把 FFN 写成多个 Expert 向量之和，再用 Router 低成本预测每个 Expert 的模长，最后只计算 Top-k 的方向向量。

## 激活作用

这个概念使 Router 不只是分类器或概率分布，而是一个用于降低计算量的近似选择器。它也解释了为什么后续均衡方法都围绕“选择哪些 Expert”而不是“重新定义 Expert 输出”展开。

## 证据

- `ev::10699::问题定义`
- `ev::10699::MoE初现`