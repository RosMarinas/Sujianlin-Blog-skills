---
title: "让Keras更酷一些！"：层与模型的重用技巧
source_id: 6985
type: source
url: https://spaces.ac.cn/archives/6985
author: 苏剑林
date: 2019-09-29
category: 信息时代
tags: [keras, layer-sharing, model-reuse, deep-learning]
license: CC BY-NC-SA
abstract: 深入探讨Keras中层与模型的权重共享和重用技巧。基础部分包括层重用、模型重用、模型克隆。进阶部分包括：通过交叉引用共享权重（如Bert中Embedding与Dense权重共享）、提取中间层特征、以及通过"移花接木"方法实现模型从中间拆解和层的插入替换。核心技巧是通过覆盖model.inputs和model._input_layers欺骗run_internal_graph函数。
key_contributions:
  - Keras层共享权重与不共享权重的写法区别
  - 模型(Model)作为层(Layer)调用的原理
  - clone_model复制结构不复制权重的用法
  - EmbeddingDense层实现Embedding与全连接权重共享
  - 提取模型中间层特征的通用方法
  - 从模型中间拆开后插入/替换层的"移花接木"技巧
---
