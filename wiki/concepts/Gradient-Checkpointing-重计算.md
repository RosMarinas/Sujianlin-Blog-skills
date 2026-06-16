---
title: Gradient Checkpointing（重计算）
type: concept
aliases: [重计算, Gradient Checkpointing, 梯度检查点, recompute]
tags: [memory-optimization, training, deep-learning, bert]
related_methods: [Keras重计算装饰器]
related_sources: [spaces-7367-节省显存的重计算技巧也有了Keras版了]
sources: [7367]
source_ids: ["7367"]
status: draft
updated: 2026-06-13
definition: "梯度检查点（Gradient Checkpointing）是一种以时间换空间的显存优化技术，在前向传播时不保存中间激活值，反向传播时重新计算。"
---

## Definition

梯度检查点（Gradient Checkpointing / 重计算）是一种以时间换空间的显存优化技术。在前向传播时不保存中间激活值（只保存检查点的激活值），反向传播时重新计算被丢弃的中间激活值，从而减少显存占用。

## 工作原理

- 前向传播：只保存少量"检查点"的激活值
- 反向传播：从最近的检查点重新计算中间激活值来计算梯度
- 时间开销：需要额外的重计算，约增加25%训练时间
- 空间收益：层数越多收益越大，BERT Base batch_size增大3倍

## Keras实现
通过`@recompute_grad`装饰器标记自定义层的`call`函数，基于`tf.recompute_grad`实现。
