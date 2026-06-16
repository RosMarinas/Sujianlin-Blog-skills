---
type: example
title: 二次求导构造ODE求∫cos x/(a²+x²) dx
aliases: []
article_id: "1946"
article: article::1946
section: 特例的计算
claim: ∫_{-∞}^{+∞} cos x/(a²+x²) dx = πe^{-a}/a
notation_mapping:
  "F(a)": 含参积分
  "a": 参数
steps:
  - "令F(a)=∫_{-∞}^{+∞} cos(ax)/(1+x²) dx"
  - "两次求导得 F''(a)=F(a)-∫cos(ax)dx"
  - "利用∫cos(ax)dx=0（欧拉数学结果）得 F''(a)=F(a)"
  - "通解 F(a)=C₁e^a+C₂e^{-a}"
  - "F(0)=π, F(∞)=0 ⇒ C₁=0, C₂=π"
  - "F(a)=πe^{-a} ⇒ 原积分=πe^{-a}/a"
used_concepts:
  - 参数微分法
  - 欧拉数学
source_span: "ev::1946::解微分方程"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-03-27-费曼积分法-7-欧拉数学的综合.md
source_ids:
  - "1946"
status: draft
updated: 2026-06-13
---

# 二次求导构造ODE求∫cos x/(a²+x²) dx

## 详细步骤

求解∫ cos x/(a²+x²) dx的关键：令F(a)=∫ cos(ax)/(1+x²) dx。两次求导得F''(a)=F(a)-∫cos(ax)dx。利用前文推导的∫cos(ax)dx=0（欧拉数学结果），得到ODE F''(a)=F(a)。通解F(a)=C₁e^a+C₂e^{-a}，由F(0)=π, F(∞)=0得F(a)=πe^{-a}，最终原积分=πe^{-a}/a。
