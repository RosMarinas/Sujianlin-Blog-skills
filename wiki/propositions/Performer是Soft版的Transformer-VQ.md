---
type: proposition
title: Performer是Soft版的Transformer-VQ
statement: 线性 Attention 架构 Performer 的特征投影映射在代数展开后，等价于对键向量 Key 施加基于 Softmax 的连续概率指派；当该指派退化为 One-hot 硬分配时，其极限形态即为 Transformer-VQ。
assumptions:
  - 键向量 $K$ 与投影中心均归一化为单位长度或等模长。
  - Softmax 的温度系数趋近于零（即实现硬指派）。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-29-我在Performer中发现了Transformer-VQ的踪迹.md
source_ids:
  - "9862"
proof_route: |
  1. 展开 Performer 的特征表示：\tilde{\boldsymbol{k}} 分量正比于 \exp(\boldsymbol{\omega}_i\cdot\boldsymbol{k} - \Vert\boldsymbol{k}\Vert^2/2 - \Vert\boldsymbol{\omega}_i\Vert^2/2)。
  2. 利用二次展开整理指数项：
     \boldsymbol{\omega}_i\cdot\boldsymbol{k} - \frac{1}{2}\Vert\boldsymbol{k}\Vert^2 - \frac{1}{2}\Vert\boldsymbol{\omega}_i\Vert^2 = -\frac{1}{2}\Vert\boldsymbol{k} - \boldsymbol{\omega}_i\Vert^2
     故 \tilde{\boldsymbol{k}} 分量正比于 \exp(-\Vert\boldsymbol{k} - \boldsymbol{\omega}_i\Vert^2/2)。
  3. 由于注意力机制最终包含归一化，故可将 \tilde{\boldsymbol{k}} 等价表示为关于负欧式距离的 Softmax 概率分配矢量：
     \tilde{\boldsymbol{k}} \propto \text{Softmax}\big(-\Vert\boldsymbol{k} - \boldsymbol{\omega}_i\Vert^2/2\big)_{i=1}^m
  4. 将随机投影中心 \boldsymbol{\omega}_i 视为离散特征码本 C 中的向量，上式代表连续特征向量 \boldsymbol{k} 对码本的软概率匹配分配。
  5. 当 Softmax 分配函数在硬化极限状态下（温度系数 $\tau \to 0$），概率分配退化为单点 one-hot 矩阵 \Delta_{i,j} = \delta_{j, \mathop{\text{argmin}} \Vert K_i - C_k\Vert}。
  6. 此时注意力算子分子部分精确等同于 Transformer-VQ 的 \exp(QC^\top)\Delta^\top V 形式。
evidence_spans:
  - ev::9862::Performer与Transformer-VQ类比
status: draft
updated: 2026-06-12
---

# Performer是Soft版的Transformer-VQ

## 命题陈述

线性自注意力模型 [Performer](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/performer.md) 的指数高斯随机投影机制，在二次型合并后，在数学上等价于利用 Softmax 权重将 Key 向量插值投影到码本中心上。该软匹配模型的硬 One-hot 分配极限，即为对 Key 实施向量量化的 [Transformer-VQ](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/wiki/concepts/Transformer-VQ.md) 算法。

## 物理意义

本命题将本来看似毫不相关的“基于高斯核蒙特卡罗采样的随机注意力（Performer）”与“基于离散码本匹配的离散注意力（Transformer-VQ）”在代数上统一起来。它指出，通过将 Performer 中固定的随机中心 $\boldsymbol{\omega}_i$ 替换为可学习的码本中心 $C$，并由软分配平滑过渡到硬分配，可以为克服硬 VQ 的梯度截断瓶颈提供了一条可导化的软概率优化通路（例如利用 GMM 转移核）。
