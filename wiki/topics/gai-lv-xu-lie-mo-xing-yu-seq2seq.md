---
type: topic
title: 概率序列模型与Seq2Seq
scope: BERT时代前后的经典序列概率模型，涵盖CRF、Seq2Seq的各类改进（双向解码、Exposure Bias缓解、重复解码分析）、中文新词发现算法、生成式对话模型（DialoGPT）、中文生成式预训练（T5 PEGASUS）以及bert4keras工具生态。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-18-简明条件随机场CRF介绍-附带纯Keras实现.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-31-基于最小熵原理的NLP库-nlp-zero.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-08-09-seq2seq之双向解码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-08-27-自己实现了一个bert4keras.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-09-重新写了之前的新词发现算法-更快更好的新词发现.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-18-从语言模型到Seq2Seq-Transformer如戏-全靠Mask.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-02-07-你的CRF层的学习率可能不够大.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-03-09-Seq2Seq中Exposure-Bias现象的浅析与对策.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-16-如何应对Seq2Seq中的-根本停不下来-问题.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-09-07-动手做个DialoGPT-基于LM的生成式多轮对话模型.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-10-19-BERT可以上几年级了-Seq2Seq-硬刚-小学数学应用题.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-11-20-跟风玩玩目前最大的中文GPT2模型-bert4keras.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-01-26-Seq2Seq重复解码现象的理论分析尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-03-T5-PEGASUS-开源一个中文生成式预训练模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-31-bert4keras在手-baseline我有-CLUE基准代码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-28-在bert4keras中使用混合精度和XLA加速训练.md
source_ids: ["5542", "5597", "6877", "6915", "6920", "6933", "7196", "7259", "7500", "7718", "7809", "7912", "8128", "8209", "8739", "9059"]
series: []
concepts:
  - "[[概念: 条件随机场]]"
  - "[[概念: 线性链CRF]]"
  - "[[概念: Exposure Bias]]"
  - "[[概念: Teacher Forcing]]"
  - "[[概念: 束搜索]]"
  - "[[概念: 自回归生成模型]]"
  - "[[概念: 重复解码]]"
  - "[[概念: 双向解码]]"
  - "[[概念: 最小熵原理]]"
  - "[[概念: 新词发现]]"
  - "[[概念: GlobalPointer]]"
  - "[[概念: UniLM]]"
  - "[[概念: PEGASUS预训练]]"
formulas:
  - "[[公式: CRF条件概率]]"
  - "[[公式: CRF归一化因子递推]]"
  - "[[公式: Attention]]"
  - "[[公式: 交叉熵]]"
  - "[[公式: Seq2Seq概率分解]]"
  - "[[公式: 重复概率公式]]"
propositions: []
methods:
  - "[[方法: 线性链CRF构建]]"
  - "[[方法: UNILM统一Mask]]"
  - "[[方法: 随机替换抗Exposure Bias]]"
  - "[[方法: 对抗训练文本增强]]"
  - "[[方法: 自截断解码停止]]"
  - "[[方法: 基于LM的多轮对话]]"
  - "[[方法: 词级Rebalanced Encoding]]"
  - "[[方法: 新词发现ngram过滤]]"
  - "[[方法: 双向解码交叉注意力]]"
  - "[[方法: GlobalPointer序列标注]]"
problem_patterns: []
reading_paths: []
open_questions:
  - "Exposure Bias的更严格理论分析"
  - "重复解码与解码不停止的统一解释"
  - "CRF在大型预训练模型中的实际价值评估"
status: draft
updated: 2026-06-12
---

# 概率序列模型与Seq2Seq

## 属于本主题的内容

本批次的16篇文章围绕"概率序列模型与Seq2Seq"这条主线，涵盖以下子主题：

- **CRF序列标注**（5542, 7196）：条件随机场的理论、实现和应用优化
- **Seq2Seq架构改进**（6877, 6933, 7259, 7500, 7809, 8128）：双向解码、Mask机制、Exposure Bias、停不下来问题、理论分析
- **无监督NLP**（5597, 6920）：最小熵原理驱动的词库构建和新词发现
- **生成式对话与预训练**（7718, 7912, 8209）：DialoGPT、CPM-LM、T5 PEGASUS
- **bert4keras生态**（6915, 8739, 9059）：框架实现、CLUE基准、加速训练

## 明确不属于本主题

- Transformer架构的完整理论分析（仅涉及Mask机制）
- BERT预训练原理本身
- 词向量的表示学习
- 图像/多模态生成

## 核心概念

参见概念列表。核心贯穿主题：**如何对序列的联合概率分布进行建模和分解**——CRF的全局归一化vs局部归一化、Seq2Seq的自回归分解、Exposure Bias的成因、语言模型作为通用序列建模框架。

## 核心方法

参见方法列表。主要操作类型包括：Decompose / reduce dimension（CRF、新词发现）、Rewrite / identity transform（UNILM Mask）、Estimate / sample instead of compute（随机替换、对抗训练）、Construct auxiliary sequence（自截断停止、双向解码）。

## 待定链接

- 与已编译的"语义相似度对比学习"批次可能的交叉点：对比学习损失与Seq2Seq的优化
