---
type: proposition
title: 梯度平方滑动平均近似对角Hessian
statement: '在损失函数最优点 $\boldsymbol{\theta}^*$ 附近，梯度的平方期望与对角 Hessian 矩阵的平方成正比。因此，自适应学习率优化器中梯度平方的滑动平均的算术平方根 $\sqrt{\hat{\boldsymbol{v}}_t}$ 构成了对角 Hessian 矩阵的有效估计，使此类算法可等效对应于二阶牛顿法。'
assumptions:
  - '待优化模型在最优点附近作缓慢的随机打转，其参数偏差 $\boldsymbol{\theta} - \boldsymbol{\theta}^*$ 可建模为各向同性高斯随机变量 $\mathcal{N}(\boldsymbol{0}, \sigma^2 \boldsymbol{I})$；最优点梯度 $\boldsymbol{g}_{\boldsymbol{\theta}^*} = \boldsymbol{0}$；且 Hessian 矩阵满足对角化近似。'
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-11-29-从Hessian近似看自适应学习率优化器.md
source_ids:
  - "10588"
requires:
  - "[[Hessian期望近似公式]]"
  - "[[Hessian近似自适应学习率]]"
proof_route: |
  1. 对当前梯度向量进行一阶泰勒展开：$\boldsymbol{g}_{\boldsymbol{\theta}} \approx \boldsymbol{g}_{\boldsymbol{\theta}^*} + \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}(\boldsymbol{\theta} - \boldsymbol{\theta}^*)$。
  2. 利用最优点性质 $\boldsymbol{g}_{\boldsymbol{\theta}^*} = \boldsymbol{0}$，化简得到：$\boldsymbol{g}_{\boldsymbol{\theta}} \approx \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}(\boldsymbol{\theta} - \boldsymbol{\theta}^*)$。
  3. 计算梯度外积的统计期望：
     $\mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\boldsymbol{g}_{\boldsymbol{\theta}}^\top] \approx \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}\mathbb{E}[(\boldsymbol{\theta} - \boldsymbol{\theta}^*)(\boldsymbol{\theta} - \boldsymbol{\theta}^*)^\top]\boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}^\top$。
  4. 带入各向同性方差假设 $\mathbb{E}[(\boldsymbol{\theta} - \boldsymbol{\theta}^*)(\boldsymbol{\theta} - \boldsymbol{\theta}^*)^\top] = \sigma^2 \boldsymbol{I}$，化简为：
     $\mathbb{E}[\boldsymbol{g}_{\boldsymbol{\theta}}\boldsymbol{g}_{\boldsymbol{\theta}}^\top] \approx \sigma^2 \boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}\boldsymbol{\mathcal{H}}_{\boldsymbol{\theta}^*}^\top$。
  5. 提取对角线分量，可得：$\text{diag}(\mathbb{E}[\boldsymbol{g}\odot\boldsymbol{g}]) \approx \sigma^2 \text{diag}(\boldsymbol{\mathcal{H}}^2)$。
  6. 两边求算术平方根，得出对角 Hessian 分量的解析估计形式：$\boldsymbol{\mathcal{H}} \approx \frac{1}{\sigma}\text{diag}(\sqrt{\mathbb{E}[\boldsymbol{g}\odot\boldsymbol{g}]})$。由于 $\hat{\boldsymbol{v}}_t$ 是二阶矩的滑动平均估计，进而证明了 $\sqrt{\hat{\boldsymbol{v}}_t}$ 对应于 Hessian 估计的正确性。
evidence_spans:
  - "ev::10588::梯度近似"
status: draft
updated: 2026-06-11
---

## 理论调和（Gauss-Newton 与 Adam）

经典的 Gauss-Newton 近似给出的 Hessian 估计为 $\boldsymbol{\mathcal{H}} \approx \mathbb{E}[\boldsymbol{\mathcal{J}}\boldsymbol{\mathcal{J}}^\top]$，而在残差为零均值噪声下可化为 $\boldsymbol{g}\boldsymbol{g}^\top \approx \sigma^2 \boldsymbol{\mathcal{H}}$，它没有根号项。

本命题指出，这两种近似的差异在于时间尺度的不同。Gauss-Newton 提供的是**瞬时估计**（不含时间维度的平滑），而 Adam/RMSprop 的 $\hat{\boldsymbol{v}}_t$ 采用的是**长期的时间滑动平均**。在随机物理轨迹的长期平均演化下，噪声的相消效应使得最终表现多出了半阶的乘幂，即表现为平方根的关系。
