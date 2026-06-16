---
type: series
title: 重温SSM
aliases:
  - SSM系列
  - revisit_ssm
article_ids:
  - "10114"
  - "10137"
  - "10162"
  - "10180"
series_goal: 从 HiPPO 的在线函数逼近推导出线性状态空间模型，再解释 S4 与 RTF 如何把卷积核计算变成高效的生成函数计算。
entry_roles:
  10114: 从在线函数逼近和正交投影推导出线性状态空间 ODE，并给出 HiPPO-LegT 与 HiPPO-LegS 矩阵。
  10137: 补全 HiPPO 离散化、LegS 尺度等变、多项式长尾衰减和 O(d) 计算性质。
  10162: 解释 S4 如何用 HiPPO-LegS 矩阵、双线性离散化、卷积核生成函数和对角加低秩分解获得高效并行计算。
  10180: 把 SSM 卷积核生成函数重新表述为有理传递函数，并用 a,b 多项式系数直接参数化训练与友矩阵推理。
key_concepts:
  - [[线性状态空间ODE]]
  - [[HiPPO矩阵]]
  - [[HiPPO-LegS]]
  - [[S4卷积核生成函数]]
  - [[对角加低秩分解]]
  - [[有理传递函数]]
key_methods:
  - [[正交基投影推导状态动力学]]
  - [[生成函数化卷积核计算]]
  - [[对角加低秩与Woodbury加速]]
  - [[有理传递函数参数化]]
reading_paths:
  - [[SSM数学基础阅读路径]]
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-05-24-重温SSM-一-线性系统和HiPPO矩阵.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-05-重温SSM-二-HiPPO的一些遗留问题.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-06-27-重温SSM-四-有理生成函数的新视角.md
source_ids:
  - "10114"
  - "10137"
  - "10162"
  - "10180"
status: stable
updated: 2026-06-09
---
## 系列问题

这个系列关心 SSM 的数学基础：为什么线性状态空间系统能作为序列记忆模型，HiPPO 矩阵从何而来，S4 怎样让 HiPPO 高效训练，RTF 又怎样把同一问题改写为有理生成函数。

## 有序文章

1. [[重温SSM（一）：线性系统和HiPPO矩阵]]：从正交投影推导 [[线性状态空间ODE]] 与 [[HiPPO矩阵]]。
2. [[重温SSM（二）：HiPPO的一些遗留问题]]：补充离散化、[[HiPPO-LegS]] 的尺度等变、多项式衰减与计算效率。
3. [[重温SSM（三）：HiPPO的高效计算（S4）]]：用 [[S4卷积核生成函数]]、[[对角加低秩分解]] 和 Woodbury 恒等式解释 S4。
4. [[重温SSM（四）：有理生成函数的新视角]]：用 [[有理传递函数]] 与 [[友矩阵]] 将参数化转到生成函数空间。

## 弱项与边界

Mamba、S5、Diagonal SSM 只作为源文中的背景对照出现，本 batch 不把它们提升为 stable 节点。
