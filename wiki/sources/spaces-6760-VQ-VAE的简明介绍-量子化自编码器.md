---
type: article_summary
title: VQ-VAE的简明介绍：量子化自编码器
article_id: "6760"
source_url: https://spaces.ac.cn/archives/6760
date: 2019-06-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-06-24-VQ-VAE的简明介绍-量子化自编码器.md
series:
  - "[[变分自编码器]]"
topics:
  - "[[生成模型]]"
  - "[[向量量化优化]]"
concepts:
  - "[[矢量量化自编码器]]"
  - "[[直通估计器]]"
methods:
  - "[[直通估计方法]]"
  - "[[stop_gradient自定义反向传播]]"
formulas:
  - "[[直通估计公式]]"
  - "[[矢量量化重构损失公式]]"
evidence_spans:
  - "ev::6760::argmin_quantize"
  - "ev::6760::straight_through_gradient"
  - "ev::6760::vq_vae_loss_split"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-24-VQ-VAE的简明介绍-量子化自编码器.md
source_ids:
  - "6760"
status: draft
updated: 2026-06-12
---

## 文章核心问题

探讨矢量量化自编码器（VQ-VAE）的核心机理，特别是如何通过最邻近搜索将连续表征转换为离散编码（量子化），以及如何在不可导操作的背景下使用直通估计器（Straight-Through Estimator, STE）完成端到端的梯度反向传播。

## 主要结论

1. **自回归生成的局限**：原生的 PixelCNN 逐像素自回归生成非常缓慢（需要依次循环预测几万个像素）。并且它把连续像素离散地视为完全割裂的分类类别，没有考虑相近数值的视觉相似度。
2. **VQ-VAE 降维建模**：VQ-VAE 先通过自编码器将图像降维（例如将 $128 \times 128 \times 3$ 压缩为 $32 \times 32$ 维度的离散编码），然后再使用自回归模型（PixelCNN 或 PixelAtt）对这个离散矩阵的先验分布进行拟合，从而大幅缩短了序列长度并显著提升生成效率。
3. **最邻近离散映射**：Encoder 输出的连续表征矩阵 $z$ 中的每个位置的向量均与 Embedding 编码表中的各个向量计算欧氏距离，通过 $\text{argmin}$ 操作被替换为最近邻的编码表向量 $z_q$，这便实现了离散化。
4. **梯度流的 STE 传输**：为了让编码器可训练，前向计算使用 $z_q$，而反向传播通过人为定制的梯度操作，将 $z_q$ 的梯度无损传回连续编码 $z$。
5. **编码表维护**：使用分离的损失项（Commitment Loss）来约束连续隐表征去逼近编码表向量，同时也约束编码表向量去靠拢连续隐表征。

## 推导结构

1. **降维与最近邻搜索**：
   - 输入图像 $x$ 经 Encoder 得到维度为 $m \times m \times d$ 的特征图 $z$。
   - 对每一个 $d$ 维向量 $z_{ij}$，在大小为 $K \times d$ 的编码表 $E$ 中寻找最近邻向量 $e_k$，并取该 $e_k$ 组合为 $z_q$。
2. **STE 的数学等价技巧**：
   - 前向需要 $z_q$，反向计算需要 $\nabla_z \approx \nabla_{z_q}$。
   - 构造等效目标：$z + \text{sg}[z_q - z]$。前向前式等于 $z_q$；反向求导时由于带 $\text{sg}$（stop gradient）的部分被忽略，对 $z$ 的偏导恒等于 1，完成了梯度直通。
3. **损失项划分与权重分配**：
   - 考虑反向传播，将码本匹配距离 $\Vert z - z_q\Vert_2^2$ 分解为两部分：第一项 $\Vert \text{sg}[z] - z_q\Vert_2^2$ 控制编码表向编码特征靠近；第二项 $\Vert z - \text{sg}[z_q]\Vert_2^2$ 约束编码特征向编码表靠近（加上 $\gamma < \beta$ 权重）。

## 关键公式

- **最近邻量子化查找**：
  $$
  z_q = e_k,\quad k = \mathop{\text{argmin}}_j \Vert z - e_j\Vert_2
  $$
- **直通估计等效目标**：
  $$
  z_{\text{STE}} = z + \text{sg}[z_q - z]
  $$
- **VQ-VAE 联合训练损失函数**：
  $$
  L = \Vert x - \text{decoder}(z_{\text{STE}})\Vert_2^2 + \beta \Vert \text{sg}[z] - z_q\Vert_2^2 + \gamma \Vert z - \text{sg}[z_q]\Vert_2^2
  $$

## 体现的方法

- **直通估计方法**：利用截断梯度重写求导图，使得离散化 argmin 操作获得恒等导数。
- **自定义梯度重构**：在前向与反向之间插入不对称表示层，规避离散空间的梯度消失。

## 所属系列位置

该文章属于《变分自编码器》系列。它将自编码器从传统的连续正态先验推向了离散编码空间（VQ），尽管没有概率分布的采样操作（更接近 AE），但提供了利用自回归模型进行离散先验密度估计的经典架构。

## 与其他文章的关系

- **变分自编码器**：打破了以往需要做高斯重参数的连续空间限制，将图像表示视为离散的 Token。
- **量化优化**：为后续的 FSQ（有限标量量化）、DiVeQ、旋转技巧等量化优化提供了最基础的基准模型。

## 原文证据锚点

- **最近邻检索机制**：见“最邻近重构”章节，给出了 argmin 欧式距离的公式。对应 [ev::6760::argmin_quantize](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2019-06-24-VQ-VAE的简明介绍-量子化自编码器.md#L68-L88)。
- **直通估计与 sg 的巧妙运用**：见“自行设计梯度”章节，描述了 `z + sg[zq - z]` 的巧妙前向反向构造。对应 [ev::6760::straight_through_gradient](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2019-06-24-VQ-VAE的简明介绍-量子化自编码器.md#L110-L117)。
- **编码表双向靠近的损失权重划分**：见“维护编码表”章节，分析了 $\beta$ 和 $\gamma$ 分别约束 $z_q$ 靠近 $z$ 以及 $z$ 靠近 $z_q$ 的过程。对应 [ev::6760::vq_vae_loss_split](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2019-06-24-VQ-VAE的简明介绍-量子化自编码器.md#L122-L135)。
