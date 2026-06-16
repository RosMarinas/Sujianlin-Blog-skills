---
type: formula
title: Attention-E熵不变性缩放公式
aliases:
- Entropy-invariant attention scale
source_ids:
- '8823'
- '9019'
- '9052'
evidence_spans:
- ev::8823::熵不变性缩放
- ev::9019::Softmax熵版本
- ev::9052::GAU归一化
standard_notation:
  Q: query matrix
  K: key matrix
  V: value matrix
  n: sequence length
  d: attention head dimension
status: draft
updated: "2026-06-14"
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-04-07-听说Attention与Softmax更配哦.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-04-22-GAU-α-尝鲜体验快好省的下一代Attention.md
latex: Attention(Q,K,V)=softmax\left(\frac{\log_{512}n}{\sqrt d}QK^\top\right)V.
symbol_meanings:
  K: key matrix
  Q: query matrix
  V: value matrix
  d: attention head dimension
  n: sequence length
conditions: （待从源文章提取）
appears_in:
- '8823'
- '9019'
- '9052'
---

# Attention-E熵不变性缩放公式

## 概述

$$Attention(Q,K,V)=softmax\left(\frac{\log_{512}n}{\sqrt d}QK^\top\right)V.$$

## 核心动机与熵不变性

在标准的Scaled Dot-Product Attention（即Attention-O）中，缩放因子固定为$1/\sqrt{d}$。然而，为了使Transformer模型在预测长度与训练长度不一致时具备更强的外推能力（例如在$n=64$上训练并外推到$n=128, 256$进行测试），注意力机制的设计应该使得其归一化后的分布 $a_{i,j}$ 尽量具备**熵不变性**。

注意力分布可以视为以位置$i$为条件、$j$为随机变量的条件分布，其条件熵表示为：
$$\mathcal{H}_i = -\sum_{j=1}^n a_{i,j}\log a_{i,j}$$

“熵不变性”意味着 $\mathcal{H}_i$ 应当对序列长度$n$的变化不敏感。如果在已有token的基础上补充新的token，原有的熵不应出现大幅改变。这是因为熵代表了注意力的“聚焦程度”（熵为0表示完全聚焦于某一个token，熵为$\log n$表示均匀分布）。如果模型不具备熵不变性，引入的新token会过度“分摊”原有的注意力权重，从而导致累加求和的结果发生显著偏移，破坏长度泛化能力。

## 缩放因子的数学推导

基于熵不变性，理论上可以推导出一个包含新超参数 $\kappa$ 的注意力缩放公式：
$$Attention(Q,K,V) = softmax\left(\frac{\kappa \log n}{d}QK^{\top}\right)V$$
其中 $\kappa$ 是与 $n, d$ 无关的超参数。

为了消除引入新超参数对现有预训练模型生态的影响，可以利用当前主流预训练配置进行边界条件约束：当前多数模型的默认预训练长度为 $n=512$，所以假设模型参数是在 $n=512$ 的标准缩放机制下调优的。令 $n=512$ 时上式严格退化为普通Scaled Dot-Product Attention：
$$\frac{\kappa \log 512}{d}=\frac{1}{\sqrt{d}}$$
由此解得 $\kappa = \frac{\sqrt{d}}{\log 512}$。将该 $\kappa$ 代入回原式，即可得到无新增超参数的最终公式：
$$Attention(Q,K,V) = softmax\left(\frac{\log_{512} n}{\sqrt{d}}QK^{\top}\right)V$$

## 实验验证与GAU-α应用

1. **长度外推优势**：
在基于RoFormer small版本（MLM任务）的控制变量实验中，模型统一在长度 $n=64$ 下进行训练。当测试长度外推至 $n=256$ 时，标准的Attention-O准确率急剧下降至 `23.02%`，而采用熵不变性缩放的Attention-E则维持在 `34.04%`，绝对准确率提升超过10个百分点，证实了该公式在处理未知长度时的优越泛化性。

2. **GAU中的归一化回退**：
在门控注意力单元（GAU）的初始设计中，为了极致的计算效率采用了单头注意力配合 $\frac{1}{n}\text{relu}^2(\cdot)$ 进行归一化。然而，后续研究表明，由于自适应序列长度 $n$ 不满足注意力权重的局部稀疏特性（实际的归一化配分函数 $Z_i$ 的增长阶数远低于 $\mathcal{O}(n)$），导致长度泛化能力大幅衰减。
为此，在升级版的开源变体 **GAU-α** 中，注意力机制被重置回Softmax，并且专门配备了此“熵不变性Softmax”（在bert4keras实现中被称为 `softmax_plus`）。这一结合不仅保留了GAU快、省的结构优势，还在多项CLUE基准任务及长序列测试中超越了原有基线，取得了更好的自适应外推表现。
