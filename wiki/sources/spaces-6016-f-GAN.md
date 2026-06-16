---
title: f-GAN简介：GAN模型的生产车间
id: article::6016
source_ids: ["6016"]
status: draft
---

# f-GAN简介：GAN模型的生产车间

- **URL**: https://spaces.ac.cn/archives/6016
- **Author**: 苏剑林
- **Date**: 2018-09-29
- **Category**: 数学研究
- **Tags**: f-GAN, f散度, 凸共轭, 局部变分

## Summary

介绍通过一般的f散度来构造一般的GAN的方案。通过凸函数的共轭（局部变分方法），将f散度转化为对偶形式，然后构造min-max过程从而得到GAN模型。

## Key Concepts

- f散度的定义与常见种类
- 凸函数与凸共轭（Fenchel共轭）
- 局部变分方法估计f散度
- f-GAN的一般框架: min_G max_T E_p[T(x)] - E_q[g(T(x))]

## Related Resources

- 关联文章: [[spaces-7210-Designing-GANs]], [[spaces-6280-Wasserstein-WGAN]]
- 关联概念: [[concepts/f-divergence]]
