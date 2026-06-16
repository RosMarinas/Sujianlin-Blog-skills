---
type: concept
title: NoPE
aliases:
- No Position Encoding
- 无位置编码
definition: 在Causal Attention（单向注意力）中不使用任何显式位置编码的方法，利用隐状态向量的方差/ℓ2范数隐式编码位置信息。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2024-09-01-Decoder-only的LLM为什么需要位置编码.md
source_ids:
- '10347'
prerequisites:
- '[[因果注意力]]'
- '[[位置编码]]'
equivalent_forms: []
related_formulas: []
related_methods:
- '[[positional-interpolation]]'
- '[[alibi]]'
series:
- '[[transformer-upgrade-path]]'
evidence_spans:
- ev::10347::单向注意
- ev::10347::方差辨位
- ev::10347::不足之处
status: draft
updated: '2026-06-12'
---

# NoPE

## Definition

NoPE (No Positional Encoding) 指在基于 Causal Attention（单向注意力）的模型中，不引入任何额外的显式位置编码的机制。

双向 Attention 具有置换不变性，所以需要位置编码来打破它。但 Causal Attention 的求和符号的上限从 $L$ 改为了 $n$，这类似于 $\text{cumsum}$，其结果依赖于 $\boldsymbol{x}_1,\boldsymbol{x}_2,\cdots,\boldsymbol{x}_L$ 的顺序。换句话说，它本身就不具有置换不变性。因此，“Causal + NoPE”的组合原则上不需要位置编码，也能取得非平凡的效果。

## 方差辨位与数学原理

“Causal + NoPE”实际上是将位置信息隐藏在了 $\boldsymbol{y}$ 的分量方差之中，或者等价地，隐藏在 $\boldsymbol{y}$ 的 $\mathcal{l}_2$ 范数中。

可以通过最简单的均匀分布情形来分析其内在机制，考虑如下的 Attention 矩阵：
$$
A = \begin{pmatrix}1 & \\
\frac{1}{2} & \frac{1}{2} & \\
\frac{1}{3} & \frac{1}{3} & \frac{1}{3} & \\
\vdots & \vdots & \vdots & \ddots \\
\frac{1}{n} & \frac{1}{n} & \cdots & \cdots & \frac{1}{n}\\
\vdots & \vdots & \vdots & \vdots & \vdots & \ddots \\
\end{pmatrix}
$$
在这个假设下，$\boldsymbol{y}_n$ 就是 $n$ 个 $\boldsymbol{v}$ 的平均：
$$
\boldsymbol{y}_n = \frac{1}{n}\sum_{m=1}^n \boldsymbol{v}_m
$$
假设每个 $\boldsymbol{v}$ 的每个分量，都是从同一个“均值为0、方差为 $\sigma^2$”的分布中独立重复采样出来的。在此假设之下，$\boldsymbol{y}_n$ 的均值和方差计算如下：
$$
\begin{aligned}
\frac{1}{d}\sum_{i=1}^d \boldsymbol{y}_{n,i} \approx&\, \mathbb{E}[\boldsymbol{y}_{n,i}] = \mathbb{E}\left[\frac{1}{n}\sum_{m=1}^n \boldsymbol{v}_{n,i}\right] = \frac{1}{n}\sum_{m=1}^n \mathbb{E}\left[\boldsymbol{v}_{n,i}\right] = 0 \\[5pt]
\frac{1}{d}\sum_{i=1}^d \boldsymbol{y}_{n,i}^2 \approx&\, \mathbb{E}[\boldsymbol{y}_{n,i}^2] = \mathbb{E}\left[\left(\frac{1}{n}\sum_{m=1}^n \boldsymbol{v}_{n,i}\right)^2\right] = \frac{1}{n^2}\sum_{m=1}^n \mathbb{E}\left[\boldsymbol{v}_{n,i}^2\right] = \frac{\sigma^2}{n} \\
\end{aligned}
$$
这表明，由于均值为零，各 $\boldsymbol{y}_n$ 的直观区别就是求平均的 $\boldsymbol{v}_m$ 的个数，而不同数量的平均导致的最直接的变化量就是方差。

## 关键性质与不足之处

尽管 NoPE 能够隐式捕捉位置信息，但本质上它相当于 $\boldsymbol{y}_n$ 由某个不带位置信息的向量 $\boldsymbol{z}_n$ 乘上某个跟位置 $n$ 相关的标量函数 $p(n)$ 得到。这导致了它在长文本任务中的固有缺陷：

1. **乘性绝对位置编码的弱表达性**：NoPE 实现的是类似于乘性的绝对位置编码，并且它只是将位置信息压缩到单个标量中，所以这是一种非常弱的位置编码。
2. **长序列的位置分辨率丧失**：单个标量能表示的信息有限。当输入长度增加时，位置编码会越来越紧凑以至于难以区分。例如在 $p(n)\sim \frac{1}{\sqrt{n}}$ 的情况下，当 $n$ 足够大时，$\frac{1}{\sqrt{n}}$ 与 $\frac{1}{\sqrt{n+1}}$ 几乎不可分辨，也就是没法区分位置 $n$ 与 $n+1$。
3. **缺乏自然语言优先级的先验**：主流观点认为相对位置编码更适合自然语言，NoPE 既没有给模型添加诸如远程衰减（即越远的Token平均而言越不重要）之类的先验，也没有赋予模型学习到这种先验的能力。当输入长度足够大可能就会出现注意力弥散/不集中的问题。

由于这些限制，尽管在 Multi-Head 和 Multi-Layer 的叠加下 NoPE 的总位置信息也是一个比较可观的大向量而不至于彻底失效，但主流的 Decoder-only 模型依然会显式加上额外的相对位置编码（如 RoPE、ALiBi 等），以解决长文本分辨率不足和效率较低的问题，从而让 LLM 本身更聚焦于整体的推理能力。
