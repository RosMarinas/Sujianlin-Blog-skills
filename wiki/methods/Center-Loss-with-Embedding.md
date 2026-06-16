---
type: method
title: "Center Loss（基于Embedding层）"
aliases:
  - "Center Loss with Keras"
  - "Embedding Center Loss"
tags: [metric-learning, face-recognition, feature-clustering, keras]
operation_types:
  primary: "Align / calibrate by invariance"
  secondary:
    - "Construct auxiliary sequence"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-07-22-Keras中自定义复杂的loss函数.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-10-13-基于fine-tune的图像分类-百度分狗竞赛.md
source_ids:
  - "4493"
  - "4611"
status: draft
updated: 2026-06-14
method_summary: "利用Embedding层的矩阵查找特性存储可训练的聚类中心，在softmax交叉熵基础上附加L2距离惩罚项，实现类内紧凑的特征表示。"
typical_structure: "Embedding层存储聚类中心；根据输入类别索引查找中心向量；计算特征与中心的L2距离作为附加loss。"
applicability: "人脸识别、细粒度分类等需要特征聚类的度量学习场景。"
tools:
  - Keras Functional API
  - Embedding层
related_concepts:
  - [[Center Loss]]
  - [[Keras自定义Loss模式]]
related_methods:
  - [[Keras自定义Loss作为输出]]
examples:
  - [[article::4493]]
  - [[article::4611]]
---

## 适用问题

标准softmax交叉熵训练得到的特征向量不具备聚类特性——同一类的特征可能散布在整个特征空间，无法直接用于度量学习场景（如人脸验证、细粒度检索）。当训练完成后希望用提取的特征做KNN匹配时，类内方差过大会导致检索准确率严重下降。

Center Loss解决的是"如何在分类训练的同时，强制同一类的特征向量相互靠拢"的问题，使特征空间具有类内紧凑、类间分离的良好结构。

## 核心变换

在标准softmax交叉熵基础上增加一个类中心L2距离惩罚项：

$$
\mathcal{L} = \mathcal{L}_{softmax} + \lambda \| \boldsymbol{x} - \boldsymbol{c}_y \|^2
$$

其中 $\boldsymbol{x}$ 是softmax前一层的特征向量，$\boldsymbol{c}_y$ 是第 $y$ 类的可训练中心向量，$\lambda$ 控制惩罚强度。

**关键设计**：利用Keras的Embedding层存储所有类中心向量。Embedding层本质上是一个可训练的查找矩阵——输入类别索引直接输出对应的中心向量，无需额外参数管理。

在Keras中的实现模式：

```python
input_target = Input(shape=(1,))
centers = Embedding(nb_classes, feature_size)(input_target)
l2_loss = Lambda(lambda x: K.sum(K.square(x[0]-x[1][:,0]), 1, keepdims=True),
                 name='l2_loss')([feature, centers])

model_train = Model(inputs=[input_image, input_target],
                    outputs=[predict, l2_loss])
model_train.compile(optimizer='adam',
                    loss=['sparse_categorical_crossentropy',
                          lambda y_true, y_pred: y_pred],
                    loss_weights=[1., 0.2])
```

第二项loss使用 `lambda y_true, y_pred: y_pred` 技巧——模型的输出本身就是loss值，训练时y_true传入任意匹配形状的数组。

## 典型步骤

1. 定义基础模型直到特征层，输出特征向量 $\boldsymbol{x}$（维度 `feature_size`）
2. 在特征层后接 `Dense(nb_classes, activation='softmax')` 做分类输出
3. 创建 `Input(shape=(1,))` 作为类别编号输入
4. 定义 `Embedding(nb_classes, feature_size)(input_target)` 存储类中心
5. 计算 `L2` 距离：`K.sum(K.square(feature - centers), 1, keepdims=True)`
6. 组装多输出模型：分类输出 + L2 loss输出
7. `compile` 时交叉熵用 `sparse_categorical_crossentropy`，center loss用 `lambda y_true, y_pred: y_pred`
8. 训练时传入 `[train_images, train_targets]` 作为输入，`[train_targets, random_y]` 作为目标

## 直觉

Embedding层在这里不是做词向量，而是纯粹利用"输入整数、输出向量"的矩阵查找语义。把类中心存在Embedding矩阵中，每个类别对应一个可训练的行向量，在梯度回传时同时更新分类权重和类中心。

两个损失的分工明确：softmax交叉熵负责把不同类的特征拉开（类间分离），center loss负责把同一类的特征向中心收拢（类内紧凑）。$\lambda$ 控制两者的平衡——太大则特征过度坍缩到中心（分类性能下降），太小则聚类效果不足。

## 边界

- `feature_size` 应小于 `nb_classes` 才有聚类意义：若特征维度大于类别数，中心点本身就能轻松分类，惩罚项效果弱
- 类中心用Embedding层存储意味着每个batch需要同时传入特征和对应的类别编号——训练数据构造略复杂
- $\lambda$ 是敏感超参，通常需要在验证集上调优（如分狗竞赛中用 `0.25`）
- 只适用于分类标签已知的监督场景，无法直接用于无监督聚类
- Embedding中心在训练初期应与其他层同步更新，否则中心点的初始随机位置会对特征造成错误牵引

## 例子

- 百度分狗竞赛（100类狗分类）：使用Xception提取特征，`feature_size=64`，`loss_weights=[1., 0.25]`，同时配合GLU激活函数和auxiliary loss
- 人脸识别场景：训练百万级分类模型，利用训练好的特征层提取向量，在应用阶段用KNN做身份匹配
- 细粒度商品检索：训练后提取特征向量做相似度排序，同类商品在特征空间自然聚拢

## 证据

- ev::4493::Center Loss核心公式：softmax交叉熵 + λ * ||x - c_y||²，Embedding层存储类中心
- ev::4493::Keras实现模式：多输出模型 + lambda y_true, y_pred: y_pred 技巧
- ev::4493::Embedding层的本质是矩阵查找，不是词向量，与NLP无关
- ev::4611::实际应用验证：百度分狗竞赛中使用Center Loss作为辅助损失，loss_weights=0.25
- ev::4611::feature_size < nb_classes 才有聚类意义（64 < 100）
