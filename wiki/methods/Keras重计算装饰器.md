---
type: method
title: "Keras重计算装饰器（Gradient Checkpointing）"
aliases:
  - recompute_grad
  - "Keras Gradient Checkpointing"
  - "重计算装饰器"
tags: [memory-optimization, gradient-checkpointing, keras]
operation_types:
  primary: "Estimate / sample instead of compute"
  secondary:
    - "Decompose / reduce dimension"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-29-节省显存的重计算技巧也有了Keras版了.md
source_ids:
  - "7367"
status: draft
updated: 2026-06-14
method_summary: "在Keras中通过@recompute_grad装饰器实现梯度检查点（重计算），以时间换空间减少显存占用，可增大batch_size 3-4倍。"
typical_structure: "使用@recompute_grad装饰自定义层的call函数；前向传播不保存中间激活，反向时从检查点重计算；插入的装饰器越多，显存节省越多。"
applicability: "显存受限的深度学习训练场景，特别是大型模型如BERT的训练。"
tools:
  - keras_recompute
  - tf.recompute_grad
  - bert4keras
related_concepts:
  - [[Gradient-Checkpointing-重计算]]
related_methods: []
examples:
  - [[article::7367]]
---

## 适用问题

深度学习训练中，显存占用主要来自前向传播时保存的中间激活值（activations）。模型越深、batch_size越大，中间激活越占显存。当GPU显存成为瓶颈时，只能被迫减小batch_size，导致训练效率下降、BatchNorm统计不稳定。

重计算（Gradient Checkpointing）以时间换空间：不在前向传播时保存所有中间激活，而是在反向传播时从最近的"检查点"重新计算，从而大幅降低显存占用。

## 核心变换

标准训练流程：

```
前向:  输入 → 层1保存激活 → 层2保存激活 → ... → 输出
反向:  输出 → 层2(用保存的激活) → 层1(用保存的激活) → 梯度
```

重计算流程：

```
前向:  输入 → 层1(不保存) → 层2(不保存) → ... → 检查点保存
反向:  输出 → 层2(从检查点重计算输入) → 层1(从检查点重计算输入) → 梯度
```

Keras中的使用方式——`@recompute_grad` 装饰器：

```python
from recompute import recompute_grad

# 对自定义层装饰
class MyLayer(Layer):
    @recompute_grad
    def call(self, inputs):
        return inputs * 2

# 对已有层通过继承装饰
class MyDense(Dense):
    @recompute_grad
    def call(self, inputs):
        return super().call(inputs)
```

启用时通过环境变量控制：`RECOMPUTE=1 python train.py`。插入的 `@recompute_grad` 越多，检查点越密集，显存节省越大，但重计算的计算开销也越大。

| 模型 | batch_size增幅 | 每样本时间增加 |
|-----|---------------|--------------|
| BERT Base | 3x | ~25% |
| BERT Large | 4x | ~25% |

## 典型步骤

1. 确定需要重计算的关键层（通常是参数量大、中间激活多的层）
2. 在自定义层的 `call` 方法上添加 `@recompute_grad` 装饰器
3. 对现有Keras层，通过继承创建新类并装饰其 `call` 方法
4. 在代码中替换原始层为装饰后的层
5. 运行前设置环境变量 `RECOMPUTE=1` 启用重计算
6. （可选）在更多层上添加装饰器以进一步节省显存

## 直觉

深度学习训练中显存的消耗大户是中间激活（每层输入输出张量）。标准做法是"保存所有，反向时读取"——空间换时间。重计算的做法是"几乎不保存，反向时重算"——时间换空间。

关键在于选择检查点位置：检查点越少，显存越省但重计算开销越大；检查点越多，越接近标准训练的速度但显存节省减少。实际使用中，在每个大块（如BERT的每个Transformer层）都设置检查点，可以达到显存和速度的良好平衡。

## 边界

- 时间开销：每样本训练时间增加约25%，对于超大模型可能是显著成本
- 仅在 `tf.recompute_grad` 支持的后端上可用（tensorflow 1.8+/2.x）
- tensorflow 2.x自带的 `tf.keras` 不支持此功能，需使用 `keras 2.3.1` + `tensorflow 2.x` 组合
- 不是插入的装饰器越多越好——需要选择关键层（参数量大、深度大的层）
- 对于小模型，重计算带来的速度损失可能超过显存收益

## 例子

- BERT Base训练：batch_size从48增大到144（3x），每个样本时间增加25%
- BERT Large训练：batch_size增大4倍
- bert4keras框架内置支持：设置 `RECOMPUTE=1` 环境变量即可启用
- 长序列Transformer训练：序列长度越长，中间激活越多，重计算收益越大

## 证据

- ev::7367::@recompute_grad装饰器的使用方式：装饰自定义层的call方法
- ev::7367::对已有层的包装方法：继承装饰 class MyDense(Dense): @recompute_grad def call(self, inputs)
- ev::7367::BERT Base batch_size增大3倍，BERT Large增大4倍，每样本时间增加约25%
- ev::7367::环境变量 RECOMPUTE=1 控制启用，插入装饰器越多显存节省越多
- ev::7367::不支持的组合：tensorflow 2.x + 自带tf.keras，推荐 keras 2.3.1 + tf 1.x/2.x
