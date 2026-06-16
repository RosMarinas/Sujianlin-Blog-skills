---
type: formula
title: FlatNCE损失公式
latex: \mathcal{L}_{\text{FlatNCE}} = \log\left(\sum_{i \neq t} e^{s_i}\right) - s_t
symbol_meanings: {"s_t": "正样本对特征经过编码后算出的相似度打分（如Scaled余弦值）", "s_i": "非正对负样本在 batch 内算出的余弦相似度分数", "\\mathcal{L}_{\\text{FlatNCE}}": "改进的 FlatNCE 对比损失值"}
standard_notation: L_{\text{FlatNCE}} = \text{LSE}_{i \neq t}(s_i) - s_t
conditions: 相似度 s_i 在数值上是有界的，且正对得分相对极高。
appears_in: ["8586"]
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md"]
source_ids: ["8586"]
status: stable
updated: 2026-06-12
---

# FlatNCE损失公式


## 概述

（待补充）

## 公式表达
FlatNCE 损失函数定义为：
$$
\\mathcal{L}_{\\text{FlatNCE}} = \\log\\left(\\sum_{i \\neq t} e^{s_i}\\right) - s_t
$$

## 原理与数值平度
在经典的交叉熵中，正对得分 $s_t$ 与负对求和项是在对数项内部进行加和计算的。如果表示特征拟合很快，使得 $s_t \\gg s_i$，交叉熵损失值会变成 $\\log(1+\\xi)$，其中 $\\xi \\to 0$。在自适应优化（如 Adam）的偏导数迭代时，其分母会被接近 0 的数值除，导致计算机浮点表示的舍入截断误差被放大成为主导噪声。FlatNCE 在 LogSumExp 中去除了 $s_t$，使求导时的极小因子被等效消去，极大稳固了小批次下的参数更新方向。