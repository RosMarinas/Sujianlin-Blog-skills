---

type: formula
title: 带遗忘门的线性Attention
aliases:
- RetNet-style Forget Gate
latex: oldsymbol{o}_t = oldsymbol{S}_t oldsymbol{q}_t, \quad oldsymbol{S}_t
  = \gamma oldsymbol{S}_{t-1} + oldsymbol{v}_t oldsymbol{k}_t^{	op}
symbol_meanings:
  oldsymbol{o}_t: t时刻输出
  oldsymbol{S}_t: t时刻的状态矩阵
  oldsymbol{q}_t: 查询向量
  oldsymbol{k}_t: 键向量
  oldsymbol{v}_t: 值向量
  \gamma: 遗忘/衰减因子
standard_notation:
  convention: gamma is the forget gate scalar. Follow RetNet convention.
conditions: gamma是衰减因子，也可推广为data-dependent形式gamma_t（如Mamba系列）。
derived_from: null
implies: null
appears_in:
- '[[线性注意力简史：从模仿、创新到反哺]]'
evidence_spans: []
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- '11033'
status: draft
updated: '2026-06-14'
---


# 带遗忘门的线性Attention


## 概述

（待补充）

## 公式本体

```tex
oldsymbol{o}_t = oldsymbol{S}_t oldsymbol{q}_t, \quad oldsymbol{S}_t = \gamma oldsymbol{S}_{t-1} + oldsymbol{v}_t oldsymbol{k}_t^{	op}
```

## 成立条件

gamma是衰减因子，也可推广为data-dependent形式gamma_t（如Mamba系列）。

## 详细说明

带遗忘门的线性 Attention 公式 $$oldsymbol{o}_t = oldsymbol{S}_t oldsymbol{q}_t, \quad oldsymbol{S}_t = \gamma oldsymbol{S}_{t-1} + oldsymbol{v}_t oldsymbol{k}_t^{	op}$$ 标志着大语言模型在解决传统线性注意力机制中历史信息累积模糊问题上的关键性架构创新。在早期的纯线性 Attention 中，状态矩阵 $oldsymbol{S}_t$ 采用无衰减的累加（cumsum），导致当序列过长时，每个 token 的记忆占比被过度稀释，分辨率急剧下降。RetNet 首次将具有递归特性的衰减因子 $\gamma \in (0,1)$（即遗忘门）引入到由外积形式 $oldsymbol{v}_t oldsymbol{k}_t^{	op}$ 更新的线性框架中，从而使模型展现出倾向于遗忘久远历史、保留近期记忆的“就近原则”（Recency Bias）。这一设计不仅高度契合自然语言模型的内在分布特性，还巧妙保持了 RNN 形式的线性特征，使得网络能够通过矩阵分块的并行化算法在 GPU 上高效训练，并被后续如 DeltaNet 和 Mamba 等模型广泛借鉴与推广。
