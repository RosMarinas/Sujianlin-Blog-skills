---
type: concept
title: 矩阵符号函数(msign)
aliases:
- msign算子
- matrix sign function
definition: 将矩阵的所有非零奇异值置为1后所得新矩阵的运算，Muon优化器的核心算子。
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-05-11-msign算子的Newton-Schulz迭代-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-05-msign算子的Newton-Schulz迭代-下.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-07-通过msign来计算奇异值裁剪mclip-上.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-23-通过msign来计算奇异值裁剪mclip-下.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-06-13-msign的导数.md
source_ids:
- '10922'
- '10996'
- '11006'
- '11059'
- '11025'
prerequisites:
- '[[奇异值分解]]'
equivalent_forms:
- $\text{msign}(M) = (MM^\top)^{-1/2} M = M(M^\top M)^{-1/2}$
- $\text{msign}(M) = U_{[:,:r]} V_{[:,:r]}^\top$ (SVD形式)
- $\text{msign}(M) = \argmin_{O^\top O = I} \|M - O\|_F^2$ (最优正交近似)
direct_consequences:
- '[[奇异值裁剪(mclip)]]'
- '[[Muon优化器更新规则]]'
related_formulas:
- '[[msign Newton-Schulz迭代公式]]'
- '[[msign导数求解公式]]'
related_methods:
- '[[用迭代逼近替代矩阵分解]]'
- '[[用矩阵恒等式重写奇异值操作]]'
status: deprecated
replaced_by: '[[concept::矩阵符号函数]]'
deprecation_reason: Merged into concept::矩阵符号函数 as part of Pass A node boundary repair.
  Same mathematical object (matrix sign function / msign) presented from different
  angles. The existing tentative_link edge between the two nodes explicitly confirmed
  they are the same core concept.
null_evidence_reason: Integrating new article 11025 details about derivatives
updated: '2026-06-12'
---

# 矩阵符号函数(msign)

## 定义

msign是Muon优化器的核心算子，它将矩阵的所有非零奇异值全部变为1。对于 $M \in \mathbb{R}^{n \times m}$，其SVD分解为 $M = U\Sigma V^\top$，则

$$\text{msign}(M) = U_{[:,:r]} V_{[:,:r]}^\top$$

其中 $r$ 是 $M$ 的秩。等价形式为 $\text{msign}(M) = (MM^\top)^{-1/2} M$。

## 性质

- **最优正交近似**：当 $M$ 是满秩方阵时，$\text{msign}(M)$ 是 $M$ 在正交矩阵集合上的 $F$ 范数最近点。
- **与极分解的关系**：$M = \text{msign}(M) \cdot (V \Sigma V^\top)$ 给出了矩阵的极分解。
- **正交变换不变性**：对任意正交矩阵 $P, Q$，有 $P \cdot \text{msign}(R) \cdot Q = \text{msign}(P R Q)$。
- **解析求导性**：由于满足恒等式 $M = \text{msign}(M)M^\top\text{msign}(M)$，其导数可通过将微分关系转化为 Sylvester 方程进行解析求解。这在结合测试时训练（Test-Time Training, TTT）与 Muon 的端到端优化反向传播中起到了关键作用。

## 计算

- **精确计算**：通过SVD，复杂度 $O(\min(n,m) nm)$。
- **近似计算**：Newton-Schulz迭代。
- **导数计算**：通过 Sylvester 方程的分块矩阵符号函数法进行 GPU 友好的 SVD-free 求解（见 [[msign导数之Sylvester方程]]）。