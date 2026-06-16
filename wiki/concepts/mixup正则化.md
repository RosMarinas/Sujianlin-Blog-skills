---
type: concept
title: "mixup正则化"
aliases:
  - "mixup augmentation"
  - "mixup正则"
definition: "通过要求模型对混合输入εx_a+(1-ε)x_b输出混合标签εy_a+(1-ε)y_b，迫使模型接近线性函数的正则化方法。"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-07-07-从SamplePairing到mixup-神奇的正则项.md
source_ids:
  - "5693"
prerequisites:
  - "[[数据扩增]]"
equivalent_forms: []
related_formulas: []
related_methods:
  - "[[用数据混合实现线性正则化]]"
evidence_spans:
  - "ev::5693::函数方程推导"
status: draft
updated: 2026-06-12
---

# mixup正则化

## Definition

mixup对输入和标签同时做凸组合：输入为 εx_a + (1-ε)x_b，标签为 εy_a + (1-ε)y_b。这一要求等价于函数方程 εf(x_a) + (1-ε)f(x_b) = f(εx_a + (1-ε)x_b)，其唯一解是线性函数，因此mixup本质上是在所有效果相近的模型中选择最接近线性函数的那一个。它与SamplePairing的区别在于混合系数ε是随机的而非固定的1/2，从而更加"柔和"。
