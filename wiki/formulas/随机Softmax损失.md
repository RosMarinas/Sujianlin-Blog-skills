---
type: formula
title: 随机Softmax损失
aliases: []
latex: L = -\log \frac{e^{z_t}}{\sum_{i \in \mathcal{S}} e^{z_i}}
symbol_meanings:
  z_t: 目标类别标签的预测 logits
  \mathcal{S}: 由目标类别 t 与随机采样的 N_neg 个负样本组成的子集
  z_i: 子集 S 中各个样本的 logits
standard_notation: L
conditions: 通过随机负采样近似计算全局 Softmax 的交叉熵损失，使得每步更新的计算量与总类别数无关
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md
source_ids:
- '4402'
appears_in:
- '[[spaces-4402-不可思议的Word2Vec-5-Tensorflow版的Word2Vec]]'
evidence_spans:
- ev::4402::随机损失
status: draft
updated: '2026-06-14'
---

# 随机Softmax损失

## 概述

随机Softmax损失（Random Softmax Loss）是针对词向量模型（如Word2Vec的CBOW或Skip-Gram）中由于庞大词汇表导致全局Softmax计算量过大这一瓶颈，而提出的一种基于随机负采样的交叉熵近似损失函数。

在完整的Softmax层中，假设词汇量为 $n$，目标类别 $t$ 的交叉熵损失为 $L=-\log \frac{e^{z_t}}{Z}$，其中配分函数 $Z = \sum_{i=1}^n e^{z_i}$。对该损失求导可得其梯度：
$$ \nabla L = -\nabla z_t + \frac{\sum_i e^{z_i}\nabla z_i}{Z} = -\nabla z_t + \sum_i p_i \nabla z_i = -\nabla z_t + \text{E}(\nabla z_i) $$
这表明梯度更新由目标标签的梯度与所有标签梯度的期望均值这两部分“拉锯”组成。精确计算该期望需要遍历全词表，使得单步迭代的计算复杂度高达 $\mathcal{O}(n)$。

为了将每步更新的计算复杂度固定，避免其随标签数增加而快速膨胀，该方法直接在损失函数层面进行了近似：对于每个“样本-标签”对，从总体类别中随机选取一定数量（`nb_negative`）的负标签，并将其与正确的目标标签 $t$ 结合，构成一个大小为 `nb_negative + 1` 的局部类别子集 $\mathcal{S}$。随后，仅在这个小子集内计算局部的 Softmax 并求交叉熵损失。由于这种损失形式的巧妙设计，对其求导后得到的梯度，天然地等效于按照概率分布进行随机采样所估计出的梯度均值。

该损失形式与深度学习框架中常见的 `nce_loss` 及 `sampled_softmax_loss` 均有所不同。如果在计算时进一步令 Softmax 层与词向量层共享权重（即设置偏置 $b=0$），这种模型结构不仅等效于原有 Word2Vec 的负采样方案或 GloVe 的词共现矩阵分解，而且由于引入了交叉熵损失，理论上收敛速度更快；同时，相较于传统的负样本模型训练完毕后网络最终输出值缺乏明确意义的缺陷，通过随机Softmax损失训练得到的输出依然保留了严谨的概率预测意义。
