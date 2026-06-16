---
title: 幂等生成网络IGN：试图将判别和生成合二为一的GAN
id: article::9969
source_ids: ["9969"]
status: draft
---

# 幂等生成网络IGN：试图将判别和生成合二为一的GAN

- **URL**: https://spaces.ac.cn/archives/9969
- **Author**: 苏剑林
- **Date**: 2024-01-31
- **Category**: 信息时代
- **Tags**: IGN, GAN, 幂等生成, 重构损失

## Summary

从GAN角度分析IGN，IGN将生成器和判别器合二为一，使用重构损失作为判别器。文章指出IGN实质上是GAN的一个特例，讨论了其自洽性条件和局限性。

## Key Concepts

- 幂等生成网络（IGN）核心: 生成器同时作为判别器, δ_φ(x) = ||G_φ(x) - x||^2
- 通过stop_gradient技巧将min-max写成单个loss
- IGN与EBGAN的联系与区别
- 自洽性分析: 输入不管是什么, 输出空间都是真实样本

## Related Resources

- 关联文章: [[spaces-6409-O-GAN]]
- 关联方法: [[methods/IGN]]
