---

type: formula
title: 线性Attention递归公式
aliases:
- Linear Attention RNN Form
latex: \boldsymbol{o}_t = \boldsymbol{S}_t \boldsymbol{q}_t, \quad \boldsymbol{S}_t
  = \boldsymbol{S}_{t-1} + \boldsymbol{v}_t \boldsymbol{k}_t^{\top}
symbol_meanings:
  \boldsymbol{S}_t: 隐含状态的线性循环神经网络（RNN）
standard_notation:
  convention: Use QKV convention with column vectors q,k,v in R^{d x 1}. S_t is a
    d x d state matrix.
conditions: 适用于Causal线性Attention。序列长度线性O(nd^2)。
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
updated: "2026-06-14"
---

# 线性Attention递归公式


## 概述

（待补充）

## 公式本体

```tex
\boldsymbol{o}_t = \boldsymbol{S}_t \boldsymbol{q}_t, \quad \boldsymbol{S}_t = \boldsymbol{S}_{t-1} + \boldsymbol{v}_t \boldsymbol{k}_t^{\top}
```

## 成立条件

适用于Causal线性Attention。序列长度线性O(nd^2)。

## 详细说明

线性Attention递归公式 $$\boldsymbol{o}_t = \boldsymbol{S}_t \boldsymbol{q}_t, \quad \boldsymbol{S}_t = \boldsymbol{S}_{t-1} + \boldsymbol{v}_t \boldsymbol{k}_t^{\top}$$ 是将传统的 Softmax Attention 移除指数归一化并转化为因果（Causal）自回归模式的核心理论基础。通过提取键值对的外积（$\boldsymbol{v}_t \boldsymbol{k}_t^{\top}$）并进行累加（cumsum），该公式构建了一个以 $\boldsymbol{S}_t$ 为隐含状态的线性循环神经网络（RNN）。这种将序列维度的二次时间复杂度转化为常数级别状态更新的架构，使得计算和内存需求关于序列长度 $n$ 呈现 $\mathcal{O}(nd^2)$ 的线性关系。尽管去除了 Softmax 的非线性能力，且纯累加可能引发历史信息的过度稀释与分辨率下降，但这套递归范式依然为后续具有并行前缀和（Prefix Sum）计算加速的复杂线性 RNN 变体（如 RetNet 与 DeltaNet 等架构）奠定了基石。
