---
type: series
title: Transformer架构与归一化
aliases: []
article_ids:
  - "7325"
  - "7430"
  - "7661"
  - "8130"
  - "8610"
  - "8934"
  - "8990"
  - "8998"
  - "9009"
  - "9105"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-07-修改Transformer结构-设计一个更快更好的MLM模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-09-线性Transformer应该不是你要等的那个模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-11-门控注意力单元-GAU-还需要Warmup吗.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-21-RoFormerV2-自然语言理解的极限探索.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-29-为什么Pre-Norm的效果不如Post-Norm.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
source_ids:
  - "7325"
  - "7430"
  - "7661"
  - "8130"
  - "8610"
  - "8934"
  - "8990"
  - "8998"
  - "9009"
  - "9105"
series_goal: 探究Transformer模型在结构重构、自注意力瓶颈优化（如低秩、线性化及融合）、层归一化（Pre-Norm对Post-Norm的深度拟合退化）以及位置编码演进与缺陷上的理论和工程调优。
entry_roles:
  "7325": 指自主注意力在大head数下的低秩瓶颈，并提出增大key_size与Talking-Heads多头混合概率分布的解决方案。
  "7430": 质疑Query-Key动态token内积的必要性，并探究Dense与Random静态注意力分布在各类NLP任务上的能力与局限。
  "7661": 提出T-TA自编码器机制，通过解耦首层Query位置编码与层间共享K,V键值对，实现MLM全Token无泄漏并行预训练。
  "8130": 系统梳理绝对与相对位置编码演化路径（如Shaw、XLNet、T5、DeBERTa），并引出复数旋转融合位置特征的RoPE草案。
  "8610": 量化评估Transformer层自注意力与FFN的乘法计算量差异，指出线性注意力为解决低秩瓶颈需扩增维度导致的算力分界线。
  "8934": 将注意力与GLU融合为单头门控注意力单元（GAU），并基于分块混合注意力（MCA）得到首个具备并行解码特征的高能线性FLASH模型。
  "8990": 对初始阶段GAU的对角线概率分布和特征尺度进行统计力学均方估计，并揭示了Halving初始权重输出缩放128倍的Crazy Scaling机制。
  "8998": 极限探索NLU性能，提出去 Bias 和去 Gamma RMS Norm 的极简 RoFormerV2 结构，并提出动态残差缩放稳定 Post-Norm 的从零训练。
  "9009": 从残差级数展开阐明 Pre-Norm 深层迭代退化为“扁而宽”浅模型的物理原因，并对比分析了 Post-Norm 保证足秤表征深度的优势。
  "9105": 构造全同输入排序探针，揭示相对位置编码概率行和恒为1的拟合缺陷，并探究了 $l_2$ 归一化自注意力及 CLS 边界符的对策。
key_concepts:
  - [[concept:Attention Low Rank Bottleneck]]
  - [[concept:Talking-Heads Attention]]
  - [[concept:Google Synthesizer]]
  - [[concept:T-TA (Transformer-based Text Autoencoder)]]
  - [[concept:Gated Attention Unit]]
  - [[concept:Mixed Chunk Attention]]
  - [[concept:RoFormerV2]]
  - [[concept:Pre-Norm vs Post-Norm]]
  - [[concept:Relative Position Encoding Flaw]]
key_methods:
  - [[method:增大key_size解除注意力低秩瓶颈]]
  - [[method:Talking-Heads Attention 混合注意力分布]]
  - [[method:Synthesizer静态注意力生成]]
  - [[method:T-TA结构与共享键值防泄漏法]]
  - [[method:门控注意力与FFN的融合方法 (GAU)]]
  - [[method:分块混合注意力自注意力线性化 (MCA)]]
  - [[method:RoFormerV2 结构极简与有监督多任务预训练]]
  - [[method:动态残差缩放稳定收敛法]]
  - [[method:l2 注意力归一化方法]]
reading_paths:
  - [[Transformer架构与归一化阅读路径]]
status: draft
updated: 2026-06-14
---

# Transformer架构与归一化

## 系列核心问题
本系列围绕自注意力机制及其层归一化设计展开深度研究，解决以下核心问题：
1. **表达力瓶颈**：如何有效识别和克服多头投影中的低秩限制，以及如何设计静态与混合头机制？
2. **计算效率优化**：注意力的 FLOPs 到底在什么序列尺度主导？门控层（GAU）与 FFN 融合以及 MCA 分块线性化注意力（FLASH）如何实现高层吞吐与低显存？
3. **收敛与表达上限**：Pre-Norm 为什么在深层发生退化？Post-Norm 在从零训练时如何结合“动态残差缩放”稳定梯度？
4. **位置与排序拟合**：位置编码的演进关系如何？为什么概率注意力对全同输入存在表达退化的理论缺陷，如何解决？

## 概念递进关系
- 由 [[concept:Attention Low Rank Bottleneck]] 引出 $Q, K$ 维度的低维逼近缺陷，进而提出 [[concept:Talking-Heads Attention]] 的混合叠加，以及 [[concept:Google Synthesizer]] 的静态降维。
- 由 [[concept:T-TA (Transformer-based Text Autoencoder)]] 证明常数 K, V 共享设计的防泄漏功效，其被后续在 [[concept:Gated Attention Unit]] 与 [[concept:Mixed Chunk Attention]] 组成的线性高效 FLASH 模型中进一步继承和推广。
- 在讨论收敛时，通过 [[concept:Pre-Norm vs Post-Norm]] 论证了 Pre-LN 因特征累加导致有效深度虚无化（深度退化），迫使 [[concept:RoFormerV2]] 在坚持 Post-LN 基础上引入动态残差缩放以达成速度和极限性能的折衷。
- 从理论缺陷探讨中，定位了在经典 [[concept:Relative Positional Encoding]] 架构中概率注意力矩阵对全同输入的拟合死锁问题，即 [[concept:Relative Position Encoding Flaw]]，并利用 [[concept:l2 Attention Normalization]] 成功突破概率行和限制。
