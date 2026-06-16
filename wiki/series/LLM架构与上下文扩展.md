---
type: series
title: LLM架构与上下文扩展
aliases:
  - LLM Architecture and Context Extension Series
article_ids:
  - 9529
  - 9547
  - 9554
  - 9577
  - 9593
  - 9617
  - 9632
  - 9648
  - 9783
  - 9889
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-17-为什么现在的LLM都是Decoder-only的架构.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-20-为什么现在的LLM都是Decoder-only的架构-FAQ.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-04-25-注意力和Softmax的两点有趣发现-鲁棒性和信息量.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-31-关于NBCE方法的一些补充说明和分析.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-06-08-Naive-Bayes-is-all-you-need.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-09-26-脑洞大开-非线性RNN居然也可以并行计算.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-12-12-注意力机制真的可以-集中注意力-吗.md
source_ids:
  - 9529
  - 9547
  - 9554
  - 9577
  - 9593
  - 9617
  - 9632
  - 9648
  - 9783
  - 9889
series_goal: |
  从注意力机制的本质性质和概率视角出发，探索如何通过架构优化（如Decoder-only满秩性、对角化线性RNN）与即插即用算法（如NBCE、RoPE-Bias）来提高大语言模型的表达容量与超长上下文处理窗口。
entry_roles:
  9529: 提出Decoder-only架构在注意力掩码下的满秩理论优势并进行控制变量实验
  9547: 针对Decoder-only满秩优势及注意力序列顺序特性的补充问答
  9554: 介绍对角化线性循环神经网络LRU的参数设计、并行计算技巧与表现对比
  9577: 揭示RoPE结合投影层Bias偏置项在长距离自适应局部化注意力并促进外推的效应
  9593: 证明Softmax注意力的防噪鲁棒性，并从信息熵量化角度阐释初始化和温度参数
  9617: 提出即插即用、无需微调的朴素贝叶斯长上下文扩展方案NBCE及最小熵Pooling
  9632: 解决NBCE的长尾低概率尾部噪声，引入转移惩罚机制并分析适用场景
  9648: 将标准注意力重写为以 Skip-Gram 为基础参数化的广义朴素贝叶斯，提供概率层面的堆叠和残差解释
  9783: 提出将非线性RNN通过减去线性骨架写成摄动序列从而间接进行并行求解的机制
  9889: 推导注意力分布的稀疏度指标，对比标准Attention与线性Attention聚焦特征的物理极限
key_concepts:
  - [Decoder-only架构](wiki/concepts/Decoder-only架构.md)
  - [LRU](wiki/concepts/LRU.md)
  - [SLRU](wiki/concepts/SLRU.md)
  - [NBCE](wiki/concepts/NBCE.md)
  - [RoPE-Bias](wiki/concepts/RoPE-Bias.md)
  - [Attention信息熵](wiki/concepts/Attention信息熵.md)
  - [Attention Sparsity](wiki/concepts/attention_sparsity.md)
key_methods:
  - [LRU参数化与初始化](wiki/methods/LRU参数化与初始化.md)
  - [LRU并行化递归算法](wiki/methods/LRU并行化递归算法.md)
  - [最小熵Pooling](wiki/methods/最小熵Pooling.md)
  - [无交跳转加权](wiki/methods/无交跳转加权.md)
  - [非线性RNN摄动并行化](wiki/methods/非线性RNN摄动并行化.md)
reading_paths:
  - [[LLM架构与上下文扩展阅读路径]]
status: draft
updated: 2026-06-14
---

# LLM架构与上下文扩展

## Series Goal
从注意力机制的本质性质和概率视角出发，探索如何通过架构优化（如Decoder-only满秩性、对角化线性RNN）与即插即用算法（如NBCE、RoPE-Bias）来提高大语言模型的表达容量与超长上下文处理窗口。

## Entry Roles
- **9529**: 提出Decoder-only架构在注意力掩码下的满秩理论优势并进行控制变量实验
- **9547**: 针对Decoder-only满秩优势及注意力序列顺序特性的补充问答
- **9554**: 介绍对角化线性循环神经网络LRU的参数设计、并行计算技巧与表现对比
- **9577**: 揭示RoPE结合投影层Bias偏置项在长距离自适应局部化注意力并促进外推的效应
- **9593**: 证明Softmax注意力的防噪鲁棒性，并从信息熵量化角度阐释初始化和温度参数
- **9617**: 提出即插即用、无需微调的朴素贝叶斯长上下文扩展方案NBCE及最小熵Pooling
- **9632**: 解决NBCE的长尾低概率尾部噪声，引入转移惩罚机制并分析适用场景
- **9648**: 将标准注意力重写为以 Skip-Gram 为基础参数化的广义朴素贝叶斯，提供概率层面的堆叠和残差解释
- **9783**: 提出将非线性RNN通过减去线性骨架写成摄动序列从而间接进行并行求解的机制
- **9889**: 推导注意力分布的稀疏度指标，对比标准Attention与线性Attention聚焦特征的物理极限