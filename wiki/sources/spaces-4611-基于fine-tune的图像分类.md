---
title: 基于fine tune的图像分类（百度分狗竞赛）
source_id: 4611
type: source
url: https://spaces.ac.cn/archives/4611
author: 苏剑林
date: 2017-10-13
category: 信息时代
tags: [fine-tuning, image-classification, xception, glu, center-loss, data-augmentation]
license: CC BY-NC-SA
abstract: 百度大数据竞赛细颗粒度图像分类方案（宠物狗100类）。使用Xception为基础模型，GLU激活函数压缩特征，Center Loss实现特征聚类，auxiliary loss作为正则。三阶段训练策略：先冻结Xception仅训练新增层，再放开部分block用SGD微调，最后减少数据扩增继续微调。数据扩增包括随机翻转、旋转、缩放、同类图片拼接、随机遮掩等。
key_contributions:
  - GLU（门控线性单元）激活函数在图像分类中的应用
  - Center Loss的Keras实现（Embedding存聚类中心）
  - 三阶段微调训练策略（冻结→部分放开→精细调整）
  - 同类图片随机拼接数据扩增
  - 四分之一随机遮掩数据扩增
  - 迁移学习（混合测试集预测结果重新训练）
  - 双预测头加权平均（GLU特征+原始特征）
---
