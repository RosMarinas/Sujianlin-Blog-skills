---
type: article_summary
title: 对比学习可以使用梯度累积吗？
article_id: 8471
source_url: https://spaces.ac.cn/archives/8471
date: 2021-06-17
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2021-06-17-对比学习可以使用梯度累积吗.md
sources: ["Data/Spaces_ac_cn/markdown/Mathematics/2021-06-17-对比学习可以使用梯度累积吗.md"]
source_ids: ["8471"]
status: draft
updated: 2026-06-12
---

# 对比学习可以使用梯度累积吗？

## 文章核心问题
对比学习损失由于在分母中包含了整个批次的样本相似度，属于非独立同分布场景，传统的基于单样本损失求和的简单梯度累积无法在此场景下等价实现大批次训练，需要探寻等效的累积计算流。

## 主要结论
通过对对比交叉熵（InfoNCE）梯度进行求导分析，发现其梯度可以通过为每个样本引入一个在 `stop_gradient` 算子下计算得到的辅助向量 $\\tilde{h}_i$（代表当前批次下的对比概率加权和）进行重写。在此重写下，总损失的导数等价于无多体交互的单样本内积求和目标 $\\sum_i \\langle h_i, \\tilde{h}_i\\rangle$。这意味着可以通过两步走的方式（在大批次下不求导计算 $\\tilde{h}_i$，再分小批次累加导数）实现等效大 Batch 梯度累积。但此方法由于重计算机制，与需要 Dropout 双重视角的 SimCSE 不兼容。

## 推导结构
1. 明确对比学习损失的非独立同分布特性。
2. 对 InfoNCE 损失求 $\\theta$ 偏导，并将概率矩阵项改写为常数算子。
3. 对内积相似度 $s_{i,j}=\\langle h_i, h_j\\rangle$ 展开求导，利用下标对称性消去其中一侧的导数流，归纳出辅助向量公式 $\\tilde{h}_i$。
4. 设计在大 batch 下计算预测向量、再以 $\\langle h_i, \\tilde{h}_i\\rangle$ 为 Dummy 损失积累梯度的两步流水线。

## 关键公式
- 对比梯度重写等价目标：$\\nabla_{\\theta}\\mathcal{L} = \\nabla_{\\theta}\\sum_{i=1}^b \\left\\langle h_i, 2\sum_{j=1}^b\\left(\\overline{p_{i,j}^{(sg)}} - t_{i,j}\\right)h_j^{(sg)}\\right\\rangle$
- 辅助目标定义：$\\tilde{h}_i = 2\\sum_{j=1}^b\\left(\\overline{p_{i,j}^{(sg)}} - t_{i,j}\\right)h_j^{(sg)}$

## 体现的方法
- [[对比学习梯度累加等效变换]]：将非独立同分布的大 batch 对比损失导数，利用 stop-gradient 提取出样本无关的常数向量，转换为单样本目标累加。

## 与其他文章的关系
- 指出了该技术与 [[中文任务还是SOTA吗？我们给SimCSE补充了一些实验]] 的不兼容性（因为多次前向与随机 Dropout 冲突）。

## 原文证据锚点
- `ev::8471::梯度累积`：对应原文中利用偏导数链式法则展开相似度矩阵，将多样本对比梯度化为单样本与基于 stop_gradient 产生的辅助向量内积梯度的完整数学推导。