---
type: series
title: CoSENT
aliases:
  - CoSENT系列
  - CoSENT Series
  - Cosine Sentence Series
article_ids:
  - "8847"
  - "8860"
  - "9341"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-06-CoSENT-一-比Sentence-BERT更有效的句向量方案.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-01-12-CoSENT-二-特征式匹配与交互式匹配有多大差距.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-11-09-CoSENT-三-作为交互式相似度的损失函数.md
source_ids:
  - "8847"
  - "8860"
  - "9341"
series_goal: 从有监督句向量检索目标出发，把句子相似度训练从分类层间接优化改写为直接优化余弦相似度排序，并进一步推广为交互式相似度模型的排序损失。
entry_roles:
  "8847": 提出 CoSENT 排序损失，直接优化句向量余弦相似度的相对顺序。
  "8860": 比较特征式匹配与交互式匹配的质量/延迟差异，明确 CoSENT 的工程边界。
  "9341": 将 CoSENT 从句向量余弦推广到任意交互式标量相似度函数。
key_concepts:
  - [[CoSENT]]
  - [[句向量]]
  - [[句向量与对比学习]]
key_methods:
  - [[CoSENT排序损失]]
reading_paths:
  - [[CoSENT阅读路径]]
status: draft
updated: 2026-06-14
---

# CoSENT

## 系列核心问题

CoSENT 系列回答的是：如果最终评测和检索都依赖余弦相似度排序，为什么还要先用分类层间接训练句向量？它把句向量学习从“分类后取特征”改写为“直接让正样本对的余弦高于负样本对”，因此更贴近 Spearman 排序相关这类评价目标。

## 文章顺序

1. [[spaces-8847-CoSENT-一-比Sentence-BERT更有效的句向量方案]] — CoSENT（一）：比Sentence-BERT更有效的句向量方案：提出排序损失，建立直接优化余弦相似度的主线。
2. [[spaces-8860-CoSENT-二-特征式匹配与交互式匹配有多大差距]] — CoSENT（二）：特征式匹配与交互式匹配有多大差距？：比较双塔特征式模型和交互式模型，说明 CoSENT 的速度/效果取舍。
3. [[spaces-9341-CoSENT-三-作为交互式相似度的损失函数]] — CoSENT（三）：作为交互式相似度的损失函数：把损失从 `cos(u, v)` 推广到任意 `f(i, j)`，连接交互式相似度模型。

## 认知网络位置

CoSENT 是 [[更别致的词向量模型]] 的句向量层 companion：更别致词向量把词共现统计压缩为几何内积，CoSENT 则把有监督句对标签压缩为几何排序约束。两者都让“相似度”不只停留在口号，而是落到可训练的内积/排序目标。

## 搜索入口

- 想查“为什么 CoSENT 比 Sentence-BERT 更直接”：从 8847 进入。
- 想查“双塔句向量和交互式匹配差多少”：从 8860 进入。
- 想查“CoSENT 能否作为通用排序损失”：从 9341 进入。
