---
type: article_summary
title: 用bert4keras做三元组抽取
article_id: "7161"
source_url: https://spaces.ac.cn/archives/7161
date: 2020-01-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md
series:
  - [[GlobalPointer与联合抽取]]
topics:
  - [[联合抽取]]
concepts:
  - [[半指针-半标注]]
methods:
  - [[基于条件LayerNorm的实体关系抽取]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md
source_ids:
  - "7161"
---

# 用bert4keras做三元组抽取

本文介绍了在作者开发的bert4keras框架下实现的三元组联合抽取任务。模型沿用了作者先前设计的“半指针-半标注”两步法框架：先通过BERT模型输出表征预测主实体（Subject），再提取主实体首尾表征作为条件，通过条件层归一化（Conditional Layer Normalization）对整体特征进行变换，最后联合预测对应的客实体（Object）和谓词关系（Predicate）。

针对指针标注中正负标签极度失衡的挑战，本文提出将预测概率值进行幂次（$p^n$）变换，该方法在保持原始概率分布物理特性的同时起到自适应调整Loss和梯度权重的效果，不仅能够加速模型收敛，且对模型优化更为友好。
