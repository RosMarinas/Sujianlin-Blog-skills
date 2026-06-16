---
type: method
title: "Label Smoothing（标签平滑）的KL实现"
aliases:
  - "Label Smoothing with KL"
  - "标签平滑正则化"
tags: [regularization, classification, loss-function]
operation_types:
  primary: "Align / calibrate by invariance"
  secondary:
    - "Estimate / sample instead of compute"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-07-22-Keras中自定义复杂的loss函数.md
source_ids:
  - "4493"
status: draft
updated: 2026-06-14
method_summary: "在交叉熵中混入均匀分布来缓解softmax过于自信的标签平滑正则化方法。"
typical_structure: "计算预测与真实分布的交叉熵 + 计算预测与均匀分布的交叉熵，加权求和。"
applicability: "需要防止分类模型过度自信的场景，可提高泛化能力。"
tools:
  - Keras backend (K.categorical_crossentropy)
related_concepts:
  - [[Label Smoothing]]
  - [[交叉熵准确率优化分析]]
related_methods:
  - [[Center-Loss-with-Embedding]]
examples:
  - [[article::4493]]
---

## 适用问题

标准softmax交叉熵训练存在"过于自信"的问题：模型倾向于为正确类别输出接近1的概率，即使输入包含噪声。这是因为增大正确类别logit的模长可以无上限地降低交叉熵——模型不需要学习有意义的特征，只需盲目放大logits即可。

这种过度自信导致过拟合风险增加，模型在校验集上的泛化能力下降，并且在实际应用中无法提供有意义的置信度估计。

## 核心变换

将训练目标从"拟合one-hot分布"改为"拟合one-hot分布与均匀分布的混合"：

$$
\text{loss} = -(1-\varepsilon)\log\frac{e^{z_y}}{Z} - \varepsilon\sum_{i=1}^n\frac{1}{n}\log\frac{e^{z_i}}{Z}
$$

其中 $Z = \sum_j e^{z_j}$，$\varepsilon$ 是平滑系数（通常取0.1）。

第一项是标准交叉熵，迫使模型关注正确类别；第二项是预测分布与均匀分布的交叉熵，惩罚模型输出过于尖锐的分布。

这种组合使得"单纯增大正确类别的logit模长"不再是最优解——模型必须在正确分类和保持概率分布平滑之间取得平衡。

Keras中的直接实现：

```python
def mycrossentropy(y_true, y_pred, e=0.1):
    nb_classes = K.int_shape(y_pred)[-1]
    loss1 = K.categorical_crossentropy(y_true, y_pred)           # 标准交叉熵
    loss2 = K.categorical_crossentropy(K.ones_like(y_pred) / nb_classes, y_pred)  # 均匀分布交叉熵
    return (1 - e) * loss1 + e * loss2

model.compile(optimizer='adam', loss=mycrossentropy)
```

## 典型步骤

1. 确定平滑系数 $\varepsilon$（通常0.1，可通过验证集调节）
2. 在自定义loss函数中构造均匀分布：`K.ones_like(y_pred) / nb_classes`
3. 计算预测与one-hot目标的交叉熵 `loss1`
4. 计算预测与均匀分布的交叉熵 `loss2`
5. 加权求和：`(1-ε) * loss1 + ε * loss2`
6. 将自定义loss传入 `model.compile(loss=mycrossentropy)`

## 直觉

标准交叉熵中，模型可以通过不断放大正确类别的logit来降低loss，这个过程没有上限——这是"过于自信"的根源。标签平滑通过引入均匀分布惩罚，给模型增加了一个"约束"：你可以在正确类别上获得高概率，但不能完全忽略其他类别。

从KL散度的角度看，标签平滑等价于让模型同时逼近两个分布：一个是训练数据的one-hot标签分布（主任务），一个是均匀分布（正则项）。均匀分布的引入充当了"软性最大熵正则化"——防止模型输出过于确定的分布。

## 边界

- $\varepsilon$ 并非越大越好：过大的平滑系数会模糊类别间的边界，降低分类准确率（典型取值范围0.05-0.2）
- 标签平滑适用于分类任务，不适用于回归任务
- 对于已经严重欠拟合的数据，标签平滑可能进一步降低模型容量
- 平滑效果等价于在logits上施加L2正则化（Hinton et al., 2015），但实现更简单
- 对于类别数极少（如二分类）的场景，均匀分布的惩罚效果有限

## 例子

- 文本分类：`epsilon=0.1` 的标签平滑可提升1-2%的测试准确率
- 图像分类：Inception v3等模型训练中默认使用标签平滑（epsilon=0.1）
- 机器翻译：Transformer训练中广泛使用标签平滑提升BLEU值

## 证据

- ev::4493::标签平滑核心公式：$(1-\varepsilon)\log(e^{z_y}/Z) + \varepsilon\sum(1/n)\log(e^{z_i}/Z)$
- ev::4493::盲目增大logit模长不再最优：平滑项约束了输出分布的锐利程度
- ev::4493::Keras实现：自定义`mycrossentropy`函数，`K.ones_like(y_pred)/nb_classes`构造均匀分布
- ev::4493::缓解softmax过于自信，在分类和NLP任务中均可提升泛化能力
