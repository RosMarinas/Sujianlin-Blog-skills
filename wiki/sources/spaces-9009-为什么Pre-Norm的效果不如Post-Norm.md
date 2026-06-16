---
type: article_summary
title: 为什么Pre-Norm的效果不如Post-Norm
article_id: "9009"
source_url: https://spaces.ac.cn/archives/9009
date: 2022-03-29
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2022-03-29-为什么Pre-Norm的效果不如Post-Norm.md
series: [Transformer架构与归一化]
topics: [归一化与稳定性]
concepts: [Pre-Norm, Post-Norm, 深度退化]
methods: [Pre-Norm / Post-Norm深度退化分析]
evidence_spans: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-29-为什么Pre-Norm的效果不如Post-Norm.md
source_ids:
  - "9009"
status: draft
updated: 2026-06-12
---

# 为什么Pre-Norm的效果不如Post-Norm

## 文章核心问题
虽然 Pre-Norm 相对 Post-Norm 更加容易训练且不依赖 Warmup 学习率调度，但在相同的模型规模和预训练设置下，为什么 Pre-Norm 预训练得到的模型在下游任务的微调/迁移（Finetuning）效果通常不如 Post-Norm？这种性能退化的底层物理机理是什么？

## 主要结论
- Pre-Norm 在深层迭代中，存在严重的“深度水分”（Effective Depth Degradation）。其等效深层特征近似于多个浅层特征乘以不同权重的宽扁网络之和，导致模型的实际表达能力更倾向于“宽模型”而非“深模型”。
- 深度比宽度在特征抽象上重要得多，因此 Pre-Norm 的有效深度退化导致其表征能力相比 Post-Norm 出现了实质性下降。
- Post-Norm 在每次残差求和后都进行了一次 Layer Normalization，不断消减恒等分支（Identity Branch）的模长权重，迫使模型更关注和突出残差分支，从而保证了每一层都有足够独立的深度表征能力（“足秤”深度）。
- 这一直观物理视角与 DeepNet 论文中的数学结论（Pre-LN 在底层的梯度较大，导致浅层主导、顶层退化）相互印证。

## 推导结构
1. **Pre-Norm 与 Post-Norm 公式形式**：
   - Pre-Norm: $\boldsymbol{x}_{t+1} = \boldsymbol{x}_t + F_t(Norm(\boldsymbol{x}_t))$
   - Post-Norm: $\boldsymbol{x}_{t+1} = Norm(\boldsymbol{x}_t + F_t(\boldsymbol{x}_t))$
2. **深度退化推导**：
   展开 Pre-Norm 递推式：$\boldsymbol{x}_{t+1} = \boldsymbol{x}_0 + F_0(Norm(\boldsymbol{x}_0)) + \dots + F_t(Norm(\boldsymbol{x}_t))$。
   每一项的量级都接近 $\mathcal{O}(1)$，累加后导致 $\boldsymbol{x}_t \approx \boldsymbol{x}_{t+1}$（随着层数 $t$ 变大，它们之间的相对差别仅为 $\mathcal{O}(1/(t+1))$，可以忽略不计）。
   因此，后继两层的输出非常接近：$F_{t+1}(Norm(\boldsymbol{x}_{t+1})) \approx F_{t+1}(Norm(\boldsymbol{x}_t))$。
   于是两层结果：$F_t(Norm(\boldsymbol{x}_t)) + F_{t+1}(Norm(\boldsymbol{x}_{t+1})) \approx (F_t + F_{t+1})(Norm(\boldsymbol{x}_t))$。
   这说明 Pre-Norm 中的多层堆叠在数学上等价于单层宽度的扩大，多出的层数只是摆设，无法真正表达更深层级的特征。
3. **解释 DeepNet 的梯度发现**：
   DeepNet 发现 Pre-LN 底层的梯度倾向于大于顶层，也就是模型能量和梯度信息被绝大部分底层占据，导致顶层无法发挥深度特征提取的作用，进而发生退化。

## 关键公式
- Pre-Norm 级数展开式: $\boldsymbol{x}_{t+1} = \boldsymbol{x}_0 + \sum_{i=0}^t F_i(Norm(\boldsymbol{x}_i))$
- 两层等效化简: $F_t(Norm(\boldsymbol{x}_t)) + F_{t+1}(Norm(\boldsymbol{x}_{t+1})) \approx \begin{pmatrix} 1 & 1 \end{pmatrix} \begin{pmatrix} F_t \\ F_{t+1} \end{pmatrix} (Norm(\boldsymbol{x}_t))$

## 体现的方法
- Pre-Norm / Post-Norm 深度退化分析

## 所属系列位置
Transformer架构与归一化系列第9篇，旨在理清预训练模型在归一化（Normalization）上设计选择的内在表征上限对比。

## 与其他文章的关系
本篇揭示的 Pre-Norm 深度虚增缺陷，是第7篇 GAU 能够避免 Warmup 的逆向物理应用。同时它说明了 Post-Norm 的重要性，进而促使了第8篇 RoFormerV2 坚持使用 Post-Norm 并在训练收敛上通过引入“动态残差缩放”来破局，也为后续更稳定的层归一化方法奠定了理论指引。

## 原文证据锚点
- Pre-Norm 递推展开： 见“直观理解”章节中的代数展开。
- 等效多层合一宽模型公式： 见 $F_t + F_{t+1}$ 的矩阵化简公式。
- DeepNet 梯度陈述： 引用 DeepNet 关于 Pre-LN 梯度分布规律的判定。
