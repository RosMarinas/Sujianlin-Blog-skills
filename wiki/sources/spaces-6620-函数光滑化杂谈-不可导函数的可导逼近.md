---
type: article_summary
title: 函数光滑化杂谈：不可导函数的可导逼近
article_id: "6620"
source_url: https://spaces.ac.cn/archives/6620
date: 2019-05-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-05-20-函数光滑化杂谈-不可导函数的可导逼近.md
source_ids:
  - "6620"
status: stable
updated: 2026-06-12
---

## 概述

本文介绍了机器学习中将离散、不可导的评测指标或操作算子（如最大值、最大值位置等）进行光滑化（又称“软化”）的常见数学逼近技巧。文章详细推导了以下几个典型算子的可导逼近形式：
1. **最大值函数 $\max$**：利用极极限关系，引入常数 $K$ 后其光滑逼近为 $\text{logsumexp}$ 算子。
2. **one-hot最大值位置**：通过平移最大值尾数，推导出其光滑近似对应常用的 $\text{softmax}$ 变换。
3. **$\text{argmax}$ 指标**：利用序向量与 one-hot 向量的内积，结合 $\text{softmax}$ 构造出浮点数近似。
4. **分类正确率与 F1 评分**：利用类别 one-hot 向量的内积作为计数函数，通过概率分布替换 one-hot 向量得到其可导近似，作为微调损失函数。
5. **Top-k 元素位置（$\text{soft-}k\text{-max}$）**：通过递归方式构造多热向量的光滑近似，每次找出最大值后在下一步递归中乘上权重遮掩以扣除该分量。

## 关键数学公式

- $\max(x_1, \dots, x_n) \approx \log\left(\sum_{i=1}^n e^{x_i}\right) = \text{logsumexp}(\boldsymbol{x})$
- $\text{argmax}(\boldsymbol{x}) \approx \sum_{i=1}^n i \times \text{softmax}(\boldsymbol{x})_i$
- $\text{Positive F1} \approx \frac{2 \sum_{\boldsymbol{x}} t(\boldsymbol{x}) p(\boldsymbol{x})}{\sum_{\boldsymbol{x}} [t(\boldsymbol{x}) + p(\boldsymbol{x})]}$
