---
type: proposition
title: RoPE-Bias外推性
aliases:
  - RoPE-Bias Extrapolation Mechanism
statement: |
  通过在包含旋转位置编码的自注意力层中开启投影 Bias 项，投影偏置的内积在经过旋转矩阵变换后，在长距离下会自适应退化为随距离单调衰减的常数项，从而起到局部化注意力和改善长度外推性的效果。
assumptions:
  - Query和Key投影层保留可学习偏置项
  - 相对位置编码采用RoPE旋转矩阵形式
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
source_ids:
  - 9577
proof_route:
  - 写出带偏置的RoPE注意力内积表达式：$(\boldsymbol{q}_m + \boldsymbol{a})^{\top}\boldsymbol{\mathcal{R}}_{n-m}(\boldsymbol{k}_n + \boldsymbol{b})$。
  - 展开该式得到：$\boldsymbol{q}_m^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{k}_n + \boldsymbol{a}^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{k}_n + \boldsymbol{q}_m^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b} + \boldsymbol{a}^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b}$。
  - 利用随机高斯夹角分布理论，Query/Key的各向同性使得第二项和第三项的期望为零。
  - 第四项 $\boldsymbol{a}^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b}$ 与具体token无关，仅是相对距离 $m-n$ 的函数。在长文本外推训练中，该常数项自适应学到随距离增加而单调递减的规律，起到局部注意力掩码的作用，提高了外推的抗熵坍塌能力。
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# RoPE-Bias外推性

## Statement
通过在包含旋转位置编码的自注意力层中开启投影 Bias 项，投影偏置的内积在经过旋转矩阵变换后，在长距离下会自适应退化为随距离单调衰减的常数项，从而起到局部化注意力和改善长度外推性的效果。

## Assumptions
- Query和Key投影层保留可学习偏置项
- 相对位置编码采用RoPE旋转矩阵形式

## Proof Route
1. 写出带偏置的RoPE注意力内积表达式：$(\boldsymbol{q}_m + \boldsymbol{a})^{\top}\boldsymbol{\mathcal{R}}_{n-m}(\boldsymbol{k}_n + \boldsymbol{b})$。
2. 展开该式得到：$\boldsymbol{q}_m^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{k}_n + \boldsymbol{a}^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{k}_n + \boldsymbol{q}_m^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b} + \boldsymbol{a}^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b}$。
3. 利用随机高斯夹角分布理论，Query/Key的各向同性使得第二项和第三项的期望为零。
4. 第四项 $\boldsymbol{a}^{\top}\boldsymbol{\mathcal{R}}_{n-m}\boldsymbol{b}$ 与具体token无关，仅是相对距离 $m-n$ 的函数。在长文本外推训练中，该常数项自适应学到随距离增加而单调递减的规律，起到局部注意力掩码的作用，提高了外推的抗熵坍塌能力。