---
type: article_summary
title: n个正态随机数的最大值的渐近估计
article_id: 11390
source_url: "https://spaces.ac.cn/archives/11390"
date: 2025-11-06
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-11-06-n个正态随机数的最大值的渐近估计.md
series: []
topics:
  - [[概率与统计]]
concepts:
  - [[正态随机变量最大值]]
methods:
  - [[拉普拉斯近似]]
  - [[Jensen不等式放缩]]
evidence_spans:
  - ev::11390::先看结论
  - ev::11390::快速上界
  - ev::11390::拉普拉斯
  - ev::11390::逆变采样
  - ev::11390::应用例子
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-11-06-n个正态随机数的最大值的渐近估计.md
source_ids:
  - 11390
status: draft
updated: 2026-06-11
---

# n个正态随机数的最大值的渐近估计

## 文章核心问题

如何渐近估计n个独立标准正态随机数最大值的数学期望，并应用于低精度BF16下Attention logits重复最大值概率的分析。

## 主要结论

- **先看结论**: n个独立标准正态随机变量的最大值的期望渐近估计为sqrt(2 log n)或更精细的sqrt(2 log (n/sqrt(2pi)))。
- **快速上界**: 利用Jensen不等式和exp的凸性，可以简单证明标准正态最大值期望的渐近上界为sqrt(2 log n)。
- **拉普拉斯**: 最大值的累积分布函数为[Phi(z)]^n，其概率密度可通过拉普拉斯近似（正态逼近）在峰值处展开得到期望。
- **逆变采样**: 通过逆累积分布函数采样最大值的平均值为n/(n+1)，利用erfc渐近形式可求得相同渐近估计。
- **应用例子**: 由于BF16低精度，同一行Attention Logits中出现两个相同最大值的概率可通过极值期望和精度范围来估计。

