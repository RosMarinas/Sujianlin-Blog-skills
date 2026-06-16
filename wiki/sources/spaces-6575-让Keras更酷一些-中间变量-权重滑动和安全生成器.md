---
type: article_summary
title: “让Keras更酷一些！”：中间变量、权重滑动和安全生成器
article_id: "6575"
source_url: https://spaces.ac.cn/archives/6575
date: 2019-04-28
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-04-28-让Keras更酷一些-中间变量-权重滑动和安全生成器.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-04-28-让Keras更酷一些-中间变量-权重滑动和安全生成器.md
source_ids:
  - "6575"
status: draft
updated: 2026-06-11
---

# “让Keras更酷一些！”：中间变量、权重滑动和安全生成器

本文介绍了在 Keras 中提取任意中间变量、实现权重滑动平均（EMA）以及编写进程安全的 Sequence 数据生成器的实用方法。

## 主要内容

1. **输出中间变量**：
   - **子模型构建**：传统方法，限制在于输出必须是某个层的直接输出。
   - **`K.function` 底层接口**：终极方案。可以通过 `K.function([inputs], [tensors])` 编译出一个后端执行函数，其中 `tensors` 可以是计算图中的任何中间张量（哪怕是自定义层内部的非输出张量，如 Attention 权重矩阵）。执行时，直接向返回的函数传入数据即可得到结果，相当于在后端会话中执行 `sess.run(tensors, feed_dict)`。

2. **权重滑动平均（Exponential Moving Average, EMA）**：
   - **基本原理**：EMA 在不改变原有优化器优化轨迹的前提下，维护一组对权重进行指数衰减平均的变量 $\boldsymbol{\Theta}_{n+1} = \alpha \boldsymbol{\Theta}_n + (1-\alpha) \boldsymbol{\theta}_{n+1}$，以此作为最终评估模型权重。
   - **Keras 巧妙注入**：利用 `K.moving_average_update` 构建滑动平均算子，并直接将其追加到 `model.metrics_updates` 中。Keras 在每步训练时会自动执行 `metrics_updates` 中的算子，从而在不修改优化器的情况下完成了 EMA。在评估前调用 `apply_ema_weights` 应用权重，在继续训练前调用 `reset_old_weights` 恢复。

3. **进程安全生成器**：
   - **多进程冲突**：直接使用 Python 的 `yield` 编写生成器，在启用多进程读取（如 `use_multiprocessing=True`）或生成器内部依赖多进程服务（如 `bert-as-service`）时容易死锁或卡住。
   - **`keras.utils.Sequence`**：通过继承该类并实现 `__len__` 和 `__getitem__(self, idx)`，可以保证在多进程环境下每个 epoch 的每个样本仅被训练一次，从而解决死锁和数据重复问题。
