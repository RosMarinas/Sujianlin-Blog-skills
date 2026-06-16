---
type: article_summary
title: 基于DGCNN和概率图的轻量级信息抽取模型
article_id: "6671"
source_url: https://spaces.ac.cn/archives/6671
date: 2019-06-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-06-03-基于DGCNN和概率图的轻量级信息抽取模型.md
series:
  - [[GlobalPointer与联合抽取]]
topics:
  - [[联合抽取]]
concepts:
  - [[半指针-半标注]]
  - [[字词混合Embedding]]
  - [[远程监督先验特征]]
methods:
  - [[基于概率分解的关系抽取]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-03-基于DGCNN和概率图的轻量级信息抽取模型.md
source_ids:
  - "6671"
---

# 基于DGCNN和概率图的轻量级信息抽取模型

本文介绍了一种在监督学习框架下进行三元组抽取的高效方案。该方案放弃了传统级联抽取（先抽取实体再分类关系）或序列标注（难以解决实体嵌套和一对多问题）的路径，而是提出了一种基于概率图思想的抽取设计。

模型首先预测主实体（Subject），然后将主实体的向量表征作为先验条件，联合预测对应的客实体（Object）和关系谓词（Predicate）。网络架构基于12层膨胀门卷积（DGCNN）与Self-Attention，并配合“字词混合Embedding”和“远程监督先验特征”等优化手段，实现了在保障准确率的同时大幅提升了训练和解码速度。
