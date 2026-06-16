---
type: formula
title: 线性Attention结合律公式
aliases:
- Linear attention associativity
source_ids:
- '7546'
- '8180'
evidence_spans:
- ev::7546::结合律线性化
- ev::8180::Nyström背景
standard_notation:
  Q: query matrix
  K: key matrix
  V: value matrix
  phi: non-negative query feature map
  varphi: non-negative key feature map
  n: sequence length
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
- Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
latex: \phi(Q)(\varphi(K)^\top V)=\left(\phi(Q)\varphi(K)^\top\right)V,
symbol_meanings:
  K: key matrix
  Q: query matrix
  V: value matrix
  n: sequence length
  phi: non-negative query feature map
  varphi: non-negative key feature map
conditions: （待从源文章提取）
appears_in:
- '7546'
- '8180'
---

# 线性Attention结合律公式

## 概述

$$\phi(Q)(\varphi(K)^\top V)=\phi(Q)\left(\varphi(K)^\top V\right)$$

线性Attention结合律公式是将 Transformer 自注意力计算的复杂度从序列长度 $n$ 的平方级别 $\mathcal{O}(n^2)$ 降低到线性级别 $\mathcal{O}(n)$ 的核心数学基础。标准 Attention 受到 softmax 的非线性限制，必须先显式计算 $n \times n$ 的注意力权重矩阵。而线性 Attention 通过剥离 softmax 或采用适当的非负特征映射 $\phi$ 和 $\varphi$（核方法思想）来取代传统的相似度计算，使得原本的结合项得以重新组合。由于矩阵乘法满足结合律，我们可以优先计算右侧的 $\varphi(K)^\top V$，得到一个较小维度的 $d \times d$ 矩阵，然后再被 $n \times d$ 的 $\phi(Q)$ 左乘。由于特征维度 $d$ 通常远小于序列长度 $n$，这一计算顺序的改变从根本上消除了对长序列二次时间、空间复杂度的依赖，在保持 Attention “token-to-token”全局交互特性的同时实现了线性扩展。
