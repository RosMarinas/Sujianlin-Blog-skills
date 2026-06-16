---
type: formula
title: FD损失梯度公式
latex: \nabla_{\boldsymbol{\Sigma}_q}\mathcal{W}_2^2 = \boldsymbol{I} - \boldsymbol{\Sigma}_p^{1/2}\left(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2}\right)^{-1/2}\boldsymbol{\Sigma}_p^{1/2}
symbol_meanings:
  Sigma_p: 真实协方差矩阵
  Sigma_q: 可优化的生成协方差矩阵
  I: 单位矩阵
standard_notation:
  gradient_wrt_sigma: \nabla_{\boldsymbol{\Sigma}_q}\mathcal{W}_2^2
conditions: 中间矩阵 S = Sigma_p^1/2 * Sigma_q * Sigma_p^1/2 必须为正定对称矩阵，以支持奇异值求导展开
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
source_ids:
- 11738
appears_in:
- - - spaces-11738-FID为Loss与流式训练
status: draft
updated: '2026-06-14'
---

## 概述

此梯度公式给出了将Fréchet Distance（如FID）直接作为生成模型损失函数（FD Loss）时，Wasserstein距离 $\mathcal{W}_2^2$ 关于生成特征分布的协方差矩阵 $\boldsymbol{\Sigma}_q$ 的导数。在视觉生成模型评估和训练中，真实样本和生成样本首先通过预训练编码器（如InceptionV3或SigLIP）被映射为特征向量 $\boldsymbol{z} = \phi(\boldsymbol{x}) \in \mathbb{R}^d$。随后通过估计各自的均值向量 $\boldsymbol{\mu}_p, \boldsymbol{\mu}_q$ 和协方差矩阵 $\boldsymbol{\Sigma}_p, \boldsymbol{\Sigma}_q$，可以计算出正态分布的差异函数，即距离度量 $\mathcal{W}_2^2[p,q] = \Vert \boldsymbol{\mu}_p - \boldsymbol{\mu}_q\Vert^2 + \mathop{\text{tr}}(\boldsymbol{\Sigma}_p + \boldsymbol{\Sigma}_q - 2(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2})^{1/2})$。

由于该距离的计算公式中包含跨样本的非线性矩阵平方根和迹运算 $\mathop{\text{tr}}(\dots)$，直接对其进行反向传播通常在求导计算上极为复杂。上述梯度公式巧妙地将对复杂的非平凡矩阵指数或对数运算的导数，规整为了简单的逆平方根运算 $\left(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2}\right)^{-1/2}$，从而大幅简化了计算流。利用该解析形式的公式，可以直接将反向传播高效地应用到生成网络的前向参数更新上。然而在实践中，由于协方差矩阵的估计以及这种跨样本的非线性计算依赖于大量样本的整体统计，如果直接使用小Batch Size进行估计会引入难以消除的有偏性。因此在应用此梯度公式进行模型微调时，通常还需要配合流式训练，或借鉴对比学习中类似的跨样本梯度累积技巧，来克服显存受限带来的Batch Size瓶颈。
