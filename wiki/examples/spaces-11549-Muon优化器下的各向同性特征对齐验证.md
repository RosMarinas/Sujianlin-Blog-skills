---
type: example
title: spaces-11549-Muon优化器下的各向同性特征对齐验证
article_id: 11549
article:
- - spaces-11549-各向同性最速下降理解
section: SGD之外
claim: 在各向同性输入（X X^T = c I）下，使用满秩谱范数最速下降 Muon 优化器进行参数更新，可导致特征空间输出变化量精确对齐到特征层面的最速下降
notation_mapping:
  X: X (输入特征 Gram 矩阵 X X^T = I)
  dL_dY: dL/dY (输出损失梯度矩阵)
  Delta_Y: Delta Y (特征空间变化量)
steps:
- 在无动量的 Muon 步中写出参数更新关系： Delta W = -eta * msign(X^T * dL/dY)
- 利用线性乘积，求出输出特征的变化量： Delta Y = -eta * X * msign(X^T * dL/dY)
- 将矩阵符号函数展开表示为： msign(M) = M * (M^T * M)^-0.5，其中 M = X^T * dL/dY
- 代入 Gram 各向同性假设 X * X^T = I，代回化简括号项： (M^T * M) = (dL/dY^T * X * X^T * dL/dY) = dL/dY^T
  * dL/dY
- 将化简结果代回 Delta Y 的表达式： Delta Y = -eta * X * X^T * dL/dY * (dL/dY^T * dL/dY)^-0.5
  = -eta * dL/dY * (dL/dY^T * dL/dY)^-0.5 = -eta * msign(dL/dY)
- 观察可知，Delta Y 精确等于特征层面的 msign 更新，即实现了参数最速下降与特征最速下降在流形几何上的完全重合
used_concepts:
- - - 各向同性特征
used_propositions:
- - - 各向同性对齐参数与特征最速下降
used_methods:
- - - 最速下降双层对齐法
source_span: ev::11549::SGD之外
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2026-01-20-为什么我们偏爱各向同性-基于最速下降的理解.md
source_ids:
- 11549
status: stable
updated: '2026-06-12'
---

## 问题

源文在“SGD之外”一节把 Muon 更新放到线性层输出 $\boldsymbol{Y}=\boldsymbol{X}\boldsymbol{W}$ 上考察：如果输入特征满足各向同性，参数空间里的谱范数最速下降是否也能成为特征空间里的谱范数最速下降？

## 推导

没有动量的 Muon 写作
$$
\boldsymbol{W}\leftarrow \boldsymbol{W}-\eta\,\mathrm{msign}\left(\boldsymbol{X}^{\top}\frac{\partial\mathcal{L}}{\partial\boldsymbol{Y}}\right).
$$
源文使用 $\mathrm{msign}(\boldsymbol{M})=\boldsymbol{M}(\boldsymbol{M}^{\top}\boldsymbol{M})^{-1/2}$ 展开输出变化量，得到 $\Delta\boldsymbol{Y}$ 中夹着 $\boldsymbol{X}\boldsymbol{X}^{\top}$。当 $\boldsymbol{X}\boldsymbol{X}^{\top}\approx\boldsymbol{I}$ 时，它化简为
$$
\Delta\boldsymbol{Y}\approx-\eta\,\mathrm{msign}\left(\frac{\partial\mathcal{L}}{\partial\boldsymbol{Y}}\right).
$$

## 方法与证据

这个例子体现的是“把优化器更新转写到特征输出层，再利用结构假设化简”的方法。证据来自 `ev::11549::SGD之外`：源文明确比较 Muon 与 SignSGD，并指出只有在各向同性输入下，参数上的谱范数最速下降才约等于特征上的谱范数最速下降。
