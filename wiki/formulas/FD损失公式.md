---
type: formula
title: FD损失公式
latex: \mathcal{F} = \|\boldsymbol{\mu}_p - \boldsymbol{\mu}_q\|^2 + \text{tr}\left(\boldsymbol{\Sigma}_p
  + \boldsymbol{\Sigma}_q - 2\left(\boldsymbol{\Sigma}_p^{1/2}\boldsymbol{\Sigma}_q\boldsymbol{\Sigma}_p^{1/2}\right)^{1/2}\right)
symbol_meanings:
  mu_p: 真实分布在特征空间的均值向量
  mu_q: 生成分布在特征空间的均值向量
  Sigma_p: 真实分布的协方差矩阵
  Sigma_q: 生成分布的协方差矩阵
  tr: 矩阵的迹
standard_notation:
  frechet_distance: \mathcal{F}
  mean_p: \boldsymbol{\mu}_p
  mean_q: \boldsymbol{\mu}_q
conditions: 特征提取向量服从多元正态分布，协方差矩阵 Sigma_p, Sigma_q 必须对称正定
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

该公式定义了两个多元正态分布在二次 Wasserstein 距离（W-距离，即 $\mathcal{W}_2^2[p,q]$）下的显式差异，最初来源于评估视觉生成模型质量的 FID（Fréchet Inception Distance）指标。其核心思想是将真实样本与生成样本分别输入到一个预训练好的特征编码器（例如 InceptionV3 或 SigLIP 等模型）中，将原始样本 $\boldsymbol{x}$ 映射到高维特征向量空间 $\boldsymbol{z}=\phi(\boldsymbol{x})\in\mathbb{R}^d$，并假设这些编码结果服从多元正态分布。基于这一假设，公式通过计算真实分布 $p$ 和生成分布 $q$ 的均值向量（$\boldsymbol{\mu}_p, \boldsymbol{\mu}_q$）之间的欧氏距离，以及协方差矩阵（$\boldsymbol{\Sigma}_p, \boldsymbol{\Sigma}_q$）的非线性相互作用项的迹，直接度量两者的统计分布差异。

虽然该距离函数在理论上是完全可导的，能够直接作为视觉生成模型微调的损失函数（统称为 FD Loss），但在实际优化实践中会遇到显著的计算困难：公式依赖于全体样本（或大 Batch）统计出的均值和协方差，接着进行迹和矩阵平方根等跨样本的非线性运算。由于这些非线性特性，使用较小 Batch Size 估计出来的 FD 存在固有偏差，且无法单纯通过增加训练步数或简单的传统梯度累积来消除，这不仅增加了模型微调时的训练成本，也促使了业界关于 FD 梯度的无偏估计及流式训练架构的深入研究。
