---
type: article_summary
title: "噪声对比估计杂谈：曲径通幽之妙"
article_id: "5617"
source_url: https://spaces.ac.cn/archives/5617
date: 2018-06-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2018-06-13-噪声对比估计-杂谈-曲径通幽之妙.md
series: []
topics:
  - 采样与估计
  - 词向量与表示学习
concepts:
  - noise contrastive estimation
  - partition function
  - negative sampling
  - exponential family distribution
  - mutual information
methods:
  - 噪声对比估计
problem_patterns: []
evidence_spans:
  - "5617::指数族分布"
  - "5617::难算的配分函数"
  - "5617::变成二分类问题"
  - "5617::等价于原来分布"
  - "5617::NCE与负采样简述"
  - "5617::Word2Vec"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-06-13-噪声对比估计-杂谈-曲径通幽之妙.md
source_ids:
  - "5617"
status: draft
updated: 2026-06-10
---

## 文章核心问题

当概率分布的归一化因子（配分函数）难以计算时，如何估计分布参数。噪声对比估计（NCE）将密度估计转化为二分类问题，无需计算配分函数即可估计参数。

## 主要结论

- NCE将真实样本与噪声样本的二分类损失等价于最大似然估计（在KL散度意义上）
- 负采样（Word2Vec）是NCE的特例（默认$\gamma=0$，按词频采样噪声）
- Word2Vec负采样实际上在拟合互信息而非条件概率，这解释了它的优越性

## 推导结构

1. 指数族分布与配分函数问题
2. NCE核心：将建模问题转化为二分类，损失函数为交叉熵
3. 证明NCE等价于最大似然估计（通过KL散度分析）
4. 扩展到Word2Vec负采样，揭示其拟合互信息的本质

## 关键公式

$$p(\boldsymbol{x}) = \frac{e^{G(\boldsymbol{x};\boldsymbol{\theta})}}{Z(\boldsymbol{\theta})} \quad\Rightarrow\quad p(1|\boldsymbol{x}) = \sigma(G(\boldsymbol{x};\boldsymbol{\theta}) - \gamma)$$

$$\text{NCE Loss} = -\mathbb{E}_{\boldsymbol{x}\sim \tilde{p}(\boldsymbol{x})}\log p(1|\boldsymbol{x}) - \mathbb{E}_{\boldsymbol{x}\sim U(\boldsymbol{x})}\log p(0|\boldsymbol{x})$$

$$\tilde{p}(w_j|w_i) / \tilde{p}(w_j) = e^{\langle \boldsymbol{u}_i,\boldsymbol{v}_j\rangle} \quad\Rightarrow\quad \log\frac{\tilde{p}(w_j|w_i)}{\tilde{p}(w_j)} = \langle \boldsymbol{u}_i,\boldsymbol{v}_j\rangle$$

## 体现的方法

- 噪声对比估计（NCE）：核心方法，将不可归一化模型的参数估计转化为二分类

## 所属系列位置

单篇独立文章，但与Word2Vec/词向量系列有交叉。

## 与其他文章的关系

NCE与重要性采样共享"estimate/sample instead of compute"操作类型。本文的Word2Vec负采样分析与互信息词向量系列相关。

## 原文证据锚点

- 指数族分布定义：指数族分布节
- NCE方法：NCE登场节
- 等价性证明：等价于原来分布节
- Word2Vec分析：Word2Vec节
