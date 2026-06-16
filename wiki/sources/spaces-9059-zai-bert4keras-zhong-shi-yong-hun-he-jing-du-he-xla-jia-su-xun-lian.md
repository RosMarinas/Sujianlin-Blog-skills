---
type: article_summary
title: 在bert4keras中使用混合精度和XLA加速训练
article_id: "9059"
source_url: https://spaces.ac.cn/archives/9059
date: 2022-04-28
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-04-28-在bert4keras中使用混合精度和XLA加速训练.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-28-在bert4keras中使用混合精度和XLA加速训练.md
source_ids:
  - "9059"
status: draft
updated: 2026-06-12
---

## 文章核心问题
介绍在bert4keras中使用混合精度训练和XLA加速线性代数运算的方法和性能表现。

## 主要结论
混合精度和XLA可叠加使用，在3090上总体加速约30%；混合精度需要处理NaN和梯度精度问题；XLA可能增加显存消耗。

## 推导结构
1. 实验环境：nvidia-tensorflow 1.15 + bert4keras
2. 混合精度：环境变量+epsilon调整+损失放大
3. XLA：环境变量、Lazy Compilation、XLA Lite
4. 性能比较：混合精度~10%+、XLA~15%+、叠加~30%+

## 关键公式
（以环境配置和实验数据为主）

## 体现的方法
混合精度训练配置方法、XLA加速配置方法、损失放大技巧

## 所属系列位置
独立文章，属于bert4keras工具优化系列

## 与其他文章的关系
基于[6915]的bert4keras框架；与[8739]共享bert4keras生态

## 原文证据锚点
环境配置代码、性能对比数据、损失放大公式