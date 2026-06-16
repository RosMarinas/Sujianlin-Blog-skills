---
title: 为什么需要残差？一个来自DeepNet的视角
source_id: 8994
type: source
url: https://spaces.ac.cn/archives/8994
author: 苏剑林
date: 2022-03-19
category: 信息时代
tags: [residual, deep-learning, deepnet, training-stability]
license: CC BY-NC-SA
abstract: 从DeepNet视角分析残差连接的必要性。提出"增量爆炸"概念——参数微小变化导致损失大幅变化（正比于层数N）。残差结构可同时稳定前向传播、反向传播和参数梯度，是训练深层模型的关键设计。
key_contributions:
  - "增量爆炸"概念的提出和数学定义
  - Warmup是治标方法（不解决landscape不平滑的根本问题）
  - 无残差前馈神经网络无法同时解决梯度缩放问题
  - 残差结构通过epsilon控制参数梯度的数学分析
  - 高维模型膨胀系数约1+epsilon^2，epsilon=1/sqrt(N)足够
  - 一维vs高维情形的不同缩放需求分析
