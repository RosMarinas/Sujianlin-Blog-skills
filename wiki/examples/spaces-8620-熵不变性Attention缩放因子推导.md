---
type: example
title: 熵不变性Attention缩放因子推导实例
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
source_ids:
- '8620'
evidence_spans:
- ev::8620::推导过程
notation_mapping:
  （待从源文章提取）: （待从源文章提取）
article_id: '8620'
article: '[[（待从源文章提取）]]'
section: （待从源文章提取）
claim: （待从源文章提取）
steps:
- （待从源文章提取）
used_concepts:
- '[[（待从源文章提取）]]'
source_span: （待从源文章提取）
---

## 问题

从熵不变性推导Attention缩放因子lambda。

## 推导步骤

1. 注意力分布: a_{i,j} = exp(lambda * q_i·k_j) / ∑exp(lambda * q_i·k_j)
2. 熵: H_i = -∑a_{i,j} log a_{i,j}
3. 代入并近似: H_i ≈ log n + log E[e^{lambda d cos theta}] - lambda d * ...
4. 拉普拉斯近似: H_i ≈ log n - 0.24*lambda*d + O(1)
5. 为抵消n的影响: log n - 0.24*lambda*d = 0
6. 所以: lambda = log n / (0.24*d)
7. 引入超参数kappa: lambda = kappa*log(n)/d
8. 匹配n=512: kappa = sqrt(d)/log(512)
9. 最终: lambda = log_512(n)/sqrt(d)