---
type: example
title: spaces-4675-simpler-GloVe损失
aliases: []
article_id: '4675'
article:
- - 更别致的词向量模型(四)：模型的求解
section: 损失函数
claim: 用平方损失拟合词向量内积与经验 PMI，并通过共现窗口估计概率。
notation_mapping:
  P_hat: tilde{P}
  v_i: boldsymbol{v}_i
  loss: loss
steps:
- 统计边缘概率和共现概率
- 写出经验 PMI
- 构造平方损失
- 用 Adagrad 更新词向量
used_concepts:
- - - 点互信息PMI
used_formulas:
- - - simpler GloVe损失公式
used_methods:
- - - 用互信息内积构造词向量几何
problem_pattern:
- - 把语言共现统计改写为向量几何问题
source_span: ev::4675::损失函数
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-四-模型的求解.md
source_ids:
- '4675'
status: stable
updated: '2026-06-12'
---

# spaces-4675-simpler-GloVe损失

## 所在文章

[[更别致的词向量模型(四)：模型的求解]]

## 原始问题

用平方损失拟合词向量内积与经验 PMI，并通过共现窗口估计概率。

## 推导步骤

1. 统计边缘概率和共现概率
2. 写出经验 PMI
3. 构造平方损失
4. 用 Adagrad 更新词向量

## 证据锚点

- `ev::4675::损失函数`