---
type: concept
title: SimBERT
definition: 基于 UniLM 的融合检索和生成的相似问微调模型，利用 Batch 内对比和自回归重构联合训练句向量。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md"]
source_ids: ["7427"]
aliases: ["SimBERTv1"]
status: stable
updated: 2026-06-12
---

# SimBERT

## 定义
SimBERT 是一种在大规模相似句对上，通过联合有监督自回归生成与批次对比检索进行微调的预训练语言模型。

## 核心价值
它集成了检索与生成两大功能，可以用做特征式相似度句向量的高水准 baseline，同时能够通过 Seq2Seq 完成同义句自动生成以进行数据扩增。
SimBERT 的对比检索使用 `[CLS]` 向量在 batch 内除对角线以外的其他负对上做 Softmax 分类训练，使检索任务以分类交叉熵形式端到端学习，极大克服了传统 Sbert 回归拟合的局限性。