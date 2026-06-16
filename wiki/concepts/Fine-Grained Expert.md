---
type: concept
title: Fine-Grained Expert
aliases:
- 细颗粒度专家
definition: 在总参数量和激活参数量基本不变时，将 Expert 切得更细，以扩大 Expert 组合空间和知识覆盖粒度。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md
source_ids:
- '10945'
prerequisites:
- '[[MoE负载均衡]]'
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods: []
series:
- '[[MoE环游记]]'
evidence_spans:
- ev::10945::细颗粒度
status: stable
updated: '2026-06-13'
---

# Fine-Grained Expert

## 定义

Fine-Grained Expert 指在总参数量和激活参数量基本不变时，把每个 Expert 切得更小、数量变得更多。例如源文把原来的 `n` 选 `k` 改成 `2n` 选 `2k`，计算预算不变，但可用组合数从 `C(n,k)` 扩大到 `C(2n,2k)`。

## 激活场景

它出现在 MoE 对“均匀分布是否最优”的反思中。源文将它与 Shared Expert 并列为 DeepSeekMoE 的重要策略，用来增加 Expert 组合多样性，并使每个小 Expert 更专注于更窄的知识区域。

## 关键关系

Fine-Grained Expert 的收益与非均匀知识覆盖有关：更多、更细的 Expert 可以用同样总面积覆盖更细的知识结构，减少遗漏和浪费。但源文也强调它不是无成本技巧，Expert 数量越大，负载不均衡、通信和协调成本往往越高，因此需要效果与效率之间的舒适区间。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2025-05-16-MoE环游记-5-均匀分布的反思.md`
- `ev::10945::细颗粒度`
