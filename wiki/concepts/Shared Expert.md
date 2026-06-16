---
type: concept
title: Shared Expert
aliases:
- 共享专家
definition: 在 MoE 中固定激活少量 Expert，将共同知识或公共残差集中到这些专家中，剩余 Routed Expert 继续按路由选择。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md
source_ids:
- '10945'
prerequisites:
- '[[MoE几何路由]]'
equivalent_forms: []
direct_consequences: []
related_formulas:
- '[[MoE基本路由公式]]'
related_methods: []
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::10945::共享专家
- ev::10945::非均匀性
status: stable
updated: '2026-06-13'
---

# Shared Expert

## 定义

Shared Expert 是 MoE 中固定必选的一小组 Expert。源文将原来的 `n` 选 `k` 改为先固定选择 `s` 个 Shared Expert，再从剩下 `n-s` 个 Routed Expert 中选择 `k-s` 个；通常 `s` 很小，如 1 或 2。

## 激活场景

该概念用于在不增加总 Expert 数和激活 Expert 数的前提下，把共同知识压缩到少量共享专家中。源文说明开启前后总 Expert 数仍为 `n`、激活数仍为 `k`，原则上不增加模型参数量和推理成本。

## 关键关系

Shared Expert 与 Loss-Free、动态激活等路由变体正交。它从残差视角看，是让 Routed Expert 学习相对 Shared Expert 的差异；从几何视角看，可理解为用共享均值减去共性，使 Routed Expert 更接近“两两正交”的假设。它也说明 MoE 中完全均匀的 Expert 分布不一定是效果最优方向。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md`
- `ev::10945::共享专家`
- `ev::10945::非均匀性`
