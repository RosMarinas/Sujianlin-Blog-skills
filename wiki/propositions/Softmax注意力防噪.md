---
type: proposition
title: Softmax注意力防噪
aliases:
  - Noise Robustness of Softmax Attention
statement: |
  基于Softmax归一化的注意力机制对于输入logits得分中加入的独立同分布噪声具有天然的抵抗力，即加入噪声后的注意力输出近似等于原输出。
assumptions:
  - 噪声与输入的得分及特征向量相互独立
  - 噪声在各个位置上是独立同分布的
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-04-25-注意力和Softmax的两点有趣发现-鲁棒性和信息量.md
source_ids:
  - 9593
proof_route:
  - 写出加噪声后的注意力输出公式：$\tilde{o} = \frac{\sum e^{s_i + \varepsilon_i} v_i}{\sum e^{s_i + \varepsilon_i}}$
  - 将分子分母同时除以序列长度 $n$，重写为数学期望的形式：$\tilde{o} = \frac{\mathbb{E}_i[e^{s_i+\varepsilon_i}v_i]}{\mathbb{E}_i[e^{s_i+\varepsilon_i}]}$
  - 由于噪声 $\varepsilon_i$ 独立于 $s_i$ 和 $v_i$，利用独立随机变量积的期望等于期望的积的性质：$\mathbb{E}_i[e^{s_i+\varepsilon_i}v_i] = \mathbb{E}_i[e^{s_i}v_i]\mathbb{E}[e^{\varepsilon}]$ 且分母同理。
  - 将期望乘积代回，在分子和分母中约去相同的噪声项期望 $\mathbb{E}[e^{\varepsilon}]$。
  - 化简结果为：$\tilde{o} \approx \frac{\mathbb{E}_i[e^{s_i}v_i]}{\mathbb{E}_i[e^{s_i}]} = o$，即噪声在归一化过程中被自动消除。
null_evidence_reason: |
  Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# Softmax注意力防噪

## Statement
基于Softmax归一化的注意力机制对于输入logits得分中加入的独立同分布噪声具有天然的抵抗力，即加入噪声后的注意力输出近似等于原输出。

## Assumptions
- 噪声与输入的得分及特征向量相互独立
- 噪声在各个位置上是独立同分布的

## Proof Route
1. 写出加噪声后的注意力输出公式：$\tilde{o} = \frac{\sum e^{s_i + \varepsilon_i} v_i}{\sum e^{s_i + \varepsilon_i}}$
2. 将分子分母同时除以序列长度 $n$，重写为数学期望的形式：$\tilde{o} = \frac{\mathbb{E}_i[e^{s_i+\varepsilon_i}v_i]}{\mathbb{E}_i[e^{s_i+\varepsilon_i}]}$
3. 由于噪声 $\varepsilon_i$ 独立于 $s_i$ 和 $v_i$，利用独立随机变量积的期望等于期望的积的性质：$\mathbb{E}_i[e^{s_i+\varepsilon_i}v_i] = \mathbb{E}_i[e^{s_i}v_i]\mathbb{E}[e^{\varepsilon}]$ 且分母同理。
4. 将期望乘积代回，在分子和分母中约去相同的噪声项期望 $\mathbb{E}[e^{\varepsilon}]$。
5. 化简结果为：$\tilde{o} \approx \frac{\mathbb{E}_i[e^{s_i}v_i]}{\mathbb{E}_i[e^{s_i}]} = o$，即噪声在归一化过程中被自动消除。