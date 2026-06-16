---
type: example
title: 微分方程法求∫₀^∞ exp(-x²-a²/x²) dx
aliases: []
article_id: "1629"
article: article::1629
section: 例子3
claim: ∫₀^∞ exp(-x²-a²/x²) dx = √π/2·e^{-2a}
notation_mapping:
  "G(a)": 含参积分
  "a": 参数
steps:
  - "G(a)=∫₀^∞ e^{-x²-a²/x²} dx"
  - "求导后变量代换得 G'(a)=-2G(a)"
  - "解ODE: G(a)=Ce^{-2a}"
  - "G(0)=√π/2 ⇒ C=√π/2"
used_concepts:
  - 参数微分法
  - 微分方程法
source_span: "ev::1629::例子3_exp"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
source_ids:
  - "1629"
status: draft
updated: 2026-06-13
---

# 微分方程法求∫₀^∞ exp(-x²-a²/x²) dx

## 详细步骤

该积分的解法巧妙之处在于不直接积分出G(a)的表达式，而是通过求导发现G(a)满足一阶ODE G'(a)=-2G(a)，从而轻松解出G(a)=Ce^{-2a}。常数由G(0)=∫₀^∞ e^{-x²}dx=√π/2确定。此方法体现了参数微分法中微分方程思想的核心威力：发现微分关系有时比直接积分更有效。

该例完美展示了参数微分法与微分方程法的结合。