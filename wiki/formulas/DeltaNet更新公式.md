---
type: formula
title: DeltaNet更新公式
aliases:
- Delta Rule for Linear Attention
latex: \boldsymbol{S}_t = \boldsymbol{S}_{t-1} - (\boldsymbol{S}_{t-1}\boldsymbol{k}_t
  - \boldsymbol{v}_t)\boldsymbol{k}_t^{\top} = \boldsymbol{S}_{t-1}(\boldsymbol{I}
  - \boldsymbol{k}_t\boldsymbol{k}_t^{\top}) + \boldsymbol{v}_t\boldsymbol{k}_t^{\top}
symbol_meanings:
  I: 单位矩阵
  S: 状态矩阵
  \boldsymbol{I}: boldsymbol{I}
  \boldsymbol{S}: 状态矩阵
  \boldsymbol{k}: boldsymbol{k} 参数
  \boldsymbol{v}: boldsymbol{v} 参数
  k: 第 k 个分量 / Top-k 数量
  t: 时间步 / 自变量
  v: 值向量 / 参数
standard_notation:
  convention: Follow original DeltaNet convention. The formula implements 'remove
    old knowledge, add new knowledge' logic.
conditions: 可加学习率eta_t，吸收到k_t,v_t中。eta_t总是可以吸收到k_t,v_t的定义中。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- '10017'
status: draft
updated: "2026-06-14"
appears_in:
- '10017'
---

# DeltaNet更新公式


## 概述

（待补充）

## 公式

DeltaNet的更新公式：S_t = S_{t-1} - (S_{t-1}k_t - v_t)k_t^T = S_{t-1}(I - k_tk_t^T) + v_tk_t^T

"先减后加"：先移除模型对k_t的旧认知(S_{t-1}k_t)k_t^T，再补充新认知v_tk_t^T。这是1960年代Widrow-Hoff算法（Delta Rule）在序列建模中的应用。