---
type: article_summary
title: 基于GRU和AM-Softmax的句子相似度模型
article_id: "5743"
source_url: https://spaces.ac.cn/archives/5743
date: 2018-07-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-07-29-基于GRU和AM-Softmax的句子相似度模型.md
source_html: Data/Spaces_ac_cn/raw/articles/5743/page.html
series: []
topics:
  - "[[topic::句子相似度]]"
concepts:
  - "[[concept::AM-Softmax]]"
methods:
  - "[[method::用AM-Softmax做句子相似度]]"
problem_patterns: []
evidence_spans:
  - ev::5743::分类问题
  - ev::5743::AM-Softmax
  - ev::5743::效果预览
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-07-29-基于GRU和AM-Softmax的句子相似度模型.md
source_ids:
  - "5743"
status: draft
updated: 2026-06-11
---

## 文章核心问题

句子相似度模型如何借鉴人脸识别中的margin softmax方法来解决分类损失与特征排序的不等价性问题？

## 主要结论

1. 句子相似度与人脸识别高度相似：用分类模型训练编码器，使用时仅用编码器做特征提取和相似度比较。
2. 分类损失与特征排序不等价——分类正确但特征排序可能出错（靠近分类边界的样本）。
3. AM-Softmax通过对z和c_i做L2归一化后，对目标cos值减去margin m，增大类间距离缩小类内距离，解决排序问题。
4. AM-Softmax在句子相似度上top1准确率91.72%，优于普通softmax的90.77%。

## 推导结构

背景（已有做法和不足）→ 模型（分类问题框架和编码器）→ 分类与排序不等价（核心问题分析）→ margin softmax（AM-Softmax原理）→ 实现（Keras代码和实验效果）。

## 关键公式

- 编码器-分类器：z = GRU(x), p = softmax(zW)
- AM-Softmax loss：-log(e^{s·(cosθ_t-m)} / (e^{s·(cosθ_t-m)} + Σ_{i≠t} e^{s·cosθ_i}))
- 加强条件：ψ(θ_t) < cosθ_t，AM-Softmax取ψ(θ_t)=cosθ_t-m

## 体现的方法

- **用AM-Softmax做句子相似度**：借鉴人脸识别的margin softmax方法，通过AM-Softmax损失训练语义编码器，使同义句编码更接近、非同义句编码更远离。

## 所属系列位置

独立文章。

## 与其他文章的关系

- 与[[article::4293]]都涉及带margin的损失函数（margin用于分类 vs margin用于度量学习）。
- 与[[article::4374]]的编码器预训练策略互补（本文用分类任务训练编码器，对方用LM预训练）。
- 与[[method::用语言模型预训练做半监督学习]]的关系：可结合——先用LM预训练初始化GRU，再用AM-Softmax微调。

## 原文证据锚点

- `ev::5743::分类问题`：句子相似度作为多分类问题的训练框架。
- `ev::5743::AM-Softmax`：AM-Softmax的数学原理和margin设计。
- `ev::5743::效果预览`：AM-Softmax与softmax的对比实验结果。
