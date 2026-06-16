---
type: article_summary
title: 熵的形象来源与熵的妙用
article_id: "3638"
source_url: https://spaces.ac.cn/archives/3638
date: 2016-02-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2016-02-20-熵的形象来源与熵的妙用.md
series:
  - [[信息论工具]]
topics:
  - [[信息论基础]]
concepts:
  - [[信息熵]]
  - [[排序算法熵分析]]
methods:

evidence_spans:
  - ev::3638::熵的计数来源
  - ev::3638::排序算法效率的熵解释
  - ev::3638::洗牌次数的熵估计
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-02-20-熵的形象来源与熵的妙用.md
source_ids:
  - "3638"
status: draft
updated: 2026-06-10
---

# article-3638: 熵的形象来源与熵的妙用

## 文章核心问题
熵作为不确定性度量的直观来源是什么？如何用熵来理解排序算法效率和洗牌次数等具体问题？

## 主要结论
1. 熵的形象来源是计数取对数：$n$个元素组成长度为$m$的序列有$n^m$种可能，取对数得$m\log n$，满足可加性要求。
2. 排序算法的平均最高效率$\mathcal{O}(n\log n)$可用熵解释：$n$个数的排列熵为$\log(n!) \sim \mathcal{O}(n\log n)$，排序即熵从$\mathcal{O}(n\log n)$到0的过程。
3. 对切洗牌$\mathcal{O}(\log n)$次即可使牌洗乱：熵$\mathcal{O}(n\log n)$，每次操作改变$\mathcal{O}(n)$的熵。

## 推导结构
- 从0-9数字组成小于10000的自然数出发，说明计数$n^m$可作为不确定性度量，取对数得$m\log n$满足可加性
- 排序算法：$n$个数排列有$n!$种，熵$\log(n!) \sim \mathcal{O}(n\log n)$，每次对调操作改变一定量熵
- 洗牌：$n$张牌熵$\mathcal{O}(n\log n)$，对切法每次改变$\mathcal{O}(n)$熵，需$\mathcal{O}(\log n)$次

## 关键公式
- $m\log n = -\sum_{i=1}^{n^m} \frac{1}{n^m}\log \frac{1}{n^m}$
- $\log(n!) \sim \log\left[\sqrt{2\pi n}\left(\frac{n}{e}\right)^n\right] \sim \mathcal{O}(n\log n)$
