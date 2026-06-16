---
title: 积分梯度：一种新颖的神经网络可视化方法
source_id: 7533
type: source
url: https://spaces.ac.cn/archives/7533
author: 苏剑林
date: 2020-06-28
category: 信息时代
tags: [visualization, interpretability, integrated-gradients]
license: CC BY-NC-SA
abstract: 介绍积分梯度（Integrated Gradients）这种神经网络可视化/归因方法。通过沿输入到参照背景的路径对梯度积分，构建精确的等式来度量各分量重要性，弥补泰勒展开的不足。
key_contributions:
  - 清晰揭示积分梯度优于朴素梯度的本质原因（路径积分vs单点梯度）
  - 朴素梯度可被对抗训练"操控"（使梯度接近0而不影响预测）
  - 参照背景的选择对归因结果的影响
  - 积分恒等式的推导和离散近似方法
  - 在情感分类任务中发现模型的"负面检测"偏差
