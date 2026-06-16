---
type: formula
title: ANNCUR矩阵近似公式
latex: \boldsymbol{S} \approx \boldsymbol{F} (\boldsymbol{F}\cap \boldsymbol{H})^{\dagger}\boldsymbol{H}
symbol_meanings: {"\\boldsymbol{S}": "包含所有 Query 与 Key 对比打分关系的全局交互式相关性矩阵", "\\boldsymbol{F}": "通过选取 key 的代表子集 U 计算得到的子得分矩阵", "\\boldsymbol{H}": "通过选取 query 的代表子集 V 计算得到的子得分矩阵", "(\\boldsymbol{F}\\cap \\boldsymbol{H})^{\\dagger}": "两代表子集相交所构成的子方阵的 Moore-Penrose 伪逆矩阵"}
standard_notation: \boldsymbol{M} \approx \boldsymbol{C} \boldsymbol{U} \boldsymbol{R}
conditions: 代表子集的选择能够大体覆盖主要特征簇，且相交矩阵是可求伪逆的。
appears_in: ["9336"]
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-11-02-利用CUR分解加速交互式相似度模型的检索.md"]
source_ids: ["9336"]
status: stable
updated: 2026-06-12
---

# ANNCUR矩阵近似公式


## 概述

（待补充）

## 公式表达
ANNCUR 中的相似度计算近似表达式为：
$$
\\boldsymbol{S} \\approx \\boldsymbol{F} (\\boldsymbol{F}\\cap \\boldsymbol{H})^{\\dagger}\\boldsymbol{H}
$$

## 矩阵分解的应用
传统的交互式 Cross-Encoder 在推理检索时面临两两交互的瓶颈。该公式通过 CUR 骨架矩阵近似，将两个元素的非线性二体关联，解耦为它们分别与选定代表基底的单体交互。计算伪逆部分可以完全离线算好并缓存为一密集矩阵，查询时只需要把少量代表 Cross-Encoder 分数向量与缓存大矩阵相乘，直接绕开了每次检索进行 $N$ 次神经网络前向的前向瓶颈。