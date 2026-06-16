---

type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: FD损失流式训练法
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-05-08-直接以FID为Loss-从梯度计算到流式训练.md
source_ids:
  - 11738
method_summary: 在视觉生成微调中，使用指数滑动平均（EMA）在训练中实时更新并缓存生成样本的均值和二阶矩统计量，以无感的极小代价模拟超大批次 FD 估计，避免矩阵求逆在小批次下的非满秩发散。
typical_structure: |
  1. 提前计算全体真实样本的固定特征均值和协方差矩阵。
  2. 初始化生成模型的历史均值和二阶矩缓存。
  3. 前向生成小批次样本，计算当前批次的均值和二阶矩。
  4. 使用 EMA 融合历史无梯度缓存与当前批次统计量（Stop Gradient）。
  5. 计算该平滑统计量与真实统计量的 FD Loss 进行反向传播更新。
applicability: 适用于将 FID 直接作为生成模型（如 GAN 或 Diffusion）微调的损失函数，但受限于计算资源无法配置数万 Batch Size 时稳定求解特征协方差逆矩阵。
examples:
  - 扩散模型单步生成微调：小批次大小为 64，使用 EMA β=0.99 模拟超大批次稳定计算 W 距离微调生成质量。
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::11738::原文历史来凑节详细介绍了基于EMA平滑历史Batch的统计量的方法及其动机。
---


## 适用问题
在视觉生成模型的训练中，直接将 Fréchet Inception Distance (FID) 等 Fréchet Distance (FD) 指标作为损失函数优化。因为计算准确的特征协方差矩阵和均值需要数万规模的样本，如果 Batch Size 过小，估计出的协方差矩阵不满秩，在求矩阵逆平方根梯度时会面临无解而发散。由于算力受限，无法直接使用超大 Batch Size 计算 FD Loss。

## 核心变换
通过指数移动平均（EMA）对历史小批次样本的特征均值向量和协方差矩阵进行缓存和融合。在计算单步小批次梯度时，将停梯度的历史统计量与当前批次的统计量加权混合，从而用 $O(1/(1-\beta))$ 个历史批次“流式”地拼凑出一个等效超大批次的协方差，确保其满秩稳定且梯度无偏。

## 典型步骤
1. **固定真实分布样本的统计量**：提前使用预训练特征提取器（如 Inception、SigLIP）计算全体真实样本的特征均值 $\boldsymbol{\mu}_p$ 和协方差矩阵 $\boldsymbol{\Sigma}_p$。
2. **初始化生成分布缓存**：在训练开始时，将历史生成的均值 $\boldsymbol{\mu}_q^{(0)}$ 和二阶矩 $\boldsymbol{V}_q^{(0)}$ 初始化为当前批次的生成统计量。
3. **迭代计算当前批次特征**：每一步从生成器生成小批次样本，抽取特征后计算当前批次的均值 $\tilde{\boldsymbol{\mu}}_q^{(t)}$ 和二阶矩 $\tilde{\boldsymbol{V}}_q^{(t)}$。
4. **EMA 滑动更新**：使用设定的动量 $\beta$ 计算当前等效统计量：
   $$ \boldsymbol{\mu}_q^{(t)} = \beta [\boldsymbol{\mu}_q^{(t-1)}]_{sg} + (1-\beta) \tilde{\boldsymbol{\mu}}_q^{(t)} $$
   $$ \boldsymbol{V}_q^{(t)} = \beta [\boldsymbol{V}_q^{(t-1)}]_{sg} + (1-\beta) \tilde{\boldsymbol{V}}_q^{(t)} $$
   （其中 $sg$ 表示 Stop Gradient）。
5. **梯度反传**：根据平滑后的统计量推导生成协方差，计算其与真实统计量的 FD Loss 并反向传播，更新生成器参数。

## 直觉
生成模型的学习率通常较小，对应生成分布的变化非常缓慢。这意味着即使使用了前几步的历史统计量，对当前生成分布特征的近似误差也很小。因此通过 EMA 将历史数据信息“沉淀”下来混合当前批次，可以起到等效扩大 Batch Size 的作用（“Batch Size不够，历史来凑”），避免因单步小批次造成的统计抖动和不满秩崩溃。

## 边界
- 只能对生成分布中“平缓”更新的情境起效，如果学习率很大或生成模型剧烈波动，会导致历史均值和方差对当前分布严重失真。
- 为了应对数值不稳定，前向及反向传播中仍需依赖矩阵平方根和逆平方根的稳定算子（如 SVD 或 Newton-Schulz 迭代）。

## 例子
微调一个单步扩散生成模型：真实数据在 SigLIP 上的分布特征 $\boldsymbol{\mu}_p, \boldsymbol{\Sigma}_p$ 已提前算好。单卡显存只能装下 Batch Size=64，通过设置 EMA $\beta=0.99$（等效利用约 100 步即 6400 个样本的历史），使得单卡也可以直接反传协方差差异。

## 证据
- 原文 11738 "历史来凑" 节阐述："引入当前批数据后，新的 $\boldsymbol{\mu}_q, \boldsymbol{V}_q$ 应当只是在旧的基础上做一些微调，我们考虑用滑动平均（EMA）来近似这个操作 ... 约等于将 $\boldsymbol{\mu}_q, \boldsymbol{V}_q$ 的统计 Batch Size 扩大到了 $\mathcal{O}(1/(1-\beta))$ 倍。"