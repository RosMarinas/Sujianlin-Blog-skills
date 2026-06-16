---
type: method
title: "ELECTRA预训练"
aliases:
  - "ELECTRA"
operation_types:
  primary: "Estimate / sample instead of compute"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-10-29-用ALBERT和ELECTRA之前-请确认你真的了解它们.md
source_ids:
  - "7846"
method_summary: "使用生成器-判别器架构的预训练方法，生成器做MLM采样替换token，判别器判断token是否被替换。"
typical_structure: |
  1. Generator做MLM预测替换token
  2. Discriminator判断每个token是否被替换
  3. 生成器和判别器同步训练
  4. 下游只使用Discriminator
applicability: "语言模型预训练，文本编码"
tools:
  - 生成器
  - 判别器
  - 替换检测
related_methods: []
examples:
  - [[article::7846]]
status: draft
updated: 2026-06-13
---

## 适用问题

语言模型预训练，旨在通过更高效的训练方式获得文本编码器。ELECTRA使用生成器-判别器架构提高训练效率，声称可用更少计算资源达到同等效果。

## 核心变换

**输入**：原始文本序列
**输出**：判别器编码器（下游任务使用）

标准MLM随机Mask部分Token后预测，ELECTRA改为：
1. 生成器（小型MLM）预测被Mask的Token
2. 用生成器的预测结果替换原文中被Mask的Token
3. 判别器判断每个Token是否被替换（原始 vs 替换）

判别器损失函数为逐Token的二分类交叉熵：
$$
\mathcal{L}_{\text{disc}} = -\sum_{t} \left[ \mathbb{1}(x_t \text{ 是原始}) \log D(x_t) + \mathbb{1}(x_t \text{ 被替换}) \log (1-D(x_t)) \right]
$$

## 典型步骤

1. **随机选择位置**：在输入序列中随机选择部分位置进行Mask
2. **生成器预测**：小型MLM模型预测被Mask位置的Token分布，从中采样替换
3. **判别器判断**：判别器接收替换后的序列，对每个位置判断是否被替换
4. **同步训练**：生成器和判别器同时优化，生成器使用MLM损失，判别器使用替换检测损失
5. **下游使用**：训练完成后，丢弃生成器，仅使用判别器的Encoder部分

## 直觉

ELECTRA的动机是MLM任务太简单——随机Mask的Token位置在训练中可能很快被模型掌握。借鉴GAN思想：生成器不断产生更逼真的"假Token"，迫使判别器学习更精细的上下文表示来区分真假。这种对抗式的渐进难度让训练过程更有针对性，理论上提高了训练效率。

但这一思路存在根本问题：当生成器足够强时，其产生的"假Token"与真实Token分布趋于一致，判别器退化为常值函数$1/2$，无法学到有用特征。因此生成器必须刻意保持弱小（大小为判别器的$1/4$到$1/2$），这使ELECTRA的训练带有一定"玄学"成分。

## 边界

- **下游效果未显著超越BERT**：开源评测显示同级别ELECTRA与BERT在下游任务上差距不大，未复现论文报告的显著优势
- **MLM权重不可用**：ELECTRA主体是判别器而非MLM模型，无法用于需要MLM的任务（文本生成、纠错等）
- **生成器质量有限**：作为MLM模型的生成器能力受刻意限制，不是优质的预训练MLM模型
- **复杂任务可能更差**：在对抗性构建的复杂数据集（如QADS）上，ELECTRA效果显著低于BERT
- **中文任务表现平平**：哈工大Chinese-ELECTRA评测显示各任务与同级别BERT持平，无碾压优势

## 例子

- 论文报告：base版ELECTRA达到large版BERT水平（dev集）；但Github开源评测显示下降约2个百分点（test集）
- 预训练效率提升：按论文说法可用$1/4$的时间达到同等BERT效果
- QADS复杂数据集：ELECTRA large仅22%，BERT large可达60%以上

## 证据

- ev::7846::ELECTRA生成器-判别器架构：生成器做MLM替换，判别器判断Token是否被替换
- ev::7846::生成器大小控制：1/4到1/2的判别器大小以维持判别器有效性
- ev::7846::判别器退化问题：理论上生成器变强时判别器趋于常值$1/2$
- ev::7846::开源评测差距：论文dev集结果与Github test集结果存在2个百分点差距
