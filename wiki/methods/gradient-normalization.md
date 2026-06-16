---

type: method
operation_types:
  primary: Construct auxiliary sequence
  secondary: []
title: 梯度归一化 (WGAN实现)
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-06-08-互怼的艺术-从零直达WGAN-GP.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-08-26-fashion-mnist的gan玩具.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-22-RSGAN-对抗模型中的-图灵测试-思想.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-01-27-让Keras更酷一些-随意的输出和灵活的归一化.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-01-泛化性乱弹-从随机噪声-梯度惩罚到虚拟对抗训练.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-正态分布距离.md
source_ids:
  - 6051
  - 8757
method_summary: 通过梯度归一化（GraN）替代WGAN-GP的梯度惩罚来施加Lipschitz约束：将判别器梯度范数直接归一化到1，在保证Lipschitz性质的同时避免二次惩罚项的调参需求。
typical_structure: |
  1. 定义标准判别器 $D(x)$。
  2. 计算 $D(x)$ 对输入 $x$ 的梯度 $\nabla_x D(x)$ 并求范数。
  3. 利用核心变换重参数化判别器的输出，得到 $\hat{D}(x)$。
  4. 将 $\hat{D}(x)$ 应用于常规 WGAN 损失进行交替对抗训练。
applicability: 在WGAN中需要为判别器施加Lipschitz约束，但不希望通过额外的梯度惩罚正则项引入复杂超参数调优时。
examples:
  - [[article::8757]]
status: stable
updated: 2026-06-12
evidence_spans: 
  - ev::8757::ICCV变体：$\hat{D}(x) = \frac{D(x)}{\Vert \nabla_x D(x)\Vert + |D(x)|}$
  - ev::8757::WACV变体：$\hat{D}(x) = \frac{D(x)\cdot \Vert \nabla_x D(x)\Vert}{\Vert \nabla_x D(x)\Vert^2 + \epsilon}$
  - ev::8757::边界指出不连续性：由于 $D(x)$ 是连续的而 $\nabla_x D(x)$ 不连续，除法会导致 $\hat{D}(x)$ 成为一个不连续的函数。
belongs_to: []
layering_edge: "detail"





---
# 梯度归一化 (WGAN实现)

## 适用问题
在WGAN中，要求判别器满足Lipschitz约束（Lipschitz常数小于等于某个固定值，如1）。主流方法有参数裁剪、谱归一化和梯度惩罚。梯度归一化提出一种新方法解决判别器梯度的软约束问题。

## 核心变换
将原始判别器输出 $D(x)$ 转换为 $\hat{D}(x)$：
$\hat{D}(x) = \frac{D(x)}{\Vert \nabla_x D(x)\Vert}$

或者变体：
$\hat{D}(x) = \frac{D(x)}{\Vert \nabla_x D(x)\Vert + |D(x)|}\in [-1,1]$ 
$\hat{D}(x) = \frac{D(x)\cdot \Vert \nabla_x D(x)\Vert}{\Vert \nabla_x D(x)\Vert^2 + \epsilon}$

这样强制梯度范数为1。

## 典型步骤
1. 定义标准判别器 $D(x)$。
2. 计算 $D(x)$ 对输入 $x$ 的梯度 $\nabla_x D(x)$ 并求范数。
3. 利用核心变换重参数化判别器的输出，得到 $\hat{D}(x)$。
4. 将 $\hat{D}(x)$ 应用于常规 WGAN 损失进行交替对抗训练。

## 直觉
如果激活函数是“近线性的”（例如ReLU，其导函数绝对值不超过1），则除边界外，$D(x)$在局部区域近似线性。如果它在局部是一个线性函数，那么它的梯度是一个常向量。将 $D(x)$ 除以其梯度范数，得到的函数的梯度范数天然为 1，从而自发满足 1-Lipschitz 约束。

## 边界
1. 分段线性假设会使得 $D(x)$ 的梯度不连续，从而导致连续函数除以不连续函数，生成的结果 $\hat{D}(x)$ 全局上看是不连续的。使用不连续函数作为判别器，在理论上可能有未知风险。
2. 相比于只在判别器训练用二阶梯度的梯度惩罚，梯度归一化要求在生成器和判别器都使用二阶梯度，导致显存占用大且训练变慢。
3. 实际实验结果不一定比梯度惩罚稳定或效果更好。

## 例子
ICCV和WACV的两个独立研究提出了这两种梯度归一化变体来稳定 GAN 的训练。

## 证据
- ev::8757::ICCV变体：$\hat{D}(x) = \frac{D(x)}{\Vert \nabla_x D(x)\Vert + |D(x)|}$
- ev::8757::WACV变体：$\hat{D}(x) = \frac{D(x)\cdot \Vert \nabla_x D(x)\Vert}{\Vert \nabla_x D(x)\Vert^2 + \epsilon}$
- ev::8757::边界指出不连续性：由于 $D(x)$ 是连续的而 $\nabla_x D(x)$ 不连续，除法会导致 $\hat{D}(x)$ 成为一个不连续的函数。
