---
type: concept
title: DropToken
definition: "一种受MAE启发提出的正则化与加速训练方法，随机丢弃部分输入Token但保留剩余Token的原始绝对位置。"
sources:
  - wiki/sources/spaces-8770-Dropout视角MLM-MAE.md
source_ids:
  - "8770"
aliases: [DropToken, Token Dropout, 随机丢弃Token]
tags: [regularization, transformer, training-speed, dropout-variant]
related_concepts: [Dropout, MAE]
related_sources: [spaces-8770-Dropout视角下的MLM和MAE]
status: draft
updated: 2026-06-12
---
## Definition

DropToken是一种受MAE启发提出的正则化方法：在训练阶段随机丢弃一些Token，但保留剩余Token的原始位置。它显式缩短了序列长度，兼顾正则化和训练加速。

## Mechanism

与常规Dropout不同，DropToken直接丢弃整个Token而非单个元素。由于Transformer自注意力机制的特性，剩余Token保留原始位置信息。在实现上等同于在Attention矩阵中将被mask Token的对应列置零。

## Effectiveness

在CLUE分类任务上的实验（BERT base）：
- **IFLYTEK**：最受益任务，drop比例0.5时达61.45%（基线60.06%）
- **TNEWS/AFQMC**：轻微提升或持平
- **WSC/CSL**：高drop比例时下降明显
- 最优drop比例：0.1~0.15

## Relationship to MAE

MAE可等价视为一种特殊的Attention Dropout：随机mask掉Attention矩阵的列。从Dropout视角看，MAE的"取消Dropout"（微调阶段）与原始模型一致，说明MAE具有更好的预训练-微调一致性。

## References

- 苏剑林. "Dropout视角下的MLM和MAE：一些新的启发". 科学空间, 2021. [spaces-8770]
- He et al., "Masked Autoencoders Are Scalable Vision Learners", CVPR 2022.
