---
type: formula
title: 超参数化BERT-whitening公式
latex: \tilde{\boldsymbol{x}}_i = (\boldsymbol{x}_i - \beta\boldsymbol{\mu})\boldsymbol{U}\boldsymbol{\Lambda}^{-\gamma/2}
symbol_meanings: {"\\boldsymbol{x}_i": "原始提取的句向量", "\\boldsymbol{\\mu}": "总体样本特征均值", "\\boldsymbol{U}": "协方差矩阵 SVD 分解后得到的正交基矩阵", "\\boldsymbol{\\Lambda}": "特征奇异值对角矩阵", "\\beta": "均值中心化调节超参数，取值在 0 到 1 之间", "\\gamma": "各项同性特征平权拉伸超参数，取值在 0 到 1 之间"}
standard_notation: \tilde{\boldsymbol{x}} = (\boldsymbol{x} - \beta\boldsymbol{\mu}) \boldsymbol{W}_{\beta,\gamma}
conditions: 协方差正定，分解对角值从大到小按降序排列。
appears_in: ["9079"]
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-05-18-当BERT-whitening引入超参数-总有一款适合你.md"]
source_ids: ["9079"]
status: stable
updated: 2026-06-12
---

# 超参数化BERT-whitening公式


## 概述

（待补充）

## 公式表达
白化泛化超参变换公式表达如下：
$$
\\tilde{\\boldsymbol{x}}_i = (\\boldsymbol{x}_i - \\beta\\boldsymbol{\mu})\\boldsymbol{U}\\boldsymbol{\Lambda}^{-\\gamma/2}
$$

## 推导与应用
该公式是对原始无参白化算法 $\\tilde{\\boldsymbol{x}} = (\\boldsymbol{x} - \\boldsymbol{\mu})\\boldsymbol{U}\\boldsymbol{\Lambda}^{-1/2}$ 的一种扩展。
1. **各向同性拉伸**：当 $\\gamma=1$ 且 $\\beta=1$ 时，退化为标准白化，强行对方差拉伸平权；
2. **正交旋转保真**：当设定 $\\beta=\\gamma=0$ 时，该式化为 $\\tilde{\\boldsymbol{x}}_i = \\boldsymbol{x}_i\\boldsymbol{U}$，由于正交旋转不影响余弦值相对顺序，我们可以将其做维度裁剪 $\\tilde{\\boldsymbol{x}}_i[:k]$，实现在有监督 SimBERT 等模型上“无损降维”的优良工程价值。