---
title: BERT-of-Theseus：基于模块替换的模型压缩方法
source_id: 7575
type: source
url: https://spaces.ac.cn/archives/7575
author: 苏剑林
date: 2020-07-17
category: 信息时代
tags: [model-compression, bert, knowledge-distillation]
license: CC BY-NC-SA
abstract: 介绍BERT-of-Theseus模型压缩方法，通过渐进式模块替换实现BERT压缩。核心思想：直接用Successor模块替换Predecessor对应模块训练，仅需下游任务loss，比蒸馏更简洁。
key_contributions:
  - 模块替换替代知识蒸馏，仅需单一下游任务loss
  - 类似Dropout的随机替换机制（0.5概率）
  - 与蒸馏的对比：简洁性和效果可比性
  - 在CLUE iflytek上6层BERT达59.61%，3层BERT达59.36%
  - 同模型压缩能力不如蒸馏（同结构Successor不能超越Predecessor）
  - 与其他技术的关系：类似SamplePairing/mixup的数据扩增思想，类似PGGAN的渐进式训练
