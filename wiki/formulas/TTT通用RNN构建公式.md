---
type: formula
title: TTT通用RNN构建公式
aliases:
- TTT RNN Construction Formula
latex: \boldsymbol{o}_t = \boldsymbol{f}(\boldsymbol{S}_t; \boldsymbol{q}_t), \quad
  \boldsymbol{S}_t = \boldsymbol{S}_{t-1} - \eta_t\nabla_{\boldsymbol{S}_{t-1}}\mathcal{L}(\boldsymbol{f}(\boldsymbol{S}_{t-1};\boldsymbol{k}_t),
  \boldsymbol{v}_t)
symbol_meanings:
  \boldsymbol{S}_t: 随时间演化的模型隐状态（即模型权重）
standard_notation:
  convention: Follow TTT paper convention. The update is a single-step SGD on the
    online learning problem.
conditions: 优化器不限于SGD。可以推广到Muon、Adam等。f的架构和损失L的选择决定了具体的RNN模型。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
- Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
- '10017'
- '11320'
status: draft
updated: "2026-06-14"
appears_in:
- '10017'
- '11320'
---

# TTT通用RNN构建公式


## 概述

（待补充）

## 公式定义与背景

在标准Softmax Attention中，模型的核心计算为 $\boldsymbol{O} = \mathop{\text{softmax}}(\boldsymbol{Q}\boldsymbol{K}^{\top} + \log \boldsymbol{M})\boldsymbol{V}$。该计算需要显式地维护 $n \times n$ 的注意力矩阵，导致正比于序列长度平方 $O(n^2)$ 的时间与空间复杂度。为了在Decoder-only生成式模型中实现常数复杂度的状态更新，TTT（Test Time Training，或Online Learning）框架提出利用优化器更新与RNN迭代的等价性，通过在线学习来隐式地压缩历史上下文。

TTT框架将序列历史中的 $\boldsymbol{K}, \boldsymbol{V}$ 视为成对的在线训练语料 $(\boldsymbol{k}_1, \boldsymbol{v}_1), (\boldsymbol{k}_2, \boldsymbol{v}_2), \cdots, (\boldsymbol{k}_t, \boldsymbol{v}_t)$。模型试图学习一个映射 $\boldsymbol{v} = \boldsymbol{f}(\boldsymbol{S}_t;\boldsymbol{k})$，并在每一步输出 $\boldsymbol{o}_t = \boldsymbol{f}(\boldsymbol{S}_t;\boldsymbol{q}_t)$。其中 $\boldsymbol{S}_t$ 代表随时间演化的模型隐状态（即模型权重），其更新过程由SGD优化器驱动：
$$
\boldsymbol{S}_t = \boldsymbol{S}_{t-1} - \eta_t\nabla_{\boldsymbol{S}_{t-1}}\mathcal{L}(\boldsymbol{f}(\boldsymbol{S}_{t-1};\boldsymbol{k}_t), \boldsymbol{v}_t)
$$

## 架构衍生与统一视角

TTT框架通过定义不同的预测函数 $\boldsymbol{f}$ 和损失函数 $\mathcal{L}$，可以统一多种现有的线性注意力及序列模型变体。通过这种参数化的在线“训练”，历史的 $(\boldsymbol{k}, \boldsymbol{v})$ 键值对被压缩至固定尺寸的权重矩阵 $\boldsymbol{S}_t$ 中，使得当前 Query $\boldsymbol{q}_t$ 可以直接利用 $\boldsymbol{S}_t$ 进行高效的自回归解码：

1. **原始线性Attention**：采用简单的线性模型与内积损失。
2. **DeltaNet**：当架构选择纯线性映射 $\boldsymbol{v} = \boldsymbol{S}_t\boldsymbol{k}$ 并且损失函数 $\mathcal{L}$ 选用均方误差（Squared Error）时，其在线梯度下降过程精确对应了DeltaNet的RNN更新规则。
3. **GDN及变体**：在纯线性映射和平方损失的基础上，通过引入正则项（如L2正则）或其他特定的优化修饰，可自然衍生出类似GDN（Gated DeltaNet）等变体。
4. **进阶优化器与Batch化**：除了基础的SGD，该参数更新规则还可以平滑推广至诸如Muon等更高级的优化器。同时在系统实现上，也可以扩展为以Chunk为单位的Mini-batch TTT，以大幅提升实际硬件上的训练与推理计算效率。
