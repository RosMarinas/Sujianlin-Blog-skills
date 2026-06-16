---
title: 基于Xception的腾讯验证码识别（样本+代码）
source_id: 4503
type: source
url: https://spaces.ac.cn/archives/4503
author: 苏剑林
date: 2017-07-24
category: 信息时代
tags: [xception, captcha, image-classification, keras, cnn]
license: CC BY-NC-SA
abstract: 使用Xception模型进行腾讯验证码识别，公开10万验证码样本。采用Keras的Xception预训练模型（imagenet权重）做特征提取，接4个Dense(26)分别预测4个字母，训练放开所有权重。测试集全对率达到85%以上，调参可达90%+。提供了完整代码和样本数据。
key_contributions:
  - Xception模型迁移学习用于验证码识别
  - 多标签输出（4个字母分别softmax分类）
  - 验证码样本生成器（节省内存）
  - 10万验证码样本公开
---
