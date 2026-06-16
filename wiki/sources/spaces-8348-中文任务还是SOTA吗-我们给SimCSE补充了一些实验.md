---
type: article_summary
title: 中文任务还是SOTA吗？我们给SimCSE补充了一些实验
article_id: 8348
source_url: https://spaces.ac.cn/archives/8348
date: 2021-04-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-04-26-中文任务还是SOTA吗-我们给SimCSE补充了一些实验.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-04-26-中文任务还是SOTA吗-我们给SimCSE补充了一些实验.md"]
source_ids: ["8348"]
status: draft
updated: 2026-06-12
---

# 中文任务还是SOTA吗？我们给SimCSE补充了一些实验

## 文章核心问题
探讨基于 Dropout 数据扩增的 SimCSE 对比学习模型在中文语义相似度任务上的实际表现和优化参数设定。

## 主要结论
1. 无监督 SimCSE 可以看作是不带文本生成支路的简化版 SimBERT，其核心在于直接利用随机 Dropout 作为极其自然且强有力的表示空间微调数据扩增（即同一个句子两次输入 Encoder 得到正对）；
2. 中文实验表明，除了 PAWSX 外，SimCSE 在 STS-B、LCQMC、BQ 等任务上相较于 BERT-whitening 具有压倒性的性能优势（部分提升超 10 个百分点）；
3. 与 whitening 偏好 first-last-avg 不同，SimCSE 之下表现最好的 pooling 方式是直接提取最后一层的 `[CLS]`。

## 推导结构
1. 剖析无监督 SimCSE Dropout 双视角增广与 InfoNCE 对比损失机制。
2. 介绍中文实验的最佳超参数适配（包括较小的 batch_size 64、较高的学习率和 dropout 比例等）。
3. 比较中文评测中 SimCSE 与 BERT-whitening 和 SimBERT 的具体数据并得出结论。

## 关键公式
- 无监督 SimCSE 对比损失：将样本经过两次带独立随机 Dropout 的前向得到正对表示，损失定义为标准的 batch 归一化内积 Softmax 损失。

## 体现的方法
- [[句向量对比学习分类训练]]：无监督特征空间局部 Dropout 双通道扩增与对比拉伸。

## 与其他文章的关系
- 比对方法启发自 [[鱼与熊掌兼得：融合检索和生成的SimBERT模型]]，是后者的无标签化纯检索精简。
- 证实了利用 Dropout 微调编码层才能有效提升 SimCSE，引发了对线性后处理与微调联合作用的思考。

## 原文证据锚点
- `ev::8348::Dropout扩增`：对应原文中以同一个句子过两次带不同随机 Dropout 的编码层来作为伪正例对进行对比学习分类损失训练的过程。