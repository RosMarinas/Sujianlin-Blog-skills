---
title: TensorFlow分布式策略（tf.distribute）
type: concept
aliases: [分布式策略, MirroredStrategy, TPUStrategy, 多GPU训练, tf.distribute]
tags: [tensorflow, distributed-training, multi-gpu, tpu, tf-keras]
related_methods: [Keras多GPU训练, Keras TPU训练]
related_sources: [spaces-7055-Keras-Tensorflow的黄金标准]
sources: [7055]
source_ids: ["7055"]
status: draft
updated: 2026-06-13
definition: "TensorFlow从1.14+开始通过tf.distribute模块提供分布式训练策略，只要Keras代码遵循标准规范即可扩展到多GPU或TPU。"
---

## Definition

TensorFlow从1.14+开始通过tf.distribute模块提供分布式训练策略。只要Keras代码遵循标准规范，通过几行代码即可将单卡模型扩展到多GPU或TPU训练。

## 主要策略

- **MirroredStrategy**：单机多卡同步训练
- **TPUStrategy**：TPU训练
- **MultiWorkerMirroredStrategy**：多机多卡训练

## Keras标准原则

1. 尽可能用Keras内置层/loss/优化器
2. 自定义层必须实现get_config方法（可通过clone_model测试）
3. 避免在模型最后用add_loss/add_metric定义loss
4. 避免动态操作（TPU要求静态图）
