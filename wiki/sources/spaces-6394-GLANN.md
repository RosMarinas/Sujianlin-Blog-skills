---
title: 非对抗式生成模型GLANN的简单介绍
id: article::6394
source_ids: ["6394"]
status: draft
---

# 非对抗式生成模型GLANN的简单介绍

- **URL**: https://spaces.ac.cn/archives/6394
- **Author**: 苏剑林
- **Date**: 2019-02-26
- **Category**: 信息时代
- **Tags**: GLANN, IMLE, 非对抗生成, perceptual loss, GLO

## Summary

介绍非对抗式生成模型GLANN，基于隐式最大似然估计（IMLE）、perceptual loss和GLO的组合。IMLE通过最小化真样本到最近假样本的距离来训练生成器。

## Key Concepts

- 隐式最大似然估计（IMLE）：通过狄拉克分布积分近似推导
- IMLE核心loss: min_j ||x_i - G(z_j)||^2
- GLO：直接优化隐变量编码
- perceptual loss替代l2距离提升生成质量

## Related Resources

- 关联方法: [[methods/IMLE]]
