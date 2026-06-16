---
title: 从去噪自编码器到生成模型
id: article::7038
source_ids: ["7038"]
status: draft
---

# 从去噪自编码器到生成模型

- **URL**: https://archives/7038
- **Author**: 苏剑林
- **Date**: 2019-10-31
- **Category**: 信息时代
- **Tags**: 去噪自编码器, 生成模型, 得分匹配, Langevin采样

## Summary

介绍两篇利用去噪自编码器做生成模型的论文。核心结论：加性高斯噪声的最优去噪自编码器能显式计算，且与分布的梯度有关：r(x) = x + σ^2 ∇_x log p_hat(x)。

## Key Concepts

- 去噪自编码器最优解与得分函数的关系
- 通过最小化 KL(q_hat || p_hat) 训练生成模型
- Langevin方程从p_hat采样 + 去噪得到无噪声样本
- 退火技巧稳定训练

## Related Resources

- 关联概念: [[concepts/score-matching]]
- 关联方法: [[methods/denoising-score-matching]]
