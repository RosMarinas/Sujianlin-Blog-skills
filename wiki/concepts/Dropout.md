---
type: concept
title: Dropout
definition: "一种防止神经网络过拟合的正则化技术，在训练过程中以特定概率随机将网络中部分神经元的输出置为零。"
sources:
  - wiki/sources/spaces-4521-谈谈dropout.md
  - wiki/sources/spaces-8770-Dropout视角MLM-MAE.md
source_ids:
  - "4521"
  - "8770"
aliases: [随机失活, 随机丢弃]
tags: [regularization, deep-learning, training-technique]
related_methods: [R-Drop, DropToken]
related_sources: [spaces-4521-谈谈dropout, spaces-8770-Dropout视角下的MLM和MAE]
status: draft
updated: 2026-06-12
---
## Definition

Dropout是一种防止过拟合的正则化技术。对于输入张量 $\boldsymbol{x}$，Dropout将部分元素以概率 $1-p$ 置零，然后将剩余元素放大 $1/p$ 倍。数学上，引入随机变量 $\varepsilon \sim \text{Bernoulli}(p)$，使模型从 $f(\boldsymbol{x})$ 变为 $f(\boldsymbol{x}\varepsilon/p)$。

## Training-Prediction Inconsistency

训练阶段：模型优化目标为 $\mathbb{E}_{(x,y)\sim\mathcal{D}}\mathbb{E}_{\varepsilon}[l(y, f_{\theta}(x,\varepsilon/p))]$。

预测阶段：通常关闭Dropout（权重平均 $f_{\theta}(x)$），而非理论最优的模型平均 $\mathbb{E}_{\varepsilon}[f_{\theta}(x,\varepsilon/p)]$。这导致了训练-预测不一致。

## Noise Shape

Dropout支持 `noise_shape` 参数控制丢弃模式。对于 $\text{shape}=(d_1,d_2,d_3)$，`noise_shape` 中值为1的轴会被一致地Dropout（同一batch/sentence/channel共享丢弃模式）。例如 `(batch, seq_len, 1)` 实现词级别Dropout。

## Generalizations

Dropout的思想被推广到多种变体：
- **R-Drop**：对同一输入做两次Dropout得到两个不同输出，通过KL散度约束输出一致性
- **DropToken**：随机丢弃Token位置，保留剩余Token原始位置，类似MAE的简化版本
- **Attention Dropout**：在Attention矩阵上施加Dropout

## References

- 苏剑林. "【备忘】谈谈dropout". 科学空间, 2017. [spaces-4521]
- 苏剑林. "Dropout视角下的MLM和MAE：一些新的启发". 科学空间, 2021. [spaces-8770]
