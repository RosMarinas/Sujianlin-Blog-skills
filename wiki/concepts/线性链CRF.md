---
type: concept
title: 线性链CRF
aliases: []
definition: 线性链CRF是CRF的一种简化形式，假设相邻位置的标签转移概率与输入x无关，由有限的状态转移矩阵参数化。P(y|x) ∝ exp(Σ h(y_t;x) + Σ g(y_t,y_{t+1}))，其中h由RNN/CNN编码，g为可训练矩阵。
standard_notation: h(y_t;x): 单标签打分函数; g(y_t,y_{t+1}): 转移打分; G_{ij}=e^{g_{ij}}
prerequisites: 条件随机场
sources: Data/Spaces_ac_cn/markdown/... (详见具体文章)
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
evidence_spans: []
null_evidence_reason: 概念提取自多篇文章，暂未绑定具体证据跨度
status: draft
updated: 2026-06-12
---

# 线性链CRF

线性链CRF是CRF的一种简化形式，假设相邻位置的标签转移概率与输入x无关，由有限的状态转移矩阵参数化。P(y|x) ∝ exp(Σ h(y_t;x) + Σ g(y_t,y_{t+1}))，其中h由RNN/CNN编码，g为可训练矩阵。

## 相关文章

本批次中涉及该概念的多篇文章请参见各文章摘要页面。

线性链CRF假设标签转移概率与输入x无关，由可训练的参数矩阵g(y_t,y_{t+1})建模。总打分函数f(y;x)=Σh(y_t;x)+Σg(y_t,y_{t+1})，其中h由RNN/CNN编码。归一化因子的递归计算可利用RNN封装实现，是Keras CRF实现的精妙之处。
