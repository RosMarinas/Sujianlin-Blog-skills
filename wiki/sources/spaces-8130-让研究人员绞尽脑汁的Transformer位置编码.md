---
type: article_summary
title: 让研究人员绞尽脑汁的Transformer位置编码
article_id: "8130"
source_url: https://spaces.ac.cn/archives/8130
date: 2021-02-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
series: [Transformer架构与归一化]
topics: [位置编码]
concepts: [绝对位置编码, 相对位置编码, 旋转位置编码]
methods: [相对位置编码计算, 乘性与复数融合位置编码]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
source_ids:
  - "8130"
status: draft
updated: 2026-06-12
---

# 让研究人员绞尽脑汁的Transformer位置编码

## 文章核心问题
对于无法识别顺序的自注意力模型，如何系统性地设计位置编码？绝对位置编码和相对位置编码有哪些主要的演化路径与变体？如何设计一种将绝对位置操作转化为相对位置计算的融合机制（即后续RoPE的基础思想）？

## 主要结论
- 位置编码主要分为绝对位置编码（融入输入中，如可学习、三角函数、FLOATER/递归式、乘性式）和相对位置编码（融入注意力矩阵中，如经典Shaw、XLNet/Transformer-XL、T5、DeBERTa）。
- 绝大多数相对位置编码仅作用于注意力得分矩阵，在 $V$ 上去除了位置偏置。
- 利用二维复数旋转性质，可以通过给 Query 和 Key 施加绝对位置操作（乘上 $e^{\text{i}n\theta}$），使其内积自发蕴含相对位置特征（依赖于相对偏置 $m-n$）。这是旋转位置编码（RoPE）的核心理论前提。
- 提出了 CNN 可以仅靠 Zero Padding 机制泄露相对边界距离以识别位置的有趣发现。

## 推导结构
1. **绝对位置编码变体**：
   - **可学习式**：常规矩阵参数，缺乏天然外推性，但可用层次分解解决。
   - **三角函数式**：Sinusoidal，基于三角公式分解相对位置。
   - **递归式/FLOATER**：用常微分方程（ODE）建模：$d\boldsymbol{p}_t/dt = \boldsymbol{h}(\boldsymbol{p}_t, t)$。
   - **相乘式**：利用逐位相乘 $\boldsymbol{x}_k \otimes \boldsymbol{p}_k$ 替代传统的相加。
2. **相对位置编码变体**：展开注意力项 $q_i k_j^{\top} = (x_i + p_i) W_Q W_K^{\top} (x_j + p_j)^{\top}$ 并简化：
   - **经典式 (Shaw)**：将 $p_j$ 替换为截断的相对距离向量 $R_{i,j}^K$。
   - **XLNet (Transformer-XL)**：用全局正弦相对向量 $R_{i-j}$ 和可学习偏置 $u, v$ 替代对 $q_i$ 的依赖。
   - **T5**：去掉输入与位置的交互项，仅保留内容交互和标量偏置：$x_i W_Q W_K^{\top} x_j^{\top} + \beta_{i,j}$。采用分桶映射对近距离精细编码、远距离粗糙编码。
   - **DeBERTa**：去除位置-位置交互项，仅保留内容-内容、内容-位置和位置-内容三项。
3. **复数融合位置编码 (RoPE前身)**：
   将 Query 和 Key 当作二维复数向量。设复数内积为 $\langle \boldsymbol{q}_m, \boldsymbol{k}_n\rangle = \text{Re}\left[\boldsymbol{q}_m \boldsymbol{k}_n^*\right]$。
   将绝对位置偏置乘在向量上：$\boldsymbol{q}_m \to \boldsymbol{q}_m e^{\text{i}m\theta}$，$\boldsymbol{k}_n \to \boldsymbol{k}_n e^{\text{i}n\theta}$。
   在求内积时：$\langle \boldsymbol{q}_m e^{\text{i}m\theta}, \boldsymbol{k}_n e^{\text{i}n\theta}\rangle = \text{Re}[\boldsymbol{q}_m \boldsymbol{k}_n^* e^{\text{i}(m-n)\theta}]$，自发将绝对位置映射为了相对位置 $m-n$ 的关系。

## 关键公式
- XLNet 注意力公式: $\boldsymbol{x}_i \boldsymbol{W}_Q \boldsymbol{W}_K^{\top}\boldsymbol{x}_j^{\top} + \boldsymbol{x}_i \boldsymbol{W}_Q \boldsymbol{W}_{K,R}^{\top}\boldsymbol{R}_{i-j}^{\top} + \boldsymbol{u}\boldsymbol{W}_K^{\top}\boldsymbol{x}_j^{\top} + \boldsymbol{v} \boldsymbol{W}_{K,R}^{\top}\boldsymbol{R}_{i-j}^{\top}$
- T5 注意力公式: $\boldsymbol{x}_i \boldsymbol{W}_Q \boldsymbol{W}_K^{\top}\boldsymbol{x}_j^{\top} + \beta_{i,j}$
- 二维复数内积相对演化: $\langle \boldsymbol{q}_m e^{\text{i}m\theta}, \boldsymbol{k}_n e^{\text{i}n\theta}\rangle = \text{Re}\left[\boldsymbol{q}_m \boldsymbol{k}_n^* e^{\text{i}(m-n)\theta}\right]$
- 旋转坐标变换: $\begin{pmatrix} x \\ y \end{pmatrix} \to \begin{pmatrix} x \cos n\theta - y \sin n\theta \\ x \sin n\theta + y \cos n\theta \end{pmatrix}$

## 体现的方法
- 相对位置编码变换与简化
- 二维复数旋转位置融合法 (RoPE 推导)

## 所属系列位置
Transformer架构与归一化系列第4篇，全面总结和梳理了业界位置编码变体，并首次公开提出了旋转融合位置编码（RoPE）的设计草案。

## 与其他文章的关系
本篇汇总的位置编码体系是第8篇 RoFormerV2 结构简化的前置知识（RoFormerV2 去除了所有 bias，使用了简化的 RoPE）。同时，本篇提出的“复数旋转内积只依赖相对距离”的推导，直接启发了后期 RoPE 在主流大模型中的应用，也是第10篇中研究相对位置编码 Transformer 拟合能力缺陷的核心背景。

## 原文证据锚点
- 绝对与相对位置公式展开：公式 (QK-exp) 及其各项分析。
- T5 与 DeBERTa 位置偏置：公式 (rp-clip) 之后的段落阐述。
- 旋转融合位置编码理论发现：式 (complex) 之后的 "融合式" 这一小节，详细展示了复数内积的证明和二维坐标变换矩阵的引出。
