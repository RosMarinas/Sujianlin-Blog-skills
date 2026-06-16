---
title: 级联抑制：提升GAN表现的一种简单有效的方法
id: article::7105
source_ids: ["7105"]
status: draft
---

# 级联抑制：提升GAN表现的一种简单有效的方法

- **URL**: https://spaces.ac.cn/archives/7105
- **Author**: 苏剑林
- **Date**: 2019-12-01
- **Category**: 信息时代
- **Tags**: GAN, 级联抑制, 正交分解

## Summary

介绍提升GAN表现的一种方法Cascading Rejection（级联抑制），通过对判别器特征向量进行正交分解，从多个视角进行打分。

## Key Concepts

- 判别器内积打分只考虑投影分量，忽略垂直分量
- 级联抑制通过迭代正交分解产生多个打分
- 几何意义鲜明，和Capsule思想有相通之处
