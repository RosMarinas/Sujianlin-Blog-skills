---
type: concept
title: MAE
definition: "一种视觉自监督预训练方法，通过随机掩码大部分图像块并仅用剩余块重构完整图像。"
sources:
  - wiki/sources/spaces-8770-Dropout视角MLM-MAE.md
source_ids:
  - "8770"
aliases: [MAE, 掩码自编码器, Masked Autoencoder]
tags: [pre-training, self-supervised, vision, autoencoder]
related_concepts: [Dropout, MLM, DropToken]
related_sources: [spaces-8770-Dropout视角下的MLM和MAE]
status: draft
updated: 2026-06-12
---
## Definition

MAE（Masked Autoencoder, He et al., 2021）是一种视觉自监督预训练方法：随机mask 75%的图像patches，仅用可见patches通过encoder生成潜在表示，再用轻量decoder重建原始图像。

## Dropout Perspective

MAE可等价为一种特殊的Attention Dropout：
- 将被mask token对应列在Attention矩阵中置零
- 各个Attention层共用同一组mask模式
- 75%的高mask比例使encoder序列长度缩短为1/4，训练速度提升3倍+

## Consistency Advantage

相比MLM，MAE的"取消Dropout"（微调阶段）与原始模型一致。数学推导证明，MAE的Attention Dropout在取消后恢复为标准Attention，因此预训练-微调一致性更好。

## Applications as Regularization

MAE的drop token做法可推广为DropToken正则化方法：在训练阶段随机丢弃部分token以提高训练速度和泛化能力。

## References

- 苏剑林. "Dropout视角下的MLM和MAE：一些新的启发". 科学空间, 2021. [spaces-8770]
- He et al., "Masked Autoencoders Are Scalable Vision Learners", CVPR 2022.
