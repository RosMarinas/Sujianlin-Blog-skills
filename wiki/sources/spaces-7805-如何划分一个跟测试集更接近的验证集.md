---
title: 如何划分一个跟测试集更接近的验证集？
source_id: 7805
type: source
url: https://spaces.ac.cn/archives/7805
author: 苏剑林
date: 2020-10-16
category: 信息时代
tags: [validation-set, test-set, importance-sampling, distribution-shift, discriminator]
license: CC BY-NC-SA
abstract: 解决训练集与测试集分布不一致时如何划分更好的验证集问题。核心方法：训练一个二分类判别器区分训练集和测试集样本，利用判别器输出D(x)构建重要性采样权重w(x)=D(x)/(1-D(x))，通过对训练样本加权使验证集更接近测试集分布。提供了权重调整和直接采样两种策略。
key_contributions:
  - 基于判别器的训练集/测试集分布差异量化
  - 重要性采样权重w(x)=D(x)/(1-D(x))的理论推导
  - 解决标签分布不一致与输入分布不一致的区分
  - 有放回采样构建分布匹配的验证集
  - 与GAN判别器的理论联系
---
