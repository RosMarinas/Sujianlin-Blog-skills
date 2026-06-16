---
type: article_summary
title: 从JL引理看熵不变性Attention
article_id: "9588"
source_url: https://spaces.ac.cn/archives/9588
date: 2023-04-10
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2023-04-10-从JL引理看熵不变性Attention.md
series:
  - [[熵归一化与熵不变性]]
topics:
  - [[Transformer架构]]
  - [[信息论基础]]
concepts:
  - [[熵不变性]]
  - [[JL引理]]
  - [[注意力机制]]
methods:

evidence_spans:
  - ev::9588::熵不变性注意力机制形式
  - ev::9588::JL引理与注意力维度关系
  - ev::9588::JL引理解释熵不变性缩放
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-04-10-从JL引理看熵不变性Attention.md
source_ids:
  - "9588"
status: draft
updated: 2026-06-10
---

# article-9588: 从JL引理看熵不变性Attention

## 文章核心问题
熵不变性Attention中的$\log n$缩放因子与Johnson-Lindenstrauss引理中的$\log n$维度要求之间是否存在内在联系？

## 主要结论
1. JL引理表明编码$n$个向量只需$\mathcal{O}(\log n)$维空间，而熵不变性Attention的缩放因子也是$\log n$量级，二者存在深层关联。
2. 由JL引理，key_size最佳选择为$d_n = \lambda\log n$，但实际使用固定$d$（为训练长度512设计）。当$n\neq512$时，实际$d$项求和代替理想$d_n$项求和，需乘以补偿因子$d_n/d = \log_{512} n$。
3. 补偿因子$\log_{512}n$恰好等于熵不变性Attention引入的缩放因子，从而建立了JL引理与熵不变性Attention之间的联系。

## 推导结构
- 回顾熵不变性Attention形式：$softmax(\frac{\log_{512}n}{\sqrt{d}}QK^{\top})V$
- 回顾JL引理：嵌入$n$个向量只需$\mathcal{O}(\log n)$维空间，实际词向量维度$8\log n$与此一致
- 建立联系：key_size最佳选择$d_n = \lambda\log n$，固定$d = \lambda\log 512$
- 内积$\langle q,k\rangle = \sum_{i=1}^d q_i k_i$共$d$项求和，理想应为$d_n$项，故乘以$d_n/d = \log_{512} n$补偿
- 补偿后形式与熵不变性Attention完全一致

## 关键公式
- 熵不变性Attention：$Attention(Q,K,V) = softmax\left(\frac{\log_{512} n}{\sqrt{d}}QK^{\top}\right)V$
- JL引理维度估计：$d_n = \lambda\log n$，实际$d = \lambda\log 512$
- 补偿因子：$\frac{d_n}{d} = \frac{\log n}{\log 512} = \log_{512} n$
