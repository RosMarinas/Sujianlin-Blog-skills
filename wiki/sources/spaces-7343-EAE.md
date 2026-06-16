---
title: EAE：自编码器 + BN + 最大熵 = 生成模型
id: article::7343
source_ids: ["7343"]
status: draft
---

# EAE：自编码器 + BN + 最大熵 = 生成模型

- **URL**: https://spaces.ac.cn/archives/7343
- **Author**: 苏剑林
- **Date**: 2020-04-20
- **Category**: 信息时代
- **Tags**: EAE, 自编码器, BN, 最大熵, k邻近估计

## Summary

介绍EAE（Entropic AutoEncoder）模型，通过BN层约束隐变量均值和方差，并通过最大熵原则使用k邻近方法估计熵，将普通自编码器变为生成模型。

## Key Concepts

- 最大熵原理：均值为0、方差为1时标准正态分布熵最大
- BN层实现均值方差约束（移除beta/gamma参数）
- k邻近方法（k-NN）估计熵
- EAE相比VAE的优势：无重参数化噪声问题

## Related Resources

- 关联概念: [[concepts/maximum-entropy]]
- 关联概念: [[concepts/k-nearest-entropy]]
