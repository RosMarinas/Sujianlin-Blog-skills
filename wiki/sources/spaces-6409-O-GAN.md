---
title: O-GAN：简单修改，让GAN的判别器变成一个编码器
id: article::6409
source_ids: ["6409"]
status: draft
---

# O-GAN：简单修改，让GAN的判别器变成一个编码器

- **URL**: https://spaces.ac.cn/archives/6409
- **Author**: 苏剑林
- **Date**: 2019-03-06
- **Category**: 信息时代
- **Tags**: O-GAN, 正交GAN, 编码器, 判别器复用

## Summary

通过简单的修改让GAN的判别器变成一个编码器（O-GAN），基于正交分解操作，充分利用判别器的自由度。通过Pearson相关系数作为重构损失实现编码功能。

## Key Concepts

- 判别器分解为 E(x) 和 T(E(x))，E(x)作为编码器
- avg(E(x))可直接作为判别器，省去T部分
- Pearson相关系数 ρ(z, E(G(z))) 作为重构损失
- 正交分解保留至少两个自由度给判别器

## Related Resources

- 关联方法: [[methods/O-GAN]]
- 关联文章: [[spaces-9969-IGN]]
