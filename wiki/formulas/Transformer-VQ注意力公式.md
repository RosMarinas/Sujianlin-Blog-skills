---
type: formula
title: Transformer-VQ注意力公式
aliases:
  - Transformer-VQ注意力机制公式
latex: |
  \exp\left(Q\hat{K}{}^{\top}\right)V = \exp\left(QC^{\top}\right)(\Delta^{\top}V)
symbol_meanings:
  Q: Query 序列矩阵，维度为 n \times d_k
  \hat{K}: 经过向量量化近似后的 Key 序列矩阵，\hat{K} = \Delta C
  C: 可学习的离散量化特征码本（Codebook）矩阵，维度为 c \times d_k
  \Delta: 离散 One-hot 指派稀疏矩阵，维度为 n \times c
  V: Value 序列矩阵，维度为 n \times d_v
  n: 序列长度
  c: 码本特征向量总数
standard_notation:
  Q: 查询矩阵
  K: 键矩阵
  V: 值矩阵
  C: 码本矩阵
  \Delta: 离散指派矩阵
conditions: 采用一阶向量量化对连续键空间进行最近邻硬分配匹配，利用乘法结合律降低矩阵乘法维度。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-29-我在Performer中发现了Transformer-VQ的踪迹.md
source_ids:
  - "9862"
appears_in:
  - "[[spaces-9862-我在Performer中发现了Transformer-VQ的踪迹]]"
evidence_spans:
  - ev::9862::Transformer-VQ近似
status: draft
updated: 2026-06-12
---

# Transformer-VQ注意力公式


## 概述

（待补充）

## 物理意义与计算流

本公式刻画了 **Transformer-VQ** 注意力模块分子的线性化计算过程。在标准 Self-Attention 中，键值乘积 $\exp(QK^\top)$ 的矩阵乘法维度为 $n \times n$。

Transformer-VQ 通过将 Key 矩阵 $K$ 近似为硬分配的码本乘积 $\hat{K} = \Delta C$，将指数形式转换为：
$$
\exp\left(Q\hat{K}{}^{\top}\right) = \exp\left(QC^{\top}\right)\Delta^{\top}
$$
根据矩阵结合律，与 Value 矩阵 $V$ 结合后的求和过程可写为：
$$
\big[\exp\left(QC^{\top}\right)\Delta^{\top}\big]V = \exp\left(QC^{\top}\right)\big[\Delta^{\top}V\big]
$$
其中，由于码本维数 $c \ll n$ 且指派矩阵 $\Delta$ 每一行仅有一个元素为 1（其余为 0），因此计算 $\Delta^\top V$ 的乘法复杂度为 $O(nc)$。随后左乘 $n \times c$ 的特征权重项 $\exp(QC^\top)$（计算复杂度为 $O(nc)$），即可让注意力的运算开销整体下降至 $O(nc)$。这成功以 VQ 映射将标准 Attention 变换成了离散空间上的线性 Attention 算法。
