---
type: article_summary
title: "AdaFactor优化器浅析（附开源实现）"
article_id: "7302"
source_url: https://spaces.ac.cn/archives/7302
date: 2020-03-23
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-03-23-AdaFactor优化器浅析-附开源实现.md
series:
  - "[[从动力学角度看优化算法]]"
topics:
  - "[[优化动力学]]"
concepts:
  - "[[AdaFactor优化器]]"
  - "[[广义KL散度]]"
  - "[[低秩分解二阶矩估计]]"
  - "[[时变Beta2衰减]]"
methods:
  - "[[把优化算法解释为动力系统离散化]]"
evidence_spans:
  - "ev::7302::Adam回顾"
  - "ev::7302::抛弃动量"
  - "ev::7302::低秩分解"
  - "ev::7302::广义KL散度推导"
  - "ev::7302::滑动权重"
  - "ev::7302::层自适应"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-03-23-AdaFactor优化器浅析-附开源实现.md
source_ids:
  - "7302"
status: draft
updated: 2026-06-10
---

# AdaFactor优化器浅析（附开源实现）

## Summary

Google提出的AdaFactor优化器通过抛弃动量、低秩分解二阶矩估计、时变Beta2衰减和层自适应，大幅减少优化器显存占用，同时解决Adam的一些缺陷。

## Key Claims

1. 移除动量（m）可省一半缓存，对NLP任务影响较小。
2. 对梯度平方矩阵做秩1分解（广义KL散度下求解析解）可大幅减少v的参数量。
3. Beta2应从固定值改为时变衰减：β̂_{2,t}=1-t^{-c}，满足β̂_{2,1}=0、β̂_{2,∞}=1。
4. 基于参数模长标准化更新量（来自LAMB思想）使各层更新更同步。
5. AdaFactor适合大Batch Size场景，学习率需设大（~1e-3）。
