---
type: method
title: "GLU激活函数"
aliases:
  - "Gated Linear Unit"
  - "门控线性单元"
tags: [activation-function, gating, deep-learning]
operation_types:
  primary: "Discrete ↔ continuous bridge"
  secondary:
    - "Structure-expose by factorization"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-10-13-基于fine-tune的图像分类-百度分狗竞赛.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-10-26-浅谈神经网络中激活函数的设计.md
source_ids:
  - "4611"
  - "4647"
status: draft
updated: 2026-06-14
method_summary: "门控线性单元通过sigmoid门控制信息流动，使网络能够选择性地传递特征。"
typical_structure: "两组独立参数分别做线性变换和sigmoid门控，逐元素相乘得到输出。"
applicability: "需要自适应门控机制的深度网络，可替代ReLU改善信息流动。"
tools:
  - Dense层
  - sigmoid激活函数
related_concepts:
  - [[GLU激活函数]]
  - [[Swish激活函数]]
related_methods: []
examples:
  - [[article::4611]]
  - [[article::4647]]
---

## 适用问题

标准激活函数（ReLU、sigmoid、tanh）对所有输入元素应用相同的非线性变换，缺乏根据输入内容动态调整信息流的能力。在需要网络自主决定"哪些信息应该通过、哪些应该抑制"的场景中，固定的非线性变换不够灵活。

GLU（Gated Linear Unit）通过引入一个独立的门控分支来解决这个问题——让网络同时学习变换和门控策略，实现数据的自适应筛选。

## 核心变换

GLU的数学定义为：

$$
\text{GLU}(\boldsymbol{x}) = (\boldsymbol{W}_1\boldsymbol{x} + \boldsymbol{b}_1) \otimes \sigma(\boldsymbol{W}_2\boldsymbol{x} + \boldsymbol{b}_2)
$$

其中两组参数完全独立：第一组做线性变换产生"内容"（$dense$），第二组经过sigmoid激活产生0到1之间的"门"（$gate$），两者逐元素相乘得到最终输出。

在Keras中的直接实现：

```python
dense = Dense(feature_size)(base_model.output)
gate = Dense(feature_size, activation='sigmoid')(base_model.output)
feature = multiply([dense, gate])
```

当gate接近1时，对应维度的信息几乎无衰减通过；当gate接近0时，对应维度的信息被完全阻断。门控值由网络自动学习，输入相关的动态决策。

**与Swish的关系**：Swish $x \cdot \sigma(x)$ 是GLU在两组参数共享时的特例。GLU用两组独立参数，Swish用同一组参数既做变换又做门控。

## 典型步骤

1. 对输入 $\boldsymbol{x}$ 并行做两个独立的线性变换（Dense层）
2. 其中一路直接输出作为内容分支
3. 另一路经过sigmoid激活输出0-1门控值
4. 使用逐元素乘法合并两路输出
5. 可将GLU作为特征压缩模块插入任何网络层之间

## 直觉

GLU将"特征提取"和"特征筛选"分离到两个独立的分支中学习。内容分支负责提取有意义的特征表示，门控分支负责学习每个特征维度在当前输入下的重要性权重。

这种解耦使得网络可以显式地学习"什么时候该听什么"——对于不相关或噪声的特征维度，门控分支可以学会将其置零。相比ReLU的硬截断（负值为0），GLU的门控是软性的、数据驱动的、可微分的。

## 边界

- 参数量翻倍：每个GLU需要两组独立的权重矩阵，参数量是普通Dense层的2倍
- 训练初期门控值不稳定：sigmoid输出在0附近时梯度饱和，需要合理的初始化或配合BatchNorm使用
- GLU更适用于特征压缩/筛选场景，在需要保留全部信息的浅层网络中不一定优于ReLU
- Swish与GLU效果相似但参数减半，当计算资源紧张时可优先尝试Swish

## 例子

- 百度分狗竞赛：在Xception池化层后使用GLU将特征从2048维压缩到64维，同时实现特征筛选
- 语言建模：GLU在多种NLP任务中表现优于ReLU和LSTM门控机制
- 特征金字塔：在多层特征融合时使用GLU控制各层的贡献权重

## 证据

- ev::4611::GLU与Xception结合：池化层后接Dense+Gate双分支，multiply合并，feature_size=64
- ev::4611::GLU输出作为softmax和center loss的共享特征输入，验证实际有效性
- ev::4647::GLU与Swish的关系：Swish是GLU在两组参数共享时的特例，GLU参数量翻倍
- ev::4647::激活函数设计原则：GLU通过sigmoid门实现软性的信息流控制
