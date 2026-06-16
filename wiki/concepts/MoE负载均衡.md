---
type: concept
title: MoE负载均衡
aliases:
- load balance
- expert load balancing
definition: 让 Expert 的实际激活分布接近目标分布，以避免 Dead Expert、Token Drop、算力浪费和有效参数量下降。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-02-21-MoE环游记-2-不患寡而患不均.md
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-22-MoE环游记-8-强制序列级均衡.md
source_ids:
- '10735'
- '11760'
prerequisites:
- '[[MoE几何路由]]'
equivalent_forms: []
direct_consequences:
- '[[Aux Loss是STE均衡目标的等效梯度]]'
- '[[QB把负载均衡转化为分位数偏置]]'
related_formulas:
- '[[Aux Loss负载均衡公式]]'
- '[[QB分位数偏置公式]]'
related_methods:
- '[[用对偶偏置改写路由约束]]'
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::10735::需求分析
- ev::11760::前文回顾
status: stable
updated: '2026-06-12'
---

# MoE负载均衡

## 定义

MoE 负载均衡关注 Expert 被激活的实际分布是否接近目标分布。它既是效率问题，也是有效参数量问题：过热 Expert 会导致 Token Drop，冷门 Expert 会接近闲置。

## 常见层级

均衡可以发生在全局 batch、设备、分组、序列或局部窗口等层级。全局均衡通常更稳定，序列级均衡更强但可能损伤效果。

## 证据

- `ev::10735::需求分析`
- `ev::11760::前文回顾`