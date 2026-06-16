---
type: article_summary
title: 基于Conv1D的光谱分类模型（一维序列分类）
article_id: "5505"
source_url: https://spaces.ac.cn/archives/5505
date: 2018-05-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-05-02-基于Conv1D的光谱分类模型-一维序列分类.md
source_html: Data/Spaces_ac_cn/raw/articles/5505/page.html
series: []
topics:
  - "[[topic::序列分类]]"
concepts: []
methods: []
problem_patterns: []
evidence_spans:
  - ev::5505::原理
  - ev::5505::训练
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-02-基于Conv1D的光谱分类模型-一维序列分类.md
source_ids:
  - "5505"
status: draft
updated: 2026-06-11
---

## 文章核心问题

如何使用一维卷积神经网络（Conv1D）对天文光谱序列（2600维长序列）进行四分类（star/unknown/galaxy/qso）？

## 主要结论

1. 光谱序列作为一维函数图像具有局部相关性，适合用CNN处理而非RNN（RNN无法并行处理长序列）。
2. 使用膨胀卷积（dilated convolution）、残差连接、最大池化和ReLU激活来识别发射线和吸收线特征。
3. 两阶段训练策略：先用交叉熵训练，再改用marco f1 score近似函数微调，可提升marco f1指标。
4. 单模型取得0.82+的marco f1，排名第4-5，接近融合模型的效果。

## 推导结构

模型（Conv1D+残差结构）→ 原理（局部相关性、光谱特征）→ 训练（两阶段训练策略和loss设计）→ 代码（完整实现和训练流程）。

## 关键公式

- marco f1 score近似loss：score_loss = -log(Σ 0.5*Σ(y_true*y_pred)/Σ(y_true+y_pred+ε))
- 每个Block：Conv1D(3,dilation=1)+Conv1D(3,dilation=2)+Conv1D(3,dilation=4) + 残差连接

## 体现的方法

本文实现的方法包括：用带残差的膨胀卷积Conv1D处理一维长序列数据，两阶段训练策略（交叉熵→marco f1 score微调）。

## 所属系列位置

独立文章。属于文本无关的序列分类任务，与本文编译批次中其他NLP任务形成对比。

## 与其他文章的关系

- 序列分类方法可迁移到NLP文本分类任务（如情感分类）。
- 与[[article::5743]]的GRU编码器形成CNN vs RNN的对比。

## 原文证据锚点

- `ev::5505::原理`：光谱序列的局部相关性和CNN适用性分析。
- `ev::5505::训练`：两阶段训练策略和marco f1 score近似loss。
