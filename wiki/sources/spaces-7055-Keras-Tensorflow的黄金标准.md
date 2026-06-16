---
title: Keras：Tensorflow的黄金标准
source_id: 7055
type: source
url: https://spaces.ac.cn/archives/7055
author: 苏剑林
date: 2019-11-06
category: 信息时代
tags: [keras, tensorflow, tf-keras, multi-gpu, tpu, deep-learning]
license: CC BY-NC-SA
abstract: 介绍tf.keras在多GPU和TPU环境下的训练方法，以及Keras成为Tensorflow标准上层API的原因。展示了通过tf.distribute.MirroredStrategy实现单机多卡训练的极简代码，以及TPUStrategy的类似用法。总结了Keras标准写法规范：全部使用内置层、自定义层实现get_config、避免add_loss/add_metric、避免动态操作。
key_contributions:
  - tf.distribute.MirroredStrategy多GPU训练
  - TPUStrategy训练配置
  - Keras标准写法规范（4条原则）
  - clone_model测试自定义层规范性
  - 静态图优于动态图的观点
  - bert4keras预训练代码介绍
---
