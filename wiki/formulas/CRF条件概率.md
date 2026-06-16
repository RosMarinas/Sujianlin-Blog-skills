---
type: formula
title: CRF条件概率
latex: P(y_1,\dots,y_n|\boldsymbol{x}) = \frac{1}{Z(\boldsymbol{x})} \exp\left(h(y_1;\boldsymbol{x}) + \sum_{t=1}^{n-1} [g(y_t,y_{t+1}) + h(y_{t+1};\boldsymbol{x})]\right)
symbol_meanings:
  y_t: 位置t的标签
  x: 输入序列
  Z(x): 归一化因子（配分函数）
  h(y_t;x): 单标签打分函数（来自RNN/CNN编码）
  g(y_t,y_{t+1}): 相邻标签转移分数
standard_notation: G_{ij}=e^{g_{ij}}为指数化转移矩阵; Z为配分函数
conditions: 马尔可夫假设（仅相邻标签关联）；标签转移与输入x无关
derived_from: []
appears_in:
  - [[spaces-5542-...]]
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
# CRF条件概率

## 概述

$$P(y_1,\dots,y_n|\boldsymbol{x}) = \frac{1}{Z(\boldsymbol{x})} \exp\left(h(y_1;\boldsymbol{x}) + \sum_{t=1}^{n-1} [g(y_t,y_{t+1}) + h(y_{t+1};\boldsymbol{x})]\right)$$

## 符号说明
{'y_t': '位置t的标签', 'x': '输入序列', 'Z(x)': '归一化因子（配分函数）', 'h(y_t;x)': '单标签打分函数（来自RNN/CNN编码）', 'g(y_t,y_{t+1})': '相邻标签转移分数'}
