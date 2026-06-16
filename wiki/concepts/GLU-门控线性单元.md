---
title: GLU（门控线性单元）
type: concept
aliases: [Gated Linear Unit, 门控线性单元, GLU激活函数]
tags: [activation-function, gating-mechanism, deep-learning]
related_methods: [GLU激活函数]
related_sources: [spaces-4611-基于fine-tune的图像分类, spaces-4647-浅谈神经网络中激活函数的设计]
sources: [4611, 4647]
source_ids: ["4611", "4647"]
status: draft
updated: 2026-06-13
definition: "GLU（门控线性单元）是一种通过sigmoid门控制信息流动的激活函数，使用两组独立参数分别做线性变换和门控。"
---

## Definition

GLU（Gated Linear Unit）是一种门控激活函数，通过sigmoid门控制信息流动。将输入分别经过线性变换和sigmoid门控，然后逐元素相乘。

## 数学形式

$\text{GLU}(\boldsymbol{x}) = (\boldsymbol{W}_1\boldsymbol{x} + \boldsymbol{b}_1) \otimes \sigma(\boldsymbol{W}_2\boldsymbol{x} + \boldsymbol{b}_2)$

其中$\sigma(\boldsymbol{W}_2\boldsymbol{x} + \boldsymbol{b}_2)$称为"门"（Gate）。

## 与Swish的关系

Swish激活函数$\text{swish}(x) = x \cdot \sigma(x)$可以看作是两组参数取相同的GLU特例。GLU使用两组独立的参数分别控制内容和门控，而Swish使用同一个输入作为内容和门控。
