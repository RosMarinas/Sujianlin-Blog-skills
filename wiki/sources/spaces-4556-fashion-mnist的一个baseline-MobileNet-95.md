---
title: fashion mnist的一个baseline (MobileNet 95%)
source_id: 4556
type: source
url: https://spaces.ac.cn/archives/4556
author: 苏剑林
date: 2017-08-27
category: 信息时代
tags: [fashion-mnist, mobilenet, image-classification, data-augmentation, keras]
license: CC BY-NC-SA
abstract: 使用MobileNet在fashion mnist数据集上达到95%准确率的baseline实验。介绍了MobileNet的depthwise卷积与SVD分解的思想类比，通过将28x28灰度图像放大到56x56三通道来适配MobileNet输入，结合随机左右翻转数据扩增提升准确率。分析了数据扩增的本质是引入测试集先验知识。
key_contributions:
  - MobileNet迁移学习用于fashion mnist分类
  - 灰度图转三通道（Lambda层repeat_elements）
  - 随机左右翻转数据扩增实现
  - depthwise卷积与SVD分解的思想类比
  - 数据扩增本质分析（引入测试集先验知识）
---
