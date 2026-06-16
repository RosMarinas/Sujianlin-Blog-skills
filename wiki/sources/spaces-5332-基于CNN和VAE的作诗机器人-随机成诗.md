---
type: article_summary
title: 基于CNN和VAE的作诗机器人：随机成诗
article_id: "5332"
source_url: https://spaces.ac.cn/archives/5332
date: 2018-03-24
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2018-03-24-基于CNN和VAE的作诗机器人-随机成诗.md
series:
  - "[[变分自编码器]]"
topics:
  - "[[生成模型]]"
concepts:
  - "[[变分自编码器]]"
  - "[[门控卷积网络]]"
methods:
  - "[[门控卷积序列建模]]"
  - "[[重参数技巧]]"
evidence_spans:
  - "ev::5332::gcnn_gate"
  - "ev::5332::cnn_vae_structure"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-03-24-基于CNN和VAE的作诗机器人-随机成诗.md
source_ids:
  - "5332"
status: draft
updated: 2026-06-12
---

## 文章核心问题

如何使用变分自编码器（VAE）来进行文本生成，特别是如何构建一个将随机数映射为特定长度（五言诗，10个字）诗句的“随机成诗”文本生成模型。

## 主要结论

1. 文本生成（特别是无条件随机文本生成）是 VAE 的优势应用，因为文本生成是基于重构进行的，不需要像 GAN 那样在离散且不可导的符号空间中训练判别器。
2. 结合一维门控卷积网络（GCNN）与 VAE 结构，能够有效建立随机隐变量到特定长度诗句的映射，生成的诗句在对仗和平仄上具有一定的合理性。
3. 门控卷积（GCNN）在多项 NLP 任务上的实测表现优于普通的 CNN + ReLU 组合。

## 推导结构

1. **结构设计**：每个字先映射为 Embedding 向量，经层叠 CNN 进行编码，池化得到表征，计算均值和方差，通过重参数采样得到隐变量；解码器通过多层全连接层将单个隐变量展开为多字序列，再接全连接输出预测。
2. **激活函数（GCNN）**：引入带“门（gate）”控的卷积设计，对比说明在文本处理中 GCNN 对比普通 CNN 的优势。
3. **实验观察**：使用全唐诗语料库进行五言单句诗（10个字）生成，建立 evaluator 跟踪训练过程中从无序随机字到具有诗歌平仄对仗结构的发展。

## 关键公式

本篇主要是架构和工程实现说明，核心公式为 GCNN 门控公式：
$$
Y = (X * W_1 + b_1) \otimes \sigma(X * W_2 + b_2)
$$
其中 $*$ 为一维卷积，$\otimes$ 表示元素对应相乘（Hadamard积），$\sigma$ 为 Sigmoid 激活函数，起到门控控制信息流的作用。

## 体现的方法

- **门控卷积序列建模**：利用门控机制自适应选择特征，代替传统 CNN 的简单非线性激活。
- **重参数技巧**：在前向中结合随机正态分布，并利用 $z = \mu + \sigma \odot \epsilon$ 保证梯度可传导。

## 所属系列位置

该文章属于《变分自编码器》系列，属于将 VAE 应用于自然语言处理（NLP）领域的具体玩具实践，验证 VAE 在离散文本建模中的易训练性。

## 与其他文章的关系

- **变分自编码器**：本篇是 [[变分自编码器]] 系列的工程落地应用展示，对比说明了 VAE 在文本生成上较 GAN 的易优化性。
- **GCNN 应用**：为后续基于卷积的序列生成和特征建模提供基础单元。

## 原文证据锚点

- **GCNN 门控机制**：见“GCNN”章节，描述为：两个外形一样的 CNN，一个不加激活函数，一个用 sigmoid 激活并相乘。对应 [ev::5332::gcnn_gate](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2018-03-24-基于CNN和VAE的作诗机器人-随机成诗.md#L34-L40)。
- **模型结构设计**：见“CNN + VAE”章节，描述了 Encoder-Decoder 结构以及全连接的多样性输出。对应 [ev::5332::cnn_vae_structure](file:///Users/polaris/Documents/Graduate/AI/Document/notes/Blog/Data/Spaces_ac_cn/markdown/Big-Data/2018-03-24-基于CNN和VAE的作诗机器人-随机成诗.md#L28-L33)。
