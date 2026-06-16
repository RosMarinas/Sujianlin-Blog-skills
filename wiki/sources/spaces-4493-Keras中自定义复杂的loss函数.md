---
title: Keras中自定义复杂的loss函数
source_id: 4493
type: source
url: https://spaces.ac.cn/archives/4493
author: 苏剑林
date: 2017-07-22
category: 信息时代
tags: [keras, loss-function, deep-learning, triplet-loss, center-loss]
license: CC BY-NC-SA
abstract: 深入介绍Keras中自定义复杂loss函数的多种方法。涵盖：Softmax交叉熵的标签平滑改进（缓解过于自信）、Triplet Loss在多输入问答模型中的实现技巧、以及基于Embedding层的Center Loss人脸识别特征聚类方法。核心思想是将loss写为层的输出，目标作为模型输入。
key_contributions:
  - 标签平滑（Label Smoothing）的Keras实现
  - Triplet Loss通过Lambda层实现（loss作为模型输出）
  - Center Loss通过Embedding层存储聚类中心
  - 多输出模型保留训练进度条和准确率显示
  - Keras灵活性的深入探讨
---
