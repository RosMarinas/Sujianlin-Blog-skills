---
type: formula
title: CRF归一化因子递推
latex: \boldsymbol{Z}_{t+1} = \boldsymbol{Z}_t \boldsymbol{G} \otimes H(y_{t+1}|\boldsymbol{x})
symbol_meanings:
  Z_t: 到时刻t的归一化因子向量
  G: 指数化转移矩阵（G_{ij}=e^{g_{ij}}）
  H(y_{t+1}|x): 位置t+1各标签打分的指数向量
  ⊗: 逐位对应相乘
standard_notation: 递归计算将指数级复杂度降为线性
conditions: 马尔可夫假设；标签转移矩阵与位置无关
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
# CRF归一化因子递推

## 概述

$$\boldsymbol{Z}_{t+1} = \boldsymbol{Z}_t \boldsymbol{G} \otimes H(y_{t+1}|\boldsymbol{x})$$

## 符号说明
{'Z_t': '到时刻t的归一化因子向量', 'G': '指数化转移矩阵（G_{ij}=e^{g_{ij}}）', 'H(y_{t+1}|x)': '位置t+1各标签打分的指数向量', '⊗': '逐位对应相乘'}
