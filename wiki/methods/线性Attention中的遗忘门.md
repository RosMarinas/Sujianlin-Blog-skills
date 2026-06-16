---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: 线性Attention遗忘门方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-18-时空之章-将Attention视为平方复杂度的RNN.md
source_ids:
  - 10017
method_summary: 给线性Attention引入衰减因子gamma∈(0,1)，在RNN递归中实现遗忘机制。
typical_structure: |
  1. 将线性 Attention 写成等价的 RNN 递归更新形式 S_t = S_{t-1} + v_t k_t^T。
  2. 引入标量或向量参数 \gamma 作为遗忘因子，将更新公式修改为 S_t = \gamma \cdot S_{t-1} + v_t k_t^T。
  3. 在长序列前向传播时，根据具体模型结构将 \gamma 设置为常数、可训练参数对角矩阵或数据依赖的 \gamma_t。
applicability: 将 Transformer 中平方复杂度的标准 Attention 改造为具有线性复杂度且具备序列依赖衰减特性的结构。
evidence_spans:
  - ev::10017::文章介绍了在线性Attention的RNN表示 S_t = S_{t-1} + V_t K_t^T 中加入衰减因子（即遗忘门），这直接构成了RetNet等后续线性RNN模型的核心改进机制。
examples:
  - [[article::10017]]
status: stable
updated: 2026-06-13
---




# 线性Attention遗忘门方法

## 适用问题

将 Transformer 中平方复杂度的标准 Attention 改造为具有线性复杂度且具备序列依赖衰减特性的结构。

## 核心变换

给线性Attention的 RNN 递归更新公式中引入衰减因子 $\gamma \in (0,1)$，从而在隐藏状态中实现类似 RNN 的遗忘机制（Forget Gate）。

## 典型步骤

1. 将线性 Attention 写成等价的 RNN 递归更新形式 $S_t = S_{t-1} + v_t k_t^T$。
2. 引入标量或向量参数 $\gamma$ 作为遗忘因子，将更新公式修改为 $S_t = \gamma \cdot S_{t-1} + v_t k_t^T$。
3. 在长序列前向传播时，根据具体模型结构将 $\gamma$ 设置为常数（如 RetNet）、可训练参数对角矩阵、数据依赖的 $\gamma_t$（如 Mamba 系列）或复数形式（结合 RoPE）。

## 直觉

标准线性Attention的RNN视角中，$S_t$ 是对所有历史 $v_k k_k^T$ 的简单累加。这种无脑累加不仅容易数值爆炸，而且无法表达“近期信息更重要、远期信息该被遗忘”的局部归纳偏置。通过乘上一个小于1的衰减因子 $\gamma$，历史信息会随着时间指数级衰减，这就是一个最简单的遗忘门。

## 边界

引入数据依赖的 $\gamma_t$ 后，模型无法再像纯线性 Attention 那样轻易地写成全局的并行矩阵乘法，需要依赖硬件感知的并行扫描（Parallel Scan）算法或局部块状注意力（Chunk-wise Attention）来实现高效训练。

## 例子

在 RetNet 中，$\gamma$ 被取为一个固定的常数（如 0.99）；在 Mamba 中，衰减项被进一步推广为依赖于输入的 $\Delta t, A$，即相当于 data-dependent 的 $\gamma_t$。

## 证据

- ev::10017::文章介绍了在线性Attention的RNN表示 $S_t = S_{t-1} + V_t K_t^T$ 中加入衰减因子（即遗忘门），这直接构成了RetNet等后续线性RNN模型的核心改进机制。
