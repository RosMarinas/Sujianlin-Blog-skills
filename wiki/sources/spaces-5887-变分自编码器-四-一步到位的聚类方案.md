---
type: article_summary
title: "变分自编码器（四）：一步到位的聚类方案"
article_id: "5887"
source_url: https://spaces.ac.cn/archives/5887
date: 2018-09-17
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-09-17-变分自编码器-四-一步到位的聚类方案.md
series:
  - "[[变分自编码器]]"
concepts:
  - "[[VAE聚类]]"
  - "[[变分自编码器]]"
  - "[[后验分布假设]]"
  - "[[联合分布KL散度]]"
methods:
  - "[[VAE联合分布最小化]]"
evidence_spans:
  - ev::5887::一般框架
  - ev::5887::分步假设
  - ev::5887::具体模型
  - ev::5887::mnist
  - ev::5887::fashion-mnist
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-09-17-变分自编码器-四-一步到位的聚类方案.md
source_ids:
  - "5887"
status: draft
updated: 2026-06-09
---

## 一句话总结

本文将VAE框架扩展至无监督聚类，通过将隐变量从连续变量 $z$ 扩展为连续变量 $z$ 加离散变量 $y$（聚类标签），在一个统一的损失函数中同时完成编码、聚类和生成三项任务，实现了真正的"一步到位"聚类方案。

## 核心问题

能否在VAE框架内同时完成特征提取、聚类和条件生成，替代传统的"先训练VAE再对隐变量做K-Means/GMM"的两阶段流程？如何设计一个统一的损失函数使其自然包含聚类导向的约束？

## 关键结论

- 通过将隐空间从 $z$ 扩展为 $(z,y)$（$y$ 为离散聚类变量），VAE框架可以自然推广到聚类任务。所有三项任务（编码、聚类、生成）在单一损失函数下联合优化。
- 结构假设 $p(z,y|x) = p(y|z)p(z|x)$（先编码后分类）、$q(x|z,y) = q(x|z)$（生成仅依赖 $z$）、$q(z,y) = q(z|y)q(y)$（类条件先验 + 均匀类别先验）使问题可解。
- 最终的损失函数自然分解为三个有清晰含义的项：(1) 重构损失 $-\log q(x|z)$ —— 保留信息；(2) 聚类对齐项 $\sum_y p(y|z)\log\frac{p(z|x)}{q(z|y)}$ —— 将 $z$ 拉向类中心 $\mu_y$；(3) 类别平衡项 $KL(p(y|z)\|q(y))$ —— 防止坍缩为单个类。
- 利用重参数化技巧可简化聚类对齐项的计算，移除参数无关项 $-\| \varepsilon\|^2/2$。
- MNIST上达到约83%聚类准确率，Fashion-MNIST上约58.5%，验证了方案的基本有效性。

## 核心推导

**从标准VAE到聚类VAE**：将VAE损失 $KL(p(x,z)\|q(x,z))$ 中的 $z$ 替换为 $(z,y)$：
$$KL(p(x,z,y)\|q(x,z,y)) = \sum_y \iint p(z,y|x)\tilde{p}(x)\ln\frac{p(z,y|x)\tilde{p}(x)}{q(x|z,y)q(z,y)}dzdx$$

代入结构假设后得到三分量损失 $(5)$。其中聚类对齐项通过 $p(z|x)$ 和 $q(z|y)$ 的高斯形式推导出简化表达式 $(8)$。

**对齐项简化**：利用重参数化 $z = \mu(x) + \varepsilon \odot \sigma(x)$，$\log\frac{p(z|x)}{q(z|y)}$ 中的 $\|\frac{z-\mu(x)}{\sigma(x)}\|^2$ 项退化为 $\|\varepsilon\|^2$（参数无关常数），可忽略。剩余 $-\frac{1}{2}\sum\log\sigma_i^2(x) + \frac{1}{2}\|z-\mu_y\|^2$。

## 关键公式

- $(2)$: $KL(p(x,z,y)\|q(x,z,y)) = \sum_y\iint p(z,y|x)\tilde{p}(x)\ln\frac{p(z,y|x)\tilde{p}(x)}{q(x|z,y)q(z,y)}dzdx$ —— 聚类VAE的一般框架
- $(3)$: $p(z,y|x)=p(y|z)p(z|x),\; q(x|z,y)=q(x|z),\; q(z,y)=q(z|y)q(y)$ —— 三个结构假设
- $(5)$: $\mathbb{E}_{x\sim\tilde{p}(x)}[-\log q(x|z) + \sum_y p(y|z)\log\frac{p(z|x)}{q(z|y)} + KL(p(y|z)\|q(y))],\; z\sim p(z|x)$ —— 三分量实用损失
- $(8)$: $\log\frac{p(z|x)}{q(z|y)} \sim -\frac{1}{2}\sum_{i=1}^d\log\sigma_i^2(x) + \frac{1}{2}\|z-\mu_y\|^2$ —— 简化后的对齐项

## 实验或案例

- **MNIST**：聚类准确率约83%，与Unsupervised Deep Embedding for Clustering Analysis的约84%相当。10个聚类可视化结果显示不同数字类被清晰分离。每类条件生成样本可辨认。
- **Fashion-MNIST**：聚类准确率约58.5%，低于MNIST（数据复杂性更高导致）。10个聚类结果和条件生成样本具备可辨认性。
- 编码器和解码器均为简单的MLP，未经过精细调优，作者自评"有显著提升空间"。

## 系列定位

本文是系列的第四篇，从前三篇的理论构建转向一个具体的应用——无监督聚类。核心贡献是：(1) 通过扩展隐变量空间 $(z,y)$ 将VAE从纯生成模型拓展为集编码、聚类、生成于一体的统一框架；(2) 三分量loss的设计为每个分量赋予明确语义，具有方法论价值；(3) 实验验证了方法的有效性，并指出框架的一般性（本文只是$(2)$式的一个具体实例化，更复杂的分解可能带来更好的效果）。
