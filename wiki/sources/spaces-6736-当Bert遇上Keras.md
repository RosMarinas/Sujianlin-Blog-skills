---
title: 当Bert遇上Keras：这可能是Bert最简单的打开姿势
source_id: 6736
type: source
url: https://spaces.ac.cn/archives/6736
author: 苏剑林
date: 2019-06-18
category: 信息时代
tags: [bert, keras, fine-tuning, nlp, text-classification, relation-extraction]
license: CC BY-NC-SA
abstract: 介绍通过keras-bert在Keras中调用和微调Bert预训练模型的方法。包含三个实战例子：文本情感分类（[CLS]+Dense，95.5%准确率）、关系抽取（极简设计，85%+ F1）、事件主体抽取（双输入接成一个句子）。总结了Bert微调的原则：用尽可能少的层、使用warmup学习率、控制序列长度和batch_size以适应显存。
key_contributions:
  - keras-bert库的基本使用方法
  - 中文Tokenizer重写（保留字符级别对齐）
  - 文本分类：[CLS]向量+Dense(1)
  - 关系抽取：序列标注+subject信息注入
  - 事件主体抽取：双输入连接为单输入
  - Bert微调原则（少加额外层、warmup学习率）
  - 显存优化建议（调小maxlen和batch_size）
---
