---
type: concept
title: HiPPO-LegS
aliases: []
definition: 使用 Scaled Legendre 映射记忆整个历史区间的 HiPPO 版本，其 A 为下三角矩阵。
prerequisites: []
equivalent_forms: []
direct_consequences:
- - - HiPPO-LegS矩阵公式
- - - LegS具有尺度等变和多项式衰减
related_formulas: []
related_methods: []
series:
- - - 重温SSM
evidence_spans:
- ev::10114::整个区间::legs_matrix
- ev::10137::尺度等变::legs
- ev::10137::长尾衰减::polynomial
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_ids:
- '10114'
- '10137'
- '10162'
status: stable
updated: '2026-06-12'
---
## 核心定义

使用 Scaled Legendre 映射记忆整个历史区间的 HiPPO 版本，其 A 为下三角矩阵。

## 典型出现位置

- `ev::10114::整个区间::legs_matrix`
- `ev::10137::尺度等变::legs`
- `ev::10137::长尾衰减::polynomial`

## 注意

本页只记录源文明确支持的数学关系，不把后续模型背景泛化为 stable 结论。