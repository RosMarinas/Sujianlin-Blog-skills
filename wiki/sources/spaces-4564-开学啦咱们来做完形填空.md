---
title: 开学啦！咱们来做完形填空～（讯飞杯）
source_id: 4564
type: source
url: https://spaces.ac.cn/archives/4564
author: 苏剑林
date: 2017-09-03
category: 信息时代
tags: [reading-comprehension, cloze, lstm, attention, nlp, tensorflow]
license: CC BY-NC-SA
abstract: 参加讯飞杯中文机器阅读理解评测的完形填空任务方案。采用双层双向LSTM分别编码上下文，通过编码向量与各时间步状态向量的内积进行注意力匹配，从上下文词中挑选最佳填空词。验证集73.55%，测试集75.77%（单系统排名第6）。关键技巧包括共享参数的上下LSTM编码、填充位置mask、重复词概率合并。
key_contributions:
  - 完形填空任务的LSTM+Attention模型
  - 共享参数的上下文双向LSTM编码
  - 内积注意力替代全连接层做上下文词选择
  - 填充位置mask处理（减大常数）
  - 重复词概率合并策略
  - 基于Word2Vec预训练词向量
---
