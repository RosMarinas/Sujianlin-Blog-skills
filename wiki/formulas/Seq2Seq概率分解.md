---
type: formula
title: Seq2Seq概率分解
latex: p(\boldsymbol{y}|\boldsymbol{x}) = p(y_1|\boldsymbol{x})p(y_2|\boldsymbol{x},y_1)\dots p(y_n|\boldsymbol{x},y_1,\dots,y_{n-1})
symbol_meanings:
  y_t: 位置t的输出token
  x: 输入序列
  y_{<t}: 前面所有已生成token
standard_notation: 自回归条件分解
conditions: Teacher Forcing训练方式
derived_from: []
appears_in:
  - [[spaces-6877-...]]
  - [[spaces-7259-...]]
  - [[spaces-8128-...]]
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
# Seq2Seq概率分解

## 概述

$$p(\boldsymbol{y}|\boldsymbol{x}) = p(y_1|\boldsymbol{x})p(y_2|\boldsymbol{x},y_1)\dots p(y_n|\boldsymbol{x},y_1,\dots,y_{n-1})$$

## 符号说明
{'y_t': '位置t的输出token', 'x': '输入序列', 'y_{<t}': '前面所有已生成token'}
