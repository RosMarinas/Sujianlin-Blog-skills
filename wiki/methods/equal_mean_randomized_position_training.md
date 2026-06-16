---


type: method
operation_types:
  primary: Estimate / sample instead of compute
  secondary: []
title: Equal Mean Randomized Position Training
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-31-Transformer升级之路-8-长度外推性与位置鲁棒性.md
  - Data/（待从源文章提取）
source_ids:
  - 9444
  - （待从源文章提取）
method_summary: A variant of Randomized Positional Training designed for functional position encodings (like RoPE or Sinusoidal). To ensure consistency between training and inference distributions: 1. A range limit $n$ is randomly sampled from a distribution (e.g., Exponential or Beta) with a mean equal to the sequence length $N$. 2. The model samples $N$ points uniformly from $[0, n]$ as the position sequence for training. This guarantees that the position intervals are continuous floats and match the sequence's expected bounds, improving length extrapolation for continuous positional embeddings.
typical_structure: |
  1. 根据训练序列目标长度 $N$，选择一个均值为 $N$ 的采样分布（如指数分布或Beta分布）。
  2. 训练中每次从上述分布中采样一个数值 $n$ 作为位置上限。
  3. 在 $[0, n]$ 均匀提取 $N$ 个浮点数作为输入的位置 ID。
  4. 结合函数式位置编码（如RoPE）进行训练。
applicability: Transformer等序列模型的长度外推任务，特别是在使用函数式位置编码时，为了消除训练和预测长度不一致带来的效果下降。
examples:
  - 训练长度64，用指数分布采样上限$n$，均匀生成64个浮点位置ID；测试时直接用自然数序列测512长度。
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::9444::原文延伸推广节提出等均值随机位置训练思路及最佳分布（指数分布），验证其在MLM任务上的卓越外推效果。
---

# Equal Mean Randomized Position Training (等均值随机位置训练)

## 适用问题
在自然语言处理或序列建模任务中，当模型需要处理比训练时更长的序列（即长度外推性问题）时，往往因为测试时出现了未训练过的位置编码而导致性能大幅下降。传统随机位置训练在训练和测试时的位置间距不一致，且对连续型函数式位置编码（如RoPE、Sinusoidal）利用不充分。

## 核心变换
在每次训练迭代中，以序列长度 $N$ 为均值从特定概率分布（如指数分布或Beta分布）中采样出一个范围上限 $n$，然后在 $[0, n]$ 之间均匀等距采样 $N$ 个浮点数作为本次输入序列的位置编码 ID。

## 典型步骤
1. 根据训练序列目标长度 $N$，选择一个均值为 $N$ 的采样分布（推荐使用指数分布或Beta分布）。
2. 在每一步训练中，从上述分布中随机采样一个数值 $n$ 作为位置区间的上限。
3. 利用等距插值（如 `np.linspace(0, n, N)`）在区间 $[0, n]$ 均匀取 $N$ 个连续浮点数，作为这 $N$ 个 Token 的位置 ID。
4. 将这些浮点数位置 ID 传入函数式位置编码（如 RoPE）中生成对应的位置向量并计算 Attention。
5. 在推理阶段，直接使用连续的正整数位置 ID（如 $[0,1,2,\dots]$）进行长序列计算。

## 直觉
模型不需要仅仅记住固定的绝对位置 ID，而是学会依赖位置序列的“序”和相对关系来理解序列。传统随机位置训练导致训练时的平均位置远大于测试时的平均位置。通过使随机上限 $n$ 的均值等于训练序列长度 $N$，能够使得训练时前 $N$ 个位置的数学期望与真实测试时长序列的前 $N$ 个位置严格一致，拉近训练和预测的数据分布差距。

## 边界
- 只能应用于连续的函数式位置编码（例如 RoPE、Sinusoidal 等可以接受浮点数作为位置输入的编码方法），不适用于可学习的离散绝对位置编码。
- 分布的选择比较关键，如果选择泊松分布（方差小）会导致外推范围过短。
- 引入了连续位置，对于极度依赖离散整数的精确绝对位置进行数值规律计算的任务可能会产生微弱干扰。

## 例子
设定训练长度 $N=64$，采样分布为均值为64的指数分布。
- 第1次迭代，采样出 $n=120$，生成的等距位置序列为 $[0, 120/63, 240/63, ..., 120]$。
- 第2次迭代，采样出 $n=30$，生成的等距位置序列为 $[0, 30/63, 60/63, ..., 30]$。
- 推理阶段，面对长度为 512 的序列，直接输入 $[0, 1, 2, ..., 511]$，模型自然地在未经训练的大位置上泛化。

## 证据
- 原文 9444 提及："等均值随机位置训练 设n服从一个均值为N、采样空间为[0, ∞)的分布...笔者的实验结果显示，结合log n缩放注意力，在MLM任务上能取得最佳的外推效果（训练长度64，测试长度512，采样分布为指数分布）。"
