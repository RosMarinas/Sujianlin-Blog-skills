---

type: method
operation_types:
  primary: Discrete ↔ continuous bridge
  secondary: []
title: Wasserstein梯度流
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-08-06-通向最优分布之路-概率空间的最小化.md
  - Data/wiki/sources/spaces-8512-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-正态分布距离.md
source_ids:
  - 10289
method_summary: 通过连续变量代换推导概率密度函数的梯度流方程：dp/dt = div[p * grad(delta F/delta p)]
typical_structure: |
  1. 通过变量代换 $\boldsymbol{x} \to \boldsymbol{x} - \eta \boldsymbol{\mu}_t(\boldsymbol{x})$ 构造迭代后的新分布 $p_{t+\eta}(\boldsymbol{x})$
  2. 利用积分和散度定理对泛函目标在极小扰动下的增量 $\mathcal{F}[p_{t+\eta}] - \mathcal{F}[p_t]$ 进行泰勒展开近似
  3. 选择能够使得泛函下降最快的“梯度”方向作为速度场 $\boldsymbol{\mu}_t(\boldsymbol{x}) = \nabla_{\boldsymbol{x}}\frac{\delta \mathcal{F}}{\delta p_t}$
  4. 取步长 $\eta \to 0$ 极限，得到控制概率密度函数演化的偏微分方程（连续化梯度流）
applicability: 概率空间的目标函数最小化、连续概率密度函数的无约束优化，在扩散模型、流匹配及能量生成模型中广泛使用。
tools: 
examples:
  - [[article::10289]]
status: stable
updated: 2026-06-13
cross_series_match: null
cross_series_match_reason: Wasserstein梯度流是概率空间优化中的核心方法，已在扩散模型等ML领域广泛使用。与现有[[梯度流]]方法共享相同的construct_auxiliary_sequence操作类型。
  - ev::10289::不需要显式引入 Wasserstein 距离，通过寻找使得泛函下降最快的变量代换方向，直接推导出了概率密度函数的梯度流偏微分方程及其对应的粒子运动常微分方程





---
## 适用问题

在函数优化中，若目标函数 $\mathcal{F}[p]$ 的自变量本身是一个连续的概率分布（如在生成模型中寻找最优分布），直接对 $p$ 求解梯度零点或执行无约束梯度下降会导致更新后的函数不再满足概率分布的要求（非负性、积分和为1）。此时需要一种能保证演化过程中始终维持概率密度特性的流体力学或最优传输的方法。

## 核心变换

将“分布上的直接加减更新”转换为“采样空间上的向量场偏移”。通过构造连续变量代换 $\boldsymbol{x} \to \boldsymbol{x} - \eta \boldsymbol{\mu}_t(\boldsymbol{x})$，并在 $\eta \to 0$ 时推导出控制概率分布 $p_t$ 随时间演化的连续偏微分方程（PDE）：
$$
\frac{\partial p_t}{\partial t} = \nabla\cdot\left[p_t\nabla\frac{\delta \mathcal{F}[p_t]}{\delta p_t}\right]
$$
同时等效于样本层面的常微分方程（ODE）：
$$
\frac{d\boldsymbol{x}_t}{dt} = - \nabla_{\boldsymbol{x}}\frac{\delta \mathcal{F}[p_t(\boldsymbol{x}_t)]}{\delta p_t(\boldsymbol{x}_t)}
$$
从而将分布优化问题转化为粒子的常微分方程积分问题。

## 典型步骤

1. **构造参数化扰动**：不再直接通过 $p_{t+\eta} = p_t - \eta \delta p$ 来下降，而是设计一个微小的空间映射变换 $\boldsymbol{x} \to \boldsymbol{x} - \eta \boldsymbol{\mu}_t(\boldsymbol{x})$。
2. **利用连续性方程计算变分**：计算代换前后目标泛函 $\mathcal{F}[p_{t+\eta}]$ 的变化。利用雅可比行列式展开或散度定理，保留至 $\eta$ 的一阶项。
3. **确定最陡下降场**：为保证目标泛函递减，选定使导数非正的向量场 $\boldsymbol{\mu}_t(\boldsymbol{x}) = \nabla_{\boldsymbol{x}} \frac{\delta \mathcal{F}}{\delta p_t}$。
4. **取极限得流方程**：令 $\eta \to 0$，即推导出概率分布演化的 Fokker-Planck 或 Wasserstein 梯度流偏微分方程，并给出实际中更易执行的粒子轨线 ODE。

## 直觉

无约束梯度的下降是沿着山坡“往下走”。但在概率空间中，如果要改变一个沙堆（概率分布）的形状来最小化某个能量泛函，不能凭空让沙堆在某处消失又在另一处出现，而是必须将沙子“推”过去。Wasserstein 梯度流就是描述这个推沙子的过程：它给出了每个质点应该沿着哪个方向、以多大的速度流动，才能保证不仅总土量守恒，且最终的沙堆形状使总能量下降最快。

## 边界

- **变分导数可计算性**：要求泛函 $\mathcal{F}[p]$ 对 $p$ 的变分（即泛函导数）存在且可求梯度。如果泛函极端非平滑，梯度场会发散。
- **微分方程求解误差**：将理论上的连续时间演化付诸实践时，需要通过欧拉法或更高阶的数值积分器（ODE/SDE Solvers）进行时间离散化，步长过大时会积累误差导致分布偏离。

## 例子

- **高斯分布降噪**：在扩散模型（Diffusion Models）的逆向过程中，从纯噪声分布到真实数据分布的逐步转化过程，可以等价看作是目标泛函包含数据似然与散度项时的 Wasserstein 梯度流求解，对应着 Score-based ODE。

## 证据

- **ev::10289::代数推导路径**：文章展示了无需依赖复杂的最优传输度量几何，仅通过简单的变量代换和泰勒展开，即可推导出严格的 Wasserstein 梯度流偏微分形式，降低了理解门槛。