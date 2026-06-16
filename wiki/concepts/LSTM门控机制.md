---
type: concept
title: "LSTM门控机制"
aliases:
  - "LSTM Gating"
  - "LSTM梯度流"
  - "遗忘门"
definition: "LSTM通过遗忘门f_t、输入门i_t和输出门o_t控制信息流和梯度流，其中∂c_t/∂c_{t-1}≈f_t使梯度爆炸风险极低，f_t在0~1间由任务需求自适应决定。"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-11-13-也来谈谈RNN的梯度消失-爆炸问题.md
source_ids:
  - "7888"
prerequisites:
  - "[[RNN梯度消失]]"
  - "[[RNN]]"
equivalent_forms: []
related_methods:
  - "[[用门控机制控制梯度传播]]"
evidence_spans:
  - "ev::7888::LSTM梯度分析"
  - "ev::7888::GRU梯度分析"
status: draft
updated: 2026-06-12
---

# LSTM门控机制

## Definition

LSTM的梯度主导项为遗忘门f_t（0~1之间），次要项如c_{t-1}∂f_t/∂c_{t-1} = f_t(1-f_t)o_{t-1}(1-tanh²c_{t-1})c_{t-1}U_f受多个门乘积压缩，数量级更小。GRU梯度主导项为1-z_t，但次要项比LSTM少1个门，稳定性更差。改进建议：将r_t∘h_{t-1}放到最后处理以保持LSTM的梯度友好性。
