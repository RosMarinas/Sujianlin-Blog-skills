---
type: method
title: 随机替换抗Exposure Bias
aliases: []
operation_types:
  primary: Estimate / sample instead of compute
  secondary:
    - Generalize from special cases
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-03-09-Seq2Seq中Exposure-Bias现象的浅析与对策.md
source_ids:
  - "7259"
method_summary: 在Seq2Seq训练中随机替换Decoder的部分输入词，构造有代表性的负样本，使模型学习在扰动输入下依然正确预测，从而缓解训练-测试不一致导致的Exposure Bias。
typical_structure: |
  1. 以50%概率决定是否替换
  2. 若替换，将输入序列中30%的词随机替换为目标序列中的任意词
  3. 正常计算交叉熵损失
applicability: 适用于各类Seq2Seq文本生成任务，特别是存在Teacher Forcing训练-测试不一致的场景。即插即用，几乎不损失训练性能。
tools:
  - 随机输入替换
  - Exposure Bias 缓解
related_methods:
  - [[对抗训练文本增强]]
  - [[Scheduled Sampling]]
examples:
  - [[article::7259]]
status: draft
updated: 2026-06-14
---

## 适用问题

Seq2Seq 训练中 Teacher Forcing 使用真实目标词作为解码器每一步的输入，但推理时解码器的输入是自身前一步的生成结果。当模型某一步生成错误时，后续所有步骤都在错误的输入条件下预测，误差不断累积（Exposure Bias）。随机替换通过模拟推理时的错误状态，让模型学会从错误中恢复。

## 核心变换

**输入**：解码器目标序列 $Y = [y_1, y_2, \dots, y_T]$
**输出**：经部分替换的抗噪目标序列 $\tilde{Y}$
**参数**：替换概率 $p_{\text{replace}}$，替换比率 $r$

以 50% 的概率决定是否在当前 batch 应用替换：
$$
\text{apply} \sim \text{Bernoulli}(0.5)
$$

若应用，以概率 $r$（通常 30%）替换每个目标词：
$$
\tilde{y}_t = \begin{cases}
y_{\text{random}} & \text{以概率 } r \\
y_t & \text{以概率 } 1-r
\end{cases}
$$

替换词 $y_{\text{random}}$ 从目标词表中随机采样。使用 $\tilde{Y}$ 作为解码器输入，仍以原始 $Y$ 为目标计算交叉熵损失。

## 典型步骤

1. **采样决策**：掷硬币决定是否在当前训练步进行替换（50% 概率）
2. **随机替换**：若替换，对解码器输入序列中 30% 的位置随机替换为目标词表中的任意词
3. **正常训练**：使用替换后的序列作为解码器输入，计算标准交叉熵损失

## 直觉

核心思想：**犯错不可怕，可怕的是没有练习过犯错后如何补救**。

Teacher Forcing 相当于给模型配了一个"标准答案提示器"，模型从不需要面对自己的错误。一旦推理时第一步生成错了，后续的每一步模型都处于"从未见过的错误状态"中，完全不知道如何应对。

随机替换在训练时就模拟了这种"错误状态"——模型在解码器的输入中看到了一些错误的、不合理的词，但仍然需要从这些错误状态下正确预测下一个词。这迫使模型学会了两件事：
1. **容错**：即使前面错了，后面也要尽力生成正确的结果
2. **纠错**：当输入不合理时，学会忽略或修正它

## 边界

- 替换概率 50% + 替换比率 30% 是经验值，需根据任务微调
- 替换词从目标词表随机采样，而非从模型预测分布采样（与 Scheduled Sampling 的区别）
- 几乎不增加训练时间（仅需生成随机索引），即插即用
- 对 Rouge 指标有明显提升，与[[对抗训练文本增强]]叠加效果更好
- 替换比例过高会破坏训练数据质量，导致欠拟合

## 例子

- 在摘要生成任务中，随机替换使模型在推理时对前几步的错误更加鲁棒
- 与对抗训练叠加：随机替换从离散输入空间做扰动，对抗训练从连续 Embedding 空间做扰动，二者互补
- 在机器翻译任务上也有效，但翻译对输入噪声更敏感，替换比例需调小

## 证据

- ev::7259::随机替换策略：50% 概率触发，30% 输入词替换
- ev::7259::与 Teacher Forcing 的对比分析
- ev::7259::Exposure Bias 现象的理论分析
