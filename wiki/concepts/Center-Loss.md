---
title: Center Loss
type: concept
aliases: [中心损失]
tags: [loss-function, face-recognition, metric-learning, feature-clustering]
related_methods: [Center Loss with Embedding]
related_sources: [spaces-4493-Keras中自定义复杂的loss函数, spaces-4611-基于fine-tune的图像分类]
sources: [4493, 4611]
source_ids: ["4493", "4611"]
status: draft
updated: 2026-06-13
definition: "Center Loss是在分类任务中对特征施加聚类约束的损失函数，通过可训练的类中心向量使同类特征具有内聚性。"
---

## Definition

Center Loss是在分类任务中对特征施加聚类约束的损失函数。在每个类定义可训练的中心向量，要求提取的特征与对应的类中心靠近，从而使得同一类的特征具有内聚性。

## 数学形式

$loss = -\log\frac{e^{\boldsymbol{W}_y^{\top}\boldsymbol{x}+b_y}}{\sum_i e^{\boldsymbol{W}_i^{\top}\boldsymbol{x}+b_i}} + \lambda \|\boldsymbol{x} - \boldsymbol{c}_y\|^2$

- 第一项：标准softmax交叉熵（拉开类间距离）
- 第二项：L2距离惩罚项（缩小类内距离）
- $\boldsymbol{c}_y$：第$y$类的可训练中心向量

## Keras实现技巧
使用Embedding层存储聚类中心，因为Embedding本质上就是一个可训练的查找矩阵。
