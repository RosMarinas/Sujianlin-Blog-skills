---
type: method
title: LRU并行化递归算法
aliases:
  - Parallel Scan for Linear RNNs
operation_types:
  primary: Rewrite / identity transform
  secondary:
    - Decompose / reduce dimension
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
method_summary: |
  将线性RNN的 $\mathcal{O}(L)$ 串行序列迭代问题，利用分治法重写为自下而上的树状并行前缀和（Prefix Sum）计算，将状态序列生成的时间复杂度降低为 $\mathcal{O}(\log L)$。
typical_structure: |
  1. 将长度为 $L$ 的输入序列等分为两半，并在两个计算核心上并行执行本级的状态迭代
  2. 计算并保留前半段序列的最后一个隐藏状态值 $x_{mid}$
  3. 将 $x_{mid}$ 乘以对应的转移矩阵幂次，并作为偏置加权叠加到后半段序列的各个对应位置上
  4. 递归地将此分治策略展开到最底层，最终构成一棵 $\mathcal{O}(\log L)$ 层的并行计算树，并使用 CUDA 核函数实现高效的并行归约
applicability: 在线性RNN模型训练中序列长度较大、直接自回归式串行迭代导致计算设备利用率低且耗时长的情况下使用。
tools:
  - 并行前缀和
  - 分治递归
  - CUDA 并行归约
related_methods:
  - [[LRU参数化与初始化]]
  - [[非线性RNN摄动并行化]]
  - [[用RNN解ODE并估计参数法]]
examples:
  - [[article::9554]]
status: draft
updated: 2026-06-14
---

## 适用问题

线性 RNN（如 LRU）的核心计算是串行递归 $x_t = \lambda x_{t-1} + u_t$。当序列长度 $L$ 很大时（如 8192 tokens），串行迭代无法利用 GPU 的并行计算能力，训练速度受限于序列长度。并行前缀和算法通过分治策略将 $\mathcal{O}(L)$ 复杂度降为 $\mathcal{O}(\log L)$。

## 核心变换

**输入**：输入序列 $\{u_1, \dots, u_L\}$，转移系数 $\lambda$，缩放系数 $\gamma$
**输出**：隐藏状态序列 $\{x_1, \dots, x_L\}$
**核心**：将串行递归重写为可并行计算的二叉树

线性递归：
$$
x_t = \gamma u_t + \lambda x_{t-1}
$$

展开形式（前缀和）：
$$
x_t = \sum_{i=1}^t \lambda^{t-i} \gamma u_i
$$

分治策略：将序列等分为 $[1, m]$ 和 $[m+1, L]$。

前半段并行计算 $x_1, \dots, x_m$，并保留 $x_m$。后半段的计算依赖 $x_m$：
$$
x_{m + k} = \lambda^k x_m + \sum_{i=m+1}^{m+k} \lambda^{m+k-i} \gamma u_i
$$

其中前半部分 $\lambda^k x_m$ 只需一次标量乘法，后半部分的求和与前半段结构相同，可继续分治递归。

## 典型步骤

1. **序列分割**：将长度为 $L$ 的序列等分为两半
2. **并行计算前半段**：递归地计算前半段的状态序列
3. **传递边界**：将前半段最后一个状态 $x_m$ 传递到后半段
4. **后半段修正**：将 $x_m$ 乘以 $\lambda^k$ 叠加到后半段各位置
5. **递归完成**：递归展开到最底层，构建 $\mathcal{O}(\log L)$ 层的计算树

## 直觉

核心思想：**将递归展开为可并行计算的树**。

串行递归 $x_t = f(x_{t-1}, u_t)$ 就像一条链条——每一项都依赖于前一项，无法并行。但线性递归有一个关键性质：**叠加性**。$x_t = Au_t + A^2 u_{t-1} + \dots$ 可以分解为若干独立部分的组合。

分治策略将这个大问题分解为：先计算前半段（可并行），然后从前半段最后一个状态出发，"扫过"后半段（也可并行）。每一层的计算相互独立，构成一棵深度 $\mathcal{O}(\log L)$ 的二叉树。在 GPU 上，每个 CUDA 线程块负责一个子段，通过共享内存实现高效协作。

## 边界

- 仅适用于**线性**递归；非线性递归（如 tanh-RNN）需借助[[非线性RNN摄动并行化]]近似
- $\mathcal{O}(\log L)$ 的复杂度是理论值，实际加速受限于 GPU 内存带宽和 kernel launch 开销
- 对极短序列（$L < 256$），串行计算可能更快（无并行开销）
- 配合[[LRU参数化与初始化]]的复值参数化，可处理数千长度的序列
- 前缀和算法的空间复杂度为 $\mathcal{O}(L)$，与串行版本相同

## 例子

- LRU 在语言模型中使用并行前缀和，序列长度 8192 时训练速度提升数十倍
- 与 Transformer 的 $\mathcal{O}(L^2)$ 注意力相比，线性 RNN + 并行前缀和在长序列上的优势巨大
- CUDA 上的并行扫描（`cub::DeviceScan`）可直接用于实现该算法

## 证据

- ev::9554::线性递归前缀和展开：$x_t = \sum_{i=1}^t \lambda^{t-i} \gamma u_i$
- ev::9554::分治并行计算：$\mathcal{O}(L) \to \mathcal{O}(\log L)$
- ev::9554::CUDA 并行归约实现方法
