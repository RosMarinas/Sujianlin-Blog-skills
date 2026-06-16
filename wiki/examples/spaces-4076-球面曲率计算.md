---
type: example
title: 二维球面的外微分法曲率计算
aliases: []
article_id: "4076"
article: article::4076
section: 二维的例子：球面
claim: 球面ds²=dθ²+sin²θ dφ²的高斯曲率K=1
notation_mapping:
  "ω¹, ω²": 正交标架
  "ω²₁": 连接形式
  "ℛ²₁": 曲率形式
steps:
  - "取正交标架：ω¹=dθ, ω²=sinθ dφ"
  - "由第一结构方程解出 ω²₁=-cosθ dφ"
  - "代入第二结构方程：ℛ²₁ = d(-cosθ dφ) = sinθ dθ∧dφ"
  - "ℛ²₁ = R̂²₁₁₂·ω¹∧ω² = R̂²₁₁₂·sinθ dθ∧dφ"
  - "⇒ R̂²₁₁₂=1 ⇒ 高斯曲率K=R̂₁₂₁₂=1"
used_concepts:
  - 外微分计算
  - Cartan结构方程
source_span: "ev::4076::球面曲率"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-11-外微分浅谈-7-有力的计算.md
source_ids:
  - "4076"
status: draft
updated: 2026-06-13
---

# 二维球面的外微分法曲率计算

## 详细步骤

以二维球面ds²=dθ²+sin²θdφ²为例演示外微分计算曲率全流程。取正交标架ω¹=dθ, ω²=sinθdφ。由第一结构方程因度规为单位阵及反对称性解得ω²₁=-cosθdφ。代入第二结构方程得ℛ²₁=sinθ dθ∧dφ。展开得正交标架下R̂²₁₁₂=1，即高斯曲率K=1。该过程比坐标基方法大幅简化。

该例展示了外微分结构方程法相比传统坐标基方法在大幅简化计算方面的强大能力。