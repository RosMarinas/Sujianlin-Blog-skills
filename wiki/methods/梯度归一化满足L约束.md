---

type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: 梯度归一化满足L约束
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-06-08-互怼的艺术-从零直达WGAN-GP.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-08-26-fashion-mnist的gan玩具.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-22-RSGAN-对抗模型中的-图灵测试-思想.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-01-泛化性乱弹-从随机噪声-梯度惩罚到虚拟对抗训练.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-正态分布距离.md
source_ids:
  - 8757
method_summary: 将判别器输出除以梯度范数hat{D}(x)=D(x)/(||grad D(x)||+|D(x)|)使梯度范数自动为1
typical_structure: |
  1. 对于判别器输入 $x$，前向传播计算出原始未经约束的标量输出 $D(x)$。
  2. 利用自动微分工具反向计算 $D(x)$ 针对输入 $x$ 的梯度向量 $\nabla_x D(x)$，并求出其范数。
  3. 应用梯度归一化公式，在分母中加上范数项和用于防止分母过小的绝对值项 $|D(x)|$，得到修正后的 $\hat{D}(x)$。
  4. 证明经过这一步变换，对于任何输入 $x$ 的微小变动，新函数 $\hat{D}(x)$ 的梯度范数被天然限制在 $1$ 以下。
  5. 使用 $\hat{D}(x)$ 代替 $D(x)$ 参与 Wasserstein GAN 的对抗损失计算并进行参数更新。
applicability: 生成对抗网络（GAN）特别是 WGAN 的判别器中，需要满足 Lipschitz 约束（函数的梯度范数被有界限制）以保证训练的稳定性和最优传输距离计算准确性的场景。
tools: 
examples:
  - [[article::8757]]
status: stable
updated: 2026-06-12
cross_series_match: null
cross_series_match_reason: Gradient normalization is a new method proposed in 2021. Shares align/calibrate operation type with spectral normalization but uses gradient instead of weight.
evidence_spans:
  - ev::8757::解释了将判别器输出除以其输入梯度范数以自动满足 Lipschitz 约束的理论推导及操作。
---

## 适用问题

生成对抗网络（GAN）特别是 WGAN 的判别器中，需要满足 Lipschitz 约束（函数的梯度范数被有界限制）以保证训练的稳定性和最优传输距离计算准确性的场景。

## 核心变换

不改变网络前向结构，不依赖权重惩罚，而是在输出端将模型原本的输出 $D(x)$ 强制除以其自身对输入 $x$ 的梯度范数，构造出一个自然满足 1-Lipschitz 的新输出 $\hat{D}(x)$：
$$ \hat{D}(x) = \frac{D(x)}{\|\nabla_x D(x)\| + |D(x)|} $$

## 典型步骤

1. 对于判别器输入 $x$，前向传播计算出原始未经约束的标量输出 $D(x)$。
2. 利用自动微分工具反向计算 $D(x)$ 针对输入 $x$ 的梯度向量 $\nabla_x D(x)$，并求出其范数。
3. 应用梯度归一化公式，在分母中加上范数项和用于防止分母过小的绝对值项 $|D(x)|$，得到修正后的 $\hat{D}(x)$。
4. 证明经过这一步变换，对于任何输入 $x$ 的微小变动，新函数 $\hat{D}(x)$ 的梯度范数被天然限制在 $1$ 以下。
5. 使用 $\hat{D}(x)$ 代替 $D(x)$ 参与 Wasserstein GAN 的对抗损失计算并进行参数更新。

## 直觉

在山地中行走，Lipschitz 约束要求我们所在的地形任何地方的坡度都不能超过1（太陡容易摔死，即梯度爆炸）。之前的方法是到处修修补补去砸平陡坡（参数裁剪、梯度惩罚）。而梯度归一化的想法非常野蛮直接：既然坡度大是因为高低落差（$D(x)$）相比水平距离变化太剧烈，那我干脆就把整座山的地形高度统一“压缩除以它当前的坡度”。这样一来，原来坡度是10的地方高度被除以了10，坡度变成了1，直接强行把整座山改造成了任何地方坡度都不超过1的安全地形。

## 边界

此方法在实际训练中需要频繁计算梯度的梯度（因为 $\hat{D}(x)$ 内部就包含了 $\nabla_x D(x)$，对 $\hat{D}$ 再次反向传播优化参数时需要二阶导数），带来较高的内存和计算代价。

## 例子

研究者在无任何其他谱归一化或参数裁剪的普通 MLP 网络上，仅在最后输出节点加入该除以梯度范数的操作，就成功使其化身为合格的 WGAN 判别器，完美复现了 Wasserstein 距离并稳定生成了高质量图像。

## 证据

- ev::8757::解释了将判别器输出除以其输入梯度范数以自动满足 Lipschitz 约束的理论推导及操作。