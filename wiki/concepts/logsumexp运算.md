---
type: concept
title: "logsumexp运算"
aliases:
  - "Log-Sum-Exp"
  - "LSE"
definition: "定义为logsumexp(x)=log∑e^{x_i}，是max的光滑近似，也是交叉熵运算的核心组件。满足凸性、Lipschitz连续（L=1）等优良性质。"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-05-10-logsumexp运算的几个不等式.md
source_ids:
  - "9070"
prerequisites:
  - "[[Softmax]]"
  - "[[凸函数]]"
equivalent_forms: []
related_formulas:
  - "[[logsumexp基本界]]"
evidence_spans:
  - "ev::9070::基本界"
  - "ev::9070::凸函数证明"
status: draft
updated: 2026-06-12
---

# logsumexp运算

## Definition

logsumexp是凸函数（H"older不等式证明），在无穷范数下Lipschitz常数为1。基本界：x_max < logsumexp(x) ≤ x_max + log n，近似误差与x无关仅与n有关。温度参数τ→0时τ·logsumexp(x/τ)→max。加权平均界：logsumexp(x) ≥ ∑p_i x_i - log∑p_i²。
