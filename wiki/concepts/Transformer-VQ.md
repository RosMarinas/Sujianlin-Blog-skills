---
type: concept
title: Transformer-VQ
aliases:
  - Transformer-VQ
  - VQ-based Linear Attention
definition: 一种通过对Key序列进行向量量化（VQ）近似，将注意力矩阵乘法转化为线性复杂度的线性Attention实现机制。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-29-我在Performer中发现了Transformer-VQ的踪迹.md
source_ids:
  - "9862"
prerequisites:
  - "[[向量量化]]"
  - "[[Performer]]"
related_formulas:
  - "[[Transformer-VQ注意力公式]]"
related_methods:
  - "[[狄拉克函数光滑近似法]]"
evidence_spans:
  - ev::9862::Transformer-VQ近似
status: draft
updated: 2026-06-12
---

# Transformer-VQ

## 核心定义

**Transformer-VQ** 是一种以向量量化（Vector Quantization）为核心近似工具的线性复杂度 Attention 机制。该方法通过将输入序列的 Key 向量集 $K$ 近似为一组离散的特征码本中心 $C$ 和指派选择矩阵 $\Delta$ 的乘积（即 $K \approx \Delta C$），从而在计算 Self-Attention 矩阵时，把指数缩放的相似度计算顺序进行结合律重写，将标准 Attention 的 $O(n^2)$ 计算复杂度降为与序列长度 $n$ 呈线性相关的 $O(nc)$。

## 数学机制与演化关系

1. **计算复杂度线性化**：
   - 经典 Attention 分子部分计算为 $\exp(QK^\top)V$，其包含 $n \times n$ 的稠密注意力乘积。
   - 引入 VQ 近似 $K \approx \Delta C$ 后，分子重写为 $\exp(QC^\top)\Delta^\top V$。因为 $C$ 是预设的常数级小码本大小（尺寸 $c \ll n$），所以可以通过先计算 $\Delta^\top V$（复杂度 $O(nc)$），再左乘 $\exp(QC^\top)$（复杂度 $O(nc)$）来规避 $n \times n$ 的大矩阵乘法。
2. **与 Performer 的类比（Soft vs Hard）**：
   - 线性 Attention 架构 [Performer](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/performer.md) 使用随机高斯投影逼近 Softmax 相似度。经过代数整理，Performer 的特征变换其实是在对 Key 向量以其投影中心 $\boldsymbol{\omega}_i$ 进行距离打分，并以 Softmax 形式给出权重分配。
   - 这意味着 Performer 本质上在扮演一个“Soft 概率指派的 Transformer-VQ”；而 Transformer-VQ 则是利用硬 argmin 离散匹配的“Hard 指派版本”。Softmax 的极限状态即为硬 One-hot 分布，故两者具有高度的代数同构性。
3. **基于 GMM 的理论起源**：
   - 可以通过狄拉克 $\delta$ 分布条件恒等式，将 Attention 的求和项精确重写为关于连续特征空间 $\boldsymbol{\omega}$ 的无限维线性 Attention 积分形式。
   - 此时引入高斯混合模型（Gaussian Mixture Model, GMM）对条件转移概率 $p(\boldsymbol{\omega}|\boldsymbol{k})$ 进行多中心逼近，并在方差极限趋近于零（$\sigma \to 0$）的物理边界下，该积分系统即自然退化为有限维的离散 Transformer-VQ 形式。这为线性 Attention 的收敛性优化提供了完备的概率物理解释。

## 瓶颈与挑战

1. **梯度估计次优性**：由于采用 One-hot 硬分类，反向传播必须通过直通估计器（STE）进行梯度截断，这不可避免地导致了梯度更新方向的不精确性。
2. **训练线性化的阻碍**：在训练阶段为消除前向传播的完整计算，Transformer-VQ 往往进行梯度隔断，这限制了模型在参数量进一步扩张时的拟合性能。
