---
type: concept
title: BERT-of-Theseus
definition: "一种基于模块随机替换的BERT模型压缩方法，通过在训练阶段随机用轻量层代替原始层来实现平滑压缩。"
sources:
  - wiki/sources/spaces-7575-BERT-of-Theseus.md
source_ids:
  - "7575"
aliases: [Theseus压缩, 忒修斯之船压缩, Progressive Module Replacing]
tags: [model-compression, bert, knowledge-distillation, module-replacing]
related_concepts: [模型压缩, 知识蒸馏]
related_sources: [spaces-7575-BERT-of-Theseus]
status: draft
updated: 2026-06-12
---
## Definition

BERT-of-Theseus是一种基于模块替换的BERT模型压缩方法（Xu et al., 2020）。命名源于"忒修斯之船"思想实验：如果将船的木头逐渐替换，直到所有木头都不是原来的，船还是原来的船吗？

## Core Idea

直接用Successor（小模型）的模块替换Predecessor（大模型）的对应模块进行训练，仅使用下游任务loss。相比蒸馏需匹配中间层输出、Attention矩阵等多重loss，Thisseus方法极为简洁。

## Algorithm

Predecessor（6层BERT）被分为3个模块，对应Successor（3层BERT）的3层：
1. 固定Predecessor权重
2. 以0.5概率随机用Successor层替换Predecessor对应模块
3. 仅用下游任务loss训练Successor层
4. 训练充分后分离Successor单独微调

数学形式（类似Dropout）：
$$
\begin{aligned}
&\varepsilon^{(l)} \sim U(\{0,1\}) \\
&x^{(l)} = x_p^{(l)} \times \varepsilon^{(l)} + x_s^{(l)} \times (1 - \varepsilon^{(l)}) \\
&x_p^{(l+1)} = F_p^{(l+1)}(x^{(l)}) \\
&x_s^{(l+1)} = F_s^{(l+1)}(x^{(l)})
\end{aligned}
$$

## Advantages over Distillation

1. **简洁**：仅需下游任务loss，无需平衡多重loss
2. **直接作用于微调**：无需预训练阶段干预

## Limitations

同模型压缩（Successor与Predecessor结构相同）时，Thisseus的Successor性能不优于Predecessor，不能完全取代蒸馏。

## References

- 苏剑林. "BERT-of-Theseus：基于模块替换的模型压缩方法". 科学空间, 2020. [spaces-7575]
- Xu et al., "BERT-of-Theseus: Compressing BERT by Progressive Module Replacing", 2020.
