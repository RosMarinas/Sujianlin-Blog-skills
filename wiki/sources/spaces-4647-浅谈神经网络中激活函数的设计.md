---
title: 浅谈神经网络中激活函数的设计
source_id: 4647
type: source
url: https://spaces.ac.cn/archives/4647
author: 苏剑林
date: 2017-10-26
category: 信息时代
tags: [activation-function, relu, swish, glu, neural-networks, deep-learning]
license: CC BY-NC-SA
abstract: 深入探讨神经网络激活函数的设计原则。从理论上的任意非线性函数（包括浮点误差）均可做激活函数，到ReLU如何解决sigmoid的饱和问题开启深度学习时代，再到Swish激活函数的分析。提出Swish优于ReLU的原因可能与初始化时参数利用率有关，并设计了$max(x, x\cdot e^{-|x|})$作为替代方案。
key_contributions:
  - 任意非线性函数做激活函数的理论可行性
  - Sigmoid饱和问题与梯度消失分析
  - ReLU的正半轴不饱和特性与"深度比宽度更重要"的关系
  - Swish激活函数（$x\cdot\sigma(x)$）的优势分析
  - Swish与GLU激活函数的关系（GLU使用独立的gate）
  - 从初始化角度解释Swish优于ReLU
  - 设计$x\cdot\min(1,e^x)$替代激活函数及防溢出写法
---
