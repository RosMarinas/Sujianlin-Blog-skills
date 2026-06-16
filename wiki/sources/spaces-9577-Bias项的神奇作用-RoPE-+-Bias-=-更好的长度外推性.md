---
type: article_summary
title: Bias项的神奇作用：RoPE + Bias = 更好的长度外推性
article_id: 9577
source_url: https://spaces.ac.cn/archives/9577
date: 2023-04-03
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-04-03-Bias项的神奇作用-RoPE-Bias-更好的长度外推性.md
source_ids:
  - 9577
status: draft
updated: 2026-06-12
---

# Bias项的神奇作用：RoPE + Bias = 更好的长度外推性

本文介绍了一个令人意外的发现：在RoPE（旋转位置编码）模型中开启Query和Key投影层的Bias（偏置）项，能够显著增强模型的长度外推性。
在没有RoPE的注意力中，Key的偏置项在Softmax中可以被约掉；但在加了RoPE之后，由于旋转矩阵的存在，偏置项与相对位置 $m-n$ 产生了关联，无法被约掉。
展开带有Bias的注意力计算式，发现第四项为 $oldsymbol{a}^{	op}oldsymbol{\mathcal{R}}_{n-m}oldsymbol{b}$，在经过参数训练后，该项在长距离下呈现出明显的衰减趋势并占据主导地位，起到了局部化注意力的作用。
实验表明，加了Bias的模型（GAU-α架构）在测试长度从512扩展到4096时，准确率衰减显著慢于不加Bias的模型。
这也解释了为什么同样是RoPE模型，KERPLE和Sandwich（包含Bias）的外推性表现优于ALIBI和XPOS（不包含Bias）。
作者同时指出，该外推效果的复现性在不同模型结构和超参数下可能存在不稳定，需斟酌使用。