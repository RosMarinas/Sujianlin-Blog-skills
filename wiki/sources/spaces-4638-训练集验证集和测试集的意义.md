---
title: 训练集、验证集和测试集的意义
source_id: 4638
type: source
url: https://spaces.ac.cn/archives/4638
author: 苏剑林
date: 2017-10-14
category: 信息时代
tags: [train-validation-test, machine-learning, methodology]
license: CC BY-NC-SA
abstract: 简明阐述训练集、验证集和测试集的本质区别。核心观点：验证集虽然不参与梯度下降，但参与了人工调参过程（超参数选择），因此也需要一个完全没有经过训练的测试集来最终评估模型。讨论了三者划分的比例、比赛场景中的特殊处理，以及测试集参与调参的无休止递归问题。
key_contributions:
  - 训练集/验证集/测试集三者的清晰定义
  - 验证集"人工调参"的本质分析
  - 比赛场景中验证集划分的特殊性
  - 测试集准确率差时陷入"更多测试集"递归的讨论
---
