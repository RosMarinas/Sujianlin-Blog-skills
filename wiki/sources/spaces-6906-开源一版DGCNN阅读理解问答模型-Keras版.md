---
type: article_summary
title: 开源一版DGCNN阅读理解问答模型（Keras版）
article_id: "6906"
source_url: https://spaces.ac.cn/archives/6906
date: 2019-08-20
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-08-20-开源一版DGCNN阅读理解问答模型-Keras版.md
series: []
topics:
  - [[联合抽取]]
concepts:
  - [[字词混合Embedding]]
methods:
  - [[基于全卷积网络的字标注序列建模]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-08-20-开源一版DGCNN阅读理解问答模型-Keras版.md
source_ids:
  - "6906"
---

# 开源一版DGCNN阅读理解问答模型（Keras版）

本文介绍了作者基于Keras复现并开源的DGCNN阅读理解问答模型。与先前非公开的TensorFlow版本相比，此版本进行了一些简化与改进。

首先，模型在输入端改为字级别输入，并引入了“字词混合Embedding”，以此克服了分词错误对跨度抽取边界带来的不良影响。其次，模型去掉了原有的所有人工特征与位置Embedding，以提升模型架构的简洁度、泛化能力及预测效率。此外，在网络训练细节上，模型应用了RAdam（Rectified Adam）优化器，在线下测试集中达到了约0.72的F1分数。
