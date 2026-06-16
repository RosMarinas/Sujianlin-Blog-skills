---
type: concept
title: DEIM
aliases:
- Discrete Empirical Interpolation Method
definition: DEIM 是一种基于 SVD 结果和贪心残差最大元素选择的行列选择方法，可用于 CUR 分解。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md
source_ids:
- '10662'
prerequisites:
- '[[奇异值分解]]'
- '[[CUR分解]]'
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods: []
series:
- '[[低秩近似之路]]'
evidence_spans:
- ev::10662::DEIM法
status: stable
updated: '2026-06-13'
---

# DEIM

## 核心定义

DEIM（Discrete Empirical Interpolation Method）是 CUR 分解中的行列选择方法。源文将它解释为从 SVD 后的 `V` 出发，利用奇异向量已按重要性排序的事实，把关键列选择转化为对 `V_{[:,:r]}` 的关键行搜索。

## 激活场景

它用于 CUR 分解需要选择原矩阵若干行列作为骨架时。CUR 的近似误差取决于公共子矩阵对应的行列式和补全效果，精确找最大行列式子矩阵是 NP-Hard，因此 DEIM 提供可执行的贪心替代。

## 贪心步骤

第一步选择 `V` 第一列绝对值最大的元素所在行。假设已经选出 `k` 个关键行 `S_k`，下一步计算第 `k+1` 列相对已选行列 CUR 近似的残差，再选择残差绝对值最大的元素所在行。由于已选行列能被该近似恢复，残差最大元素不会落在已选行中。

## 关键关系

DEIM 与杠杆分数都借助 SVD 结果，但杠杆分数用行模长平方排序，DEIM 则用贪心残差最大原则逐行选择。源文强调 DEIM 与 CUR 联系更紧密，适合用原始行列保留可解释性的低秩近似。

## 证据

- `Data/Spaces_ac_cn/markdown/Mathematics/2025-01-12-低秩近似之路-五-CUR.md`
- `ev::10662::DEIM法`
