---
type: example
title: spaces-10878-SVD等效前向梯度
aliases: []
article_id: '10878'
article:
- - SVD的导数
section: 梯度（一）
claim: 用 stop_gradient 构造前向值相同的表达以保留 SVD 奇异值梯度。
notation_mapping:
  sigma_i: sigma_i
  u_i: boldsymbol{u}_i
  v_i: boldsymbol{v}_i
steps:
- 先由微分确定奇异值梯度
- 把 sigma_i 替换为 sg(u_i)^T W sg(v_i)
- 保持前向值不变
- 让自动求导沿 W 计算梯度
used_concepts:
- - - SVD可导性
used_formulas:
- - - SVD等效前向梯度公式
used_methods:
- - - 用等效前向表达保留SVD梯度
problem_pattern:
- - 把表示学习模型改写为矩阵分解问题
source_span: ev::10878::梯度一
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-04-26-SVD的导数.md
source_ids:
- '10878'
status: stable
updated: '2026-06-12'
---

# spaces-10878-SVD等效前向梯度

## 问题

源文“梯度（一）”面对的问题是：SVD 微分已经能写出 $d\boldsymbol{U},d\boldsymbol{\Sigma},d\boldsymbol{V}$，但直接表达 $\boldsymbol{U}$ 或奇异值关于 $\boldsymbol{W}$ 的完整梯度会涉及高阶张量。如何让自动求导框架得到正确梯度，同时保持前向值不变？

## 推导

源文先由对角部分得到
$$
d\sigma_i=\boldsymbol{u}_i^{\top}(d\boldsymbol{W})\boldsymbol{v}_i.
$$
因此 $\sigma_i$ 对 $\boldsymbol{W}$ 的梯度等价于
$$
\mathrm{sg}[\boldsymbol{u}_i]^{\top}\boldsymbol{W}\,\mathrm{sg}[\boldsymbol{v}_i]
$$
对 $\boldsymbol{W}$ 的梯度。又因为前向数值上 $\sigma_i=\boldsymbol{u}_i^{\top}\boldsymbol{W}\boldsymbol{v}_i$，所以代码里可把 $\boldsymbol{\Sigma}$ 替换为
$$
\boldsymbol{I}\otimes(\mathrm{sg}[\boldsymbol{U}]^{\top}\boldsymbol{W}\,\mathrm{sg}[\boldsymbol{V}]).
$$
源文进一步给出 $\boldsymbol{U}$、$\boldsymbol{V}$ 的等效替换式，利用 stop_gradient 固定 SVD 结果，仅让梯度沿 $\boldsymbol{W}$ 传播。

## 方法与证据

本例体现“由微分构造等效前向表达，再交给自动求导”的方法。证据锚点为 `ev::10878::梯度一`，源文明确说这些替换保持正确前向结果，同时获得正确梯度。
