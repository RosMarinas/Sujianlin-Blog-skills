---
type: concept
title: FD Loss
aliases:
- Fréchet Distance Loss
- Frechet Loss
definition: 将真实样本与生成样本在特定编码器特征层输出的均值向量和协方差矩阵代入 W-距离，直接作为生成模型端到端训练的损失函数。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
source_ids:
- 11738
status: draft
updated: '2026-06-12'
---

FD Loss（Fréchet Distance Loss）是指将真实样本与生成样本通过某个预训练好的编码器 $\phi$（如 InceptionV3、SigLIP 等）编码成特征向量 $\boldsymbol{z}=\phi(\boldsymbol{x})$ 后，估计各自的均值向量 $\boldsymbol{\mu}_p,\boldsymbol{\mu}_q$ 和协方差矩阵 $\boldsymbol{\Sigma}_p,\boldsymbol{\Sigma}_q$，并计算它们之间的正态分布差异（即 W-距离），将其直接作为生成模型端到端训练的损失函数。

其核心的数学定义为：
$$
\begin{aligned}
\mathcal{F}\triangleq\mathcal{W}_2^2[p,q]=&\,\Vert \boldsymbol{\mu}_p - \boldsymbol{\mu}_q\Vert^2 + \mathop{\text{tr}}(\boldsymbol{\Sigma}_p + \boldsymbol{\Sigma}_q - 2(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{1/2})
\end{aligned}
$$
当编码器选取为 InceptionV3 时，对应的结果即为著名的 FID（Fréchet Inception Distance）。

### 关键性质与梯度计算

FD 实际上是可导的，其作为 Loss 的主要技术难点在于矩阵的平方根与逆平方根求导，以及对大 Batch Size 的依赖。
生成分布的协方差矩阵 $\boldsymbol{\Sigma}_q$ 的梯度计算结果为：
$$
\nabla_{\boldsymbol{\Sigma}_q}\mathcal{W}_2^2[p,q] = \boldsymbol{I} - \boldsymbol{\Sigma}_p^{1/2}(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{-1/2}\boldsymbol{\Sigma}_p^{1/2}
$$
这要求对正定对称矩阵求平方根和逆平方根，可以通过 `eigh` 函数或 Newton-Schulz 迭代方案完成。

**边界条件与限制**：从上述梯度公式可以看出，如果 Batch Size 很小，估算出来的样本二阶矩 $\boldsymbol{V}_q$ 不满秩，从而导致 $\boldsymbol{\Sigma}_q$ 也不满秩。此时 $(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{-1/2}$ 的求逆便面临 $0^{-1/2}$ 的无解情况。由于需要跨样本做非线性运算，小 Batch 估计出来的 FD 是有偏的，且无法通过简单的梯度累积消除偏差。

### 关系与流式训练实现

FD Loss 与视觉中的**对比学习**有类似之处，均具有“需要跨样本做非线性运算”和“需要大 Batch Size”的特点。它与 **Perceptual Loss** 不同，后者主要作为样本级别的重构 Loss，不涉及跨样本的统计运算。

为了在受限算力下用小 Batch Size 模拟大 Batch Size 的效果（“Batch Size不够，历史来凑”），通常引入**滑动平均（EMA）**来缓慢更新均值和协方差矩阵：
$$
\boldsymbol{\mu}_q^{(t)} = \beta \boldsymbol{\mu}_q^{(t-1)} + (1-\beta) \tilde{\boldsymbol{\mu}}_q^{(t)},\qquad \boldsymbol{V}_q^{(t)} = \beta \boldsymbol{V}_q^{(t-1)} + (1-\beta) \tilde{\boldsymbol{V}}_q^{(t)}
$$
结合 stop gradient（$[\cdot]_{sg}$）算子，每一步可以按照以下等效损失求梯度进行流式更新：
$$
\mathcal{F}_t = \mathcal{F}(\beta \color{skyblue}{[}\boldsymbol{\mu}_q^{(t-1)}\color{skyblue}{]_{sg}} + (1-\beta) \tilde{\boldsymbol{\mu}}_q^{(t)},\beta \color{skyblue}{[}\boldsymbol{V}_q^{(t-1)}\color{skyblue}{]_{sg}} + (1-\beta) \tilde{\boldsymbol{V}}_q^{(t)})
$$

### 具体示例

在生成模型的后训练中，如果混合使用多个不同的编码器去计算 FD Loss，为了平衡不同量级的损失，通常使用损失归一化技巧：
$$
\mathcal{L} = \sum_i \frac{\mathcal{F}[\phi_i]}{\color{skyblue}{[}\mathcal{F}[\phi_i]\color{skyblue}{]_{sg}} + \epsilon}
$$
在实践中，FD Loss 能够成功将 FID 用于生成模型的微调，并明显改进单步生成模型的效果，将单步生成的 FID 推向了极高水平。
