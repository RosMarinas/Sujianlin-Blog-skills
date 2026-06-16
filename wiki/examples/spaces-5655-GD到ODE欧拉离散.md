---
type: example
title: spaces-5655-GD到ODE欧拉离散
aliases: []
article_id: '5655'
article:
- - 从动力学角度看优化算法（一）：从SGD到动量加速
section: GD与ODE
claim: GD 更新可作为梯度流 ODE 的欧拉离散。
notation_mapping:
  theta: boldsymbol{theta}
  L: L
  t: t
steps:
- 从离散 GD 更新写出差分商
- 让差分商近似连续时间导数
- 得到梯度流 ODE
- 把原更新解释为欧拉法
used_concepts:
- - - 梯度流
- - - 优化动力学视角
used_formulas:
- - - 梯度流ODE公式
used_methods:
- - - 把优化算法解释为动力系统离散化
problem_pattern:
- - 把优化器经验现象改写为动力系统问题
source_span: ev::5655::GD与ODE
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2018-06-27-从动力学角度看优化算法-一-从SGD到动量加速.md
source_ids:
- '5655'
status: stable
updated: '2026-06-12'
---

# spaces-5655-GD到ODE欧拉离散

## 问题

源文“GD与ODE”从动力学角度解释梯度下降：离散更新为什么可以看成某个连续时间系统的数值解法。

## 推导

全量梯度下降写作
$$
\boldsymbol{\theta}_{n+1}
=\boldsymbol{\theta}_n-\gamma\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta}_n).
$$
由于通常 $\gamma\ll1$，源文把它改写成差分商
$$
\frac{\boldsymbol{\theta}_{n+1}-\boldsymbol{\theta}_n}{\gamma}
=-\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta}_n).
$$
把左侧近似为连续时间导数，就得到梯度流 ODE：
$$
\dot{\boldsymbol{\theta}}
=-\nabla_{\boldsymbol{\theta}}L(\boldsymbol{\theta}).
$$
原来的离散 GD 更新正是这个 ODE 的欧拉解法。

## 方法与证据

本例体现“差分商连续化，把优化迭代解释为动力系统离散化”的方法。证据锚点为 `ev::5655::GD与ODE`，源文还指出该系统是不动点收敛视角的基础：稳定不动点对应极小值点，但未必是全局最小值。
