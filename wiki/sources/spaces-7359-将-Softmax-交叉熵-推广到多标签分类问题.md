---
type: article_summary
title: 将"Softmax+交叉熵"推广到多标签分类问题
article_id: "7359"
source_url: https://spaces.ac.cn/archives/7359
date: 2020-04-25
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-04-25-将-Softmax-交叉熵-推广到多标签分类问题.md
series:
  - [[多标签分类交叉熵]]
topics:
  - [[概率分布构建]]
concepts:
  - [[多标签分类损失]]
  - [[Softmax替代品]]
  - [[交叉熵]]
methods:
  - [[多标签分类统一损失]]
evidence_spans:
  - ev::7359::组合Softmax构造
  - ev::7359::统一loss形式
  - ev::7359::多标签loss实现
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-04-25-将-Softmax-交叉熵-推广到多标签分类问题.md
source_ids:
  - "7359"
status: draft
updated: 2026-06-10
---

# article-7359: 将"Softmax+交叉熵"推广到多标签分类问题

## 文章核心问题
如何将单标签分类中有效的"Softmax+交叉熵"方案推广到多标签分类场景，使其自动处理类别不平衡问题，避免手动调整正负样本权重和阈值？

## 主要结论
1. 一种初步推广是构建组合Softmax，以任意$k$个类别总得分为基本单位构造Softmax，通过牛顿恒等式递归计算配分函数$Z_k$。
2. 更简明的统一形式为$\log(1 + \sum_{i\in\Omega_{neg},j\in\Omega_{pos}} e^{s_i-s_j})$，本质是让每个目标类得分不小于每个非目标类得分。
3. 引入$0$类作为阈值处理不定长多标签分类，最终形式简化为$\log(1+\sum_{i\in\Omega_{neg}}e^{s_i}) + \log(1+\sum_{j\in\Omega_{pos}}e^{-s_j})$，该损失无类别不均衡问题。

## 推导结构
- 从单标签Softmax交叉熵$-\log(e^{s_t}/\sum_i e^{s_i})$出发
- 改写为$\log\sum_i e^{s_i-s_t}$，揭示本质是目标类得分与非目标类得分的两两比较
- 推广到多标签：$\log(1 + \sum_{i\in\Omega_{neg},j\in\Omega_{pos}} e^{s_i-s_j})$
- 引入$0$类作为阈值，得最终形式$\log(e^{s_0}+\sum_{i\in\Omega_{neg}}e^{s_i}) + \log(e^{-s_0}+\sum_{j\in\Omega_{pos}}e^{-s_j})$
- 阈值为0时简化为$\log(1+\sum_{i\in\Omega_{neg}}e^{s_i}) + \log(1+\sum_{j\in\Omega_{pos}}e^{-s_j})$

## 关键公式
- 单标签损失：$-\log\frac{e^{s_t}}{\sum_i e^{s_i}} = \log\sum_i e^{s_i-s_t}$
- 统一多标签损失：$\log(1 + \sum_{i\in\Omega_{neg},j\in\Omega_{pos}} e^{s_i-s_j})$
- 含阈值形式：$\log(e^{s_0}+\sum_{i\in\Omega_{neg}}e^{s_i}) + \log(e^{-s_0}+\sum_{j\in\Omega_{pos}}e^{-s_j})$
- 阈值归零简化：$\log(1+\sum_{i\in\Omega_{neg}}e^{s_i}) + \log(1+\sum_{j\in\Omega_{pos}}e^{-s_j})$
