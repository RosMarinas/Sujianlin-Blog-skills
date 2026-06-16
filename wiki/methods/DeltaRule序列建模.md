---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Delta Rule序列建模方法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-18-时空之章-将Attention视为平方复杂度的RNN.md
source_ids:
  - 11033
method_summary: 基于在线学习和TTT（测试时训练）视角，使用梯度下降优化平方误差损失来构建序列模型的隐藏状态更新规则，实现“除旧迎新”的精准记忆。
typical_structure: |
  1. 将序列模型记忆视作一个在线线性回归/神经网络训练问题。
  2. 设定平方误差损失函数 L = 1/2 ||S_t k_t - v_t||^2。
  3. 根据当前状态计算预测值和目标值的残差：u_t = v_t - S_{t-1} k_t。
  4. 利用梯度下降法更新状态矩阵（即引入 Delta Rule）：S_t = S_{t-1} + u_t k_t^T。
  5. 展开为并行化的分块矩阵算法（利用逆矩阵 (I+B)^-1）以实现硬件加速计算。
applicability: 适用于构建具有恒定空间复杂度且能够精确追踪/更新关键信息的长序列线性注意力（Linear Attention）或RNN模型，解决传统滑动平均机制导致的记忆模糊问题。
examples:
  - [[article::11033]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::11033::从TTT（测试时训练）在线学习的视角来看，DeltaNet将损失函数定义为平方损失，通过梯度下降实现更新，先移除对k_t的旧认知再补充新认知，称为Delta Rule
---

## 适用问题

设计复杂度为 $\mathcal{O}(N)$ 的线性 Attention 或非线性 RNN 结构时，需要克服简单累加（如标准线性Attention）带来的状态叠加模糊、容量稀释问题，使得模型能够精准记住和遗忘特定 Token 信息。

## 核心变换

将传统的“直接把 Value 累加进隐状态矩阵”的记忆存储机制，重写为“在给定 Key 上的预测值与当前 Value 之间计算差值，并将残差通过外积更新回隐状态矩阵”的梯度下降过程。

## 典型步骤

1. **设定目标**：将序列状态 $S$ 作为可学习参数，把每个时刻输入的 $(k_t, v_t)$ 当作训练数据。
2. **预测旧认知**：在时刻 $t$，首先使用过去的隐状态 $S_{t-1}$ 和当前的键 $k_t$ 进行预测，得到当前模型对该键的理解：$S_{t-1} k_t$。
3. **计算残差**：计算真实要存入的值 $v_t$ 和预测值之间的差：$u_t = v_t - S_{t-1} k_t$。
4. **梯度更新**：执行类似梯度下降的操作，更新模型隐状态：$S_t = S_{t-1} + u_t k_t^T$。
5. **推理输出**：在给定 query $q_t$ 时，输出 $o_t = S_t q_t$。
6. **并行化加速（训练期）**：通过展开递推公式，转化为解含带状低秩成分的逆矩阵方程求解，实现 GPU 高效的分块矩阵乘法加速。

## 直觉

想象你有一个记事本（状态矩阵 S），当接收到新知识 $(k, v)$ 时，如果你不假思索全写进去，很快记事本就会塞满并产生大量重叠。Delta Rule 相当于你先看看记事本里关于 $k$ 已经记了啥，如果跟 $v$ 差不多，就不怎么写了；如果相反或者有新信息，你就先把旧的错误信息划掉（减去预测值），再填上新的。这就是“除旧迎新”，一种具备纠错和覆写能力的在线学习。

## 边界

1. 若在算法展开求逆矩阵 $(\mathbf{I} + \mathbf{B})^{-1}$ 的步骤未能良好设计并行算法，计算将退化为不能充分利用 GPU 的逐个步骤迭代，或者退化为复杂度大于 $\mathcal{O}(N^2)$ 的暴力求逆。
2. 由于涉及减法操作和递归乘法，若不结合额外的 L2 Normalize 或层归一化操作，可能会导致数值稳定性较弱或容易发散。

## 例子

在 DeltaNet 中，原始的线性注意力更新 $S_t = S_{t-1} + v_t k_t^T$ 被替换为 $S_t = S_{t-1} + (v_t - S_{t-1} k_t)k_t^T$。此外，还有变体如 Gated DeltaNet 会在每一步叠加一个门控衰减因子 $\gamma_t S_{t-1}$。

## 证据

- ev::11033::“DeltaNet的区别是在加$v_t k_t^T$前多减了个$(S_{t-1} k_t)k_t^T$...直观来想，先减后加就是先移除模型对$k_t$的旧认知，然后根据$(k_t,v_t)$补充新认知...这个规则称为 Delta Rule”
