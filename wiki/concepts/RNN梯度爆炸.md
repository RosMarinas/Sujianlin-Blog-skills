---
type: concept
title: "RNN梯度爆炸"
aliases:
  - "Exploding Gradient in RNN"
definition: "RNN中当|∂h_t/∂h_{t-1}| > 1时梯度随步数指数增长，导致训练不稳定甚至NaN。tanh激活函数通过使∂h_t/∂h_{t-1}有界来缓解，但根本缓解依赖梯度裁剪。"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-13-也来谈谈RNN的梯度消失-爆炸问题.md
source_ids:
  - "7888"
prerequisites:
  - "[[RNN]]"
equivalent_forms:
  - "[[梯度裁剪]]"
evidence_spans:
  - "ev::7888::SimpleRNN梯度分析"
status: draft
updated: 2026-06-12
---

# RNN梯度爆炸

## Definition

SimpleRNN中 ∂h_t/∂h_{t-1} = (1-h_t²)U。tanh使该值有界，但未能完全消除爆炸风险。处理梯度爆炸的最根本方法是参数裁剪或梯度裁剪。使用ReLU激活时 ∂h_t/∂h_{t-1}=U 无界，爆炸风险更高，因此RNN倾向用tanh。配合良好初始化和裁剪方案，ReLU版RNN也可训练但拟合能力可能下降。梯度裁剪是在(L0,L1)-smooth条件下的最优学习率策略。
