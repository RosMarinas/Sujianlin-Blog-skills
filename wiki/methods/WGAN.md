---

type: method
operation_types:
  primary: Construct auxiliary sequence
  secondary: []
title: WGAN (Wasserstein GAN)
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
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-15-WGAN的成功-可能跟Wasserstein距离没啥关系.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-01-20-从Wasserstein距离-对偶理论到WGAN.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-07-08-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-08-06-通向最优分布之路-概率空间的最小化.md
  - Data/wiki/sources/spaces-8512-两个多元正态分布的KL散度-巴氏距离和W距离.md
  - Data/wiki/sources/spaces-8512-正态分布距离.md
source_ids:
  - 6051
  - 6280
  - 7388
  - 8244
  - 8512
  - 8757
  - 9797
method_summary: Wasserstein GAN：用Earth Mover's Distance替代JS散度作为生成对抗网络的分布度量，通过Kantorovich-Rubinstein对偶和Lipschitz约束提供有意义的梯度，根本性解决GAN训练不稳定的问题。
typical_structure: |
  1. 将分布之间的差异度量替换为基于最优传输成本的 Wasserstein 距离
  2. 利用 Kantorovich-Rubinstein 对偶定理，将 Wasserstein 距离转化为对满足 1-Lipschitz 连续的函数的求上确界问题
  3. 引入判别器（Critic）网络 $D(x)$ 来近似该 1-Lipschitz 函数
  4. 设计并应用 Lipschitz 约束方法（如权重裁剪、梯度惩罚等）保证 $D(x)$ 满足约束
  5. 交替优化判别器 $D(x)$（最大化 Wasserstien 距离估计）和生成器 $G(z)$（最小化距离估计）
applicability: 生成对抗网络训练不稳定、模式崩溃、需要更有意义的生成损失梯度；或原目标难以直接优化或存在梯度消失时。
examples:
  - （待从源文章提取）
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::6280::基于 Kantorovich-Rubinstein 对偶将最优传输成本转化为判别器的最大化问题，从数学上推导了 WGAN 的目标函数
  - ev::8244::批判性观点指出，WGAN的成功可能主要来自对判别器施加的Lipschitz约束，而精确近似Wasserstein距离反而可能导致效果变差
belongs_to: []
layering_edge: "foundation"





---
## 适用问题

生成对抗网络（GAN）在使用 JS 散度等 f-散度度量分布距离时，常面临训练不稳定、梯度消失、模式崩溃（Mode Collapse）等问题，尤其在真实分布与生成分布没有重叠或重叠测度为零时。

## 核心变换

使用 Wasserstein 距离（最优传输距离）替代 JS 散度作为分布之间的度量，并通过 Kantorovich-Rubinstein 对偶将最小化最优传输成本的目标转化为：
$$
\min_G \max_{D, \Vert D\Vert_L \leq 1} \mathbb{E}_{x \sim P_r}[D(x)] - \mathbb{E}_{z \sim P_z}[D(G(z))]
$$
其中 $D$ 是判别器网络，受 1-Lipschitz 连续性约束。这使得即使分布不重叠也能提供平滑且有意义的梯度。

## 典型步骤

1. **引入距离度量**：将生成模型的目标定义为最小化生成分布与真实分布之间的 Wasserstein 距离。
2. **对偶转化**：利用 Kantorovich-Rubinstein 对偶定理，将 Wasserstein 距离的下确界计算转化为对所有 1-Lipschitz 函数求期望差的上确界问题。
3. **参数化近似**：使用判别器网络 $D(x)$ 来逼近该 1-Lipschitz 函数。
4. **施加 L 约束**：采用各种实现方式强制判别器满足 Lipschitz 约束，包括：
   - Weight Clipping (原始WGAN)
   - Gradient Penalty (WGAN-GP)
   - Spectral Normalization (SN-GAN)
   - Gradient Normalization
5. **交替优化**：交替最大化 $D(x)$ 的损失以估计 W 距离，最小化 $G(z)$ 的损失以拉近分布。

## 直觉

Wasserstein 距离可以直观理解为“推土机距离（Earth Mover's Distance）”，即把一个概率分布的“土”搬运成另一个分布所需的最小做功。相比于 JS 散度在分布不相交时直接为常数（导致梯度为 0），推土机距离总是连续且可导的，指引着生成分布一步步“移向”真实分布。通过对偶形式，判别器被赋予了衡量搬运距离（而非仅作二分类真假判定）的新物理意义，因而被称为 Critic。

## 边界

- **计算负担**：强加 Lipschitz 约束（尤其是梯度惩罚等）通常会引入额外的计算开销（如二阶导数计算），导致训练变慢。
- **理论与实际偏差（WGAN 批判）**：后续研究指出，WGAN 的成功可能主要来源于 L 约束赋予了判别器平滑性并避免了过拟合，而非 Wasserstein 距离本身。实际上，若试图更精确地逼近 Wasserstein 距离，生成效果反而可能变差。

## 例子

- **WGAN-GP**：通过在真实样本与生成样本之间的插值点处增加梯度范数的惩罚项 $\lambda \mathbb{E}_{\hat{x}} [(\Vert \nabla_{\hat{x}} D(\hat{x})\Vert_2 - 1)^2]$ 来软性实现 Lipschitz 约束，极大稳定了高分辨率图像生成任务中的对抗训练。

## 证据

- **ev::6280::对偶理论**：博客详细探讨了通过 Kantorovich-Rubinstein 对偶性将复杂的最优传输成本转化为对抗模型的数学基础。
- **ev::8244::WGAN批判**：讨论了 WGAN 的有效性主要来自于 Lipschitz 约束所带来的泛化能力，而非真的在优化 W 距离。
