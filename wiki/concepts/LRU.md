---
type: concept
title: LRU
aliases:
  - Linear Recurrent Unit
  - 线性循环单元
definition: |
  线性循环单元（Linear Recurrent Unit）是一种极简的线性RNN结构。它去掉了传统RNN中的非线性激活函数，从而能够利用矩阵对角化在复数域中实现element-wise的快速串行状态转移，并通过Prefix Sum并行前缀和算法在训练中实现 $O(\log L)$ 级别的序列并行计算，极大地提高了长序列的训练和推理效率。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# LRU

## Definition
线性循环单元（Linear Recurrent Unit）是一种极简的线性RNN结构。它去掉了传统RNN中的非线性激活函数，从而能够利用矩阵对角化在复数域中实现element-wise的快速串行状态转移，并通过Prefix Sum并行前缀和算法在训练中实现 $O(\log L)$ 级别的序列并行计算，极大地提高了长序列的训练和推理效率。

## Details
LRU的提出是为了解决传统非线性RNN（如LSTM、GRU）因无法并行训练而在面对超长序列时计算速度缓慢的弊端。
它的核心理念在于：
1. **线性循环**：移除递归状态转移中的非线性激活函数。
2. **复数域对角化**：将状态转移矩阵 $A$ 投影到复数特征空间进行对角化。标量递归形式为 $x_t = \lambda x_{t-1} + \gamma u_t$，其中状态转移系数 $\lambda = r e^{i\theta}$ 为复数。
3. **训练并行化**：由于其完全线性，传统的 $O(L)$ 串行递归可以通过 Prefix Sum 算法改写为 $O(\log L)$ 树状并行，可以在现代加速器上快速训练。
4. **性能表现**：在长程依赖测试集（LRA）上取得了优秀的表现。在语言模型（LM）对照实验中表现好于实数域的 SLRU 模型，但略逊于带有门控的实数模型 RWKV。