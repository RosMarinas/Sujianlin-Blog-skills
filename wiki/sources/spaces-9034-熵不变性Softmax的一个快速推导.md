---
type: article_summary
title: 熵不变性Softmax的一个快速推导
article_id: "9034"
source_url: https://spaces.ac.cn/archives/9034
date: 2022-04-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2022-04-11-熵不变性Softmax的一个快速推导.md
series:
  - [[熵归一化与熵不变性]]
topics:
  - [[Transformer架构]]
  - [[信息论基础]]
concepts:
  - [[熵不变性]]
  - [[Softmax]]
  - [[注意力机制]]
methods:

evidence_spans:
  - ev::9034::熵不变性缩放因子推导
  - ev::9034::Softmax熵近似公式
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-04-11-熵不变性Softmax的一个快速推导.md
source_ids:
  - "9034"
status: draft
updated: 2026-06-10
---

# article-9034: 熵不变性Softmax的一个快速推导

## 文章核心问题
为之前提出的具有熵不变性质的注意力机制 $Attention(Q,K,V) = softmax(\kappa \log n / d \cdot QK^{\top})V$ 提供一个简洁明快的推导，避免原推导中繁琐的假设和步骤。

## 主要结论
1. 熵不变性要求缩放因子 $\lambda \propto \log n / d$，其中 $n$ 是序列长度，$d$ 是注意力向量维度。
2. 熵的近似表达式为 $H \approx \log n - \lambda(s_{\max} - \bar{s})$，其中 $\bar{s}$ 是 logits 均值，$s_{\max}$ 是最大值。
3. 若要使注意力分布的熵与序列长度 $n$ 解耦（即熵不变），必须令 $\lambda$ 与 $\log n$ 成正比，同时考虑 $QK^{\top} \propto d$，综合得到 $\lambda \propto \log n / d$。

## 推导结构
- 设定带缩放因子 $\lambda$ 的 Softmax：$p_i = e^{\lambda s_i} / \sum_{j=1}^n e^{\lambda s_j}$
- 写出熵的表达式：$H = \log\sum_i e^{\lambda s_i} - \lambda \sum_i p_i s_i$
- 拆分为 $H = \log n + \log( \frac{1}{n}\sum_i e^{\lambda s_i}) - \lambda \sum_i p_i s_i$
- 用平均场近似：$\log \frac{1}{n}\sum_i e^{\lambda s_i} \approx \lambda \bar{s}$
- 用 $\max$ 近似 Softmax 加权和：$\lambda \sum_i p_i s_i \approx \lambda s_{\max}$
- 得到 $H \approx \log n - \lambda(s_{\max} - \bar{s})$，进而推出 $\lambda \propto \log n$，结合注意力得分尺度 $\propto d$，最终得 $\lambda \propto \log n / d$

## 关键公式
- 带缩放因子的 Softmax：$p_i = e^{\lambda s_i} / \sum_{j=1}^n e^{\lambda s_j}$
- 熵的近似展开：$H = \log n + \log \frac{1}{n}\sum_i e^{\lambda s_i} - \lambda \sum_i p_i s_i$
- 平均场近似：$\log \frac{1}{n}\sum_i e^{\lambda s_i} \approx \lambda \bar{s}$
- Softmax 的 max 近似：$\lambda \sum_i p_i s_i \approx \lambda s_{\max}$
- 最终熵近似：$H \approx \log n - \lambda(s_{\max} - \bar{s})$
- 熵不变缩放因子：$\lambda \propto \log n / d$
