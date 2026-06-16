---
type: method
title: "Keras层重用技巧"
aliases:
  - "Keras Layer Sharing"
  - "Keras权重共享"
operation_types:
  primary: "Structure-expose by factorization"
  secondary:
    - "Generalize from special cases"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-29-让Keras更酷一些-层与模型的重用技巧.md
source_ids:
  - "6985"
method_summary: "初始化层/模型实例并存储为变量，多次调用同一变量实现权重共享；覆盖 model.inputs 和 model._input_layers 实现从中间层拆解模型。"
typical_structure: |
  1. 层重用：初始化层实例 → 存为变量 → 多次调用同一变量
  2. 模型拆解：覆盖 model.inputs = [start_tensor] → 覆盖 model._input_layers → 调用 model(new_input) 重建子图
applicability: "Keras 中需要权重共享的多层相同变换；需要从已有模型中提取子模型或插入/替换中间层的场景。"
tools:
  - Keras Functional API
  - Model 内部图遍历
related_concepts:
  - [[Keras层重用与模型重用]]
related_methods:
  - [[Keras自定义Loss作为输出]]
  - [[Keras重计算装饰器]]
examples:
  - [[article::6985]]
status: draft
updated: 2026-06-14
---

## 适用问题

在 Keras 中需要实现两类重用：(1) 多个位置使用**相同的变换且共享权重**同步更新；(2) 从训练好的模型中**拆出子模型**，或往已有模型中**插入/替换中间层**。

前者如 Bert 中 MLM 预测头全连接层与 Embedding 层共享权重；后者如从 ResNet50 中间层提取特征构建新模型。

## 核心变换

**技术一：层重用（权重共享）**

关键规则：**先初始化，存为变量，再反复调用**。每次调用同一变量共享权重。

```python
layer = Dense(784, activation='relu')  # 初始化，存为变量
x = layer(x)  # 第一次调用
x = layer(x)  # 再次调用 — 共享权重
```

反例：每次新建实例不共享权重：

```python
x = Dense(784, activation='relu')(x)
x = Dense(784, activation='relu')(x)  # 不共享！
```

模型也可以当层一样调用（`Model` 继承自 `Layer`），因此模型嵌套同样共享权重。若只需结构复用但不共享权重，用 `clone_model` + `set_weights`。

**技术二：模型中间拆解**

给定模型 `inputs → h1 → h2 → h3 → outputs`，仅需 h3 之后的子图。核心是欺骗 Keras 的 `run_internal_graph` 函数，让它以为输入从 h3 开始：

```python
model.inputs = [start_tensor]                           # 替换输入张量
model._input_layers = [x._keras_history[0] for x in ...] # 替换输入层历史
outputs = model(new_input)                               # 重建子图
```

可选：裁剪 `model._layers` 只保留用到的层，以准确统计参数量。

**交叉引用**：自定义层可通过直接引用另一层的属性实现权重借用（如 EmbeddingDense 的 kernel 设为 `transpose(embedding_layer.embeddings)`）。

## 典型步骤

**层重用**：
1. 初始化层实例并赋值给变量
2. 在模型定义中多次调用该变量，传入不同张量
3. 每次调用自动共享权重

**模型拆解**：
1. 确定起始中间层，获取其输出张量 `start_tensor`
2. 创建新的 `Input` 层，shape 匹配 `start_tensor`
3. 覆盖 `model.inputs = [start_tensor]`
4. 覆盖 `model._input_layers`
5. 调用 `model(new_input)` 得到输出
6. （可选）整理 `model._layers` 只保留用到的层

## 直觉

Keras 的 `Model` 本质上是一个计算图。`model(input)` 调用时，框架从 `model.inputs` 出发，按拓扑序遍历所有节点重建计算图。因此，**替换 `model.inputs` 就相当于改变了图的起点**——框架会自然地只重建从新起点可达的子图。

这种"欺骗"而非重写的策略是 Keras 优雅设计的体现：框架内部的 `run_internal_graph` 已经处理了所有复杂拓扑（残差连接、多分支等），不需要用户手动遍历计算图。

## 边界

- 层重用仅适用于**权重完全共享**的场景；若需要功能相同但独立更新的层，用 `clone_model`
- 模型拆解的 `_input_layers` 覆盖依赖私有属性 `_keras_history`，不同 Keras 版本可能内部实现不同（已验证 keras-team/keras 主线）
- `Sequential` 模型拆解更简单：直接 `for layer in model.layers[2:]` 遍历即可，无需覆盖内部属性
- 交叉引用技巧中，自定义层必须手动管理 `build()` 和 `compute_output_shape()`

## 例子

- Bert MLM 预测头：`EmbeddingDense(embedding_layer)` 直接引用 Embedding 层的 embedding 矩阵作为分类权重
- ResNet50 中间特征提取：从 `add_15` 层拆开，构建只含后半段的子模型
- 残差网络通用拆解：`get_outputs_of(model, model.get_layer('target').output)` 一步到位
- Keras 官方未提供 `model.slice(start_layer)` 接口，此方法填补了这一缺口

## 证据

- ev::6985::层重用核心规则：先初始化存为变量再反复调用，反例不共享权重
- ev::6985::模型拆解三行核心代码：`model.inputs` + `model._input_layers` + `model(input_layers)`
- ev::6985::交叉引用：`EmbeddingDense` 自定义层通过 `K.transpose(embedding_layer.embeddings)` 实现权重共享
- ev::6985::`Model` 继承自 `Layer` 的源码依据：Keras `keras/engine/network.py`
