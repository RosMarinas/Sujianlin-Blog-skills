---
title: 标签平滑 (Label Smoothing)
type: concept
aliases: [标签平滑, Label Smoothing, 标签平滑正则化]
tags: [regularization, classification, loss-function, softmax]
related_methods: [Label Smoothing with KL]
related_sources: [spaces-4493-Keras中自定义复杂的loss函数]
sources: [4493]
source_ids: ["4493"]
status: draft
updated: 2026-06-13
definition: "标签平滑是一种防止分类模型过于自信的正则化技术，通过在目标分布中混入均匀分布来缓解softmax过于自信的问题。"
---

## Definition

标签平滑是一种防止分类模型过于自信的正则化技术。标准交叉熵拟合one-hot分布会鼓励模型增大输出向量模长来降低loss，标签平滑通过在目标分布中混入均匀分布来缓解这一问题。

## 数学形式

标准交叉熵: $loss = -\log(e^{z_1}/Z)$

标签平滑交叉熵: $loss = -(1-\varepsilon)\log(e^{z_1}/Z) - \varepsilon\sum_{i=1}^n \frac{1}{n}\log(e^{z_i}/Z)$

## 效果
- 缓解softmax过于自信的问题
- 提高测试准确率（防止过拟合）
- 增加模型对噪声输入的鲁棒性
