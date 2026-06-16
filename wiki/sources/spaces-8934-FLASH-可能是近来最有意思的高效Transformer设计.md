---
type: article_summary
title: FLASH：可能是近来最有意思的高效Transformer设计
article_id: "8934"
source_url: https://spaces.ac.cn/archives/8934
date: 2022-02-25
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
series: [Transformer架构与归一化]
topics: [Attention优化, GAU]
concepts: [Gated Attention Unit, Mixed Chunk Attention, FLASH]
methods: [Gated Attention Unit, Mixed Chunk Attention]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
source_ids:
  - "8934"
status: draft
updated: 2026-06-12
---

# FLASH：可能是近来最有意思的高效Transformer设计

## 文章核心问题
如何融合注意力层（Attention）和前馈神经网络（FFN），以简化 Transformer 架构并提升运行速度与显存利用率？如何在自注意力中仅用单头（Single Head）就替代传统的多头注意力？如何利用局部与全局混合的线性化策略（Mixed Chunk Attention）在大序列长度下实现稳定的线性时间复杂度？

## 主要结论
- 提出 GAU（Gated Attention Unit，门控注意力单元），将门控线性单元（GLU）和自注意力完美融合成一个单一的架构层，大幅减少了模型的层冗余。
- 在 GAU 中，由于强大的门控特性，注意力层仅需要单头（Single Head, $h=1$）便能获得与多头注意力相当甚至更优的拟合性能，从而彻底去除了存储 $bhn^2$ 级别多头得分矩阵的资源负担。
- 基于 GAU 的二次复杂度模型称为 FLASH-Quad，其在速度、效果、最大批尺寸（batch_size）上全面超越传统的 Transformer 架构。
- 提出 MCA（Mixed Chunk Attention，分块混合注意力）机制，将长序列分成若干不重叠的块。块内计算局部自注意力（二次复杂度），块间通过共享的 Key-Value 进行线性注意力计算（线性复杂度），构成具有真正线性复杂度的 FLASH 模型，成功实现了高效的 Decoder  causal 训练并行性。

## 推导结构
1. **构建 GAU 架构**：
   以 GLU 式 FFN 为基础：$\boldsymbol{O} = (\boldsymbol{U} \odot \boldsymbol{V})\boldsymbol{W}_o$。为引入 token 之间的信息交互，将注意力项融合进去，形成 $\boldsymbol{O} = (\boldsymbol{U} \odot \boldsymbol{A}\boldsymbol{V})\boldsymbol{W}_o$。
2. **简化自注意力矩阵**：
   GAU 的单头注意力得分直接使用普通的非 softmax 激活函数计算：$\boldsymbol{A} = \frac{1}{ns} \text{relu}^2(\mathcal{Q}(\boldsymbol{Z})\mathcal{K}(\boldsymbol{Z})^{\top})$，其中 $\boldsymbol{Z} = \phi_z(\boldsymbol{X}\boldsymbol{W}_z) \in \mathbb{R}^{n \times s}$ 且注意力投影维度固定为 $s=128$，去除了多头。
3. **线性化 Mixed Chunk Attention (MCA)**：
   将序列划分为 $n/c$ 个长为 $c$ 的非重叠块。
   - **局部注意力**：块 $g$ 内部做局部交互，$\hat{\boldsymbol{V}}_g^{\text{quad}} = \frac{1}{cs}\text{relu}^2\left(\boldsymbol{Q}_g^{\text{quad}}{\boldsymbol{K}_g^{\text{quad}}}^{\top}\right)\boldsymbol{V}_g$，复杂度正比于 $nc$。
   - **全局注意力**：利用线性注意力跨块交互，$\hat{\boldsymbol{V}}_g^{\text{lin}} = \frac{1}{n}\boldsymbol{Q}_g^{\text{lin}}\sum_{h} {\boldsymbol{K}_h^{\text{lin}}}^{\top}\boldsymbol{V}_h$。
   - **结合输出**：$\boldsymbol{O}_g = \left[\boldsymbol{U}_g \odot \left(\hat{\boldsymbol{V}}_g^{\text{quad}} + \hat{\boldsymbol{V}}_g^{\text{lin}}\right)\right]\boldsymbol{W}_o$。

## 关键公式
- GAU 注意力表示: $\boldsymbol{O} = (\boldsymbol{U} \odot \boldsymbol{A}\boldsymbol{V})\boldsymbol{W}_o$
- GAU 单头激活矩阵: $\boldsymbol{A} = \frac{1}{ns} \text{relu}^2(\mathcal{Q}(\boldsymbol{Z})\mathcal{K}(\boldsymbol{Z})^{\top})$
- MCA 块间全局线性项（Causal 形式）: $\hat{\boldsymbol{V}}_g^{\text{lin}} = \frac{1}{(g-1)n/c}\boldsymbol{Q}_g^{\text{lin}}\sum_{h=1}^{g-1} {\boldsymbol{K}_h^{\text{lin}}}^{\top}\boldsymbol{V}_h$

## 体现的方法
- Gated Attention Unit (GAU) 融合技术
- Mixed Chunk Attention (MCA) 线性化技术

## 所属系列位置
Transformer架构与归一化系列第6篇，是本系列在结构重构和注意力高效线性化上的集大成之作。

## 与其他文章的关系
本篇提出的 GAU 由于其独特的非 softmax 归一化（直接除以序列长度 $n$），在后续第10篇中被分析证明：其天然避开了经典相对位置编码因 row-sum 恒等于 1 导致的无法拟合恒等零输入排序探针的理论缺陷。同时，GAU 的超大规模扩展和稳定性，在第7篇中得到了基于恒等映射的理论证明。

## 原文证据锚点
- GAU 计算框架：公式 (mix) 到 (relu-att)。
- 单头消融实验：消融图表证实 Head=1 与 GAU-GLU 配合足以媲美 Head=12。
- MCA 全局分块与 Causal 并行性：见 "高效线性" 章节下的 Causal 递归推导。
- 实验结论：FLASH-Quad 和 FLASH 在 LRA 以及语言模型预训练的速度-效果曲线上均占据主导地位。
