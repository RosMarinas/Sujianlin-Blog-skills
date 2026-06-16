---
type: concept
title: "RNN梯度消失"
aliases:
  - "Vanishing Gradient in RNN"
  - "RNN梯度弥散"
definition: "RNN中当|∂h_t/∂h_{t-1}| < 1时，历史梯度随步数指数衰减，导致距离当前时间步越长的反馈信号越弱，模型无法捕捉长距离依赖。"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-13-也来谈谈RNN的梯度消失-爆炸问题.md
source_ids:
  - "7888"
prerequisites:
  - "[[RNN]]"
  - "[[梯度]]"
equivalent_forms: []
related_methods:
  - "[[用门控机制控制梯度传播]]"
evidence_spans:
  - "ev::7888::梯度消失含义"
  - "ev::7888::SimpleRNN梯度分析"
status: draft
updated: 2026-06-12
---

# RNN梯度消失

## Definition

RNN梯度也是递归的：dh_t/dθ = (∂h_t/∂h_{t-1})(dh_{t-1}/dθ) + ∂h_t/∂θ。展开后远端梯度项前面是t-1项的连乘 ∏(∂h_i/∂h_{i-1})。梯度消失不意味着总梯度为0，而是远端历史信息对梯度的贡献被衰减到可忽略。SimpleRNN中 ∂h_t/∂h_{t-1} = (1-h_t²)U，U的大小和h_t的饱和度共同决定梯度行为。
