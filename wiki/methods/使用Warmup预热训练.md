---
type: method
title: "使用Warmup预热训练"
aliases:
  - "Learning Rate Warmup"
  - "Warmup Strategy"
operation_types:
  primary: "Construct auxiliary sequence"
  secondary:
    - "Align / calibrate by invariance"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-08-模型优化漫谈-BERT的初始标准差为什么是0-02.md
source_ids:
  - "8747"
method_summary: "在训练开始阶段将学习率从0线性或指数增加到预定值，防止Post Norm Transformer等结构中因梯度消失导致的训练崩盘。Warmup抑制后面层过快学习，给前面层预留优化时间，促进各层同步收敛。"
typical_structure: |
  1. 选定Warmup步数W和目标学习率η_target。
  2. 前W步学习率从0线性增加到η_target: η_t = η_target·t/W（t=1,...,W）。
  3. W步后正常衰减或恒定。
  4. 可选：Warmup后配合余弦退火或线性衰减。
applicability: 必须用于Post Norm Transformer/BERT训练。对Pre Norm或无梯度消失的结构非必需。对需要精细调参的大模型训练几乎标配。
tools:
  - "学习率调度"
examples:
  - "[[模型优化漫谈：BERT的初始标准差为什么是0.02？]]"
problem_patterns: []
related_methods:
  - "[[用门控机制控制梯度传播]]"
evidence_spans:
  - "ev::8747::Warmup必要性"
status: draft
updated: 2026-06-12
---

## 适用问题

深度神经网络训练中的梯度消失和训练崩盘问题，特别是Post Norm Transformer/BERT等结构。Warmup几乎是大模型训练的标配技巧。

## 核心变换

**输入**：固定学习率$\eta_{\text{target}}$
**输出**：$W$步预热学习率$\eta_t$

$$
\eta_t = \eta_{\text{target}} \cdot \frac{t}{W}, \quad t = 1, 2, \ldots, W
$$

前$W$步学习率从0线性（或指数）增加到目标值，$W$步后正常衰减。

## 典型步骤

1. **选择预热步数$W$**：通常为训练总步数的5%-10%
2. **选择目标学习率$\eta_{\text{target}}$**：Post Norm Transformer常见1e-4到5e-5
3. **线性预热**：$\eta_t = \eta_{\text{target}} \cdot t / W$
4. **到达目标学习率**：$W$步后按预定策略衰减（余弦退火、线性衰减等）
5. **训练监控**：观察loss是否在预热阶段平稳下降

## 直觉

Warmup的必要性源于Post Norm结构的梯度消失特性。在Post Norm中，深层网络的输出方差随层数增加而增大，导致早期训练时梯度在反向传播中快速衰减。Adam虽然能自适应调整学习率，但它对每个参数独立调整，无法解决"各层优化不同步"的问题。

Warmup通过在前$W$步使用小学习率，**抑制后面层的过快学习**，让前面层有足够时间找到合理的表示方向。无Warmup时：
1. 后面层在糟糕的输入上快速收敛到局部最优
2. 反向传播给前面层的梯度变弱且方向不准
3. Adam的常数量级更新导致前面层按随机方向更新
4. 最终训练崩盘

## 边界

- **非必需**：对Pre Norm结构（输出方差可控）或无梯度消失的模型，Warmup可省略
- Warmup步数$W$过短起不到稳定作用，过长浪费训练时间
- 也有些工作使用指数式Warmup（从极小学习率指数增长到目标值）
- Warmup后通常配合学习率衰减策略（余弦退火、多项式衰减等）

## 例子

- Post Norm BERT训练：通常前10%步Warmup，学习率从0线性增加到5e-5
- BERT初始标准差0.02：Post Norm结构的标准设计，Warmup的必要性由此而来

## 证据

- ev::8747::Warmup必要性：通过抑制后面层学习速度让各层同步优化，防止Post Norm训练崩盘
