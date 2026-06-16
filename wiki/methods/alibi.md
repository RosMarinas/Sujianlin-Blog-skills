---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: ALIBI
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
source_ids:
  - 9431
method_summary: "在 Attention softmax 前按相对距离减去线性偏置，增强局部注意力归纳偏置并支持短训长测的长度外推。"
typical_structure: |
  1. 获取当前输入序列中所有 token 之间的相对距离矩阵。
  2. 根据相对距离矩阵计算惩罚项：$-\lambda |m - n|$。
  3. 为不同的 Attention Head 分配不同的超参数 $\lambda$。
  4. 将计算出的惩罚项直接加到 Softmax 操作之前的 Attention Score $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$ 上。
  5. 经过 Softmax 及后续操作完成注意力机制的计算。
applicability: "需要在不重新训练或微调的情况下，使基于自注意力机制的模型能够外推到比训练时更长的文本序列时。"
examples:
  - "[[article::9431]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::9431::ALIBI所做的改动非常简单，只是在Softmax之前，将Attention的计算从 q_m^T k_n 改为 q_m^T k_n - \\lambda|m - n|，其中 \\lambda > 0 是超参数，每个head设置不同的值。"
---

# ALIBI

## 适用问题
如何让在短序列上训练的 Transformer 模型，能够在不微调的情况下处理长序列（提升长度外推性）？

## 核心变换
将 Attention 的计算从 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$ 改为：
$$ \boldsymbol{q}_m^{\top}\boldsymbol{k}_n - \lambda|m - n| $$
其中 $\lambda > 0$ 是超参数，每个 head 设置不同的值。

## 典型步骤
1. 获取当前输入序列中所有 token 之间的相对距离矩阵。
2. 根据相对距离矩阵计算惩罚项：$-\lambda |m - n|$。
3. 为不同的 Attention Head 分配不同的超参数 $\lambda$。
4. 将计算出的惩罚项直接加到 Softmax 操作之前的 Attention Score $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$ 上。
5. 经过 Softmax 及后续操作完成注意力机制的计算。

## 直觉
长度外推性问题本质上是一个训练和预测的长度不一致的问题：预测时用到了没训练过的位置编码，且预测时注意力机制处理的 token 数量远超训练时的数量导致熵过大。ALIBI 通过在 Softmax 前减去一个随相对距离单调递减的偏置项，构造了一个“光滑的局部注意力”，使得模型只关注局部的 token，有效缓解了注意力分散问题，并增强了局域性。

## 边界
ALIBI 如果应用于双向注意力模型，由于 $|m - n|=|n - m|$，模型无法区分左和右，只能识别相对距离的远近，因此无法准确识别完整的位置信息。它的成功很大程度上是因为单向语言模型即便不加位置编码也能取得一定效果，ALIBI 主要起到了增强局域性的作用。

## 例子
在单向语言模型中，对序列长度为 L 的输入进行 Attention 计算时，构建一个大小为 L x L 的相对距离矩阵，乘以对应的 $\lambda$ 衰减系数后直接在 Softmax 之前从 Attention Score 中减去。

## 证据
- 9431 提到 ALIBI 作为“开山之作”，核心改动是在Softmax之前，将Attention的计算改为 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n - \lambda|m - n|$。
