---
type: example
title: spaces-10657-Adam优化器梯度裁剪步长分析
article_id: 10657
article:
- - spaces-10657-梯度裁剪默认模长为1
section: 怎么办
claim: 在 Adam 优化器中，由于更新向量服从符号约束，其单步泰勒损失改变量正比于参数维度的平方根，因而模型增大到 4 倍参数时学习率需减半以保持稳定性
notation_mapping:
  u_t: u_t (Adam 的单步参数更新向量，近似表示为 sign(g_t))
  N: N (模型全体参数的总数量)
  g_t: g_t (梯度向量)
steps:
- 写出泰勒一阶损失变化近似关系： Delta L = -eta * u_t . g_t
- 在 Adam 中将更新方向用符号函数进行近似代换： u_t = sign(g_t)
- 利用内积性质展开： u_t . g_t = sign(g_t) . g_t = ||g_t||_1
- 在没有零梯度分量的假设下，利用单位方向几何投影关系，写出 L1 范数与 L2 范数的关系： ||g_t||_1 = sqrt(N) * ||g_t|| * cos(sign(g_t),
  g_t)
- 观察可知损失改变量 Delta L 包含项 sqrt(N)。由于实验发现梯度范数与夹角余弦在不同尺度下均偏向常数，为维持 Delta L 在平稳范围，学习率 eta
  必须反比于参数量的平方根 sqrt(N)
used_concepts:
- - - 梯度裁剪
used_formulas:
- - - 梯度裁剪更新公式
used_methods:
- - - 基于内积自适应步长裁剪法
source_span: ev::10657::怎么办
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-01-02-为什么梯度裁剪的默认模长是1.md
source_ids:
- 10657
status: stable
updated: '2026-06-12'
---

## 问题

源文“怎么办”一节从梯度裁剪默认模长为 1 的现象出发，进一步分析 Adam 类优化器在参数量变大时学习率应如何缩放，才能保持单步损失变化量稳定。

## 推导

一般更新 $\boldsymbol{\theta}_{t+1}=\boldsymbol{\theta}_t-\eta\boldsymbol{u}_t$ 下，一阶泰勒近似给出
$$
\Delta\mathcal{L}\approx-\eta\,\boldsymbol{u}_t\cdot\boldsymbol{g}_t.
$$
对 Adam 等优化器，源文用 $\boldsymbol{u}_t=\mathrm{sign}(\boldsymbol{g}_t)$ 近似，因此
$$
\Delta\mathcal{L}=-\eta\,\mathrm{sign}(\boldsymbol{g}_t)\cdot\boldsymbol{g}_t=-\eta\Vert\boldsymbol{g}_t\Vert_1.
$$
再写成
$$
\Delta\mathcal{L}=-\eta\sqrt{N}\Vert\boldsymbol{g}_t\Vert\cos(\mathrm{sign}(\boldsymbol{g}_t),\boldsymbol{g}_t),
$$
其中 $N$ 是模型总参数量。若 $\Vert\boldsymbol{g}_t\Vert$ 和夹角余弦在不同模型尺度下近似为常数，为维持 $\Delta\mathcal{L}$ 不变，就应有 $\eta\propto1/\sqrt{N}$。

## 方法与证据

本例体现“把 Adam 更新近似为符号方向，再用一阶损失变化推学习率缩放”的方法。证据锚点为 `ev::10657::怎么办`，源文明确给出参数量增加到 4 倍时学习率可考虑减半。
