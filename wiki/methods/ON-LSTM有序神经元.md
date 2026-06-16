---
type: method
title: "ON-LSTM有序神经元"
aliases:
  - "Ordered Neurons LSTM"
operation_types:
  primary: "Structure-expose by factorization"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-05-28-ON-LSTM-用有序神经元表达层次结构.md
source_ids:
  - "6621"
method_summary: "对LSTM神经元排序后分段更新，通过主遗忘门和主输入门预测层级边界，自动学习层次结构。"
typical_structure: |
  1. 预测d_f和d_i确定层级边界
  2. 分段更新c_t：低于d_f用当前输入，[d_f,d_i]区间融合，高于d_i保留历史
  3. 使用cumax实现分段软化
applicability: "语言模型，句法分析，层次结构建模"
tools:
  - cumax
  - 主遗忘门
  - 主输入门
  - 层级分段
related_methods: []
examples:
  - [[article::6621]]
status: draft
updated: 2026-06-13
---

## 适用问题

需要层次化序列建模的场景，如语言模型、句法分析、文本生成等。特别适用于希望模型无监督地学习到句子的层级结构（字→词→短语→句子）的任务。

## 核心变换

**输入**：标准LSTM更新方程
**输出**：分层更新的ON-LSTM方程，引入主遗忘门$\tilde{f}_t$和主输入门$\tilde{i}_t$

标准LSTM的细胞更新为$c_t = f_t \circ c_{t-1} + i_t \circ \hat{c}_t$。ON-LSTM将神经元排序后分段更新：
$$
c_t = \tilde{f}_t \circ c_{t-1} + \tilde{i}_t \circ \hat{c}_t + \omega_t \circ (f_t \circ c_{t-1} + i_t \circ \hat{c}_t)
$$
其中$\tilde{f}_t = \text{cumax}(\text{onehot}(d_f))$，$\tilde{i}_t = 1 - \text{cumax}(\text{onehot}(d_i))$，$\omega_t = \tilde{f}_t \circ \tilde{i}_t$表示交集区域。

## 典型步骤

1. **预测层级边界**：用两个子网络$F_1, F_2$分别预测主遗忘门$d_f$和主输入门$d_i$，表示历史信息和当前输入的层级
2. **生成分段门**：通过$\text{cumax}$函数（累积softmax）获得可微分的分段软门
3. **分区间更新**：
   - $d_f \leq d_i$：低段（$<d_f$）直接覆盖为输入，中段（$[d_f,d_i]$）LSTM融合，高段（$>d_i$）保留历史
   - $d_f > d_i$：低段覆盖为输入，中间空白，高段保留历史
4. **标准门计算**：遗忘门$f_t$、输入门$i_t$、输出门$o_t$与标准LSTM相同
5. **输出**：$h_t = o_t \circ \tanh(c_t)$

## 直觉

将LSTM神经元按位置排序，index小=低层级信息（字粒度），index大=高层级信息（句子粒度）。高层级信息需要跨更多时间步传播（跨度大），所以被分配在更靠近历史信息保留端的神经元；低层级信息在每一步都可能被新输入更新，所以分配在靠近输入端的神经元。

$\text{cumax}$函数的可微分性是关键创新：它让模型能输出离散层级边界的同时保持梯度可传播。训练完成后，通过分析$d_f$和$d_i$随序列位置的变化，可以析出句子的句法树结构。

## 边界

- 神经元的"有序性"要求网络设计支持位置编码，不能随意打乱权重
- $\text{cumax}$实现需注意数值稳定性（累积和可能导致较大数值）
- 当$d_f > d_i$时中间区域的置零操作可能导致信息损失
- ON-LSTM参数量比标准LSTM有所增加（需预测$d_f, d_i$的子网络）
- 层级结构的可解释性在简单句子上较好，复杂长句上可能模糊

## 例子

- 无监督句法分析：训练ON-LSTM语言模型后，通过$d_f$和$d_i$的变化可以解析出句子的成分句法树
- 语言模型perplexity：ON-LSTM在多项语言模型基准上优于标准LSTM
- ICLR 2019最佳论文之一，证明了在RNN中融入层级结构的价值

## 证据

- ev::6621::ON-LSTM分段更新机制：$d_f \leq d_i$时的三段式更新（直接覆盖 + LSTM融合 + 保留历史）
- ev::6621::cumax可微分分段：$\tilde{f}_t = \stackrel{\rightarrow}{\text{cs}}(1_{d_f})$，$\tilde{i}_t = \stackrel{\leftarrow}{\text{cs}}(1_{d_i})$实现软分段
- ev::6621::层级结构与神经元排序的对应：低index=低层信息（字），高index=高层信息（句子）
