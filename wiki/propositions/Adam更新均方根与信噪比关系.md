---
type: proposition
title: Adam更新均方根与信噪比关系
statement: '在训练稳态极限下，Adam/AdamW 优化器的更新均方根（Update RMS）可以通过平均场近似写为梯度信噪比 $\text{SNR} = \|\boldsymbol{\mu}\|^2 / \|\boldsymbol{\sigma}\|^2$ 与动量超参数 $\beta_1$ 的函数形式，该值在统计上与二阶矩衰减参数 $\beta_2$ 几乎无关。'
assumptions:
  - '模型处于训练稳态，时间步 $t \to \infty$ 使得偏差修正项可忽略；梯度各分量满足独立同分布假设，均值为 $\boldsymbol{\mu}$，方差为 $\boldsymbol{\sigma}^2$。'
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
source_ids:
  - "11267"
requires:
  - "[[Adam更新均方根公式]]"
  - "[[Adam更新RMS]]"
proof_route: |
  1. 将稳态下的更新项表示为 $\boldsymbol{u}_t = \boldsymbol{m}_t / \sqrt{\boldsymbol{v}_t}$。
  2. 引入平均场近似以估计平方期望：$\mathbb{E}[\boldsymbol{u}_t^2] \approx \frac{\mathbb{E}[\boldsymbol{m}_t^2]}{\mathbb{E}[\boldsymbol{v}_t]}$。
  3. 计算分母期望：展开 $\boldsymbol{v}_t$ 二阶矩级数，当 $t \to \infty$ 时，其收敛于 $\mathbb{E}[\boldsymbol{v}_t] \approx \boldsymbol{\mu}^2 + \boldsymbol{\sigma}^2$。该项与 $\beta_2$ 无关。
  4. 计算分子期望：将二阶矩拆分为期望的平方加方差：$\mathbb{E}[\boldsymbol{m}_t^2] = \mathbb{E}[\boldsymbol{m}_t]^2 + \mathbb{V}ar[\boldsymbol{m}_t]$。当 $t \to \infty$ 时，$\mathbb{E}[\boldsymbol{m}_t] \approx \boldsymbol{\mu}$，方差项对方差求级数和得到 $\mathbb{V}ar[\boldsymbol{m}_t] \approx \frac{1-\beta_1}{1+\beta_1}\boldsymbol{\sigma}^2$。
  5. 合并上述两式并代入均方根计算公式，通过 SNR 分子分母归一化化简得出：
     $$\|\boldsymbol{u}_t\|_{RMS} \approx \sqrt{\frac{\text{SNR} + \frac{1 - \beta_1}{1 + \beta_1}}{\text{SNR} + 1}}$$
     推导表明，此稳态值仅取决于 SNR 和 $\beta_1$，其二阶矩衰减率 $\beta_2$ 仅在过渡态有微弱影响，在稳态下被完全抵消。
evidence_spans:
  - "ev::11267::平均近似"
status: draft
updated: 2026-06-11
---

## 结论解析

该命题解释了为什么不同任务、不同尺度的模型在使用 Adam 优化器时，其 Update RMS 总是呈现出惊人的稳定性（多在 0.2~0.3 之间）。

由于实际深度网络训练中单步梯度的信噪比（SNR）极低，几乎可以近似为 0（纯噪声极限），此时 Update RMS 仅由动量超参 $\beta_1$ 决定。代入常用的 $\beta_1 = 0.9$，可求得极限下界为 $\sqrt{0.1/1.9} \approx 0.2294$。这为该经验观测值提供了完整的数学与物理学解释。
