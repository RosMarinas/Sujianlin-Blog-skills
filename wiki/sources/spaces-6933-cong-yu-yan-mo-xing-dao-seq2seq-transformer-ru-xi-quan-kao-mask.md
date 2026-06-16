---
type: article_summary
title: 从语言模型到Seq2Seq：Transformer如戏，全靠Mask
article_id: "6933"
source_url: https://spaces.ac.cn/archives/6933
date: 2019-09-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-09-18-从语言模型到Seq2Seq-Transformer如戏-全靠Mask.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-18-从语言模型到Seq2Seq-Transformer如戏-全靠Mask.md
source_ids:
  - "6933"
status: draft
updated: 2026-06-12
---

## 文章核心问题
系统分析Transformer中Attention矩阵的Mask方式，解释单向语言模型、乱序语言模型、Seq2Seq（UNILM）的实现原理。

## 主要结论
Attention矩阵的Mask方式是各种花式Transformer模型的核心门道；UNILM方案可以用单个BERT模型完成Seq2Seq任务。

## 推导结构
1. Attention数学形式回顾
2. 单向语言模型的三角Mask
3. 乱序语言模型的随机Mask——重排输入等价方案
4. UNILM的Seq2Seq Mask——拼接式双向+单向Attention
5. 基于bert4keras的实验实现

## 关键公式
- Attention(Q,K,V) = softmax(QK^T/√d)V
- 语言模型条件概率 p(x_1...x_n) = Π p(x_t|x_{<t})
- UNILM Mask设计

## 体现的方法
基于Attention Mask的单向/双向控制方法、UNILM统一Seq2Seq方法、乱序语言模型实现方法

## 所属系列位置
独立文章，属于Transformer预训练模型分析系列

## 与其他文章的关系
与[6877]共同探讨Seq2Seq；为[7809][8209]的实践提供理论基础；使用[6915]的bert4keras实现

## 原文证据锚点
各种Mask图示、UNILM模型图、代码实现、实验结果