---
type: topic
title: Keras工程技巧
aliases: [Keras Engineering, Keras实战技巧]
tags: [keras, engineering, deep-learning, tf-keras]
sources:
  - source_id: "4493"
  - source_id: "6985"
  - source_id: "7055"
  - source_id: "7367"
  - source_id: "6736"
related_concepts:
  - Keras自定义Loss模式
  - Keras层重用与模型重用
  - Gradient-Checkpointing-重计算
  - tf-distribute-多GPU训练
  - Label-Smoothing-标签平滑
  - Center-Loss
related_methods:
  - Keras自定义Loss作为输出
  - Keras层重用技巧
  - Keras重计算装饰器
  - Keras多GPU训练
  - Label-Smoothing-with-KL
  - Center-Loss-with-Embedding
---

# Keras工程技巧

## 概述

Keras（及tf.keras）作为TensorFlow的官方高级API，提供了优雅的模型构建和训练接口。本主题汇总了Keras工程实践中的关键技巧，涵盖自定义损失函数、层与模型重用、多GPU/TPU分布式训练、显存优化等方面。

## 核心技巧

### 1. 自定义复杂Loss
Keras支持三种自定义loss模式：直接函数、loss作为模型输出（通用模式）、多输出loss。其中"loss作为输出"模式最为灵活，适用于Triplet Loss、Center Loss等复杂场景。

### 2. 层与模型重用
通过先初始化后多次调用实现权重共享；利用Model继承Layer的特性实现模型嵌套调用；通过覆盖内部属性实现模型的中间拆解和重组。

### 3. 分布式训练
tf.keras配合tf.distribute模块，通过简单的几行配置即可实现多GPU和TPU训练。关键前提：使用Keras标准写法。

### 4. 显存优化
重计算（Gradient Checkpointing）将前向传播的中间激活值丢弃，反向传播时重新计算，可增大batch_size 3-4倍，仅增加25%训练时间。
