---
type: concept
title: "Warmup训练策略"
aliases:
  - "Warmup"
  - "学习率预热"
definition: "在训练开始阶段将学习率从0缓增到指定大小的策略，用于防止Post Norm结构模型因梯度消失导致后面层过快收敛后崩盘。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-08-模型优化漫谈-BERT的初始标准差为什么是0-02.md
source_ids:
  - "8747"
prerequisites:
  - "[[PostNorm梯度消失]]"
  - "[[Adam优化器]]"
equivalent_forms: []
related_methods:
  - "[[使用Warmup预热训练]]"
evidence_spans:
  - "ev::8747::Warmup必要性"
status: draft
updated: 2026-06-12
---

# Warmup训练策略

## Definition

在Post Norm Transformer中，梯度消失使后面层对输出更敏感、学习更快。无Warmup时后面层快速在糟糕输入上收敛到局部最优点，此时反向传播给前面层的梯度变弱且不准，Adam的常数量级更新使前面层按随机方向更新，导致崩盘。Warmup通过小学习率启动，抑制后面层学习速度，给前面层更多优化时间，促进各层同步优化。通常前W步学习率从0线性增加到目标值，然后正常衰减。
