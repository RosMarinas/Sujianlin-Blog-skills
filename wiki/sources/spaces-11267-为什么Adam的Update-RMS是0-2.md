---
type: article_summary
title: 为什么Adam的Update RMS是0.2？
article_id: "11267"
source_url: https://spaces.ac.cn/archives/11267
date: 2025-09-02
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-09-02-为什么Adam的Update-RMS是0-2.md
source_ids:
  - "11267"
status: draft
updated: 2026-06-11
---

# 为什么Adam的Update RMS是0.2？

本文探讨了在大规模 LLM 训练中观察到的一个稳定现象：在训练正式开始后，Adam 优化器的更新均方根（Update RMS）总是稳定在 0.2~0.3 之间。作者通过数值模拟和理论推导，给出了这现象的物理解释与数学解析解。

## 主要内容

1. **更新均方根（Update RMS）定义**：
   - 设更新向量 $\boldsymbol{u}_t = \hat{\boldsymbol{m}}_t / (\sqrt{\hat{\boldsymbol{v}}_t} + \epsilon)$，其二阶均方根为 $\Vert \boldsymbol{u}_t \Vert_{RMS} = \sqrt{\text{mean}(\boldsymbol{u}_t^2)}$。

2. **纯噪声数值模拟**：
   - 假定单次梯度的信噪比极小，以至于单步梯度可被近似模拟为纯高斯噪声 $\boldsymbol{g}_t \sim \mathcal{N}(\boldsymbol{0}, \boldsymbol{I})$。
   - 模拟在超参数为 $\beta_1=0.9, \beta_2=0.95$ 时，得到的稳态 $\Vert \boldsymbol{u}_t \Vert_{RMS}$ 约为 0.225，与实际 LLM 训练监控曲线高度一致。

3. **平均场近似推导**：
   - 设 $t \to \infty$ 稳态。利用平均场近似 $\mathbb{E}[\boldsymbol{u}_t^2] \approx \frac{\mathbb{E}[\boldsymbol{m}_t^2]}{\mathbb{E}[\boldsymbol{v}_t]}$。
   - 假定 $\mathbb{E}[\boldsymbol{g}]=\boldsymbol{\mu}, \mathbb{E}[\boldsymbol{g}^2]=\boldsymbol{\mu}^2+\boldsymbol{\sigma}^2$。可分别求得：
     $$\mathbb{E}[\boldsymbol{v}_t] \approx \boldsymbol{\mu}^2 + \boldsymbol{\sigma}^2$$
     $$\mathbb{E}[\boldsymbol{m}_t^2] = \mathbb{E}[\boldsymbol{m}_t]^2 + \mathbb{V}ar[\boldsymbol{m}_t] \approx \boldsymbol{\mu}^2 + \frac{1 - \beta_1}{1 + \beta_1}\boldsymbol{\sigma}^2$$
   - 最终推导出 Update RMS 的解析表达式：
     $$\Vert\boldsymbol{u}_t\Vert_{RMS} \approx \sqrt{\frac{\Vert\boldsymbol{\mu}\Vert^2/\Vert\boldsymbol{\sigma}\Vert^2 + \frac{1 - \beta_1}{1 + \beta_1}}{\Vert\boldsymbol{\mu}\Vert^2/\Vert\boldsymbol{\sigma}\Vert^2 + 1}}$$
   - **结果分析**：
     - 在纯噪声情况（信噪比 $\text{SNR} = 0$）下，公式简化为 $\sqrt{\frac{1-\beta_1}{1+\beta_1}}$。对于 $\beta_1=0.9$，该值计算为 $\sqrt{0.1/1.9} \approx 0.2294$，与模拟值 0.225 极度接近。
     - 该公式表明，Update RMS 仅与动量超参数 $\beta_1$ 和梯度的信噪比（SNR）相关，而与 $\beta_2$ 几乎无关。

4. **应用场景**：
   - **Match Adam Update RMS 迁移法**：将其他没有二阶矩归一化的优化器（如 Muon）的更新步 RMS 统一设置为 0.2，即可无缝复用 Adam 调好的学习率和权重衰减。
   - **反向估计梯度信噪比**：可通过实际测量的 Update RMS（或者带动量优化器的 $\Vert\boldsymbol{m}_t\Vert/\Vert\boldsymbol{g}_t\Vert$ 比值）反向计算得到当前训练阶段的梯度信噪比 $\Vert\boldsymbol{\mu}\Vert^2/\Vert\boldsymbol{\sigma}\Vert^2$。
