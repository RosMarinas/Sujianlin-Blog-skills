---
title: 又是Dropout两次！这次它做到了有监督任务的SOTA
source_id: 8496
type: source
url: https://spaces.ac.cn/archives/8496
author: 苏剑林
date: 2021-07-01
category: 信息时代
tags: [dropout, regularization, supervised-learning, r-drop]
license: CC BY-NC-SA
abstract: 介绍R-Drop（Regularized Dropout），将SimCSE的"Dropout两次"思想推广到有监督任务。通过对同一输入两次Dropout得到不同输出，用KL散度约束一致性，在多种任务上取得显著提升。
key_contributions:
  - R-Drop损失函数设计（交叉熵+对称KL散度）
  - 训练-预测不一致性问题的理论分析（模型平均vs权重平均）
  - 与非目标类正则化的关系（交叉熵不关心非目标类分布）
  - 与虚拟对抗训练（VAT）的对比：R-Drop扰动更随机但更多层
  - 半监督学习能力（不逊于VAT，更简单更快）
  - 在中文分类（IFLYTEK 62.69%）和文本生成任务上的优异表现
  - 超参数建议：alpha=4, dropout=0.3
