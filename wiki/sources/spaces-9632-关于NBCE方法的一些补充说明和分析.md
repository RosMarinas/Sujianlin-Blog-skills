---
type: article_summary
title: 关于NBCE方法的一些补充说明和分析
article_id: 9632
source_url: https://spaces.ac.cn/archives/9632
date: 2023-05-31
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-05-31-关于NBCE方法的一些补充说明和分析.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-31-关于NBCE方法的一些补充说明和分析.md
source_ids:
  - 9632
status: draft
updated: 2026-06-12
---

# 关于NBCE方法的一些补充说明和分析

本文是针对NBCE上下文扩展方法的补充分析与改版更新。
作者首先分析了为什么标准的平均Pooling在NBCE中随着上下文数量 $n$ 增大会导致完全乱码：因为语言模型的训练目标是One-Hot，导致分布的尾部预测（低概率词）不可靠，而公式中的负项 $-eta\log p(T)$ 会在平均 Pooling 弱化头部后放大不可信的尾部词。
解决方案是对每个上下文分布在计算前进行 Top-P 或 Top-K 截断，并将 $\log p(T) = -\infty$ 处的未定义运算（$-\infty - (-\infty)$）定义为直接取 Pooling 分布。
为了解决回答观点型问题时由于 argmin 抖动导致生成文本在不同上下文间反复跳转而产生幻觉的问题，引入了转移惩罚参数 $\eta > 0$，只有当前上下文的熵显著小于上一步上下文时才发生跳转。
最后，作者分析了NBCE的适用场景，说明其本质是使用LLM的熵作为相似度进行每步动态检索，不限制上下文之间的重叠性（可通过滑窗分割长文本），但在处理需要严格顺序的上下文或强耦合上下文时表现较差。