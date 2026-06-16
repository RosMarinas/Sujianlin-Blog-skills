---

type: formula
title: Warmup-Decay最优学习率
aliases: null
latex: \eta_t=\frac{R G_t^{-2}}{\sqrt{Q_T}}(1-Q_t/Q_T)
symbol_meanings:
  G_t: 第 t 步梯度模长二阶矩平方根
  Q_t: sum_{k=1}^t G_k^{-2}
  R: 初始点到最优点的距离上界
  T: 总训练步数
  eta_t: 第 t 步学习率
standard_notation:
  eta_t: 第 t 步学习率
  R: 初始点到最优点的距离上界
  G_t: 第 t 步梯度模长二阶矩平方根
  Q_t: sum_{k=1}^t G_k^{-2}
  T: 总训练步数
conditions: 动态梯度界、Q_t=sum_{k=1}^t G_k^{-2}；直接形式不满足在线因果。
derived_from: null
implies: null
appears_in:
- '[[让炼丹更科学一些（五）：基于梯度精调学习率]]'
- '[[让炼丹更科学一些（六）：自上而下的精妙构造]]'
evidence_spans:
- ev::11530::集大成者
- ev::11540::最强结论
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-09-让炼丹更科学一些-五-基于梯度精调学习率.md
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-16-让炼丹更科学一些-六-自上而下的精妙构造.md
source_ids:
- '9902'
- '11469'
- '11480'
- '11494'
- '11530'
- '11540'
status: draft
updated: "2026-06-14"
---

# Warmup-Decay最优学习率


## 概述

（待补充）

## 公式本体

```tex
\eta_t=\frac{R G_t^{-2}}{\sqrt{Q_T}}(1-Q_t/Q_T)
```

## 成立条件

动态梯度界、Q_t=sum_{k=1}^t G_k^{-2}；直接形式不满足在线因果。

## 推导来源

- `ev::11530::集大成者`
- `ev::11540::最强结论`

## 详细说明

Warmup-Decay最优学习率公式 $$\eta_t=\frac{R G_t^{-2}}{\sqrt{Q_T}}(1-Q_t/Q_T)$$ 为深度学习中广泛采用的“先预热后衰减”学习率调度策略提供了坚实的数学理论支撑。在优化随机梯度下降（SGD）以最小化终点损失而非平均损失的严谨推导中，该公式展示了最优学习率设计的两个核心维度：首先，学习率的大小应当反比于当前时刻梯度的模长平方（即正比于 $G_t^{-2}$），这解释了为什么在训练初期梯度剧烈震荡时需要较小的学习率进行 Warmup；其次，包含累积梯度信息比率的系数 $(1-Q_t/Q_T)$ 是一个严格单调递减函数，当梯度模长趋于稳定时，该项自然退化为经典的线性衰减（Linear Decay）策略。尽管其精确形式依赖于全局梯度累积量 $Q_T$ 从而不满足在线因果律，但它为利用历史梯度平方和 $Q_t$ 进行因果近似与自适应学习率优化器（如 AdaGrad 和 Adam）的设计指明了收敛方向。
