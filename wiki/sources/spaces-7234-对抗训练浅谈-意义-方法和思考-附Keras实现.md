---
type: article_summary
title: "对抗训练浅谈：意义、方法和思考（附Keras实现）"
article_id: "7234"
source_url: https://spaces.ac.cn/archives/7234
date: 2020-03-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-03-01-对抗训练浅谈-意义-方法和思考-附Keras实现.md
series: []
topics:
  - "[[优化与损失函数]]"
concepts:
  - "[[对抗训练]]"
  - "[[梯度惩罚]]"
  - "[[FGM对抗训练]]"
evidence_spans:
  - "ev::7234::MinMax公式"
  - "ev::7234::FGM推导"
  - "ev::7234::梯度惩罚等价性"
  - "ev::7234::几何图像"
  - "ev::7234::L约束"
  - "ev::7234::实验结果"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-03-01-对抗训练浅谈-意义-方法和思考-附Keras实现.md
source_ids:
  - "7234"
status: draft
updated: 2026-06-12
---

# 对抗训练浅谈：意义、方法和思考（附Keras实现）

## Summary

本文系统介绍了对抗训练的基本概念、FGM方法及其Keras实现，并论证了对抗训练与梯度惩罚的等价性，给出了"坑中坑"的几何直观理解。

## Key Claims

1. 对抗训练统一形式: min_θ E[max_{Δx∈Ω} L(x+Δx, y; θ)]
2. FGM对抗扰动: Δx = ε ∇_x L(x,y;θ) / ∥∇_x L(x,y;θ)∥
3. FGM对抗训练等价于在loss中加入梯度惩罚项 ½ε∥∇_x L∥²。
4. 梯度惩罚的几何意义：让样本位于"坑底"（梯度为零），从而对扰动最稳定。
5. 梯度惩罚也促使模型满足Lipschitz约束，增强对抗防御能力。
6. BERT+对抗训练在IFLYTEK和TNEWS任务上分别提升约2%和1%。

## Key Formulas

- 对抗训练目标: min_θ E[max_{Δx∈Ω} L(x+Δx, y; θ)]
- FGM扰动: Δx = ε ∇_x L / ∥∇_x L∥
- 等价梯度惩罚: ½ε∥∇_x L(x,y;θ)∥²

## Connections

本文的梯度惩罚与8796中讨论的输入梯度惩罚与参数梯度惩罚的关系直接相关。对抗训练的L约束视角与7469中梯度裁剪使用的L-smooth条件一脉相承。mixup正则化（5693）同为通过约束模型行为提升泛化性的方法。
