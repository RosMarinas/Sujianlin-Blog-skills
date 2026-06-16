---
title: WGAN的成功，可能跟Wasserstein距离没啥关系
id: article::8244
source_ids: ["8244"]
status: draft
---

# WGAN的成功，可能跟Wasserstein距离没啥关系

- **URL**: https://spaces.ac.cn/archives/8244
- **Author**: 苏剑林
- **Date**: 2021-03-15
- **Category**: 信息时代
- **Tags**: WGAN, Wasserstein距离, Lipschitz约束, c-transform

## Summary

指出现有WGAN并没有很好近似Wasserstein距离，更好近似Wasserstein距离反而生成效果变差。WGAN成功的关键可能在于L约束而非Wasserstein距离本身。

## Key Concepts

- 效果好的WGAN并未精确近似Wasserstein距离
- c-transform方法更好近似Wasserstein距离但效果更差
- 交替训练与batch采样导致无法精确逼近概率度量
- 欧氏距离作为度量与视觉感知的不匹配
