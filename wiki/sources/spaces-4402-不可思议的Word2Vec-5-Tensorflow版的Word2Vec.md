---
type: article_summary
title: 【不可思议的Word2Vec】5. Tensorflow版的Word2Vec
article_id: "4402"
source_url: https://spaces.ac.cn/archives/4402
date: 2017-05-27
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md
series:
  - [[不可思议的Word2Vec]]
concepts:
  - [[Word2Vec]]
  - [[CBOW]]
  - [[Skip-Gram]]
methods:
  - [[随机Softmax损失函数优化]]
formulas:
  - [[随机Softmax损失]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-27-不可思议的Word2Vec-5-Tensorflow版的Word2Vec.md
source_ids:
  - "4402"
status: draft
updated: 2026-06-11
---

# 【不可思议的Word2Vec】5. Tensorflow版的Word2Vec

## 内容概要
文章利用 TensorFlow 实现了一个支持 CBOW 和 Skip-Gram 的 Word2Vec 模型。重点探讨了 Softmax 计算瓶颈的优化，提出了一种称为 “随机 Softmax 损失” (random softmax loss) 的交叉熵近似优化方法，并与 TensorFlow 原生的 `nce_loss` 及 `sampled_softmax_loss` 进行了对比实验。此外，文章还探索了 Softmax 投影层与词向量层权重共享的参数设置。

## 关键内容
1. **Softmax 梯度的期望表示**：
   全局 Softmax 交叉熵损失的梯度为：$\nabla L = -\nabla z_t + \mathbb{E}(\nabla z_i)$。
   因为每次迭代计算所有类别的配分函数 $Z$ 具有 $\mathcal{O}(V)$ 的时间复杂度，限制了大规模标签下的训练速度。
2. **随机 Softmax 损失 (Random Softmax Loss)**：
   由于均值项具有概率期望意义，该方法对每个“样本-标签”对在当前 batch 中随机选取 $N_{neg}$ 个负样本，与原标签组成 $N_{neg}+1$ 个类别子集，直接在此子集内算 Softmax 和交叉熵。这相当于在损失层面对梯度均值进行了蒙特卡洛随机采样近似。
3. **参数共享模型**：
   考虑 Softmax 的投影矩阵 $W$ 与词向量矩阵形状相同，文章实现了 Softmax 层与输入/输出词向量层参数共享（此时偏置置零）。由于共享参数，词向量在反向传播中更新更为充分，且训练完成后的 Softmax 输出依然具有预测概率的实际含义。
4. **对比实验结果**：
   在两万多篇旅游语料上进行的对比实验（CBOW 架构）表明：
   - 相同训练时长下，Random Softmax 损失的相似度性能与 Sampled Softmax 损失效果相当。
   - NCE 损失效果最差，需要极大的负采样数（如 1000）才能达到部分合理的效果。
   - Random Softmax 对每个样本分别进行独立负采样，因此负采样数较少时（如 10~30）即可收敛。
