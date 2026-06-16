---
type: article_summary
title: Naive Bayes is all you need ?
article_id: 9648
source_url: https://spaces.ac.cn/archives/9648
date: 2023-06-08
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-06-08-Naive-Bayes-is-all-you-need.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-06-08-Naive-Bayes-is-all-you-need.md
source_ids:
  - 9648
status: draft
updated: 2026-06-12
---

# Naive Bayes is all you need ?

本文阐述了朴素贝叶斯与Attention机制之间的深刻关联，指出单层的Dot-Product Attention在做语言模型时，实质上可以被视为一种广义的、加权平均的、参数化的朴素贝叶斯模型。
作者通过贝叶斯公式将 $p(x_t|x_{<t})$ 展开，引入类似Word2Vec中Skip-Gram的“Embedding + 内积 + Softmax”形式来参数化二元转移概率 $\log p(x_t|x_j)$。
在将传统的等权Pooling推广到依赖于前一Token与历史Token关联的加权平均后，整理计算式可自然导出标准的点积注意力公式。
此外，作者还提出可以通过隐变量模型和狄拉克分布来理解多层Attention的堆叠，而残差连接可以理解为对2-gram语言模型强先验的保留。
这一视角为解释In-Context Learning为何有效以及探索长度外推提供了新颖的概率物理图景。