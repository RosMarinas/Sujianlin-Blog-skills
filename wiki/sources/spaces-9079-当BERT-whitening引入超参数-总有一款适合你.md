---
type: article_summary
title: 当BERT-whitening引入超参数：总有一款适合你
article_id: 9079
source_url: https://spaces.ac.cn/archives/9079
date: 2022-05-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-05-18-当BERT-whitening引入超参数-总有一款适合你.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2022-05-18-当BERT-whitening引入超参数-总有一款适合你.md"]
source_ids: ["9079"]
status: draft
updated: 2026-06-12
---

# 当BERT-whitening引入超参数：总有一款适合你

## 文章核心问题
如何解决传统无参数 BERT-whitening 强行对方差进行平权缩放，导致在已被有监督微调过的句向量（如 SimBERT）上性能严重退化，无法实现保真降维的问题。

## 主要结论
通过在白化变换中引入均值调节因子 $\\beta$ 和特征平权调节因子 $\\gamma$，能够平滑调整模型对各向同性的修正强度。特别地，当设定 $\\beta=\\gamma=0$ 时，变换退化为纯正交特征旋转。此正交基不改变余弦相似度的打分顺序，通过直接截断前 $k$ 维（如降至 256 维）可以实现几乎无损的“免费午餐式”特征降维。

## 推导结构
1. 回顾 BERT-whitening SVD 及协方差白化的局限性。
2. 引入标量超参数 $\\beta, \\gamma$，给出超参化公式 $\\tilde{\\boldsymbol{x}}_i = (\\boldsymbol{x}_i - \\beta\\boldsymbol{\mu})\\boldsymbol{U}\\boldsymbol{\Lambda}^{-\\gamma/2}$。
3. 详细解释 $\\beta=\\gamma=0$ 时利用正交旋转矩阵 $\\boldsymbol{U}$ 保持内积与余弦排序的数学原理。
4. 给出 SimBERT-P1 和 BERT-P4 在 STS-B、ATEC 等中文相似度任务上 $\\beta=\\gamma=0$ 与传统 $\\beta=\\gamma=1$ 的实验对比，证明其降维无损性。

## 关键公式
- 超参化白化公式：$\\tilde{\\boldsymbol{x}}_i = (\\boldsymbol{x}_i - \\beta\\boldsymbol{\mu})\\boldsymbol{U}\\boldsymbol{\Lambda}^{-\\gamma/2}$
- 对角特征标准方差项：$\\boldsymbol{\Lambda}^{-\\gamma/2}$

## 体现的方法
- [[超参数化BERT-whitening]]：使用两组控制中心度和方差归一拉伸程度的参数泛化标准白化。

## 与其他文章的关系
- 修正了 [[无监督语义相似度哪家强？我们做了个比较全面的评测]] 中白化会损害有监督模型性能的缺陷。

## 原文证据锚点
- `ev::9079::超参数`：对应原文中引入 $\\beta$ 和 $\\gamma$ 超参数并推导 $\\beta=\\gamma=0$ 产生正交保真映射，在降至 256 维时无损甚至提升句向量特征精度的公式与实验数据。