---
type: article_summary
title: 用开源的人工标注数据来增强RoFormer-Sim
article_id: 8541
source_url: https://spaces.ac.cn/archives/8541
date: 2021-07-19
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-07-19-用开源的人工标注数据来增强RoFormer-Sim.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-07-19-用开源的人工标注数据来增强RoFormer-Sim.md"]
source_ids: ["8541"]
status: draft
updated: 2026-06-12
---

# 用开源的人工标注数据来增强RoFormer-Sim

## 文章核心问题
无监督与弱监督相似度模型（如旧检索版）极易在逻辑对立（如“喜欢”与“不喜欢”）等极小维度差异上给出超高相似度。需要引入有监督微调方案在保留 RoFormer-Sim 生成能力的同时，通过人工标注数据校正检索语义度量空间。

## 主要结论
1. 人主观认知的“反义”在自然语义特征上实际上处于极其相似的各向同性子空间。要拉开该维度的距离，必须依靠有监督标签约束。
2. 实验发现直接基于 $\\cos(u,v)$ 计算分类的损失在句向量上表现不佳，而训练和预测不一致的 Sentence-BERT 方案效果最优。通过把 $u,v,|u-v|$ 拼接再接全连接做分类，能够有效地将“主题相关度”和“绝对语义邻近”解耦（$|u-v|\\to 0$ 约束语义邻近），从而训练出高质量特征。
3. 训练好的句向量检索能力可通过相似度矩阵蒸馏回馈给 RoFormer-Sim-FT。

## 推导结构
1. 讨论人类反义认知与无监督客观相似性的偏差，说明有监督微调的必要。
2. 分类归纳 ATEC、BQ、PAWSX 等中文相似度与 NLI 数据。
3. 比较余弦直接损失与 Sentence-BERT 拼接分类损失的效果，分析 $u,v,|u-v|$ 的数学直觉。
4. 给出 fine-tuned-FT 模型的实例对比。

## 关键公式
- SBERT 特征拼接打分映射：$s = \\langle u, w_1\\rangle + \\langle v, w_2\\rangle + \\langle |u-v|, w_3\\rangle$

## 体现的方法
- [[Sentence-BERT训练与拼接特征]]：使用 $[u, v, |u-v|]$ 特征表示与线性层训练句向量。
- [[人工标注数据有监督增强]]：利用有标签数据注入人类主观偏置。

## 与其他文章的关系
- 蒸馏和整合的后处理步骤参见 [[SimBERTv2来了！融合检索和生成的RoFormer-Sim模型]]。

## 原文证据锚点
- `ev::8541::特征拼接`：对应原文中介绍 Sentence-BERT 训练时拼接 $u, v, |u-v|$ 特征，并解释其在数学上如何解耦“主题相关”和“语义相似”以包容数据标注噪声的直觉分析。