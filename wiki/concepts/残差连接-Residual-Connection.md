---
type: concept
title: 残差连接 (Residual Connection)
definition: "一种神经网络的短路连接设计，使得某层的输出为输入与残差分支映射之和，借此稳定深层网络的数值范围和梯度流。"
sources:
  - wiki/sources/spaces-8994-为什么需要残差.md
source_ids:
  - "8994"
aliases: [ResNet, Skip Connection, 跳跃连接, 恒等映射]
tags: [architecture, deep-learning, resnet, training-stability]
related_methods: [DeepNet, 增量爆炸]
related_sources: [spaces-8994-为什么需要残差]
status: draft
updated: 2026-06-12
---
## Definition

残差连接（Residual Connection）是一种神经网络结构设计，通过将层的输入直接加到输出上形成跳跃连接，即 $\boldsymbol{y} = \boldsymbol{x} + \varepsilon \boldsymbol{f}(\boldsymbol{x};\boldsymbol{\theta})$。这种设计允许梯度直接流经恒等路径，缓解深层网络中的梯度消失/爆炸和增量爆炸问题。

## Key Insights from DeepNet Perspective

从DeepNet的视角（[spaces-8994]），残差连接的核心优势在于：

1. **同时稳定前向和反向传播**：当 $\varepsilon$ 足够小时，$\partial \boldsymbol{y}/\partial \boldsymbol{x} = \boldsymbol{I} + \varepsilon \cdot \partial \boldsymbol{f}/\partial \boldsymbol{x}$ 接近单位矩阵，梯度传播稳定。

2. **解决增量爆炸**：残差结构允许通过 $\varepsilon$ 控制参数梯度大小。要使梯度缩放至 $\mathcal{O}(1/\sqrt{N})$（$N$ 为层数），令 $\varepsilon = 1/\sqrt{N}$ 即可。这是因为高维情形下每层的膨胀系数约为 $1+\varepsilon^2$，故 $\varepsilon^2 = \mathcal{O}(1/N)$ 足够。

3. **深层前馈神经网络的固有缺陷**：无残差的普通前馈网络，即使通过Xavier初始化稳定了前向传播，也无法使梯度随层数变化，因此无法解决增量爆炸问题。

## Mathematical Formulation

对于SGD更新 $\Delta\boldsymbol{\theta} = -\eta \nabla_{\boldsymbol{\theta}}\mathcal{L}(\boldsymbol{\theta})$，损失变化为 $\Delta\mathcal{L} \approx -\eta\|\nabla_{\boldsymbol{\theta}}\mathcal{L}(\boldsymbol{\theta})\|^2$。对于 $N$ 层模型，每层参数梯度为 $\mathcal{O}(1)$ 时，$\Delta\mathcal{L} = \mathcal{O}(\eta NK)$，即更新量正比于深度 $N$。残差结构通过 $\varepsilon$ 缩放梯度从根本上解决了这一缩放问题。

## Relationship to DeepNet

DeepNet（微软，2022）通过增大恒等路径权重和降低残差分支初始化，成功训练了1000层Transformer。其核心思想正是利用残差连接的梯度缩放能力。

## References

- 苏剑林. "为什么需要残差？一个来自DeepNet的视角". 科学空间, 2022. [spaces-8994]
- DeepNet: Scaling Transformers to 1,000 Layers, Microsoft, 2022.
