---
title: Keras多GPU/TPU训练（tf.keras）
type: method
aliases: [Keras MirroredStrategy, Keras TPU Training, tf.distribute Keras]
tags: [tensorflow, keras, multi-gpu, tpu, distributed-training]
operation_types:
  primary: "Decompose / reduce dimension"
  secondary: ["Estimate / sample instead of compute"]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-11-06-Keras-Tensorflow的黄金标准.md
source_ids:
  - "7055"
status: draft
updated: 2026-06-13
method_summary: "通过tf.distribute.MirroredStrategy在tf.keras中实现极简的多GPU和TPU分布式训练。"
typical_structure: "定义strategy后在strategy.scope()下创建模型和compile，正常使用model.fit()。"
applicability: "需要多GPU或TPU加速训练的Keras模型，前提是遵循Keras标准写法。"
examples: "单机多卡BERT训练、TPU训练"
belongs_to: [分布式训练技巧, Keras工程技巧]
layering: [训练阶段, 分布式配置]
formula_standard_notation: false
related_concepts: [tf-distribute-多GPU训练]
---

## 适用问题

需要在多GPU或TPU环境下加速Keras模型训练的场景。特别适用于模型较大、单卡训练时间过长的任务。

## 核心变换

**输入**：单卡Keras模型（`model.compile()` + `model.fit()`）
**输出**：多卡分布式训练的Keras模型

通过`tf.distribute.Strategy`将模型自动复制到多个设备，数据自动分片，梯度自动同步：
$$
\theta_{t+1} = \theta_t - \eta \cdot \frac{1}{N}\sum_{i=1}^N \nabla L_i(\theta_t)
$$
其中$N$为GPU/TPU数量，$\nabla L_i$为第$i$个设备上的梯度。

## 典型步骤

1. **定义策略**：`strategy = tf.distribute.MirroredStrategy()`（单机多卡）或`TPUStrategy`（TPU）
2. **在策略作用域下创建模型**：`with strategy.scope(): model = create_model(); model.compile()`
3. **正常调用fit**：`model.fit(train_x, train_y, epochs=10)`，数据自动分配
4. **（可选）切换到TPU**：替换Strategy为`TPUStrategy`，代码基本不变

## 直觉

分布式训练的核心思想是数据并行：每个设备持有完整模型副本，处理不同的数据批次，独立计算梯度后同步平均。`tf.distribute.Strategy`封装了设备管理、数据分片、梯度聚合等底层细节。关键是必须在`strategy.scope()`下创建模型和编译，确保变量的创建和优化器的操作都在分布式上下文中进行。

## 边界

- **必须使用Keras标准写法**：使用内置层、实现`get_config`方法。可用`clone_model`测试规范性
- **避免`add_loss`/`add_metric`**：自定义loss应定义为层的输出
- **避免动态操作**：TPU训练中`tf.where`的x/y不能为None，避免变长操作
- `multi_gpu_model`（Keras自带）不如`tf.distribute.MirroredStrategy`可靠
- 支持单机多卡和多机多卡，需要对应配置

## 例子

- 单机多卡BERT训练：定义`MirroredStrategy`后，在`scope`下`build_transformer_model`和`compile`
- TPU训练：使用`TPUClusterResolver`和`TPUStrategy`，其余代码不变
- bert4keras预训练框架在TPU/多GPU环境下测试通过

## 证据

- ev::7055::MirroredStrategy用法：`strategy = MirroredStrategy(); with strategy.scope(): model = create_model(); model.compile(); model.fit()`
- ev::7055::TPUStrategy用法：`TPUClusterResolver → initialize_tpu_system → TPUStrategy`
- ev::7055::标准Keras写法要求：内置层、get_config、避免add_loss/add_metric、避免动态操作
