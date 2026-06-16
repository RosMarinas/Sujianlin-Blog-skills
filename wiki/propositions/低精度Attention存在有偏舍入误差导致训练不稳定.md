---
type: proposition
title: 低精度Attention存在有偏舍入误差导致训练不稳定
aliases:
  - Low-precision Attention Biased Rounding Error
statement: BF16精度下Attention的P_bar*V计算存在有偏的舍入误差，触发条件是V各向异性、注意力集中、"两大一小"加法场景。该偏差可导致MaxLogit爆炸和Loss Spike。
assumptions:
  - "BF16精度下P_bar*V使用FP32累加后转BF16"
  - "注意力分布具有集中特性"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-27-低精度Attention可能存在有偏的舍入误差.md
source_ids:
  - "11371"
evidence_spans:
  - "ev::11371::量身定制"
  - "ev::11371::两大一小"
status: draft
updated: 2026-06-10
---

# 低精度Attention存在有偏舍入误差导致训练不稳定

## 内容

BF16精度下，Attention的softmax输出与V的矩阵乘法存在系统性偏差。极小余项破坏"向偶舍入"规则产生正偏差，且注意力越集中偏差越显著。修正方案为使用beta>=2的缩放因子使极小项下溢消失。
