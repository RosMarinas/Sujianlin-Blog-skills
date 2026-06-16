---


type: method
operation_types:
  primary: Structure-expose by factorization
  secondary: []
title: 用预训练补充Transformer归纳偏置
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-08-预训练一下-Transformer的长序列成绩还能涨不少.md
source_ids:
  - 9787
method_summary: 将 Transformer 相对较弱的归纳偏置（缺乏显式的局域性和序列先验）通过预训练的参数初始化来补偿，从而拉平与其他强归纳偏置模型（如线性RNN）的差距。
typical_structure: |
  1. 选择给定的长序列训练集数据。
  2. 在该数据上对模型进行预训练（例如 MLM 或 GPT 任务）。
  3. 使用预训练后的权重作为初始权重，在目标长序列任务上进行微调与评测。
applicability: 长序列建模任务、Transformer 与 RNN 等模型进行架构对比与基准测试（如 Long Range Arena）。
evidence_spans:
  - ev::9787::文章指出，缺乏预训练是 Transformer 在 LRA 长序列基准上效果较差的主要原因，通过在相同训练集上进行 MLM 或 GPT 预训练补充归纳偏置，Transformer 成绩可得到极其明显的提升。
examples:
  - [[article::9787]]
status: stable
updated: 2026-06-13
---

# 用预训练补充Transformer归纳偏置

## 适用问题

长序列建模任务、Transformer 与 RNN 等模型进行架构对比与基准测试（如 Long Range Arena）。

## 核心变换

将 Transformer 相对较弱的归纳偏置（缺乏显式的局域性和序列先验）通过预训练的参数初始化来补偿，从而拉平与其他强归纳偏置模型（如线性RNN）的差距。

## 典型步骤

1. 选择给定的长序列训练集数据。
2. 在该数据上对模型进行预训练（例如 MLM 或 GPT 任务）。
3. 使用预训练后的权重作为初始权重，在目标长序列任务上进行微调与评测。

## 直觉

长序列数据往往不仅需要远程依赖，还需要局域特征，这正是线性RNN擅长的（具有很强的归纳偏置）。Transformer 是通用架构，归纳偏置弱（即便加了位置编码），如果从零训练很难自己学到这些先验。但在下游数据上先做一遍预训练，能让模型从数据中“学出”这些必要的先验偏置（Data-Driven Priors），从而大幅提升在长序列测试集上的成绩。

## 边界

预训练需要消耗额外的算力；并非改变架构本身，而是改变训练范式，因此仍会保留 Transformer 的平方复杂度（除非配合 Effective 变体使用）。

## 例子

在 LRA (Long Range Arena) 基准上，标准 Transformer 表现落后于 S4 等线性 RNN，但在训练集上先进行 MLM 预训练后，Transformer 成绩大幅飙升，甚至逼近 SOTA。

## 证据

- ev::9787::文章指出，缺乏预训练是 Transformer 在 LRA 长序列基准上效果较差的主要原因，通过在相同训练集上进行 MLM 或 GPT 预训练补充归纳偏置，Transformer 成绩可得到极其明显的提升。
