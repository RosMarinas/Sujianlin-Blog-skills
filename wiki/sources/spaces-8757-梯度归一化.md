---
title: WGAN新方案：通过梯度归一化来实现L约束
id: article::8757
source_ids: ["8757"]
status: draft
---

# WGAN新方案：通过梯度归一化来实现L约束

- **URL**: https://spaces.ac.cn/archives/8757
- **Author**: 苏剑林
- **Date**: 2021-11-15
- **Category**: 信息时代
- **Tags**: WGAN, 梯度归一化, Lipschitz约束, Gradient Normalization

## Summary

介绍WGAN中实现Lipschitz约束的新方案——梯度归一化（Gradient Normalization），将判别器输出除以其梯度范数。但该方案导致判别器不连续，存在理论疑问。

## Key Concepts

- 梯度归一化: D_hat(x) = D(x) / ||∇_x D(x)||
- 分段线性函数假设下梯度在局部为常向量
- 不连续函数作为判别器的理论问题
- 梯度惩罚效果优于梯度归一化

## Related Resources

- 关联方法: [[methods/gradient-normalization]]
- 关联文章: [[spaces-6280-Wasserstein-WGAN]]
