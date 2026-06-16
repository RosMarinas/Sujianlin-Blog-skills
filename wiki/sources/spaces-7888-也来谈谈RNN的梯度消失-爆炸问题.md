---
type: article_summary
title: "也来谈谈RNN的梯度消失/爆炸问题"
article_id: "7888"
source_url: https://spaces.ac.cn/archives/7888
date: 2020-11-13
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-11-13-也来谈谈RNN的梯度消失-爆炸问题.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[RNN梯度消失]]"
  - "[[RNN梯度爆炸]]"
  - "[[LSTM门控机制]]"
  - "[[GRU梯度分析]]"
evidence_spans:
  - "ev::7888::RNN梯度递归"
  - "ev::7888::梯度消失含义"
  - "ev::7888::SimpleRNN梯度分析"
  - "ev::7888::LSTM梯度分析"
  - "ev::7888::GRU梯度分析"
  - "ev::7888::改进GRU建议"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-13-也来谈谈RNN的梯度消失-爆炸问题.md
source_ids:
  - "7888"
status: draft
updated: 2026-06-12
---

# 也来谈谈RNN的梯度消失/爆炸问题

## Summary

本文从梯度递归公式出发，系统分析了SimpleRNN、LSTM和GRU的梯度流，指出RNN用tanh而非ReLU是因为tanh保证了梯度有界性，而LSTM通过遗忘门主导梯度流同时缓解了梯度消失和爆炸。

## Key Claims

1. RNN梯度以递归方式传播：dh_t/dθ = (∂h_t/∂h_{t-1})(dh_{t-1}/dθ) + ∂h_t/∂θ。
2. |∂h_t/∂h_{t-1}| < 1导致梯度消失，> 1导致梯度爆炸。
3. RNN用tanh而非ReLU是因为tanh使∂h_t/∂h_{t-1}有界，降低梯度爆炸风险。
4. LSTM的∂c_t/∂c_{t-1} ≈ f_t（遗忘门），f_t在0~1之间且自洽地由任务决定。
5. GRU的梯度比LSTM更不稳定，因为门控较少导致次要项更大。

## Key Formulas

- SimpleRNN梯度: ∂h_t/∂h_{t-1} = (1-h_t²)U
- LSTM梯度主导项: ∂c_t/∂c_{t-1} ≈ f_t
- LSTM次要项: c_{t-1}∂f_t/∂c_{t-1} = f_t(1-f_t)o_{t-1}(1-tanh²c_{t-1})c_{t-1}U_f (<0.45U_f)

## Connections

本文的梯度消失分析与7469的梯度裁剪直接相关——梯度裁剪是缓解梯度爆炸的实用方法。LSTM的梯度流分析展示了一种通过模型设计控制梯度传播的思路，与8747中Post Norm/LN对梯度的影响分析类似。
