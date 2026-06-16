---
type: concept
title: 点互信息PMI
aliases: []
definition: 点互信息衡量词对共现概率相对独立共现概率的对数偏离，是 simpler GloVe 拟合的核心目标。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-二-对语言进行建模.md
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-四-模型的求解.md
source_ids:
- '4669'
- '4675'
related_methods:
- - - 用互信息内积构造词向量几何
evidence_spans:
- ev::4669::从条件概率到互信息
- ev::4675::损失函数
status: draft
updated: '2026-06-12'
---

# 点互信息PMI

## 定义

点互信息衡量词对共现概率相对独立共现概率的对数偏离，是 simpler GloVe 拟合的核心目标。

## 激活场景

源文用 PMI 替代条件概率来描述词与上下文的关系。条件概率 $P(w_2|w_1)$ 不对称且需要归一化，而 PMI 来自
$$
\frac{P(w_1,w_2)}{P(w_1)P(w_2)}
$$
的对数，直接比较真实共现与随机相遇的倍数；大于 0 表示倾向共同出现，小于 0 表示低于独立假设。

## 关键关系

PMI 是互信息词向量的目标量。源文第三篇把相关度建模为词向量内积的函数，并推导出 $\text{PMI}(w_i,w_j)=\langle \boldsymbol{v}_i,\boldsymbol{v}_j\rangle$；第四篇则用经验概率 $\tilde{P}$ 构造平方损失
$$
\sum_{w_i,w_j}\left(\langle \boldsymbol{v}_i,\boldsymbol{v}_j\rangle-\log\frac{\tilde{P}(w_i,w_j)}{\tilde{P}(w_i)\tilde{P}(w_j)}\right)^2.
$$
因此 PMI 同时是统计语义解释和训练目标。

## 相关方法

- [[用互信息内积构造词向量几何]]

## 证据

- `ev::4669::从条件概率到互信息`
- `ev::4675::损失函数`
