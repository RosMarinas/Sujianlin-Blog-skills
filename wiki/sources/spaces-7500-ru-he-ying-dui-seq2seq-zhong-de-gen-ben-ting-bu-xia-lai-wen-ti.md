---
type: article_summary
title: 如何应对Seq2Seq中的"根本停不下来"问题？
article_id: "7500"
source_url: https://spaces.ac.cn/archives/7500
date: 2020-06-16
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-06-16-如何应对Seq2Seq中的-根本停不下来-问题.md
series: []
topics: []
concepts: []
methods: []
problem_patterns: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-16-如何应对Seq2Seq中的-根本停不下来-问题.md
source_ids:
  - "7500"
status: draft
updated: 2026-06-12
---

## 文章核心问题
讨论Seq2Seq自回归解码中"根本停不下来"（不产生<eos>）的现象，介绍ICML 2020的应对策略并评价其有效性。

## 主要结论
解码算法缺乏停下的理论保障；对于随机解码，有界隐向量可保证最终停下的理论成立但实践价值有限；自截断设计对确定性解码有效但不优雅。

## 推导结构
1. 确定性解码（Greedy/Beam Search）和随机性解码（原生/Top-k/Nucleus）
2. 有界隐向量保证随机解码停下
3. 主动添加<eos>到采样空间
4. 自截断概率设计：p(<eos>|y_{<t},x)=1-α(h_t)
5. 个人评价：理论视角不高，结论弱，没有解释"为什么"

## 关键公式
- p(y_t|y_{<t},x) = softmax(Wh_t+b)
- 自截断：p(<eos>|y_{<t},x) = 1 - Π σ(w^T h_i + b)
- 下界：p(<eos>|y_{<t},x) ≥ 1 - (1-ε)^{t+1}

## 体现的方法
自截断解码停止方法、束搜索/贪心搜索确定性解码方法、Top-k/Top-p随机解码方法

## 所属系列位置
独立文章，属于Seq2Seq解码优化系列

## 与其他文章的关系
与[8128]紧密相关（该文为停不下来的理论补充）；与[7259]共享Seq2Seq主题

## 原文证据锚点
自截断公式推导、解码算法分类定义