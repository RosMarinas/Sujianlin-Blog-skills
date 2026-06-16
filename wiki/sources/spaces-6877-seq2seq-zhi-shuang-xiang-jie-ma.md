---
type: article_summary
title: seq2seq之双向解码
article_id: "6877"
source_url: https://spaces.ac.cn/archives/6877
date: 2019-08-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-08-09-seq2seq之双向解码.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-08-09-seq2seq之双向解码.md
source_ids:
  - "6877"
status: draft
updated: 2026-06-12
---

## 文章核心问题
提出Seq2Seq的双向解码机制，通过同时维护从左到右和从右到左两个解码器并相互注意力交互，改善解码不对称性。

## 主要结论
双向解码能提高生成文本首尾部分的质量，使解码过程对称化，但存在信息泄漏和无法对应清晰概率模型的问题。

## 推导结构
1. 统计L2R和R2L解码的不对称性
2. 双向解码基本思路：两个方向解码器通过Attention交互信息
3. 数学描述：以h_n^{(l2r)}为query查询H^{(r2l)}做Attention
4. 训练方案：Teacher Forcing，损失为两方向交叉熵平均
5. 双向束搜索（Beam Search）
6. 信息泄漏分析与缓解策略

## 关键公式
- 概率分解：p(Y|X)=p(y_1|X)p(y_2|X,y_1)...p(y_n|X,y_{<n})
- L2R向量序列 H^{(l2r)}=[h_1^{(l2r)},...,h_n^{(l2r)}]
- 交叉注意力机制

## 体现的方法
双向解码生成方法、交叉注意力信息融合方法、双向束搜索算法

## 所属系列位置
独立文章，属于Seq2Seq模型改进系列

## 与其他文章的关系
与[7259][7500][8128]共同构成Seq2Seq专题；为[6933]的Mask方法提供了替代方案

## 原文证据锚点
解码不对称性统计表、双向解码示意图、信息泄漏示意图