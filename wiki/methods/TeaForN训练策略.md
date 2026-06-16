---
type: method
title: "TeaForN训练策略"
aliases:
  - "Teacher-Forcing with N-grams"
operation_types:
  primary: "Construct auxiliary sequence"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-10-27-TeaForN-让Teacher-Forcing更有-远见-一些.md
source_ids:
  - "7818"
method_summary: "通过嵌套迭代让模型在训练时提前预估后N个token，介于Teacher Forcing和Student Forcing之间。"
typical_structure: |
  1. 用M处理Embedding得到h^{(1)}
  2. 用[h^{(1)}_{<L}]替代Embedding再次输入M
  3. 迭代N次得到h^{(N)}
  4. 各步交叉熵加权求和
applicability: "Seq2Seq文本生成，缓解Exposure Bias"
tools:
  - 嵌套迭代
  - 共享权重M
  - Teacher Forcing
related_methods: []
examples:
  - [[article::7818]]
status: draft
updated: 2026-06-13
---

## 适用问题

Seq2Seq文本生成中的Exposure Bias问题。标准Teacher Forcing训练时每步使用真实token，但推理时使用预测token，这种训练-推理不一致导致误差累积。

## 核心变换

**输入**：Decoder Embedding序列 $[e_0, e_1, \ldots, e_{L-1}]$
**输出**：N次迭代的隐藏状态序列，每次迭代都计算交叉熵损失

$$
\begin{aligned}
[h_1^{(1)}, \ldots, h_L^{(1)}] &= M([e_0, e_1, \ldots, e_{L-1}]) \\
[h_1^{(2)}, \ldots, h_L^{(2)}] &= M([e_0, h_1^{(1)}, \ldots, h_{L-1}^{(1)}]) \\
&\vdots \\
[h_1^{(N)}, \ldots, h_L^{(N)}] &= M([e_0, h_1^{(N-1)}, \ldots, h_{L-1}^{(N-1)}])
\end{aligned}
$$

各步损失加权求和：$\text{loss} = -\sum_{t=1}^L \sum_{i=1}^N \lambda_i \log p_t^{(i)}[w_t]$

## 典型步骤

1. **计算第一次迭代**：$h^{(1)} = M(E(w))$，使用真实Embedding（标准Teacher Forcing）
2. **迭代计算**：将上一轮的$h^{(i)}$作为下一轮的输入$h^{(i+1)} = M([e_0, h_1^{(i)}, \ldots, h_{L-1}^{(i)}])$
3. **多步损失**：每次迭代的$h_t^{(i)}$都计算交叉熵$\log p_t^{(i)}[w_t]$并加权求和
4. **推理**：训练完成后只使用$h^{(1)}$进行标准解码（Beam Search等），不需要额外步骤

## 直觉

Teacher Forcing只要求$h_t$预测当前$y_t$，缺乏"远见"。TeaForN让$h_t$通过嵌套迭代同时预测后续多个token（$y_{t+1}, y_{t+2}, \ldots$），迫使每个隐藏状态携带更长期的信息。迭代中共享权重$M$，第$i$次迭代实际上是"用模型自己的输出替代真实token"，但每次迭代的序列仍然并行计算（与Student Forcing的串行不同）。

## 边界

- 嵌套迭代N次，$N$一般取2-3即可，过大收益递减且计算量增加
- 各迭代的权重$\lambda_i$需调节（通常$\lambda_1$最大，后续递减）
- 训练完成后无需增加推理成本（只用$h^{(1)}$解码）
- 与Student Forcing的关键区别：TeaForN的训练批次内仍可并行（所有迭代在批次维度并行），而Student Forcing需串行
- 缓解但未完全解决Exposure Bias

## 例子

- 文本生成任务：TeaForN使模型在解码时减少重复生成和安全回复
- 与Teacher Forcing的对比：TeaForN训练时模型需同时预测第$t$步和后$N-1$步，迫使隐向量携带长期依赖信息
- 参数$M$在所有迭代中共享，不增加参数总量

## 证据

- ev::7818::TeaForN嵌套迭代公式：$h^{(1)} = M(E(w))$，$h^{(i+1)} = M([e_0, h^{(i)}_{<L}])$，多次迭代后加权求和loss
- ev::7818::与Teacher/Student Forcing的对比：TeaForN介于两者之间，增加远见且保持并行性
- ev::7818::训练/推理流程：训练用多步损失，推理只用$h^{(1)}$解码
