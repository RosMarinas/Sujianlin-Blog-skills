---
type: example
title: spaces-4233-Word2Vec矩阵视角
aliases: []
article_id: '4233'
article:
- - SVD分解(三)：连Word2Vec都只不过是个SVD？
section: Word2Vec=SVD？
claim: Word2Vec/CBOW 在结构上可与词袋线性层、自编码器和 SVD 放入同一矩阵视角比较。
notation_mapping:
  N: 词表大小
  n: 低维词向量维度
steps:
- 把 one-hot 和 embedding 看成全连接层
- 把词向量求和看成词袋模型线性等价
- 比较 CBOW 与线性自编码器/SVD 的结构
- 保留 softmax 和预测目标的差异
used_concepts:
- - - 线性自编码器-SVD等价
used_formulas:
- - - 线性自编码器矩阵分解公式
used_methods:
- - - 用矩阵分解重写表示学习结构
problem_pattern:
- - 把表示学习模型改写为矩阵分解问题
source_span: ev::4233::Word2VecSVD
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-02-23-SVD分解-三-连Word2Vec都只不过是个SVD.md
source_ids:
- '4233'
status: stable
updated: '2026-06-12'
---

# spaces-4233-Word2Vec矩阵视角

## 所在文章

[[SVD分解(三)：连Word2Vec都只不过是个SVD？]]

## 推导步骤

1. 把 one-hot 和 embedding 看成全连接层
2. 把词向量求和看成词袋模型线性等价
3. 比较 CBOW 与线性自编码器/SVD 的结构
4. 保留 softmax 和预测目标的差异

## 证据

- `ev::4233::Word2VecSVD`