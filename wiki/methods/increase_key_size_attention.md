---
type: method
title: 增大key_size解除注意力低秩瓶颈
operation_types:
  primary: Rewrite / identity transform
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
source_ids:
  - "7325"
method_summary: 通过将自注意力计算中 Query 和 Key 的投影维度（key_size）与 Value 的投影维度（head_size = d/h）进行解耦并单独调大，实现在不改变模型总体隐层维度（hidden_size）的前提下，提升自注意力矩阵的秩和分布拟合能力，消除多头注意力中 head_size 过小带来的低秩表示瓶颈。
typical_structure: |
  1. 在定义自注意力机制的多头投影时，设置独立的 key_size 参数，使其大于 head_size（即 $d/h$）
  2. 对输入特征进行投影：$Q = XW_q \in \mathbb{R}^{n \times key\_size}$，$K = XW_k \in \mathbb{R}^{n \times key\_size}$，$V = XW_v \in \mathbb{R}^{n \times head\_size}$
  3. 计算注意力得分矩阵：$P = softmax(\frac{QK^\top}{\sqrt{key\_size}})$
  4. 计算输出 $O = PV \in \mathbb{R}^{n \times head\_size}$，拼接各头输出后通过输出矩阵映射回 hidden_size
applicability: 当设计 Transformer 模型（尤其是小体量模型或头数 $h$ 较大时），遇到注意力得分矩阵由于通道维度极小而出现低秩表示瓶颈、拟合分布能力受限时激活此方法。
tools:
  - 解耦 key_size
  - 注意力低秩优化
related_methods:
  - [[Talking-Heads Attention 混合注意力分布]]
  - [[Synthesizer静态注意力生成]]
examples:
  - [[article::7325]]
status: draft
updated: 2026-06-14
---

## 适用问题

多头注意力中，当注意力头数 $h$ 较大时，每个头的投影维度 $head\_size = d/h$ 变得很小（如 $d=768, h=12 \to head\_size=64$）。此时 $Q, K \in \mathbb{R}^{n \times 64}$，二者内积得到的注意力得分矩阵 $P \in \mathbb{R}^{n \times n}$ 的秩被严格限制在 64 以内，形成低秩表示瓶颈。这导致注意力分布无法拟合 $n^2$ 量级的复杂联合分布，模型表达能力受限。

## 核心变换

**输入**：标准多头自注意力 $Q, K \in \mathbb{R}^{n \times head\_size}$
**输出**：解耦后的 $Q, K \in \mathbb{R}^{n \times key\_size}$，其中 $key\_size \gg head\_size$

标准设计中 $Q, K, V$ 共享相同的投影维度：
$$
Q = XW_q, \quad K = XW_k, \quad V = XW_v, \quad W_q, W_k, W_v \in \mathbb{R}^{d \times head\_size}
$$

增大 key_size 后，将 $Q, K$ 的投影维度独立调大：
$$
Q = XW_q \in \mathbb{R}^{n \times key\_size}, \quad K = XW_k \in \mathbb{R}^{n \times key\_size}, \quad V = XW_v \in \mathbb{R}^{n \times head\_size}
$$

注意力计算变为：
$$
P = softmax\left(\frac{QK^\top}{\sqrt{key\_size}}\right), \quad O = PV \in \mathbb{R}^{n \times head\_size}
$$

注意力得分矩阵 $P$ 的最大秩从 $head\_size$ 提升至 $key\_size$。

## 典型步骤

1. **定义独立 key_size**：在多头注意力中，将 $Q$ 和 $K$ 的投影维度设为独立的 $key\_size$ 超参数（通常取 128），与 $head\_size$ 解耦
2. **投影计算**：对输入特征分别投影为 $Q \in \mathbb{R}^{n \times key\_size}$、$K \in \mathbb{R}^{n \times key\_size}$、$V \in \mathbb{R}^{n \times head\_size}$
3. **注意力得分计算**：$P = softmax(QK^\top / \sqrt{key\_size})$
4. **值汇聚与拼接**：$O = PV \in \mathbb{R}^{n \times head\_size}$，拼接各头后通过输出矩阵映射回 $hidden\_size$

## 直觉

核心思想：**注意力矩阵的秩决定其拟合能力**。

自注意力机制的核心是生成 $n \times n$ 的注意力得分矩阵。在标准多头设计中，$Q$ 和 $K$ 的投影维度 $head\_size$ 同时决定了该矩阵的秩上限。当 $head\_size$ 很小时（如 32 或 64），注意力矩阵只能表达低秩分布——无论序列多长，注意力模式都被限制在极小的子空间中。

将 $Q, K$ 的维度独立调大（如固定为 128），相当于在不增加 $V$ 的参数量和不改变 $hidden\_size$ 的前提下，为注意力矩阵提供了更大的"表达空间"。这对应了"瓶颈在注意力得分本身，而非后续的值汇聚"这一洞察——$V$ 的维度可以保持 $head\_size$ 不变，因为值汇聚的瓶颈不在维度而在注意力权重的质量。

## 边界

- 增大 key_size 会略微增加 $Q, K$ 投影矩阵的参数量和 $QK^\top$ 的计算量，但远小于增加 $hidden\_size$ 的开销
- 经验推荐 $key\_size = 128$，更大的 key_size 边际收益递减
- 该方法不改变 $V$ 的维度，因此多头输出的拼接维度保持不变
- 当 $head\_size$ 本身已经足够大（如大模型中 $head\_size=128$），低秩瓶颈不再明显，此方法的收益有限

## 例子

- 在 $d=512, h=8, head\_size=64$ 的 Transformer 中，将 key_size 固定为 128，注意力矩阵的秩上限从 64 提升至 128
- 实验表明，在参数量基本相同的情况下，增大 key_size 可显著提升小体量模型的语言建模性能
- Talking-Heads Attention 与此方法结合，可在更小的 key_size 下通过头间混合获得更强表达

## 证据

- ev::7325::低秩瓶颈分析：公式 (46) 揭示 Softmax 前的内积逼近受限于 $head\_size$
- ev::7325::key_size 调大方案：$Q, K$ 维度解耦为独立 key_size，$V$ 保持 head_size
- ev::7325::实验结论：key_size 固定为 128 效果最优
