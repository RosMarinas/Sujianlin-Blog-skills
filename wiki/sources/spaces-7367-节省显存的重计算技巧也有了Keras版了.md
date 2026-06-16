---
title: 节省显存的重计算技巧也有了Keras版了
source_id: 7367
type: source
url: https://spaces.ac.cn/archives/7367
author: 苏剑林
date: 2020-04-29
category: 信息时代
tags: [gradient-checkpointing, memory-optimization, keras, bert, recompute]
license: CC BY-NC-SA
abstract: 实现Keras版的重计算（Gradient Checkpointing）技巧，通过@recompute_grad装饰器标记自定义层的call函数，用时间换空间减少显存占用。理论上层数越多节省越多，实际测试BERT Base下batch_size增大3倍，Large版增大4倍，每样本训练时间增加约25%。已内置到bert4keras中。
key_contributions:
  - Keras版recompute_grad装饰器实现
  - 基于tf.recompute_grad的梯度检查点
  - BERT重计算显存优化效果量化（Base 3x, Large 4x）
  - 环境兼容性测试（tensorflow 1.x/2.x + keras 2.3.1）
  - bert4keras内置重计算支持
---
