---
type: article_summary
title: CoSENT（三）：作为交互式相似度的损失函数
article_id: "9341"
source_url: https://spaces.ac.cn/archives/9341
date: 2022-11-09
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-11-09-CoSENT-三-作为交互式相似度的损失函数.md
series:
  - [[CoSENT]]
topics:
  - [[句向量与对比学习]]
concepts:
  - [[CoSENT]]
methods:

evidence_spans:
  - ev::9341::CoSENT通用化
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-11-09-CoSENT-三-作为交互式相似度的损失函数.md
source_ids:
  - "9341"
status: draft
updated: 2026-06-10
---
# CoSENT（三）：作为交互式相似度的损失函数

## 文章核心问题

CoSENT能否超越特征式句向量训练，应用于交互式相似度模型？与交叉熵相比孰优孰劣？

## 主要结论

CoSENT可用于交互式模型（将cos相似度替换为任意标量输出f(i,j)），效果与交叉熵基本持平。在较难的任务或较弱模型上，CoSENT可能略微优于交叉熵。

## 推导结构

1. CoSENT的通用形式：log(1 + ∑ e^{λ(f(neg)-f(pos))})
2. 实验对比：CE vs CoSENT on interact models

## 关键公式

通用CoSENT: log(1 + ∑_{sim(i,j)>sim(k,l)} e^{λ(f(k,l)-f(i,j))})

## 所属系列位置

CoSENT系列第三篇，探索CoSENT的通用性。

## 原文证据锚点

- ev::9341::CoSENT通用化 — CoSENT作为通用排序损失
