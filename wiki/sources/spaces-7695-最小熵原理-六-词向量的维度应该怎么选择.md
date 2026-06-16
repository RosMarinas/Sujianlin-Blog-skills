---
type: article_summary
title: 最小熵原理（六）：词向量的维度应该怎么选择？
article_id: "7695"
source_url: https://spaces.ac.cn/archives/7695
date: 2020-08-20
category: Big-Data
source_markdown: Data/Spaces_ac_cm/markdown/Big-Data/2020-08-20-最小熵原理-六-词向量的维度应该怎么选择.md
series:
  - [[最小熵原理]]
topics:
  - [[最小熵原理]]
  - [[互信息词向量]]
concepts:
  - [[最小熵原理]]
  - [[互信息词向量]]
methods:
  - [[用互信息内积构造词向量几何]]
evidence_spans:
  - ev::7695::维度选择公式
  - ev::7695::熵阈值条件
  - ev::7695::拉普拉斯近似
sources:
  - Data/Spaces_ac_cm/markdown/Big-Data/2020-08-20-最小熵原理-六-词向量的维度应该怎么选择.md
source_ids:
  - "7695"
status: draft
updated: 2026-06-10
null_evidence_reason: "Sixth article on dimension selection; evidence spans to be formalized."
---

# 最小熵原理（六）：词向量的维度应该怎么选择？

## 文章核心问题

给定词表大小 $N$，词向量的维度 $n$ 应该取多大才能有效编码所有词语？

## 主要结论

词向量维度应满足 $n > 8.33\log N$（自然对数），简约版 $n > 8\log N$。对于 $N=100000$，$n\approx 96$ 即可；对于 $N=5000000$，$n\approx 128$。

推导基于最小熵原理：词向量模型的信息熵 $H$ 应不小于语言本身的熵 $\tilde{H}$，当 $H < 0$ 时（由于采样近似误差出现）说明维度已经"绰绰有余"。

## 推导结构

1. 假设词向量模型为 $p(w_i,w_j) = e^{\langle\boldsymbol{u}_i,\boldsymbol{v}_j\rangle}/Z$
2. Skip Gram模型的信息熵计算
3. 采样近似：将求和转化为期望
4. 分布假设：词向量均匀分布在半径为 $\sqrt{n}$ 的超球面上
5. 利用 $n$ 维空间随机向量夹角分布公式
6. 数值计算 $h_n$ 与 $n$ 的线性关系 $h_n/n \approx -0.24$
7. 令 $H\approx \log N^2 - 0.24n < 0$ 解出 $n > 8.33\log N$

## 关键公式

$$
n > 8.33\log N \quad\text{或简约版}\quad n > 8\log N
$$

其中 $h_n/n \approx -0.24$ 的解析解为 $\frac12\log\frac{\sqrt{5}+1}{2}$。

## 体现的方法

- [[用互信息内积构造词向量几何]] — 文章6使用该方法的Skip Gram模型进行维度分析
- 新贡献：用熵阈值确定词向量维度的下限

## 所属系列位置

系列第六篇，第五个具体应用——词向量维度选择。

## 与其他文章的关系

- 基于[[最小熵原理（四）]]的Word2Vec/Skip Gram模型框架
- 与[[更别致的词向量模型]]系列相关的维度分析
- 与[[用稳定性指标约束优化器缩放]]构成互补：前者从训练稳定性定维度，本文从容量需求定维度

## 原文证据锚点

- `ev::7695::维度选择公式` — $n > 8.33\log N$ 的推导
- `ev::7695::熵阈值条件` — 以 $H < 0$ 作为维度充分的判据
- `ev::7695::拉普拉斯近似` — 用拉普拉斯近似求 $h_n$ 的渐近值
