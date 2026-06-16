---
type: reading_path
title: SSM数学基础阅读路径
aliases:
  []
goal: 按源文递进顺序理解 SSM 的数学基础和两种高效计算视角。
audience: 已经熟悉线性代数、常微分方程、正交基和基本 DFT 的读者。
ordered_nodes:
  - [[重温SSM（一）：线性系统和HiPPO矩阵]]
  - [[重温SSM（二）：HiPPO的一些遗留问题]]
  - [[重温SSM（三）：HiPPO的高效计算（S4）]]
  - [[重温SSM（四）：有理生成函数的新视角]]
prerequisites:
  - 正交投影
  - 矩阵对角化
  - DFT/FFT
checkpoints:
  - 为什么 HiPPO 不是预设线性 ODE，而是从投影系数动力学推出线性 ODE？
  - LegS 的完整历史记忆为什么会转化为多项式衰减？
  - S4 的卷积核生成函数如何把矩阵幂变成逆矩阵？
  - RTF 为什么可以把卷积核生成函数直接参数化为有理函数？
next_paths:
  []
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
## 路径

1. 先读 10114，建立 [[线性状态空间ODE]] 与 [[HiPPO矩阵]] 的来源。
2. 再读 10137，理解 [[HiPPO-LegS]] 的离散化、尺度等变、长尾衰减和 O(d) 计算。
3. 再读 10162，关注 [[S4卷积核生成函数]] 与 [[对角加低秩分解]]。
4. 最后读 10180，理解 [[有理传递函数]] 如何接管 SSM 的参数化和训练计算。
