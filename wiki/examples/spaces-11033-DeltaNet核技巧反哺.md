---
type: example
title: DeltaNet核技巧反哺
article_id: 11033
article: '[[spaces-11033-线性注意力简史-从模仿-创新到反哺]]'
section: 反哺进行时
claim: 通过高维核映射phi，将DeltaNet的Attention矩阵重新写回带逆项的Softmax形式
notation_mapping:
  standard_phi: phi(x)
  source_phi: phi
steps:
- 1. 定义无限维核映射使得 exp(QK^T) = phi(Q)phi(K)^T
- 2. 将DeltaNet的矩阵表达式中的Q, K替换为phi(Q), phi(K)
- 3. 展开低秩求逆表达式，恢复矩阵指数项
- 4. 最终导出形如 A(I+B)^{-1}V 的新型Softmax Attention变体（DeltaFormer）
used_concepts:
- - - 线性注意力
- - - DeltaNet
used_formulas: []
used_methods:
- - - DeltaRule序列建模
source_span: ev::11033::反哺进行时
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-06-20-线性注意力简史-从模仿-创新到反哺.md
source_ids:
- 11033
status: draft
updated: '2026-06-12'
---

# DeltaNet核技巧反哺

该实例展示了如何将线性注意力机制的最新算法应用到标准Softmax注意力机制的改写中，从而实现两种范式的理论闭环与统一。

在标准的Softmax Attention中，Causal场景下第$t$步的注意力输出本质上是基于掩码矩阵$\boldsymbol{M}$的计算。根据定义，其分量形式可表示为 $\boldsymbol{o}_t = \frac{\sum_{j=1}^t \exp(\boldsymbol{q}_t^{\top}\boldsymbol{k}_j) \boldsymbol{v}_j}{\sum_{j=1}^t \exp(\boldsymbol{q}_t^{\top}\boldsymbol{k}_j)}$，而忽略缩放因子的全局矩阵表达则是 $\boldsymbol{O} = (\exp(\boldsymbol{Q}\boldsymbol{K}^{\top})\odot \boldsymbol{M})\boldsymbol{V}$。因为其需要计算$n\times n$的 $\exp(\boldsymbol{Q}\boldsymbol{K}^{\top})$ 矩阵，这种平方级的复杂度使得长序列生成面临巨大挑战。线性Attention早期的主要思路便是模仿和近似这一结构。

然而，随着生成式Decoder-only模型的发展，这种单向模仿演变成了深度的“反哺”。具体而言，这一反哺过程通过以下数学推导完成：

1. **引入无限维核映射**：寻找或定义一个高维核映射 $\phi$，使得查询矩阵 $\boldsymbol{Q}$ 和键矩阵 $\boldsymbol{K}$ 映射后的内积严格等于原始的指数项，即满足 $\exp(\boldsymbol{Q}\boldsymbol{K}^{\top}) = \phi(\boldsymbol{Q})\phi(\boldsymbol{K})^{\top}$。
2. **替换DeltaNet变量**：将DeltaNet（基于Delta Rule序列建模的线性注意力架构）矩阵表达式中的常规 $\boldsymbol{Q}$ 和 $\boldsymbol{K}$，整体替换为无限维映射后的 $\phi(\boldsymbol{Q})$ 和 $\phi(\boldsymbol{K})$。
3. **展开低秩求逆表达式**：在DeltaNet的递推公式中存在低秩矩阵的求逆操作。对替换后的表达式进行代数展开，此时由于核技巧 $\phi(\boldsymbol{Q})\phi(\boldsymbol{K})^{\top}$ 的作用，原本针对线性注意力设计的内积被精确恢复成了Softmax Attention中标志性的矩阵指数项 $\exp(\boldsymbol{Q}\boldsymbol{K}^{\top})$。
4. **导出新型变体**：经过矩阵恒等式化简，最终导出了一种形如 $\boldsymbol{A}(\boldsymbol{I}+\boldsymbol{B})^{-1}\boldsymbol{V}$ 的新型Softmax Attention变体（即DeltaFormer）。

这一精妙的推导成功将DeltaNet中为了处理RNN递归态而引入的更新机制，重新写回了带有矩阵逆项的Softmax形式。它不仅证明了线性注意力代数结构（带有记忆衰减与更新规则）具备反哺原始二次方范式的能力，还为Attention架构突破简单的Softmax归一化提供了新颖的代数视角。
