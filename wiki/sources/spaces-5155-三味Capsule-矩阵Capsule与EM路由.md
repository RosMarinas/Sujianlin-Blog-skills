---
type: article_summary
title: 三味Capsule：矩阵Capsule与EM路由
article_id: "5155"
source_url: https://spaces.ac.cn/archives/5155
date: 2018-03-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-03-02-三味Capsule-矩阵Capsule与EM路由.md
series:
  - "[[新理解矩阵]]"
topics:
  - "[[矩阵代数]]"
  - "[[生成模型]]"
concepts:
  - "[[矩阵Capsule]]"
  - "[[高斯混合模型]]"
  - "[[非方阵的行列式]]"
  - "[[矩阵指数]]"
methods:
  - "[[带参求导构造ODE证明法]]"
  - "[[显式可逆矩阵构造法]]"
  - "[[EM路由算法]]"
problem_patterns:
  - "[[将经验判断转化为可计算命题]]"
evidence_spans:
  - ev::5155::内容摘要
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-03-02-三味Capsule-矩阵Capsule与EM路由.md
source_ids:
  - "5155"
status: stable
updated: 2026-06-12
---

# 三味Capsule：矩阵Capsule与EM路由

## 文章总结
本文介绍了一种名为Matrix Capsules（矩阵Capsule）的模型及其使用EM（Expectation-Maximization）路由的更新算法。该模型将网络特征以矩阵而非向量表示，并且不再通过模长反映特征显著性，而是采用高斯混合模型（GMM）作为聚类模型，推导了基于信息熵度量的激活值计算，从而实现了更加合理的动态路由聚合。
