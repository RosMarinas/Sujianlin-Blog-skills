---
title: Keras层重用与模型重用
type: concept
aliases: [Keras Layer Reuse, Keras Model Reuse, Keras权重共享]
tags: [keras, weight-sharing, model-reuse, deep-learning]
related_methods: [Keras层重用技巧, Keras模型中间层拆解]
related_sources: [spaces-6985-让Keras更酷一些层与模型的重用技巧]
sources: [6985]
source_ids: ["6985"]
status: draft
updated: 2026-06-13
definition: "Keras中层和模型的重用机制，通过先初始化后多次调用实现权重共享，通过覆盖内部属性实现模型拆解和重组。"
---

## Definition

Keras中层和模型的重用机制支持权重共享和结构复用。初始化后存为变量反复调用实现权重共享；通过Model继承Layer让模型可当层调用；通过覆盖model.inputs实现模型从中间拆解。

## 关键机制

- **层重用**：先初始化再调用（共享权重）vs 多次初始化（独立权重）
- **模型重用**：Model继承Layer，模型可像层一样调用
- **模型克隆**：clone_model复制结构，set_weights复制权重
- **模型拆解**：通过覆盖model.inputs和model._input_layers欺骗run_internal_graph实现从中间层重建

## 交叉引用
通过自定义Layer引用已有层的权重（如Bert中Embedding与全连接权重共享）。
