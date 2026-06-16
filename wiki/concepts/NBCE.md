---
type: concept
title: NBCE
aliases:
  - Naive Bayes-based Context Extension
  - 基于朴素贝叶斯的上下文扩展
definition: |
  基于朴素贝叶斯的上下文扩展（Naive Bayes-based Context Extension）是一种在推理阶段即插即用、无需微调的LLM上下文长度扩展方法。它通过将长上下文划分为若干独立的段落，利用朴素贝叶斯公式在概率层面将长序列预测转化为各个短上下文预测概率的乘性聚合（或对数空间的加权Pooling），并减去无上下文预测以过滤背景知识幻觉。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-31-关于NBCE方法的一些补充说明和分析.md
source_ids:
  - 9617
  - 9632
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# NBCE

## Definition
基于朴素贝叶斯的上下文扩展（Naive Bayes-based Context Extension）是一种在推理阶段即插即用、无需微调的LLM上下文长度扩展方法。它通过将长上下文划分为若干独立的段落，利用朴素贝叶斯公式在概率层面将长序列预测转化为各个短上下文预测概率的乘性聚合（或对数空间的加权Pooling），并减去无上下文预测以过滤背景知识幻觉。

## Details
NBCE 为扩展大语言模型的上下文窗口提供了一个全新的即插即用视角。
在面对超长文本（如多篇文档、长篇小说）时，常规LLM受限于预训练的位置编码范围无法直接输入。NBCE 将长文本切分为 $n$ 个小于预训练长度的短 Contexts $S_1, \dots, S_n$。
在生成下一个 Token $T$ 时，NBCE 让模型并行推理每个 Context $S_i$ 加上已生成 $T$ 的条件概率 $p(T|S_i)$，再结合无 Context 时的 $p(T)$。
根据朴素贝叶斯推导，对数空间下的聚合概率为各概率的加权 Pooling 减去背景项的对数概率。
为解决语言模型预测尾部噪声大的问题，NBCE 必须对每个分布在计算前进行 Top-P 截断。通过引入“最小熵 Pooling”和“跳转惩罚 $\eta$”，NBCE 能够稳定、连续地根据上万字的长输入生成可读性极高且幻觉较少的正确答案。