---
type: article_summary
title: UniVAE：基于Transformer的单模型、多尺度的VAE模型
article_id: "8475"
source_url: https://spaces.ac.cn/archives/8475
date: 2021-06-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md
series:
  - "[[变分自编码器]]"
topics:
  - "[[生成模型]]"
  - "[[Attention效率与归一化]]"
concepts:
  - "[[变分自编码器]]"
  - "[[多尺度变分自编码]]"
methods:
  - "[[多尺度注意力掩码自编码]]"
  - "[[重参数技巧]]"
evidence_spans:
  - "ev::8475::uniae_attention_mask"
  - "ev::8475::multiscale_cls_aggregation"
  - "ev::8475::latent_dimension_reduction"
  - "ev::8475::layer_split_mask_decoupling"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md
source_ids:
  - "8475"
status: draft
updated: 2026-06-12
---

## 文章核心问题

如何在统一的 Transformer 架构中（权重共享的单模型），通过精细定制 Attention Mask 隐式融入 VAE 结构，并构造一种面向 NLP 文本生成的多尺度隐变量提取与重构机制。

## 主要结论

1. **UniAE 式 Attention Mask**：沿用类似 UniLM 将 Seq2Seq 融合在单模型中的思想，调整 Attention Mask 使得解码部分在每一步只能依赖于编码部分的固定 [CLS] 标记向量以及当前已完成的解码前缀，由此实现权重共享的 Unified Autoencoder（UniAE）。
2. **Transformer 的多尺度结构**：如果在每一层 Attention 都采用上述掩码，解码器每层在计算自注意力时均会关联到编码器对应层的 [CLS] 特征。将所有层的 [CLS] 拼接起来就构成了完整的隐表征，天然形成多尺度结构。
3. **两阶段特征降维**：为了控制总隐变量维度，对每层 [CLS] 向量使用全连接层先降维，在传入后续层前再升维拼回。
4. **解耦层与独立掩码**：为使隐变量拥有更好的解耦能力，前 $k$ 层（如前 8 层）采用独立式 Attention Mask（即编码与解码完全隔离），仅在靠输出的 $L-k$ 层采用 UniAE 掩码，从而保证隐变量有充足的深度表征进行解耦。

## 推导结构

1. **从 UniLM 到 UniAE 的演变**：
   - 传统 UniLM 的 Decoder 在每一位置都能关联到 Encoder 的每一个 Token 的输出。
   - 调整掩码矩阵，将 Decoder 的感受野限制为只有 Encoder 的 [CLS] 标记以及已解码的前序 Token，从而实现固定长度向量（信息瓶颈）的 AE 机制。
2. **多尺度表示拼接**：
   - 对于 $L$ 层 Attention 共享的网络，每一层输出的 [CLS] 均包含不同深度和尺度的抽象特征。
   - 所有层级 [CLS] 进行全连接降维：$h_l \to z_l \in \mathbb{R}^{d_{\text{latent}}}$。整个句子的隐空间表征由 $z = [z_{k+1}, \dots, z_L]$ 拼接而成。
3. **隐变量层级解耦实验**：
   - 实验表明，替换前部维度（靠近输入层）的隐变量，生成的文本大致上保持了主题词不变，仅改变句式；而替换后部维度（靠近输出层）的隐变量，句式大致保留，仅改变主题词，实现了层次化控制。

## 关键公式

本篇主要是关于 Transformer 的注意力遮蔽（Attention Masking）设计，其注意力计算的核心公式为：
$$
\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)V
$$
其中 $M$ 为定制的注意力掩码矩阵。对于 UniAE 掩码，设计规则为：
- 编码器位置之间可见：$M_{i,j} = 0\ (i, j \le L_{\text{enc}})$。
- 解码器位置对编码器仅 [CLS] 可见：$M_{i,j} = 0\ (i > L_{\text{enc}}, j = 1)$，而 $M_{i,j} = -\infty\ (1 < j \le L_{\text{enc}})$。
- 解码器位置对解码器前序可见：$M_{i,j} = 0\ (i > L_{\text{enc}}, L_{\text{enc}} < j \le i)$。

## 体现的方法

- **多尺度注意力掩码自编码**：通过精细定制的单模型 Transformer 掩码，在权重共享下完成层次化信息压缩与提取。
- **瓶颈自适应降维**：对 Transformer 中的高维中间状态执行局部全连接降维，以构造可控维度的隐表征。

## 所属系列位置

该文章属于《变分自编码器》系列。它提供了一种在 Transformer 中优雅嵌入 VAE 信息瓶颈的方法，并且通过共享权重和掩码控制，在文本生成领域实现了类似 CV 中经典的多尺度 VAE（如 NVAE）架构。

## 与其他文章的关系

- **变分自编码器**：本篇是 [[变分自编码器]] 系列与 Transformer 架构相结合的产物，展示了在自注意力框架下融合概率瓶颈的统一网络设计。
- **NVAE**：在 NLP 任务上实现类似 [[强大的NVAE]] 的多尺度隐空间表征。

## 原文证据锚点

- **UniAE 掩码矩阵设计**：见“UniAE”章节，对比了 UniLM 与 UniAE 掩码矩阵的图示和关联。对应 [ev::8475::uniae_attention_mask](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md#L20-L31)。
- **多尺度 [CLS] 拼接提取**：见“多尺度”章节，阐明了解码器每层 Attention 都依赖于编码器对应层 [CLS] 输出的拼接特征。对应 [ev::8475::multiscale_cls_aggregation](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md#L32-L43)。
- **全连接先降维再升维**：见“降低维度”章节，描述了使用全连接层解决 [CLS] 拼接特征过高维度的问题。对应 [ev::8475::latent_dimension_reduction](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md#L44-L51)。
- **前k层掩码隔离与深度解耦**：见“解耦能力”章节，讲述了前 $k$ 层使用独立掩码来为隐变量生成强特征，进而提升解耦能力。对应 [ev::8475::layer_split_mask_decoupling](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2021-06-29-UniVAE-基于Transformer的单模型-多尺度的VAE模型.md#L52-L68)。
