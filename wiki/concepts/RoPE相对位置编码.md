---
type: concept
title: RoPE相对位置编码
aliases:
- Rotary Position Embedding
- 旋转式位置编码
definition: 通过旋转矩阵 $\mathcal{R}_i$ 将相对位置信息注入Attention计算的编码方式，满足 $\mathcal{R}_i^\top
  \mathcal{R}_j = \mathcal{R}_{j-i}$。
standard_notation: $s_\alpha(i,j) = (\mathcal{R}_i \boldsymbol{q}_{i,\alpha})^\top
  (\mathcal{R}_j \boldsymbol{k}_{j,\alpha}) = \boldsymbol{q}_{i,\alpha}^\top \mathcal{R}_{j-i}
  \boldsymbol{k}_{j,\alpha}$
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
source_ids:
- '8373'
prerequisites:
- - - concept::位置编码
- - - concept::Transformer
related_methods:
- - - method::GlobalPointer
status: draft
updated: '2026-06-13'
---

# RoPE相对位置编码

## 定义

RoPE相对位置编码是用位置相关旋转矩阵 `R_i` 作用在 query/key 上的编码方式。源文使用性质 `R_i^T R_j=R_{j-i}`，使打分 `s_alpha(i,j)` 可化为 `q_{i,alpha}^T R_{j-i} k_{j,alpha}`，从而显式包含相对位置 `j-i`。

## 激活场景

它在 GlobalPointer 的实体跨度打分中被激活。源文说明如果没有相对位置信息，GlobalPointer 对实体长度和跨度不敏感，容易把无关首尾组合成实体；加入 RoPE 后，模型能更好地区分真正的实体边界。

## 关键关系

RoPE 被选中是因为多数相对位置编码需要截断或引入较多可学习参数，而旋转式位置编码不需要截断。在人民日报 NER 实验中，源文报告 GlobalPointer 不加 RoPE 与加 RoPE 的 F1 差距超过 30 个点，说明它是该设计中的关键支撑。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md`
