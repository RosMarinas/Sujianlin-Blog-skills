---
title: Keras自定义Loss模式
type: concept
aliases: [Keras Custom Loss, Keras loss as output, Keras triplet loss pattern]
tags: [keras, loss-function, deep-learning, engineering]
related_methods: [Keras自定义Loss作为输出, Label Smoothing, Center Loss]
related_sources: [spaces-4493-Keras中自定义复杂的loss函数]
sources: [4493]
source_ids: ["4493"]
status: draft
updated: 2026-06-13
definition: "Keras中将损失函数定义为模型输出层的通用设计模式，通过Lambda层或自定义层实现复杂损失函数。"
---

## Definition

Keras中自定义复杂loss的核心模式：将损失函数定义为模型的输出层（而非在compile中指定），通过Lambda层或自定义层实现。训练时以模型输出作为loss值，即`loss=lambda y_true,y_pred: y_pred`。这种模式突破了Keras常规的单输入单输出loss限制。

## 三种核心模式

### 模式一：自定义loss函数
最简单的形式，定义接收`(y_true, y_pred)`的函数传入`model.compile(loss=my_loss)`。

### 模式二：Loss作为模型输出（通用模式）
将loss写成一个层作为最后输出，适用于多输入、度量学习等复杂场景。目标值作为输入传入模型。

### 模式三：多输出loss
使用多个输出头，每个头单独设置loss函数和权重，保留metrics显示。

## 应用场景
- Triplet Loss（问答匹配）
- Center Loss（人脸识别特征聚类）
- 带正则项的自定义损失
- 多任务学习
