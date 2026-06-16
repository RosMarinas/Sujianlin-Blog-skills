---
type: example
title: spaces-4671-PMI内积词向量模型
aliases: []
article_id: '4671'
article:
- - 更别致的词向量模型(三)：描述相关的模型
section: 模型的形式
claim: 把词对点互信息作为词向量内积，得到可解释的词向量几何模型。
notation_mapping:
  v_i: boldsymbol{v}_i
  P_ij: P(w_i,w_j)
  PMI: log P(w_i,w_j)/(P(w_i)P(w_j))
steps:
- 从互信息可加性出发
- 将词关系写成几何内积
- 把模型目标写成 PMI 内积形式
- 保留类比和相似度解释
used_concepts:
- - - 互信息词向量
- - - 点互信息PMI
used_formulas:
- - - PMI内积词向量公式
used_methods:
- - - 用互信息内积构造词向量几何
problem_pattern:
- - 把语言共现统计改写为向量几何问题
source_span: ev::4671::模型形式
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-三-描述相关的模型.md
source_ids:
- '4671'
status: stable
updated: '2026-06-13'
---

# spaces-4671-PMI内积词向量模型

## 问题

源文要把“机场-飞机+火车=火车站”这类词向量可加性，解释成词与上下文共现相关度的代数关系。文章先把词对与任意上下文词 `w` 的相关度写成概率比值，再用朴素假设把复合词关系拆成若干单词关系。

## 推导步骤

1. 从类比关系推出式(11)中的共现概率比值乘法关系。
2. 假设相关度可由词向量内积的函数 `f(<v_i,v_w>)` 表示，得到式(12)。
3. 为保持向量加减对应到相关度乘除，要求 `f(x+y-z)=f(x)f(y)/f(z)`；在连续性条件下通解为指数形式。
4. 将指数形式代回，得到 `PMI(w_i,w_j)=<v_i,v_j>`，即词对点互信息由词向量内积建模。

## 使用的概念与公式

该例使用点互信息 PMI、互信息词向量和 PMI 内积词向量公式。它体现的方法是把语言共现统计改写为向量几何：PMI 矩阵在形式上类似被词向量做内积分解。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-三-描述相关的模型.md`
- `ev::4671::模型形式`
