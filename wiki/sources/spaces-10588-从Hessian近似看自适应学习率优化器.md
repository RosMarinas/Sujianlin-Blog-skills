---
type: article_summary
title: 从Hessian近似看自适应学习率优化器
article_id: "10588"
source_url: https://spaces.ac.cn/archives/10588
date: 2024-11-29
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-11-29-从Hessian近似看自适应学习率优化器.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-11-29-从Hessian近似看自适应学习率优化器.md
source_ids:
  - "10588"
status: draft
updated: 2026-06-11
---

# 从Hessian近似看自适应学习率优化器

本文介绍了自适应学习率优化器（如 Adam, RMSprop）在 Newton 法框架下的新视角，阐释了梯度平方的滑动平均与 Hessian 矩阵平方的关系。

## 主要内容

1. **自适应优化器与 Newton 法**：
   - 二阶 Newton 法更新规则为：$\boldsymbol{\theta}_{t+1} = \boldsymbol{\theta}_t - \boldsymbol{\mathcal{H}}_t^{-1}\boldsymbol{g}_t$。
   - 在此视角下，SGD 假设 Hessian 矩阵是各向同性的 $\boldsymbol{\mathcal{H}}_t = \eta_t^{-1}\boldsymbol{I}$。
   - Adam 则相当于假设了一个对角 Hessian 矩阵 $\boldsymbol{\mathcal{H}}_t = \eta_t^{-1} \text{diag}(\sqrt{\hat{\boldsymbol{v}}_t} + \epsilon)$。

2. **梯度一阶近似与 Hessian 关联**：
   - 考虑在最优点 $\boldsymbol{\theta}^*$ 处的梯度一阶展开（此处最优梯度 $\boldsymbol{g}_{\boldsymbol{\theta}^*} = \boldsymbol{0}$）：
     $$\boldsymbol{g}_{\boldsymbol{\theta}} \approx \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*} (\boldsymbol{\theta} - \boldsymbol{\theta}^*)$$
   - 若将偏离最优点打转时的参数偏差 $\boldsymbol{\theta} - \boldsymbol{\theta}^*$ 视为各向同性的高斯随机变量 $\mathcal{N}(\boldsymbol{0}, \sigma^2 \boldsymbol{I})$，则其梯度的外积期望为：
     $$\mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\boldsymbol{g}_{\boldsymbol{\theta}}^\top] \approx \sigma^2 \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*} \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}^\top$$
   - 假设 Hessian 是对角阵，可得：
     $$\boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*} \approx \frac{1}{\sigma} \text{diag}\left(\sqrt{\mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\odot\boldsymbol{g}_{\boldsymbol{\theta}}]}\right)$$
   - 这表明，Adam 的 $\hat{\boldsymbol{v}}_t$（对梯度平方的滑动平均）实际上是在近似 $\mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\odot\boldsymbol{g}_{\boldsymbol{\theta}}]$，从而 $\eta_t^{-1}\text{diag}(\sqrt{\hat{\boldsymbol{v}}_t})$ 是 Hessian 矩阵的合理近似。
   - **超参数含义**：该理论解释了为何自适应优化器中 $\beta_2$（估计 Hessian）应接近 1 以保留长期平均，而 $\beta_1$（估计动量）应相对小以防止长期平均导致动量归零。

3. **与 Gauss-Newton Hessian 近似的对比**：
   - Gauss-Newton 法基于 Jacobi 矩阵外积进行 Hessian 近似，得出 $\boldsymbol{g}_{\boldsymbol{\theta}} \boldsymbol{g}_{\boldsymbol{\theta}}^\top \approx \sigma^2 \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}_t}$。
   - 该式与上述期望公式 $\mathbb{E}[\boldsymbol{g}\boldsymbol{g}^\top] \approx \sigma^2 \boldsymbol{\mathcal{H}}^2$ 相比，差了一个根号/平方。
   - **理论调和**：Gauss-Newton 提供的是瞬时近似（不含平均），而 Adam 估计的是时间步的“长期平均”结果。类似于随机微分方程（SDE）中，由于随机噪声的长期平均抵消效应，噪声强度项相较于非噪声项在阶数上会高出半阶（反映在算子中即为一个根号）。

4. **与 AdaBelief 的关联**：
   - 若 $\boldsymbol{\theta}^*$ 不是全局最优点而是任意点（梯度不为 0），则应当使用协方差形式：
     $$\mathbb{E}[(\boldsymbol{g}_{\boldsymbol{\theta}} - \boldsymbol{g}_{\boldsymbol{\theta}^*})(\boldsymbol{g}_{\boldsymbol{\theta}} - \boldsymbol{g}_{\boldsymbol{\theta}^*})^\top] \approx \sigma^2 \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*} \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}^\top$$
   - 这恰好对应了 AdaBelief 优化器（使用 $\boldsymbol{g}_t - \boldsymbol{m}_t$ 的平方滑动平均作为分母）的理论基础。
