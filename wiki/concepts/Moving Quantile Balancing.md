---
type: concept
title: Moving Quantile Balancing
aliases:
- MQB
definition: 用分桶分布估计和 EMA 近似序列局部 Quantile 的 Loss-Free 序列级均衡方法。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
source_ids:
- '11760'
prerequisites:
- '[[Quantile Balancing]]'
equivalent_forms:
- '[[MQB分桶EMA公式]]'
direct_consequences:
- '[[MQB用分桶EMA近似序列级分位数]]'
related_formulas:
- '[[MQB分桶EMA公式]]'
related_methods:
- '[[用分布估计近似滑动分位数]]'
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::11760::滑动分位
- ev::11760::分桶估计
status: stable
updated: '2026-06-12'
---

# Moving Quantile Balancing

## 定义

MQB 将序列级 Quantile 估计改写为分桶分布的 EMA 更新。它保留 QB 的分位数解释，同时避免逐位置直接计算滑动 Quantile 的高成本。

## 限制

过强的序列级均衡会损伤效果，实际需要用 `lambda` 控制干预强度。

## 证据

- `ev::11760::滑动分位`
- `ev::11760::分桶估计`