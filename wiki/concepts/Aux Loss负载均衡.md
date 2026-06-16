---
type: concept
title: Aux Loss负载均衡
aliases:
- Auxiliary Loss load balancing
definition: 通过额外损失项推动 MoE 实际负载分布接近目标分布的均衡方法，其经典形式可由 STE 等效梯度解释。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
source_ids:
- '10735'
prerequisites:
- '[[MoE负载均衡]]'
equivalent_forms:
- '[[Aux Loss负载均衡公式]]'
direct_consequences:
- '[[Aux Loss是STE均衡目标的等效梯度]]'
related_formulas:
- '[[Aux Loss负载均衡公式]]'
related_methods: []
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::10735::辅助损失
- ev::10735::直通估计
status: stable
updated: '2026-06-12'
---

# Aux Loss负载均衡

## 定义

Aux Loss 路线用额外目标约束 Router，使 Top-k 后的负载分布 `F` 向目标分布移动。本文批次中的关键点是：经典 `F·P` 形式有等效梯度意义，但不能简单按普通 Loss 理解。

## 限制

Aux Loss 需要权重系数，并且可能让均衡目标和 LM Loss 优化方向互相干扰。这一限制推动了 [[Loss-Free偏置]] 路线。

## 证据

- `ev::10735::辅助损失`
- `ev::10735::直通估计`