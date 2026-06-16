---
type: proposition
title: Loss-Free通过偏置隔离均衡优化
aliases: []
statement: Loss-Free 的核心作用是把负载均衡优化集中到只参与路由排序的偏置项上，从而减少 Aux Loss 对 LM Loss 优化方向的直接干扰。
assumptions:
  - "偏置只用于 Expert 分配，不乘到 Expert 输出上"
  - "偏置更新发生在当前 batch 路由之后"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-03-05-MoE环游记-3-换个思路来分配.md
source_ids:
  - "10757"
requires:
  - "[[Loss-Free偏置]]"
  - "[[Loss-Free偏置更新]]"
proof_route: 文章将 Loss-Free 与 Aux Loss 对比，指出前者让 Aux Loss 类目标只优化新引入偏置，而 LM Loss 优化其余参数。
methods:
  - "[[用对偶偏置改写路由约束]]"
limits:
  - 仍需要偏置学习率或等价更新规则；SignSGD 版本对 Router 激活函数和层分布敏感。
examples:
  - "[[spaces-10757-Loss-Free偏置隔离]]"
evidence_spans:
  - ev::10757::一脉相承
status: stable
updated: 2026-06-09
---

# Loss-Free通过偏置隔离均衡优化

## 命题

Loss-Free 的关键不是简单取消损失，而是把均衡压力从主模型梯度中拆出来，让偏置承担路由均衡职责。

## 证据

- `ev::10757::一脉相承`
