---
type: article_summary
title: 函数光滑化杂谈：不可导函数的可导逼近
article_id: "6620"
source_url: https://spaces.ac.cn/archives/6620
date: 2019-05-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
series: []
topics:
  - 函数逼近论
  - 深度学习理论
concepts:
  - logsumexp
  - softmax
  - 光滑近似
methods: []
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
source_ids:
  - "6620"
status: draft
updated: 2026-06-10
---

## 总结

本文系统讨论不可导操作（max, argmax, onehot, 正确率等）的光滑可导近似方法。核心途径是用softmax近似onehot向量，进而构造各种离散指标的光滑版本。文中还递归构造了 soft-k-max。

## 关键思想

- $\max$ 的光滑近似是 $\text{logsumexp}(x_1,\dots,x_n)=\log\sum e^{x_i}$ 而非 softmax
- $\text{softmax}$ 是 $\text{onehot}(\text{argmax}(\boldsymbol{x}))$ 的光滑近似
- $\text{argmax}$ 的光滑近似是 $\sum i\times\text{softmax}(\boldsymbol{x})_i$
- 正确率光滑近似：用预测概率分布代替 onehot 向量计算内积
- soft-k-max：递归减去最大值后反复应用 softmax

## 所属系列

[[函数逼近论]] — [[深度学习理论]]
