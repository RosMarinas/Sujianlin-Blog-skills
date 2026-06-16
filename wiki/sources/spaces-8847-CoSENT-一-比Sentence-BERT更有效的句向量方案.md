---
type: article_summary
title: CoSENT（一）：比Sentence-BERT更有效的句向量方案
article_id: "8847"
source_url: https://spaces.ac.cn/archives/8847
date: 2022-01-06
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-01-06-CoSENT-一-比Sentence-BERT更有效的句向量方案.md
series:
  - [[CoSENT]]
topics:
  - [[句向量与对比学习]]
concepts:
  - [[CoSENT]]
  - [[句向量]]
methods:
  - [[用互信息内积构造词向量几何]]
evidence_spans:
  - ev::8847::直接优化Cos失效
  - ev::8847::InferSent有效原因
  - ev::8847::CoSENT损失函数
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-06-CoSENT-一-比Sentence-BERT更有效的句向量方案.md
source_ids:
  - "8847"
status: draft
updated: 2026-06-10
---
# CoSENT（一）：比Sentence-BERT更有效的句向量方案

## 文章核心问题

如何设计一个直接优化余弦相似度、且训练与预测一致的有监督句向量方案？

## 主要结论

直接优化cos效果差的原因是负样本对目标过低（困难负样本不应低至0或-1）。InferSent/Sentence-BERT有效是因为它们利用了分类层的聚类能力，但存在训崩风险。CoSENT使用排序损失 log(1 + ∑ e^{λ(cos(neg)-cos(pos))})，直接优化cos相似度的相对顺序，在收敛速度和效果上均优于Sentence-BERT。

## 推导结构

1. 分析直接优化Cos失败的原因（困难负样本）
2. InferSent/Sentence-BERT的有效机制与问题
3. CoSENT损失函数的设计
4. 推广到通用排序损失（NLI数据也可用）
5. 实验对比

## 关键公式

CoSENT损失：log(1 + ∑_{pos,neg} e^{λ(cos(u_k,u_l) - cos(u_i,u_j))})

## 体现的方法

连接到已有方法 用互信息内积构造词向量几何（词向量方法家族），CoSENT提供了sentence-level的对比方案。

## 所属系列位置

CoSENT系列第一篇，核心方法提出。

## 与其他文章的关系

- 与更别致的词向量模型系列共享句向量/词向量的目标
- 后续连接CoSENT（二）和（三）

## 原文证据锚点

- ev::8847::直接优化Cos失效 — 直接优化cos失败的原因分析
- ev::8847::InferSent有效原因 — 为什么训练预测不一致的方案仍然有效
- ev::8847::CoSENT损失函数 — CoSENT的排序损失设计
