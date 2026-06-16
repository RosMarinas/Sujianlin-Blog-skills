---
type: article_summary
title: Google新作Synthesizer：我们还不够了解自注意力
article_id: "7430"
source_url: https://spaces.ac.cn/archives/7430
date: 2020-05-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
series: [Transformer架构与归一化]
topics: [Attention优化]
concepts: [Google Synthesizer]
methods: [Synthesizer注意力生成]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
source_ids:
  - "7430"
status: draft
updated: 2026-06-12
---

# Google新作Synthesizer：我们还不够了解自注意力

## 文章核心问题
标准的自注意力机制中，通过 Query 和 Key 计算“token对token”的动态交互，这种计算方式是必须的吗？能不能通过去除或简化这种动态计算，换成更简单的映射或者静态矩阵来生成注意力权重，并且保持良好的性能？

## 主要结论
- 自注意力核心在于生成 $n \times n$ 的注意力分布矩阵。传统的“token对token”内积并非唯一可行的途径。
- Dense 形式（固定 Key 为常数矩阵，注意力矩阵 $B = X W_a$）以及 Random 形式（注意力矩阵 $B = R$ 为完全随机的常数矩阵）在许多单任务场景（如机器翻译、对话生成）中都能取得与标准自注意力几乎相当甚至更好的效果。
- 静态/简化的自注意力变体（如 Random，等价于可分离卷积）在迁移学习（如预训练微调 T5）上面表现较为逊色，说明动态自注意力在模型通用迁移能力上依然重要，但在单一领域的速度和效率优化上，简化自注意力具有很大优势。

## 推导结构
1. **统一自注意力公式**：自注意力本质上是 $A X W_v$，其中注意力分布 $A = softmax(B)$。标准注意力中 $B = \frac{X W_q W_k^{\top} X^{\top}}{\sqrt{d_k}}$。
2. **提出 Synthesizer 变体**：
   - **Dense**：令 $B = relu(X W_1 + b_1) W_2 + b_2$，直接使用前馈网络根据当前位置 $X$ 预测该位置对所有其他位置的注意力，不计算 token 两两内积。
   - **Random**：令 $B = R \in \mathbb{R}^{n \times n}$，完全不依赖输入 $X$，类似于卷积核在训练期间固定或更新，代表了一种全局静态的位置注意先验。
   - **Factorized 低秩分解**：为了防止 Dense 和 Random 参数过大，设计 Factorized Dense ($B = \tilde{B}_1 \otimes \tilde{B}_2$) 和 Factorized Random ($B = R_1 R_2^{\top}$)。
   - **Mixture 混合模式**：以可学习权重 $\alpha_i$ 将上述多种注意力得分叠加：$B = \sum_i \alpha_i B_i$。
3. **评测与实验**：在机器翻译、摘要、对话、以及 T5 预训练任务上评测。Random 在对话生成上表现最好，但在迁移性上较弱。

## 关键公式
- Dense注意力得分: $B = relu(X W_1 + b_1) W_2 + b_2$
- Random注意力得分: $B = R$
- Factorized Random低秩分解: $B = R_1 R_2^{\top}$，其中 $R_1, R_2 \in \mathbb{R}^{n \times k}$
- 混合模式注意力: $B = \sum_i \alpha_i B_i$

## 体现的方法
- Synthesizer注意力生成 (Dense/Random/Factorized)

## 所属系列位置
Transformer架构与归一化系列第2篇，对注意力核心机制中“动态 token 对交互”的必要性进行了根本性质疑。

## 与其他文章的关系
本文表明常数注意力矩阵或无交互注意力也能工作良好，这启发了第3篇 T-TA 中保持 K, V 恒定以预测所有 token 的重构设计，也与第6篇 FLASH 局部与全局分块混合注意力设计形成对比。

## 原文证据锚点
- Dense 与 Random 定义：公式 (59) 到 (72)。
- 机器翻译、摘要、对话实验：翻译上 Dense/Random 媲美标准 Attention；对话上标准 Attention 表现最差。
- T5 预训练实验：标准 Attention 表现最好，Dense 和 Random 在迁移能力上受限。
