---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: Sandwich
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
source_ids:
  - 9431
method_summary: Sandwich修改了ALIBI的相对距离惩罚项，通过Sinusoidal绝对位置编码的点积替代显式的绝对距离惩罚，利用其随距离增加而震荡衰减的特性实现类似局部注意力的效果。
typical_structure: |
  1. 计算当前层输入中每个 Token 对应位置 $m, n$ 的传统 Sinusoidal 绝对位置编码 $\boldsymbol{p}_m$ 和 $\boldsymbol{p}_n$。
  2. 在 Attention 模块中计算常规的 Query 和 Key 内积 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$。
  3. 计算对应位置编码的内积项 $\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$，并引入超参数 $\lambda > 0$ 进行缩放。
  4. 将位置编码点积作为偏置加到 Attention 得分上：$\boldsymbol{q}_m^{\top}\boldsymbol{k}_n + \lambda\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$，然后进行 Softmax。
applicability: 适用于 Transformer 模型在进行长序列处理和长度外推时，希望以添加绝对位置编码的方式隐式实现相对位置的距离惩罚，并保持更好的长距离泛化能力。
evidence_spans:
  - ev::9431::"Sandwich也是KERPLE的作者们搞的...它将式$\eqref{eq:alibi}$替换为 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n + \lambda\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$"
  - ev::9431::"$\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$是$m-n$的标量函数，并且平均而言是$|m-n|$的单调递增（注：实际上随距离增加内积下降，起到惩罚作用）函数，所以它的作用也跟$-\lambda|m-n|$相似"
examples:
  - [[article::9431]]
status: stable
updated: 2026-06-12
---

# Sandwich

## 适用问题

在 Transformer 中实现长度外推时，直接使用 ALIBI 的绝对线性惩罚（$-\lambda|m-n|$）虽然有效，但惩罚过于生硬且完全抛弃了绝对位置信息。需要一种更自然平滑的距离惩罚项来模拟局部注意力，同时兼顾绝对与相对位置特征的平滑过渡。

## 核心变换

将 ALIBI 强加于 Attention Score 的严格相对距离惩罚 $-\lambda|m-n|$，替换为原版 Transformer 的正弦绝对位置编码（Sinusoidal Position Embeddings）的点积形式 $\lambda \boldsymbol{p}_m^{\top}\boldsymbol{p}_n$。整体 Attention Score 计算式变换为：
$$ \boldsymbol{q}_m^{\top}\boldsymbol{k}_n + \lambda\boldsymbol{p}_m^{\top}\boldsymbol{p}_n $$

## 典型步骤

1. 获取输入序列中每个位置 $m, n$ 的标准 Sinusoidal 绝对位置编码 $\boldsymbol{p}_m$ 和 $\boldsymbol{p}_n$。
2. 计算 Query 和 Key 的标准内积注意力得分 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n$。
3. 计算两个绝对位置编码的内积 $\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$，并乘以超参数 $\lambda$。
4. 将两者相加即 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n + \lambda\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$ 作为最终的 Attention Score 输入到 Softmax 计算权重中。

## 直觉

标准的 Sinusoidal 位置编码向量如果做点积，其结果 $\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$ 本质上是一个关于相对距离 $|m-n|$ 的标量函数。虽然它存在波动，但宏观“平均而言”，随着距离 $|m-n|$ 的增大，两个正弦编码向量的内积会震荡下降。把它直接加在 Attention Score 上，就相当于隐性地给距离较远的 Token 对施加了负向偏置，其效果非常类似于 ALIBI 中引入距离惩罚的效果，从而使得模型更倾向于关注邻近局部的上下文，自然带来了长度外推性。

## 边界

- **非严格单调**：由于 $\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$ 是正余弦波的叠加，其函数图像并非严格单调递减，而是呈现震荡下降的趋势。这可能导致在某些特定远距离处出现异常的注意力峰值（惩罚变弱）。
- **计算开销冗余**：虽然等价于将 $\boldsymbol{p}_m$ 直接拼接到 $\boldsymbol{q}_m$ 并在特征维度计算内积（即 $[\boldsymbol{q}_m, \sqrt{\lambda}\boldsymbol{p}_m]^{\top}[\boldsymbol{k}_n, \sqrt{\lambda}\boldsymbol{p}_n]$），但这实际上增加了向量的有效维度，相比单纯的相对距离偏置，并未减少计算量，反而如果不加融合可能会带来额外算力消耗。

## 例子

在语言模型的预训练中，给定序列中的第 5 个和第 10 个 Token。计算它们的注意力分数时，先算出内容上的匹配度 $\boldsymbol{q}_5^{\top}\boldsymbol{k}_{10}$。同时，取出正弦位置编码 $\boldsymbol{p}_5$ 与 $\boldsymbol{p}_{10}$ 做内积，得到一个较小的负偏置（由于距离为 5）。而对于第 5 个和第 6 个 Token，$\boldsymbol{p}_5^{\top}\boldsymbol{p}_6$ 的内积会相对较大（距离为 1）。将这些内积值乘以 $\lambda$ 后加到内容得分上，模型自动给近距离词语更高的权重补偿。

## 证据

- ev::9431::"Sandwich...将式$\eqref{eq:alibi}$替换为 $\boldsymbol{q}_m^{\top}\boldsymbol{k}_n + \lambda\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$"
- ev::9431::"$\boldsymbol{p}_m^{\top}\boldsymbol{p}_n$是$m-n$的标量函数...它的作用也跟$-\lambda|m-n|$相似"
- ev::9431::"Sandwich通过拼接的方式补充绝对位置信息，其Attention结果则相当于相对位置编码...拼接增加了向量维度，反而会进一步增加Attention的计算量。"
