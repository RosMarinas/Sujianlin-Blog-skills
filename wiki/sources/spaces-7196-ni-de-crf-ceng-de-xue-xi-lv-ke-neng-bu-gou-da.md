---
type: article_summary
title: 你的CRF层的学习率可能不够大
article_id: "7196"
source_url: https://spaces.ac.cn/archives/7196
date: 2020-02-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-02-07-你的CRF层的学习率可能不够大.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-02-07-你的CRF层的学习率可能不够大.md
source_ids:
  - "7196"
status: draft
updated: 2026-06-12
---

## 文章核心问题
发现BERT+CRF中CRF层可能因学习率不足导致转移矩阵不合理的问题，提出增大CRF层学习率的改进方案。

## 主要结论
CRF层的转移矩阵在BERT+CRF中常因学习率不足而训练不充分；增大CRF层学习率（为主体100倍以上）可得到合理转移矩阵。

## 推导结构
1. 观察糟糕的转移矩阵（数值不合理）
2. 分析原因：BERT拟合能力强，逐标签分布迅速收敛，CRF层梯度变小
3. 增大CRF层学习率的实验验证
4. 降低BERT拟合能力的验证实验

## 关键公式
（以实验数据为主；转移矩阵表格）

## 体现的方法
CRF层学习率自适应调节方法、分层学习率设置方法

## 所属系列位置
独立文章，属于CRF应用优化系列

## 与其他文章的关系
基于[5542]的CRF实现；与[6933][6915]共享bert4keras技术栈

## 原文证据锚点
转移矩阵对比表、实验数据表格