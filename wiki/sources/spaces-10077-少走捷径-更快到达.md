---
type: article_summary
title: 生成扩散模型漫谈（二十四）：少走捷径，更快到达
article_id: "10077"
source_url: https://spaces.ac.cn/archives/10077
date: 2024-04-23
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-04-23-生成扩散模型漫谈-二十四-少走捷径-更快到达.md
series: [生成扩散模型漫谈]
concepts: [捷径调优]
methods: []
evidence_spans:
  - 10077-模型回顾
  - 10077-寥寥几行
  - 10077-个人思考
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-04-23-生成扩散模型漫谈-二十四-少走捷径-更快到达.md
source_ids:
  - "10077"
status: draft
updated: 2026-06-09
---

## 一句话总结

Skip Tuning（捷径调优）通过降低U-Net中Skip Connection的权重（特别是靠近瓶颈层的skip）来补偿加速采样中损失的非线性能力，是一种零额外计算成本的采样质量提升技巧。

## 核心问题

扩散模型的加速采样（无论使用何种加速技术）都会降低采样映射的非线性表达能力，导致生成质量下降。能否通过调整模型结构来补偿这部分损失的非线性能力？

## 关键结论

1. U-Net的Skip Connection除了避免信息瓶颈外，还具有线性正则化的归纳偏置——skip权重越大，模型越接近线性/浅层模型。
2. 加速采样损失的非线性能力，恰好可以通过降低Skip Connection权重来部分恢复——这是Skip Tuning的核心经验发现。
3. 调整方式极其简单：最外层skip乘以 $\rho_{\text{top}}=1$，最内层乘以 $\rho_{\text{bottom}} < 1$，中间按深度线性插值；实际只需调节一个参数 $\rho_{\text{bottom}}$。
4. 与FreeU的关系：Skip Tuning主要针对ODE-based模型（缩减步数后噪声增加），降低skip权重增强主干去噪能力；SDE-based模型可能需要相反调整（因过度平滑）。

## 核心推导

本文不涉及复杂数学推导。Skip Tuning的核心操作是线性深度依赖的skip权重缩放：设有 $k+1$ 个skip连接，最外层（靠近输入）权重为 $\rho_{\text{top}}$，最内层（靠近瓶颈）权重为 $\rho_{\text{bottom}}$，中间层按深度线性变化。典型设置为 $\rho_{\text{top}}=1$，仅调节 $\rho_{\text{bottom}}$。

## 关键公式

Skip Connection权重调整（数学描述）：
$$\rho^{(i)} = \rho_{\text{top}} + \frac{i}{k}(\rho_{\text{bottom}} - \rho_{\text{top}}), \quad i = 0, 1, \dots, k$$

其中 $\rho^{(i)}$ 是第 $i$ 层skip的权重（$i=0$ 最外层，$i=k$ 最内层），$\rho_{\text{top}}=1$，$\rho_{\text{bottom}}$ 为可调超参数。

## 实验或案例

- 在多个数据集和多种加速方法上，Skip Tuning一致提升FID等指标。
- 提升以零额外计算成本实现（仅在推理时调整权重）。
- ODE-based模型的最佳调整是降低skip权重（$\rho_{\text{bottom}} < 1$）。
- 推测DiT等无skip架构可通过调整残差连接获得类似收益。

## 系列定位

作为系列第24篇，本文是系列中最简单的一篇文章——几句话就能说清核心思想，但体现的是"别出心裁的想象力和观察力"。它与第21篇（AMED）同属采样加速主题，但角度完全不同：AMED改进ODE求解器本身，Skip Tuning则是通过调整模型结构补偿加速带来的非线性损失，可以与任意加速技术配合使用。
