---

type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: Gumbel Softmax离散重参数
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-06-10-漫谈重参数-从正态分布到Gumbel-Softmax.md
source_ids:
  - 6705
method_summary: 通过Gumbel Max + Softmax退火为离散分布提供可微的重参数采样：softmax((log p_i - log(-log epsilon_i))/tau)
typical_structure: |
  1. 计算各类别的 Logits $o_i$。
  2. 采样均匀分布并计算 Gumbel 噪声 $g_i = -\log(-\log \varepsilon_i)$。
  3. Logits 结合噪声并通过带温度的 Softmax：$\text{softmax}((o_i + g_i)/\tau)$。
  4. 随训练进行，将温度 $\tau$ 逐步退火衰减至接近 0。
applicability: 深度学习模型中间存在离散变量且需从其分布中采样（如 VAE的离散隐变量、文本GAN的词采样）并进行端到端可导优化的场景。
examples:
  - 文本GAN生成器中使用 Gumbel-Softmax 输出可导的近似词向量，使判别器可以无缝将梯度反传至生成器。
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::6705::原文"总结"节论述Gumbel Softmax源于对Gumbel Max的光滑化，并对比说明相对REINFORCE能显著降低梯度方差。
---





## 适用问题
在深度学习中，当神经网络的某一中间层是离散的类别分布，且我们需要从该分布中采样进行下一步前向计算时，由于 `argmax` 算子或离散采样过程本身不可导，反向传播的梯度无法穿透离散采样层。如果使用 REINFORCE (SF估计) 等方法直接计算期望梯度，方差非常大导致训练极不稳定。为了通过标准梯度下降联合端到端训练离散概率模型，需要使得离散采样可微。

## 核心变换
将标准的分类离散采样重构为 Gumbel-Max 操作：$\boldsymbol{z} = \text{one\_hot}(\text{argmax}_i (\log p_i + g_i))$，其中 $g_i$ 是独立同分布的 Gumbel 噪声 $g_i = -\log(-\log \varepsilon_i)$，$\varepsilon_i \sim U[0,1]$。然后用带温度参数 $\tau$ 的 Softmax 函数光滑化替换不可导的 `argmax` 算子，实现从均匀分布产生随机性并通过连续变换生成近似 one-hot 向量的 Gumbel-Softmax 重参数化。

## 典型步骤
1. 根据网络的前一输出计算各个离散类别的对数概率（Logits），记作 $o_i = \log p_i$。
2. 从均匀分布 $U(0, 1)$ 中独立采样 $\varepsilon_i$。
3. 对每个类别的 $\varepsilon_i$ 进行变换，构造 Gumbel 噪声：$g_i = -\log(-\log \varepsilon_i)$。
4. 将 Logits 和 Gumbel 噪声相加。
5. 施加带温度 $\tau$ 的 Softmax 函数进行可微近似：$y_i = \frac{\exp((o_i + g_i)/\tau)}{\sum_j \exp((o_j + g_j)/\tau)}$。
6. 将连续的 $\boldsymbol{y}$ 作为近似离散采样结果代入后续网络，并将 $\tau$ 在训练周期内由大逐步衰减（退火）逼近至 0。

## 直觉
普通的分类离散采样等价于给对数概率随机注入 Gumbel 噪声后求 `argmax`。但 `argmax` 输出的是不可导的尖锐突变信号。引入带有温度 $\tau$ 的 `softmax`，其本质是在“确定的平滑混合”和“绝对的唯一离散决策”之间搭起一座连续可调的桥梁。当 $\tau$ 较大时，梯度像流水一样顺畅反传；随着训练推进逐渐降低 $\tau$ ，桥梁向着坚硬的 `argmax` 阶梯收缩，最终让网络渐渐习惯近似绝对离散下的梯度方向。相比 REINFORCE 依赖大波动的“奖励信号”，Gumbel-Softmax 转换为确定性网络解析传导，极大减小了随机性带来的波动。

## 边界
- 这种近似始终存在偏差-方差权衡（Bias-Variance Trade-off），$\tau$ 越大偏置（Bias）越高，生成的向量越偏离真实的 One-hot 限制；$\tau$ 趋向 0 则变成真实 `argmax`，梯度消失。
- 通常需要精细调整 $\tau$ 的退火策略（Annealing Schedule）。
- 直通估计器（Straight-Through Estimator, ST）变体虽然前向保证离散，但造成梯度错配。

## 例子
在文本 GAN 中生成离散文本：基于 RelGAN 等模型，生成器在每一步输出词表大小的 Logits。通过在 Logits 上加入 Gumbel 噪声并调用 Gumbel-Softmax($\tau$)，把输出变成词表维度上的平滑概率向量（对应词嵌入组合）。由于该过程连续可导，随后的判别器可直接将交叉熵算出的 Loss 梯度一路传回生成器。

## 证据
- 原文 6705 "总结" 节提及："理论上来说，离散情形的...不一定需要重参数。但事实上，'有限'也可能是相当大的数字，因此遍历求和可能难以进行，所以还是要转化为采样形式，从而需要重参数技巧，这就是 Gumbel Softmax，源于对 Gumbel Max 的光滑化。"