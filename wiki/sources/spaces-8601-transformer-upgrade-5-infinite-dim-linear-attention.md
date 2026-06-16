---
type: article_summary
title: "Transformer升级之路：5、作为无限维的线性Attention"
article_id: "8601"
source_url: https://spaces.ac.cn/archives/8601
date: 2021-08-06
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
series: [Transformer升级之路]
topics: [线性Attention, 无限维]
concepts: [Linear Attention, Standard Attention, Random Projection, Taylor Expansion, Natural Exponential Definition]
methods: [Performer Random Projection, Taylor Expansion Method, Natural Exponential Definition Method]
evidence_spans:
  - "The paper argues that Standard Attention can be viewed as an infinite-dimensional linear attention, avoiding the low-rank bottleneck inherent in typical Linear Attention setups."
  - "The use of Taylor Expansion provides a polynomial kernel approximation with dimensions $d^n$."
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
source_ids:
  - "8601"
status: draft
updated: 2026-06-09
---

# Transformer升级之路：5、作为无限维的线性Attention

## 文章核心问题
标准Attention能否被视为无限维的线性Attention？除了Performer的随机投影方法，是否存在确定性的近似方案？为什么标准Attention在相同参数量下通常比线性Attention表现更好？

## 主要结论
- 标准Attention可以视为无限维的线性Attention，从而避免有限维线性Attention固有的低秩瓶颈。
- 除了Performer的随机投影方案，存在两种确定性方法：基于泰勒展开的多项式核函数，以及基于自然指数定义的方法。
- 这两种确定性方案由于维度呈指数级增长而不具实用性，但它们提供了更简明的理论解释。
- 该理论框架帮助理解Attention矩阵的秩的问题，以及标准Attention通常优于线性Attention的原因。

## 推导结构
从标准Attention的指数函数 $e^{\boldsymbol{q}\cdot\boldsymbol{k}}$ 出发，将其视为核函数，分别通过三种途径近似为有限维特征映射：Performer的随机投影（基于高斯分布积分）、泰勒展开的多项式核函数（$e^x = \sum_{m=0}^{\infty} x^m/m!$）、以及自然指数定义（$e^x = \lim_{n\to\infty}(1+x/n)^n$）。通过分析映射维度的差异，解释标准Attention（无限维）与线性Attention（有限维）之间的能力差距。

## 关键公式
- 标准Attention的核函数形式: $\text{sim}(\boldsymbol{q},\boldsymbol{k}) = e^{\boldsymbol{q}\cdot\boldsymbol{k}}$
- 泰勒展开: $e^{\boldsymbol{q}\cdot\boldsymbol{k}} = \sum_{m=0}^{\infty} \frac{(\boldsymbol{q}\cdot\boldsymbol{k})^m}{m!}$
- 自然指数定义: $e^{\boldsymbol{q}\cdot\boldsymbol{k}} = \lim_{n\to\infty} \left(1+\frac{\boldsymbol{q}\cdot\boldsymbol{k}}{n}\right)^n$
- Performer随机投影: $e^{\boldsymbol{q}\cdot\boldsymbol{k}} = \mathbb{E}_{\omega\sim\mathcal{N}(0,\boldsymbol{I}_d)}[\exp(\omega^{\top}\boldsymbol{q} - \|\boldsymbol{q}\|^2/2) \cdot \exp(\omega^{\top}\boldsymbol{k} - \|\boldsymbol{k}\|^2/2)]$

## 体现的方法
- Performer随机投影: 基于高斯分布的积分将 $e^{\boldsymbol{q}\cdot\boldsymbol{k}}$ 转化为特征向量内积的期望
- 泰勒展开方法: 利用 $e^{\boldsymbol{q}\cdot\boldsymbol{k}} = \sum_{m=0}^{\infty} \frac{(\boldsymbol{q}\cdot\boldsymbol{k})^m}{m!}$ 结合向量张量积（外积）得到确定性的高维近似表示
- 自然指数定义方法: 利用 $e^{\boldsymbol{q}\cdot\boldsymbol{k}} \approx \left(1+\frac{{\boldsymbol{q}\cdot\boldsymbol{k}}}{n}\right)^n$，通过对向量张量积求幂来实现向线性Attention的转换

## 所属系列位置
Transformer升级之路系列第5篇，从线性Attention切入无限维视角分析标准Attention。

## 与其他文章的关系
本文在第3篇线性Attention讨论的基础上，进一步从理论上将标准Attention解释为无限维的线性Attention，解释了标准Attention与线性Attention之间的根本差距。与第2篇的RoPE结合，为构建高效且表达能力强的Transformer变体提供了理论指导。

## 原文证据锚点
- 标准Attention可视为无限维线性Attention，避免低秩瓶颈
- 泰勒展开提供维度为 $d^n$ 的多项式核近似
- 确定性展开因 $O(d^n)$ 维度增长而不具实用性
