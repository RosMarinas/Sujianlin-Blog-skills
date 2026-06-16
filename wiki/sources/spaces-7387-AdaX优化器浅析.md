---
type: article_summary
title: "AdaX优化器浅析（附开源实现）"
article_id: "7387"
source_url: https://spaces.ac.cn/archives/7387
date: 2020-05-11
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-05-11-AdaX优化器浅析-附开源实现.md
series: []
topics:
  - "[[优化动力学]]"
concepts:
  - "[[AdaX优化器]]"
  - "[[指数长期记忆优化器]]"
  - "[[时变Beta2衰减]]"
evidence_spans:
  - "ev::7387::AdaX格式"
  - "ev::7387::等价形式变换"
  - "ev::7387::衰减策略比较"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-11-AdaX优化器浅析-附开源实现.md
source_ids:
  - "7387"
status: draft
updated: 2026-06-10
---

# AdaX优化器浅析（附开源实现）

## Summary

介绍AdaX优化器，其v_t更新采用(1+β2)v_{t-1}+β2 g_t^2的指数长期记忆策略，并证明其等效Beta2衰减满足β̂_{2,1}=0, β̂_{2,∞}=1的理想性质。

## Key Claims

1. AdaX将Adam的v_t滑动平均改为(1+β2)v_{t-1}+β2 g_t^2，β2默认0.0001。
2. 变换后β̂_{2,t}=1-β2/((1+β2)^t-1)，满足β̂_{2,1}=0, β̂_{2,∞}=1。
3. 该性质（β̂_{2,1}=0, β̂_{2,∞}=1）应成为优化器改进的基本条件之一，与AdaFactor的结论一致。
