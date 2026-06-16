---
type: formula
title: LU分解通道卷积公式
latex: \boldsymbol{W} = \boldsymbol{P} \boldsymbol{L} \boldsymbol{U}
symbol_meanings:
  \boldsymbol{W}: 1x1 可逆卷积的通道混合参数方阵
  \boldsymbol{P}: 恒定的置换矩阵
  \boldsymbol{L}: 对角线全为 1 的下三角参数矩阵
  \boldsymbol{U}: 对角线可变的右上三角参数矩阵
standard_notation: \boldsymbol{W} = \boldsymbol{P} \boldsymbol{L} \boldsymbol{U}
conditions: 对角线元素 \boldsymbol{U}_{ii} 绝对值必须严格大于 0 且优化时固定符号，以保证 W 的可逆性。
appears_in:
  - "5807"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-08-26-细水长flow之RealNVP与Glow-流模型的传承与升华.md
source_ids:
  - "5807"
status: draft
updated: 2026-06-12
---

# LU分解通道卷积公式

## 概述

LU 分解通道卷积公式是 Glow 模型中为降低 1x1 可逆卷积雅可比行列式计算开销所引入的代数参数化形式。在图像通道变换 $h = x W$ 中，直接计算 $W$ 的行列式需要 $\mathcal{O}(c^3)$ 的开销。通过引入 LU 分解 $W = P L U$，由于 $P$ 是置换矩阵（行列式绝对值为 1），$L$ 为对角线全 1 的三角矩阵（行列式为 1），整个通道混合层的对数雅可比行列式被极大地化简为：
$$
\log | \det W | = \sum_{i=1}^c \log | U_{ii} |
$$
这使通道线性组合的雅可比计算开销降为 $\mathcal{O}(c)$ 复杂度，从而保证了 Glow 模型在大尺度图像训练上的高效并行。
