---
type: concept
title: Copy机制
aliases:
- Copy Mechanism
- Pointer Network
- BIO Copy
definition: 在Seq2Seq生成中允许模型直接从输入文本复制token或连续片段的机制。通过增加额外的序列预测任务（如BIO标签），结合Mask解码策略强制复制连续片段，从而极大提高生成文本的忠实度并避免专业性错误。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-01-01-SPACES-抽取-生成-式长文本摘要-法研杯总结.md
source_ids:
- '8046'
related_methods:
- - - method::BIO Copy机制
status: draft
updated: '2026-06-12'
---

# Copy机制

在文本生成模型中，传统的Copy机制（如常规的 Pointer Networks）通常有两个不足之处：一是每次只能 Copy 一个 token，不能保证 Copy 一个连续片段（n-gram）出来；二是实现起来比较复杂，不够即插即用。为了解决这一问题并保证摘要与原始文本的忠实程度，避免出现专业性错误，苏剑林等人在 SPACES 模型中提出了一种新型的连续片段复制机制，称为 **BIO Copy**。

## 数学定义与核心原理

BIO Copy 机制实现起来非常简单，且具有 Copy 连续片段的能力。它其实就是在 Decoder 部分多加一个序列预测任务，即原来 Decoder 建模的是每个 Token 的分布 $p(y_t|y_{< t}, x)$，现在多预测一个标签分布，变为：
$$
p(y_t, z_t|y_{< t}, x) = p(y_t|y_{< t}, x) p(z_t|y_{< t}, x)
$$
其中 $z_t\in\{\text{B},\text{I},\text{O}\}$，其具体含义如下：
*   **B**：表示该token复制而来；
*   **I**：表示该token复制而来且跟前面Token组成连续片段；
*   **O**：表示该token不是复制而来的。

## 训练与标签构建

在训练阶段，$z$ 标签的获取采用了一种直接且简单的方法：算摘要与原文的“最长公共子序列”。只要是出现在最长公共子序列的 token，都算是 Copy 过来的，并根据 BIO 的具体含义设置不同的标签。整个过程仅增加了一个已知标签的序列预测任务，实现容易且几乎不增加计算成本。

**官方具体示例：**
例如，“我 真的 非常 热爱 我 的 祖国”与“我 爱 我 的 祖国”的最长公共子序列为“我 我 的 祖国”。
其中第一个“我”是单字，标签为 **B**；后面“我 的 祖国”是一个连续片段，标签为“**B I I**”，其他非公共部分的标签为 **O**。所以总的标签分布为“**B O B I I**”。

## 解码与强制复制（Masking策略）

解码的时候模型依然是一步步解码，并不是一次性生成一个片段，但可以通过 mask 的方式，保证 BI 部分位置对应的 token 是原文中的一个真实片段。预测阶段的具体步骤如下：
1. 对于每一步，首先预测标签 $z_t$。
2. 如果 $z_t$ 是 **O**，那么 token 分布不用改变。
3. 如果 $z_t$ 是 **B**，那么在 token 的分布中 mask 掉所有不在原文中的 token。
4. 如果 $z_t$ 是 **I**，那么在 token 的分布中 mask 掉所有不能组成原文中对应的 n-gram 的 token。

## 关键性质与工程经验

*   **提升忠实度（Fidelity）**：单纯引入 Copy 机制未必能大幅度提高传统评测分数（如 Rouge 可能仅提升 0.5% 左右），但是 Copy 机制可以强有力地保证摘要与原始文本的忠实程度，避免出现不可接受的专业性错误，这在实际使用（如司法裁判文书摘要）中是相当必要的。
*   **Encoder-Decoder 同步性增强**：虽然理论上只需要在 Decoder 处新增一个 BIO 预测，但在实际训练时，“同时在 Encoder 和 Decoder 处都加了，我们发现这样能提升模型的最终效果”。这种做法增强了 Encoder 和 Decoder 之间的同步性，能够引导 Decoder 更精准地 Attention 到 Encoder 的合理位置。
