---
type: concept
title: VAE聚类
aliases:
- VAE-based Clustering
- 一步到位聚类
definition: 将VAE的隐变量从连续变量 $z$ 扩展为连续变量 $z$ 加离散变量 $y$（聚类标签），在统一的KL散度最小化框架下同时完成编码、聚类和条件生成的无监督聚类方法，替代传统的"先训练VAE再聚类"两阶段流程。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2018-09-17-变分自编码器-四-一步到位的聚类方案.md
source_ids:
- '5887'
prerequisites:
- '[[变分自编码器]]'
- '[[联合分布KL散度]]'
equivalent_forms: []
direct_consequences: []
related_formulas: []
related_methods:
- '[[VAE联合分布最小化]]'
series:
- '[[变分自编码器]]'
evidence_spans:
- ev::5887::一般框架
- ev::5887::具体模型
- ev::5887::mnist
status: draft
updated: '2026-06-12'
---

# VAE聚类 (VAE-based Clustering)

## 方法概述

将标准VAE的损失函数 $KL(p(x,z)\|q(x,z))$ 中的隐变量 $z$ 替换为 $(z,y)$，其中 $y$ 是离散的聚类变量，得到：

$$KL(p(x,z,y)\|q(x,z,y)) = \sum_y \iint p(z,y|x)\tilde{p}(x)\ln\frac{p(z,y|x)\tilde{p}(x)}{q(x|z,y)q(z,y)}dzdx$$

引入三个结构假设使问题可解：
- $p(z,y|x) = p(y|z)p(z|x)$：先编码再分类
- $q(x|z,y) = q(x|z)$：生成只依赖连续特征
- $q(z,y) = q(z|y)q(y)$：类条件先验 + 均匀类先验

## 三分量损失函数

最终损失函数自然分解为三个有明确语义的项：

1. **重构损失** $-\log q(x|z)$：保留信息，确保编码质量
2. **聚类对齐项** $\sum_y p(y|z)\log\frac{p(z|x)}{q(z|y)}$：将 $z$ 拉向类专属中心 $\mu_y$
3. **类别平衡项** $KL(p(y|z)\|q(y))$：防止坍缩为单个类

## 实验表现

- MNIST：约83%聚类准确率
- Fashion-MNIST：约58.5%聚类准确率
- 编码器和解码器均为简单MLP，未精细调优