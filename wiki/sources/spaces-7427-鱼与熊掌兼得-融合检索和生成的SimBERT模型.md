---
type: article_summary
title: 鱼与熊掌兼得：融合检索和生成的SimBERT模型
article_id: 7427
source_url: https://spaces.ac.cn/archives/7427
date: 2020-05-18
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md"]
source_ids: ["7427"]
status: draft
updated: 2026-06-12
---

# 鱼与熊掌兼得：融合检索和生成的SimBERT模型

## 文章核心问题
如何构建一个同时具备相似问生成（NLG）和相似句检索（NLU）能力的统一 Transformer 语言模型。

## 主要结论
提出了 SimBERT 模型。基于 UniLM 的注意力掩码（Attention Mask）控制机制，输入端执行双向编码以生成能够代表句子全局语义的 `[CLS]` 检索向量，输出端执行单向自回归解码以生成相似句。利用 Batch 内的非相似句作为负样本，通过 Softmax 交叉熵损失拉近相似句表示并推远负样本，最终联合 Seq2Seq 损失实现多任务端到端微调。

## 推导结构
1. 介绍 UniLM 的注意力掩码构造原理。
2. 阐述 SimBERT 的双向编码与单向自回归微调融合方案。
3. 提出 Batch Softmax 对比检索损失，提取 L2 归一化后的 `[CLS]` 进行句子表征，以分类任务代替传统回归。

## 关键公式
- Batch 内相似度分类损失：对归一化特征矩阵 $\\tilde{\\boldsymbol{V}}$ 计算内积矩阵 $\\tilde{\\boldsymbol{V}}\\tilde{\\boldsymbol{V}}^{\\top}$，并乘以 scale（一般取30），对角线 mask 后做分类 Softmax 交叉熵训练。

## 体现的方法
- [[UniLM自回归掩码编码]]：控制不同分块的可见性以执行多任务。
- [[句向量对比学习分类训练]]：使用批次内负采样及 Softmax 对比损失训练检索。

## 与其他文章的关系
- 为升级版 [[RoFormer-Sim]] 提供了架构基础。
- 对比学习部分直接启发了 [[SimCSE]] 的无监督化探索。

## 原文证据锚点
- `ev::7427::检索部分`：对应原文中提取批次句向量并计算 scaled 对角线掩码相似度 Softmax 分类损失的部分。