---
title: 增量爆炸 (Incremental Explosion)
definition: 增量爆炸（Incremental Explosion）是指在深层神经网络中，参数微小变化导致损失函数大幅变化的现象。对于 $N$ 层模型，SGD更新量
  $\Delta\mathcal{L} \approx -\eta\|\nabla\theta\mathcal{L}(\theta)\|^2 = \mathcal{O}(\eta
  NK)$，即与层数 $N$ 成正比。
type: concept
aliases:
- 增量爆炸
- 参数更新爆炸
- loss spike
tags:
- deep-learning
- training-stability
- optimization
- initialization
related_methods:
- 残差连接
- Warmup
related_sources:
- spaces-8994-为什么需要残差
status: draft
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## Definition

增量爆炸（Incremental Explosion）是指在深层神经网络中，参数微小变化导致损失函数大幅变化的现象。对于 $N$ 层模型，SGD更新量 $\Delta\mathcal{L} \approx -\eta\|\nabla_\theta\mathcal{L}(\theta)\|^2 = \mathcal{O}(\eta NK)$，即与层数 $N$ 成正比。

## Cause

即使通过Xavier初始化等方法解决了梯度消失/爆炸，使得每层参数梯度为 $\mathcal{O}(1)$ 量级，累积效应仍导致 $\Delta\mathcal{L} \propto N$。这使模型在初始阶段容易进入不良局部最优点，导致训练停滞或崩溃。

## Solutions

### 1. Warmup (治标)
初始阶段使用极小学习率，待模型平稳渡过"危险期"后恢复正常学习率。但Warmup不解决模型landscape不平滑的根本问题。

### 2. Residual Connection (治本)
残差结构 $\boldsymbol{y} = \boldsymbol{x} + \varepsilon\boldsymbol{f}(\boldsymbol{x};\boldsymbol{\theta})$ 通过 $\varepsilon$ 控制参数梯度大小。令 $\varepsilon = 1/\sqrt{N}$ 可使梯度缩放至 $\mathcal{O}(1/\sqrt{N})$，抵消深度 $N$ 的影响。

### 3. DeepNet-Style Initialization
增大恒等路径权重、降低残差分支初始化方差，从模型设计层面消除增量爆炸。

## Key Formula

残差结构的反向传播：
$$
\frac{\partial\mathcal{L}}{\partial\boldsymbol{\theta}} = \varepsilon\frac{\partial\mathcal{L}}{\partial\boldsymbol{y}}\frac{\partial\boldsymbol{f}}{\partial\boldsymbol{\theta}}
$$

通过 $\varepsilon$ 的缩放实现梯度与层数的解耦。

## References

- 苏剑林. "为什么需要残差？一个来自DeepNet的视角". 科学空间, 2022. [spaces-8994]
- DeepNet: Scaling Transformers to 1,000 Layers, Microsoft, 2022.