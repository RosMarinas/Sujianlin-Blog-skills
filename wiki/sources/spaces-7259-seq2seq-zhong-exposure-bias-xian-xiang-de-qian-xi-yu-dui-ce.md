---
type: article_summary
title: Seq2Seq中Exposure Bias现象的浅析与对策
article_id: "7259"
source_url: https://spaces.ac.cn/archives/7259
date: 2020-03-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-03-09-Seq2Seq中Exposure-Bias现象的浅析与对策.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-03-09-Seq2Seq中Exposure-Bias现象的浅析与对策.md
source_ids:
  - "7259"
status: draft
updated: 2026-06-12
---

## 文章核心问题
深入分析Seq2Seq中Exposure Bias现象的成因，提出随机替换Decoder输入词和对抗训练两种缓解策略。

## 主要结论
Teacher Forcing训练方式存在Exposure Bias；随机替换Decoder输入词（50%概率替换30%词）能有效缓解该问题；对抗训练（梯度惩罚）也能进一步提升效果。

## 推导结构
1. Softmax+交叉熵的数学理解
2. Teacher Forcing的定义与问题
3. Exposure Bias的直观解释与数学形式（局部归一化 vs 全局归一化）
4. 简单例子说明Beam Search下的错误
5. 随机替换策略设计
6. 对抗训练（梯度惩罚）策略
7. 实验验证（CSL和LCSTS数据集）

## 关键公式
- 交叉熵：-log p_t = log(Σ e^{x_i}) - x_t
- Seq2Seq概率分解：p(y|x) = Π p(y_t|x,y_{<t})
- 局部归一化 vs 全局归一化的对比

## 体现的方法
随机替换抗Exposure Bias方法、对抗训练（梯度惩罚）文本增强方法、Teacher Forcing训练方法

## 所属系列位置
独立文章，属于Seq2Seq训练优化系列

## 与其他文章的关系
与[6877][7500][8128]共同组成Seq2Seq深度分析系列；使用[6915]的bert4keras

## 原文证据锚点
Exposure Bias示意图、随机替换策略图、CSL/LCSTS实验结果表格