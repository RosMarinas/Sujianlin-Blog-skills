---
type: example
title: spaces-4677-词向量模长ICF解释
aliases: []
article_id: '4677'
article:
- - 更别致的词向量模型(五)：有趣的结果
section: 模长的含义
claim: 在同词共现近似下，词向量模长平方与 -log P(w) 同阶，从而表达词重要性。
notation_mapping:
  v_w: boldsymbol{v}_w
  P_w: P(w)
steps:
- 近似 P(w,w) 与 P(w) 同阶
- 代入 PMI 内积模型
- 得到 ||v_w||^2 与 -log P(w) 同阶
- 解释高频虚词模长较小
used_concepts:
- - - 词向量模长ICF解释
used_formulas:
- - - 词向量模长ICF公式
used_methods:
- - - 用互信息内积构造词向量几何
problem_pattern:
- - 把语言共现统计改写为向量几何问题
source_span: ev::4677::模长的含义
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-11-19-更别致的词向量模型-五-有趣的结果.md
source_ids:
- '4677'
status: stable
updated: '2026-06-12'
---

# spaces-4677-词向量模长ICF解释

## 所在文章

[[更别致的词向量模型(五)：有趣的结果]]

## 原始问题

在同词共现近似下，词向量模长平方与 -log P(w) 同阶，从而表达词重要性。

## 推导步骤

1. 近似 P(w,w) 与 P(w) 同阶
2. 代入 PMI 内积模型
3. 得到 ||v_w||^2 与 -log P(w) 同阶
4. 解释高频虚词模长较小

## 证据锚点

- `ev::4677::模长的含义`