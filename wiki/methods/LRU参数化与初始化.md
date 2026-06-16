---
type: method
title: LRU参数化与初始化
aliases:
  - LRU Initialization Method
operation_types:
  primary: Align / calibrate by invariance
  secondary:
    - Rewrite / identity transform
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
method_summary: |
  通过对复对角化转移系数进行双重指数无约束参数化、复平面圆环均匀采样初始化，并结合 element-wise 的缩放因子 $\gamma$，实现LRU模型在初始阶段状态向量的模长稳定性并防止梯度消失或爆炸。
typical_structure: |
  1. 将特征值表示为极坐标：$\lambda = r e^{i\theta}$
  2. 将模长参数化为无约束优化形式：$r = e^{-\nu}$，其中 $\nu = e^{\nu^{\log}}$
  3. 相位参数化：$\theta = e^{\theta^{\log}}$
  4. 在圆环内初始化采样：$\theta \sim U[0, 2\pi]$，$r^2 \sim U[r_{\min}^2, r_{\max}^2]$，$r_{\min}=0.9, r_{\max}=0.999$
  5. 计算稳定缩放系数 $\gamma = \sqrt{1 - r^2}$
applicability: 在设计或实现线性RNN层（如LRU）并需要在大模型或长序列训练中确保数值稳定性与极佳的收敛效率时使用。
tools:
  - 双重指数参数化
  - 复平面圆环采样
  - 模长稳定初始化
related_methods:
  - [[LRU并行化递归算法]]
  - [[非线性RNN摄动并行化]]
  - [[可逆残差网络前向与逆迭代]]
examples:
  - [[article::9554]]
status: draft
updated: 2026-06-14
---

## 适用问题

线性递归单元（LRU）的复值转移系数 $\lambda$ 在训练过程中容易产生梯度消失（$|\lambda| \ll 1$）或梯度爆炸（$|\lambda| \gg 1$）。同时，参数 $\lambda$ 的约束形式（$|\lambda| < 1$ 以保证稳定性）使得无约束优化无法直接使用。LRU 参数化与初始化方法通过双重指数参数化和复平面圆环采样，实现了稳定且高效的长序列建模。

## 核心变换

**输入**：复值转移系数 $\lambda$，输入缩放系数 $\gamma$
**输出**：无约束参数化形式，适合梯度下降优化
**核心**：双重指数确保 $|\lambda| < 1$ 且可微

LRU 的递归方程（复数标量形式）：
$$
x_t = \lambda x_{t-1} + \gamma u_t
$$

### 参数化

将特征值表示为极坐标 $\lambda = r e^{i\theta}$。模长 $r$ 的无约束参数化：
$$
r = e^{-\nu}, \quad \nu = e^{\nu^{\log}}
$$

相位 $\theta$ 的无约束参数化：
$$
\theta = e^{\theta^{\log}}
$$

稳定性缩放系数：
$$
\gamma = \sqrt{1 - r^2}
$$

### 初始化

在复平面圆环内进行特征值初始化采样：
$$
\theta \sim U[0, 2\pi], \quad r^2 \sim U[r_{\min}^2, r_{\max}^2]
$$

其中常规选择 $r_{\min} = 0.9$，$r_{\max} = 0.999$。

## 典型步骤

1. **极坐标表示**：将复数转移系数写为 $\lambda = r e^{i\theta}$
2. **双重指数参数化**：$r = \exp(-\exp(\nu^{\log}))$，使得 $r$ 自动保持在 $(0, 1)$ 区间
3. **相位参数化**：$\theta = \exp(\theta^{\log})$，确保相位在正实数域优化
4. **圆环初始化**：在 $r \in [0.9, 0.999]$、$\theta \in [0, 2\pi]$ 内采样
5. **设置缩放系数**：$\gamma = \sqrt{1 - r^2}$，使初始状态模长稳定

## 直觉

核心思想：**用数学约束替代手工调参**。

LRU 的稳定性要求 $|\lambda| < 1$——这就像在优化空间中心画了一个半径为 1 的圆，所有可行解必须在圆内。双重指数参数化 $r = \exp(-\exp(\nu^{\log}))$ 将 $r$ 自动约束在 $(0, 1)$ 区间内，同时保持梯度畅通：$\nu^{\log}$ 的任何实数值都对应一个合法的 $r$。

初始化时在 $r \in [0.9, 0.999]$ 的圆环内采样，意味着初始转移系数具有"长记忆"——状态可以传递较远的步数而不衰减。$\gamma = \sqrt{1 - r^2}$ 源于能量守恒：如果转移系数接近 1（长记忆），则需要较小的输入缩放来防止累积膨胀。

## 边界

- 双重指数参数化可能带来数值问题：$r$ 极接近 1 时 $\nu^{\log}$ 需要非常大
- 复值参数化适用于对角线 LRU，全矩阵 LRU 需使用不同的参数化策略
- $r_{\min}=0.9$ 和 $r_{\max}=0.999$ 是经验值——对不同序列长度和任务可能需要调整
- $\gamma = \sqrt{1 - r^2}$ 仅在输入 $u_t$ 为白噪声时严格成立

## 例子

- LRU 在语言模型任务上使用该参数化方法，长序列建模（8192 tokens）稳定收敛
- 与 RWKV 等线性 RNN 架构相比，LRU 的复值参数化提供了更丰富的动态范围
- $r$ 接近 0.999 的维度负责建模长期依赖，$r$ 接近 0.9 的维度负责建模短期依赖

## 证据

- ev::9554::双重指数参数化：$r = \exp(-\exp(\nu^{\log}))$
- ev::9554::稳定缩放系数：$\gamma = \sqrt{1 - r^2}$
- ev::9554::圆环初始化：$r^2 \sim U[0.9^2, 0.999^2]$
