---
type: concept
definition: GAU（Gated Attention Unit）将门控结构与Attention结合，GAU-alpha进一步用熵不变性Softmax归一化提升长序列迁移表现。
title: GAU
aliases:
- Gated Attention Unit
- GAU-alpha
source_ids:
- '9019'
- '9052'
evidence_spans:
- ev::9019::Softmax归一化
- ev::9052::GAU替换
- ev::9052::GAU归一化
status: draft
updated: '2026-06-12'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-04-07-听说Attention与Softmax更配哦.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-04-22-GAU-α-尝鲜体验快好省的下一代Attention.md
---

# GAU

## 定义与核心数学形式

GAU（Gated Attention Unit，门控注意力单元或门控线性单元）是一种融合了GLU和Attention的新设计，被誉为“目前最有潜力的下一代Attention设计”，因为它真正达到了“更快（速度）、更好（效果）、更省（显存）”的特点。

GAU的整体运算可以简写成：
$$
\boldsymbol{O}=(\boldsymbol{U}\odot\boldsymbol{A}\boldsymbol{V})\boldsymbol{W}_o
$$
其中$\boldsymbol{U},\boldsymbol{V},\boldsymbol{W}_o$都是token-wise的，也就是说它们根本不会受到长度变化的影响。

在原始设计中，GAU显示了注意力未必需要Softmax归一化，可以换成简单的$\text{relu}^2$除以序列长度：
$$
\boldsymbol{A}=\frac{1}{n}\text{relu}^2\left(\frac{\mathcal{Q}(\boldsymbol{Z})\mathcal{K}(\boldsymbol{Z})^{\top}}{\sqrt{s}}\right)=\frac{1}{ns}\text{relu}^2\left(\mathcal{Q}(\boldsymbol{Z})\mathcal{K}(\boldsymbol{Z})^{\top}\right)
$$

## 关键属性与边界情况

除了效果，GAU在设计上给我们带来的冲击主要有两点：一是它显示了单头注意力未必就逊色于多头注意力，这奠定了它“快”、“省”的地位；二是它是显示了注意力未必需要Softmax归一化。

然而，原始GAU的$\frac{1}{n}\text{relu}^2(\cdot)$在样本长度方面的迁移能力并不如想象中好。通过分析发现，存在某个常数$k$，使得超出一定距离后Attention接近于0，归一化因子$Z_i$应该更接近$\mathcal{O}(k)$而不是$\mathcal{O}(n)$。Attention的归一化因子应该是接近常数量级的，所以GAU用$n$或者$n^2$做归一化因子会表现不佳。将GAU中Attention的归一化方式换回Softmax后重新训练一个GAU模型，然后微调测试不同长度的任务，发现其效果比$\frac{1}{n}\text{relu}^2(\cdot)$时明显要好。结论是：Attention还是与Softmax更配。

## 衍生变体：GAU-α与熵不变性

GAU-α是对GAU的一种改进与应用实践。在模型架构上，GAU-α就是将RoFormerV2的Attention+FFN换成了两层GAU（因为两层GAU的计算量和参数量大致相当于Attention+FFN组合）。RoFormerV2的特点是保留了Post Norm结构，去掉了所有的Bias项，并且Layer Norm换成了RMS Norm的最简单变体，在GAU-α中也是如此。

在归一化方面，为了解决长度外推能力，GAU-α的Attention归一化选取了具有较好外推能力的“熵不变性Softmax”：
$$
Attention(Q,K,V) = softmax\left(\frac{\log_{512} n}{\sqrt{d}}QK^{\top}\right)V
$$
通过“熵不变性”的拓展，可以进一步增强模型在超出训练长度外的效果。而$\text{relu}^2(\cdot)$由于具备正齐次性，归一化后参数会被抵消，无法像指数函数那样推导出一个“熵不变性”的版本。
