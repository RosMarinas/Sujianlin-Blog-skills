---
type: article_summary
title: 无监督语义相似度哪家强？我们做了个比较全面的评测
article_id: 8321
source_url: https://spaces.ac.cn/archives/8321
date: 2021-04-11
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-04-11-无监督语义相似度哪家强-我们做了个比较全面的评测.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-04-11-无监督语义相似度哪家强-我们做了个比较全面的评测.md"]
source_ids: ["8321"]
status: draft
updated: 2026-06-12
---

# 无监督语义相似度哪家强？我们做了个比较全面的评测

## 文章核心问题
通过中英文双语大范围（含600余个实验组合）的评测，系统检验 BERT-whitening 白化变换的有效性与工程应用限制。

## 主要结论
1. 在无监督句向量模型中，应用 BERT-whitening 能够普遍提升语义相似度衡量指标（Spearman 相关系数），且降维到 256/384 维往往能取得比保留全维度更好的表现；
2. 最好的 pooling 方案为第一层与最后一层的平均值（first-last-avg）；
3. 若句向量本身就是通过有监督对比模型（如 SimBERT）微调得来的，做白化处理反而会使检索表现下降。同时，在部分特定分布的数据集（如 BQ Corpus）上白化也存在失效的“天下没有免费的午餐”效应。

## 推导结构
1. 概述 BERT-whitening 的基本架构和降维重要性。
2. 展示英文无监督和 SBERT 监督特征下的白化和降维效果。
3. 对比 11 个中文预训练模型、5个相似度数据集、4类 Pooling 在白化与降维处理前后的性能指标。

## 体现的方法
- [[BERT-whitening变换]]：作为无监督特征后处理手段在不同 pooling 表征下的性能基线评估。

## 与其他文章的关系
- 为 [[你可能不需要BERT-flow：一个线性变换媲美BERT-flow]] 补充了全面英文与中文对比。
- 指出了白化操作对于 fine-tuned 句向量（如 SimBERT）的损害，推动了 [[当BERT-whitening引入超参数：总有一款适合你]] 的提出。

## 原文证据锚点
- `ev::8321::白化操作`：对应原文中测试 11 个模型和 5 个任务，并指出白化降维对无监督模型一般有效，但对于 SimBERT 等已有监督优化的模型会产生性能损害的实验分析。