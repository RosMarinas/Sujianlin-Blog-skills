---
type: concept
title: 时变Beta2衰减
aliases:
- time-varying beta2
- adaptive beta2 schedule
definition: 优化器（Adam/AdaFactor/AdaX）中二阶矩衰减系数应随步数变化：初期β̂_{2,1}=0（用实时梯度校正），后期β̂_{2,∞}=1（退化为SGD/固定学习率），而非固定常数。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-03-23-AdaFactor优化器浅析-附开源实现.md
- Data/Spaces_ac_cn/markdown/Big-Data/2020-05-11-AdaX优化器浅析-附开源实现.md
source_ids:
- '7302'
- '7387'
prerequisites:
- '[[Adam优化器]]'
equivalent_forms: []
related_formulas: []
related_methods: []
evidence_spans:
- ev::7302::滑动权重
- ev::7387::衰减策略比较
status: draft
updated: '2026-06-12'
---

# 时变Beta2衰减

## Definition

标准Adam使用固定β₂（如0.999），导致训练后期当前梯度权重(1-β₂)非零——但后期梯度变小，校正学习率意义不大。理想性质：β̂_{2,1}=0（起始用实时梯度），β̂_{2,∞}=1（退化为SGD）。AdaFactor使用β̂_{2,t}=1-t^{-c}，AdaX使用β̂_{2,t}=1-β₂/((1+β₂)^t-1)，两者均满足该条件。