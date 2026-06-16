---

type: method
operation_types:
  primary: Construct auxiliary sequence
  secondary: []
title: 虚拟对抗训练VAT
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-06-08-互怼的艺术-从零直达WGAN-GP.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-08-26-fashion-mnist的gan玩具.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-07-深度学习中的Lipschitz约束-泛化与生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-10-22-RSGAN-对抗模型中的-图灵测试-思想.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-07-WGAN-div-一个默默无闻的WGAN填坑者.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-11-20-不用L约束又不会梯度消失的GAN-了解一下.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-12-10-BiGAN-QP-简单清晰的编码-生成模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-01-泛化性乱弹-从随机噪声-梯度惩罚到虚拟对抗训练.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-15-WGAN新方案-通过梯度归一化来实现L约束.md
source_ids:
  - 7466
method_summary: 通过幂迭代构造使l(f(x+epsilon), f(x))最大的噪声，实现无监督的对抗训练
typical_structure: |
  1. 抽取无标签样本 x，随机初始化一个高斯噪声向量 u。
  2. 迭代计算当前模型预测输出的最敏感方向 u \gets \nabla_u D_{KL}(p_\theta(y|x) \| p_\theta(y|x+u))。
  3. 将求得的 u 归一化并放大到 \epsilon 强度作为对抗微扰。
  4. 约束模型在 x+u 和 x 的输出保持一致，执行训练。
applicability: 半监督学习、需要无标签信号的泛化性提升
evidence_spans:
  - ev::7466::文章中指出，通过幂迭代构造使 l(f(x+\epsilon), f(x)) 最大的噪声以进行对抗训练，即可实现无需真实标签的虚拟对抗训练（VAT）。
examples:
  - [[article::7466]]
status: stable
updated: 2026-06-13
cross_series_match: null
cross_series_match_reason: VAT是半监督学习的专用方法，使用幂迭代构造对抗噪声，与普通对抗训练（监督）共享construct_auxiliary_sequence类型。
---





## 适用问题

半监督学习、需要无标签信号的泛化性提升。

## 核心变换

通过幂迭代（Power Iteration）近似构造出使模型预测输出散度变化最大（最敏感）的局部扰动噪声，并将其作为正则化项引入对抗训练中。

## 典型步骤

1. 抽取无标签样本 $x$，随机初始化一个高斯噪声向量 $u$。
2. 在输入 $x$ 周围寻找使当前模型预测概率分布 $p_\theta(y|x)$ 和 $p_\theta(y|x+r)$ 之间 KL 散度最大的对抗方向 $r$，通常利用幂迭代法近似计算：$r \gets \nabla_r D_{KL}(p_\theta(y|x) \| p_\theta(y|x+r))$。
3. 将求得的对抗扰动归一化后叠加到 $x$ 上，得到对抗样本 $x_{adv} = x + \epsilon \cdot r_{norm}$。
4. 计算该对抗样本的损失项 $D_{KL}(p_\theta(y|x) \| p_\theta(y|x_{adv}))$ 并加入总损失中，促使模型输出在局部对抗扰动下保持一致（平滑）。

## 直觉

我们希望模型不要死记硬背，而是有很好的泛化性（在输入稍微改变时，输出不要剧变）。传统的对抗训练是有标签的，而 VAT 则是在“无标签”的情况下：它不关心 $x$ 的真实标签是什么，只关心模型“现在认为 $x$ 是什么”。VAT 会寻找那个最能改变模型现有看法的微小扰动方向，然后强迫模型在加上这个扰动后，看法依然保持不变。

## 边界

需要两次前向/反向传播来计算对抗方向，增加了训练时间（通常增加一倍）；如果数据流形极其复杂，局部的平滑性假设可能限制模型的拟合能力。

## 例子

在文本分类的半监督任务中，将词嵌入视为连续输入，通过 VAT 找到使当前分类器最容易改变分类结果的词向量微扰，并加入一致性损失，从而大幅提升未标注数据的利用率。

## 证据

- ev::7466::文章中指出，通过幂迭代构造使 $l(f(x+\epsilon), f(x))$ 最大的噪声以进行对抗训练，即可实现无需真实标签的虚拟对抗训练（VAT）。