---
type: example
title: spaces-11486-EFLA连续动力学求导
article_id: 11486
article:
- - spaces-11486-DeltaNet的L2-Normalize解释
section: 连续视角
claim: 通过对 DeltaNet 的连续时间一阶微分方程求出解析解，可以使用秩为 1 的矩阵指数公式将 EFLA 递归更新公式还原
notation_mapping:
  S_t: S_t (循环状态矩阵)
  k_t: k_t (Key 投影向量)
  v_t: v_t (Value 投影向量)
  A_t: A_t (秩为 1 的转移矩阵 -k_t * k_t^T)
steps:
- 写出一阶状态微分控制方程： dS_t/dt = S_t * A_t + v_t * k_t^T，其中 A_t = -k_t * k_t^T
- 对区间 [t-eta_t, t] 积分，求得解析解公式： S_t = S_{t-1} * exp(eta_t * A_t) + B_t * A_t^-1 * (exp(eta_t
  * A_t) - I)，其中 B_t = v_t * k_t^T
- 应用秩为 1 的矩阵指数特征公式： exp(eta_t * A_t) = exp(-eta_t * k_t * k_t^T) = I - (1 - e^(-eta_t
  ||k_t||^2)) * (k_t * k_t^T) / ||k_t||^2
- 代入 B_t * A_t^-1 展开化简： B_t * A_t^-1 * (exp(eta_t * A_t) - I) = (1 - e^(-eta_t ||k_t||^2))
  * (v_t * k_t^T) / ||k_t||^2
- 将化简后的项合并，可得到 EFLA 递归式： S_t = S_{t-1} ( I - (1 - e^(-eta_t ||k_t||^2)) * (k_t * k_t^T)
  / ||k_t||^2 ) + (1 - e^(-eta_t ||k_t||^2)) * (v_t * k_t^T) / ||k_t||^2
used_concepts:
- - - EFLA
used_formulas:
- - - EFLA递归更新公式
used_methods:
- - - 连续动力学精确解递归法
source_span: ev::11486::连续视角
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2025-12-23-为什么DeltaNet要加L2-Normalize.md
source_ids:
- 11486
status: stable
updated: '2026-06-12'
---

## 问题

源文“连续视角”把 DeltaNet 的递归看成连续时间微分方程在区间 $[t-\eta_t,t]$ 上的离散化，并用精确解解释 EFLA 为什么会自然出现 L2 Normalize 形式。

## 推导

文章先写出常系数线性方程
$$
\frac{d}{dt}\boldsymbol{S}_t=\boldsymbol{S}_t(-\boldsymbol{k}_t\boldsymbol{k}_t^{\top})+\boldsymbol{v}_t\boldsymbol{k}_t^{\top}.
$$
令 $\boldsymbol{A}_t=-\boldsymbol{k}_t\boldsymbol{k}_t^{\top}$、$\boldsymbol{B}_t=\boldsymbol{v}_t\boldsymbol{k}_t^{\top}$，精确解为
$$
\boldsymbol{S}_t=\boldsymbol{S}_{t-\eta_t}e^{\eta_t\boldsymbol{A}_t}+\boldsymbol{B}_t\boldsymbol{A}_t^{-1}(e^{\eta_t\boldsymbol{A}_t}-\boldsymbol{I}).
$$
由于 $\boldsymbol{A}_t$ 是秩 1 矩阵，源文用矩阵函数 $f(\boldsymbol{x}\boldsymbol{y}^{\top})$ 的级数化简，把矩阵指数转成标量函数，得到系数
$$
\frac{1-e^{-\eta_t\Vert\boldsymbol{k}_t\Vert^2}}{\Vert\boldsymbol{k}_t\Vert^2}.
$$

## 方法与证据

这个例子体现“把递归改写为 ODE，再用精确解和秩 1 矩阵函数化简”的方法。证据来自 `ev::11486::连续视角`：源文明确指出 EFLA 等价于把 $\eta_t$ 换成上述系数，分母中的 $\Vert\boldsymbol{k}_t\Vert^2$ 与 $\boldsymbol{k}_t\boldsymbol{k}_t^{\top}$ 相乘正好表现为对 $\boldsymbol{K}$ 的 L2 Normalize。
