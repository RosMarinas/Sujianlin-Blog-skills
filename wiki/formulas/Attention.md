---
type: formula
title: Attention
latex: Attention(\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}) = \text{softmax}\left(\frac{\boldsymbol{Q}\boldsymbol{K}^{\top}}{\sqrt{d_k}}\right)\boldsymbol{V}
symbol_meanings:
  Q: query向量序列
  K: key向量序列
  V: value向量序列
  d_k: 缩放因子（key的维度）
standard_notation: 标准Transformer Attention定义
conditions: Q、K、V维度匹配
derived_from: []
appears_in:
  - [[spaces-6933-...]]
evidence_spans: []
null_evidence_reason: 公式提取自源文章，暂未绑定证据跨度
sources: Data/Spaces_ac_cn/markdown/...
source_ids:
  - 5542
  - 5597
  - 6877
  - 6915
  - 6920
  - 6933
  - 7196
  - 7259
  - 7500
  - 7718
  - 7809
  - 7912
  - 8128
  - 8209
  - 8739
  - 9059
status: draft
updated: 2026-06-12
---
# Attention

## 概述

$$Attention(\boldsymbol{Q},\boldsymbol{K},\boldsymbol{V}) = \text{softmax}\left(\frac{\boldsymbol{Q}\boldsymbol{K}^{\top}}{\sqrt{d_k}}\right)\boldsymbol{V}$$

## 符号说明
{'Q': 'query向量序列', 'K': 'key向量序列', 'V': 'value向量序列', 'd_k': '缩放因子（key的维度）'}
