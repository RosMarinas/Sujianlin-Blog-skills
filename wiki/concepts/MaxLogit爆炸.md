---
type: concept
title: MaxLogit爆炸
aliases:
- MaxLogit Explosion
definition: 多头注意力层中 Softmax 前的注意力 Logits 矩阵最大绝对值随训练推进呈现线性或超线性无边界增长，引发梯度尖峰或训练崩溃的异常现象。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2025-07-12-QK-Clip-让Muon在Scaleup之路上更进一步.md
source_ids:
- 11126
status: draft
updated: '2026-06-12'
---

## 核心定义

回顾Attention的定义：
$$
\boldsymbol{O} = softmax(\boldsymbol{Q}\boldsymbol{K}^{\top})\boldsymbol{V}
$$
“MaxLogit爆炸”中的Logit，指的是Softmax前的Attention矩阵，即$\boldsymbol{Q}\boldsymbol{K}^{\top}$，而MaxLogit指的是全体Logit的最大值，我们将它记为：
$$
S_{\max} = \max_{i,j}\, \boldsymbol{q}_i\cdot \boldsymbol{k}_j
$$
这里的$\max$其实还要在batch_size维度上取，最终得到一个标量。MaxLogit爆炸是指，$S_{\max}$随着训练的推进一直往上涨，增长速度是线性甚至是超线性的，并且在相当长的时间内没有稳定的迹象。

## 理论主因与数学性质

MaxLogit本质上是一个异常值指标，它的爆炸意味着异常值超出了可控范围。具体来说，我们有：
$$
|\boldsymbol{q}_i\cdot \boldsymbol{k}_j| \leq \Vert\boldsymbol{q}_i\Vert \Vert\boldsymbol{k}_j\Vert = \Vert\boldsymbol{x}_i\boldsymbol{W}_q\Vert \Vert\boldsymbol{x}_j\boldsymbol{W}_k\Vert \leq \Vert\boldsymbol{x}_i\Vert \Vert\boldsymbol{x}_j\Vert \Vert\boldsymbol{W}_q\Vert \Vert\boldsymbol{W}_k\Vert
$$
由于$\boldsymbol{x}$通常会加RMSNorm，所以一般情况下$\Vert\boldsymbol{x}_i\Vert \Vert\boldsymbol{x}_j\Vert$是不会爆炸的，因此MaxLogit爆炸意味着谱范数$\Vert\boldsymbol{W}_q\Vert,\Vert\boldsymbol{W}_k\Vert$有往无穷大发展的风险。由于再大的数值经过Softmax后都变得小于1，所以比较幸运的情况下，这个现象不会带来太严重的后果，顶多是浪费了一个Attention Head，但比较糟糕的情况下，可能会引起Grad Spike甚至训练崩溃。因此，保险起见应当尽量避免MaxLogit爆炸的出现。

Attention Logit的特殊之处在于，它是双线性形式$\boldsymbol{q}_i\cdot \boldsymbol{k}_j = (\boldsymbol{x}_i \boldsymbol{W}_q)\cdot(\boldsymbol{x}_j \boldsymbol{W}_k)$，$\boldsymbol{W}_q,\boldsymbol{W}_k$的连乘使得爆炸的风险更大，还容易导致“糟的更糟”的恶性循环，最终促成了MaxLogit爆炸。

### 模型尺度与优化器影响

MaxLogit爆炸更多出现在非常大参数量的模型中，模型越大，训练的不稳定因素越多，Weight Decay越难稳定训练。

在优化器选择上，Muon普遍比Adam更容易引发MaxLogit爆炸。Muon给出的更新量是经过$\mathop{\text{msign}}$运算的，所有奇异值都相等，即它的有效秩是满秩；而一般情况下的矩阵，奇异值通常都是有大有小，并且以前面几个奇异值为主，从有效秩的角度看它们是低秩的，我们对Adam更新量的假设也是如此。由于Muon的更新量是满秩的，所以它与参数矩阵的“碰撞几率”会远大于Adam的，所以Muon更容易增大参数的奇异值（即增加谱范数爆炸的风险）。不过，即便是Adam训练的大模型（如DeepSeek-V3和Gemma2），同样也存在MaxLogit爆炸现象。

## 关联概念与应对策略

业界在抑制MaxLogit爆炸方面有多种尝试与相关机制：

1. **Weight Decay**：能一定程度上预防MaxLogit爆炸。对于几十B规模的小模型（如16B的Moonlight），MaxLogit最多涨到一定数值（如120）后就自动降下来了。但在千亿参数以上模型中，单纯依靠增大Weight Decay会带来明显的效果损失。
2. **Softcap**：由Gemma2引入，$\text{softcap}(x;\tau) = \tau\tanh(x/\tau)$。由于$\tanh$的有界性，$\text{softcap}$自然是能够保证$\text{softcap}$后的Logit有界的，但无法保证$\text{softcap}$前的Logit是有界的，因此只是将一个问题转化为另一个问题，实际上并没有解决本质问题。
3. **QK-Norm**：即对 $\boldsymbol{Q}$ 和 $\boldsymbol{K}$ 进行 RMSNorm，由Gemma3引入。QK-Norm确实是压制MaxLogit非常有效的方法，但它只适用于MHA、GQA等，不适用于MLA。因为MLA在Decoding阶段没法完全Materialize训练阶段的$\boldsymbol{K}$，从而无法做QK-Norm。
4. **QK-Clip**：一种直接对$\boldsymbol{W}_q,\boldsymbol{W}_k$进行事后缩放的新策略。MaxLogit本身就是触发缩放的最直接信号。当MaxLogit超过期望阈值$\tau$时，根据 $S_{\max}$ 与阈值 $\tau$ 的比例来对 $\boldsymbol{Q},\boldsymbol{K}$ 的权重进行裁剪。因为它是直接对权重进行修改的方法，所以它兼容性比QK-Norm更好，可以完美用于MLA结构。

### 关键实施细节（QK-Clip 的过度裁剪与 Per-Head 机制）
如果所有Head按同一个比例来Clip，那么没有爆炸趋势的大部份Head都会被“无辜受累”（由于长期无端被乘一个小于1的数趋于零），产生“过度裁剪”。为了避免“殃及池鱼”，必须 **Per-Head地进行监控MaxLogit和QK-Clip**。

### 具体案例
在万亿参数模型 Kimi K2 的训练中，设置QK-Clip的阈值$\tau$为100。从大致7k steps开始出现MaxLogit超过$\tau$的Head，随后在相当长的时间内Muon与QK-Clip处于拉锯战。有趣的是，70k steps之后，所有Head的MaxLogit都主动降低到了100以下，QK-Clip不再生效。这表明，在Weight Decay的作用下，只要能稳住训练，模型最后很可能都会主动将MaxLogit降下来，QK-Clip的作用正是帮助模型更平稳地度过训练初期。
