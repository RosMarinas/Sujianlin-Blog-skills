---
type: proposition
title: Mitchell近似误差上界
aliases:
  - Mitchell error bound
  - 1/9 error bound
statement: Mitchell近似将乘法转化为加法时，其相对误差不超过 $1/9$，在 $x_1 = x_2 = 0.5$ 时达到。
assumptions:
  - "$p = 2^{n_1}(1+x_1)$，$q = 2^{n_2}(1+x_2)$，其中 $x_1,x_2 \in [0,1)$"
  - "使用近似 $\log_2(1+x) \approx x$ 和 $2^{n+x} \approx 2^n(1+x)$"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-12-14-Mitchell近似-乘法变为加法-误差不超过1-9.md
source_ids:
  - "7991"
requires:
  - "formula::Mitchell近似对数公式"
proof_route: |
  分两种情况讨论：当 $x_1+x_2<1$ 时，近似比例为 $(1+x_1+x_2)/(1+x_1+x_2+x_1x_2)$；当 $x_1+x_2 \geq 1$ 时，比例为 $2(x_1+x_2)/(1+x_1+x_2+x_1x_2)$。两种比例在 $x_1=x_2=0.5$ 处取最小值 $8/9$，因此最大相对误差 $1-8/9=1/9$。
methods: []
limits: 只适用于正数的乘法近似。除法的误差略大，为 $12.5\%$。
examples:
  - "example::Mitchell近似计算实例"
evidence_spans: []
status: draft
updated: 2026-06-12
---

## 命题

Mitchell近似乘法转化为加法运算后，与精确乘法的相对误差不超过 $1/9 \approx 11.1\%$。

## 证明要点

将待乘的两个正数写成浮点形式 $p = 2^{n_1}(1+x_1)$，$q = 2^{n_2}(1+x_2)$，其中 $x_1, x_2 \in [0,1)$。利用近似 $\log_2(1+x) \approx x$ 和 $2^{y} \approx 2^{\lfloor y \rfloor}(1 + y - \lfloor y \rfloor)$，分 $x_1 + x_2 < 1$ 和 $x_1 + x_2 \geq 1$ 两种情况计算近似乘积与真实乘积的比值。两种情况均在 $x_1 = x_2 = 0.5$ 时取得最小值 $8/9$，因此最大相对误差为 $1 - 8/9 = 1/9$。该误差在硬件实现中有明确指导意义，确定了在何种精度要求下可安全使用此近似。
