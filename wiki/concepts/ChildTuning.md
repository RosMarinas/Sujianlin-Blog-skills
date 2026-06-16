---
type: concept
title: ChildTuning
aliases:
- 梯度Dropout
- Gradient Dropout
definition: 在finetune时对梯度应用Dropout（随机保留p比例梯度分量）或基于Fisher信息选择重要参数子集更新，以降低过拟合风险的方法。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-11-22-ChildTuning-试试把Dropout加到梯度上去.md
source_ids:
- '8764'
prerequisites:
- '[[Dropout]]'
- '[[Adam优化器]]'
equivalent_forms: []
related_formulas: []
related_methods: []
evidence_spans:
- ev::8764::ChildTuning-D
- ev::8764::ChildTuning-F
- ev::8764::个人理解
status: draft
updated: '2026-06-12'
---

# ChildTuning

## Definition

两种变体：
- **ChildTuning-D**（Task-Dependent）：计算每个参数的Fisher信息F_i = (1/n)∑(∂log p(y|x;θ)/∂θ_i)²，选择top-p%参数，其余梯度置零（g←g⊗M/p）。
- **ChildTuning-F**（Task-Free）：每步随机构建保留比例p的0/1矩阵M，g←g⊗M/p。
在Adam下梯度Dropout等价于学习率乘以√p。