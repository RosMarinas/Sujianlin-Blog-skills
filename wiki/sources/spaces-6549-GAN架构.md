---
title: 从DCGAN到SELF-MOD：GAN的模型架构发展一览
id: article::6549
source_ids: ["6549"]
status: draft
---

# 从DCGAN到SELF-MOD：GAN的模型架构发展一览

- **URL**: https://spaces.ac.cn/archives/6549
- **Author**: 苏剑林
- **Date**: 2019-04-19
- **Category**: 信息时代
- **Tags**: GAN, DCGAN, ResNet, SELF-MOD, StyleGAN

## Summary

梳理GAN的模型架构发展，从DCGAN、ResNet到SELF-MOD和StyleGAN，重点讨论生成器架构的演变。

## Key Concepts

- DCGAN：反卷积+BN+ReLU/LeakyReLU的标准架构
- 棋盘效应：反卷积stride>1导致的问题
- ResNet架构：去除反卷积，使用UpSampling2D+卷积
- SELF-MOD：将条件BN中的条件改为噪声z自身
- AdaIN与StyleGAN
