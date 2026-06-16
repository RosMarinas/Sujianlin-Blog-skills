---
type: concept
title: Tiger优化器
aliases:
  - Tiger
  - Tight-fisted Optimizer
definition: 一种将Lion优化器滑动平均率退化为单个常数β的极简符号优化器。该设计允许优化器在进行梯度累积时，无需分配额外显存即可无感实现等效更新。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-07-Tiger-一个-抠-到极致的优化器.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-28-Lion-Tiger优化器训练下的Embedding异常和对策.md
source_ids:
  - "9512"
  - "9736"
related_formulas:
  - "[[Tiger优化器更新公式]]"
related_methods:
  - "[[用符号函数重写优化器更新方向]]"
  - "[[通过矩阵块自适应缩放学习率]]"
evidence_spans:
  - ev::9512::Tiger更新公式
status: draft
updated: 2026-06-12
---

# Tiger优化器

## 核心定义

**Tiger优化器**（Tight-fisted Optimizer，抠门的优化器）是基于 [Lion优化器](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Lion优化器.md) 在滑动平均率统一时的特例（$\beta_1 = \beta_2 = \beta$）演化出的极简符号优化算法。由于更新过程不再交织当前的原始梯度，仅依赖于动量本身的符号信息，因而能够实现理论上最省显存的梯度累积实现。

## 核心特性

1. **零显存无感梯度累积**：
   - 在传统的自适应优化器（如 AdamW、Lion）中，进行 $k$ 步梯度累积时，必须新增一组变量缓存这 $k$ 步的平均/累加梯度。
   - 而 Tiger 更新量仅为 $\text{sign}(\boldsymbol{m}_t)$。由“动量中隐含的梯度累积”原理，通过在 $t \not\equiv 0 \pmod k$ 时停止参数更新，并在整除步时才进行符号方向更新，同时动态调节 $\beta$ 与全局学习率，即可完美等价实现梯度累积而**不占用任何额外显存空间**。
2. **块级均方根 (RMS) 自适应缩放**：
   - 采用自适应步长策略，对偏置（bias）、归一化参数（beta, gamma）不进行权重衰减并使用固定的一半相对步长。
   - 对线性层的核心 Kernel 矩阵，将学习率动态乘以权重模长 $\text{RMS}(\boldsymbol{\theta})$。此举将参数的模长与更新步长进行尺度解耦，使全局学习率 $\alpha_t$ 可以无感移植于不同规模的大模型。
3. **天然支持全半精度 (FP16) 计算**：
   - 由于最终的有效更新分量只有符号 $\pm 1$，因此在混合精度或直接全半精度训练中，只要学习率落在 FP16 表示边界（$\ge 6\times 10^{-8}$）以上，参数就绝对不会发生下溢出，相比 AdamW 稳定性更高。
4. **异常梯度防御（防NaN）**：
   - 内置异常检测：若当前步梯度为 NaN，则保持动量不变，并将模型参数朝着其初始化中心方向做以 $s=0.99$ 为比例的中心化收缩，以减缓模型发散的风险。
