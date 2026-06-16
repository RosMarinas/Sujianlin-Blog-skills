---
type: example
title: 指数衰减因子法求Dirichlet积分
aliases: []
article_id: "1629"
article: article::1629
section: 例子2
claim: ∫₀^∞ sin x/x dx = π/2
notation_mapping:
  "x": 积分变量
  "a": 指数衰减因子参数
  "G(a)": 含参积分
steps:
  - "G(a)=∫₀^∞ e^{-ax} sin x/x dx"
  - "G'(a)=-∫₀^∞ e^{-ax} sin x dx = -1/(a²+1)"
  - "G(a)=-arctan(a)+C"
  - "G(∞)=0 ⇒ C=π/2"
  - "G(0)=π/2 ⇒ ∫₀^∞ sin x/x dx = π/2"
used_concepts:
  - 参数微分法
source_span: "ev::1629::例子2_sinx"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2012-06-23-费曼积分法-积分符号内取微分-3.md
source_ids:
  - "1629"
status: draft
updated: 2026-06-13
---

# 指数衰减因子法求Dirichlet积分

## 详细步骤

经典Dirichlet积分∫₀^∞ sin x/x dx = π/2的费曼积分法证明：引入指数衰减因子e^{-ax}构造G(a)=∫₀^∞ e^{-ax} sin x/x dx。求导得G'(a)=-1/(a²+1)，积分得G(a)=-arctan(a)+C，由G(∞)=0得C=π/2，取a=0得π/2。这一e^{-ax}因子法成为费曼积分法的标志性技巧，适用于∫f(x)/x型积分。
