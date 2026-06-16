---
type: example
title: GCNN作诗机器人模型结构
article_id: "5332"
article: "[[spaces-5332-基于CNN和VAE的作诗机器人-随机成诗]]"
section: CNN + VAE
claim: 一维层叠门控卷积网络与变分自编码器结合可实现定长文本的无条件随机生成
notation_mapping:
  input_sequence: x
  word_embeddings: X
  encoder_output: h
  latent_mean: \mu
  latent_log_variance: \log\sigma^2
  sampled_latent: z
  reconstructed_sequence: \hat{x}
steps:
  - 1. **文本输入分词与Embedding**：将五言诗序列 $x$ 的每个字映射为 $d_{\text{word}}$ 维的一维嵌入向量，得到特征矩阵 $X \in \mathbb{R}^{10 \times d_{\text{word}}}$。
  - 2. **编码器门控卷积提取**：通过多层层叠的一维门控卷积网络（GCNN）对 $X$ 编码特征，最后使用全局最大池化层进行时序池化，获得句子的全局连续隐向量表示 $h \in \mathbb{R}^{d_{\text{hidden}}}$。
  - 3. **均值与方差映射**：将 $h$ 分别送入两个独立的 Dense 全连接层，生成高斯后验分布的绝对均值 $\mu \in \mathbb{R}^{d_{\text{latent}}}$ 以及对数方差 $\log\sigma^2 \in \mathbb{R}^{d_{\text{latent}}}$。
  - 4. **潜表征重参数化采样**：利用正态分布噪声 $\epsilon \sim \mathcal{N}(0, I)$ 进行重参数化采样，求得隐随机特征 $z = \mu + \exp(\frac{1}{2}\log\sigma^2) \odot \epsilon$。
  - 5. **解码器多样性输出展开**：在解码阶段，由于只有一个编码特征 $z$，为生成固定长度的 10 个字，使用 10 个独立的全连接层分别处理 $z$ 得到每个位置的不同隐藏表征，然后接 GCNN 和 Dense softmax，最终输出预测字概率序列 $\hat{x}$。
used_concepts:
  - "[[变分自编码器]]"
  - "[[门控卷积网络]]"
used_methods:
  - "[[门控卷积序列建模]]"
  - "[[重参数技巧]]"
source_span: ev::5332::cnn_vae_structure
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-03-24-基于CNN和VAE的作诗机器人-随机成诗.md
source_ids:
  - "5332"
status: draft
updated: 2026-06-12
---

本例展示了利用 CNN + VAE 架构处理固定长度（10个字）文本随机映射生成的可行方案。它利用全连接的多样性输出解决了单个隐变量展开为多字时序的难题，并采用 GCNN 门控结构保证了特征的保留度。

在该模型架构的实现和设计上，其最关键的技术难点在于文本生成的离散型特点。在传统的图像自编码生成中，Decoder 预测的是连续的像素灰度值；但在文本生成任务中，Decoder 必须在每一位置预测词表中上万个离散字詞的概率。采用纯一维层叠卷积 GCNN 的编码-解码结构，避开了传统 GAN 在处理离散符号时 Jacobian 不可导、训练发散的难题。由于 GCNN 包含了基于 Sigmoid 的自适应信息调制门控分支，对诗歌这类具有强烈对仗、平仄规律以及紧凑结构的空间文本序列具有极佳的拟合表现，其实测的句式对齐效果比普通的 CNN 网络有显著提升。
