---
type: concept
title: Relative Positional Encoding
aliases:
  - 相对位置编码
definition: 相对位置编码是通过修改注意力计算中的得分矩阵（Attention Score），融入两两 Token 之间相对距离（$i-j$）表示的位置注入机制。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "8130"
  - "9105"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Relative Positional Encoding

## Definition
相对位置编码是通过修改注意力计算中的得分矩阵（Attention Score），融入两两 Token 之间相对距离（$i-j$）表示的位置注入机制。

## Explanation
相对位置编码不在输入端直接改动，而是在算 Attention 时将注意力交互偏置建模为相对偏移量 $i-j$ 的函数。主要的演进路线包括：
- **经典式 (Shaw)**：在注意力得分和值汇聚中均加入截断的相对距离向量。
- **XLNet**：将注意力内积项彻底展开，引入全局正弦相对向量并省去值上的偏置。
- **T5**：省去输入与位置的交叉交互，直接在注意力矩阵上加上随距离分桶映射的可学习偏置 $\beta_{i,j}$。
- **DeBERTa**：保留内容-位置与位置-内容的交互，并在最后一两层（EMD机制）引入绝对位置编码以结合相对与绝对的优势。
- **旋转位置编码 (RoPE)**：将绝对位置以二维复数旋转的形式直接乘在特征上，在做内积时自发表达相对位置关系。
相对位置编码在语言建模和长文本外推上有着极佳的表现。
