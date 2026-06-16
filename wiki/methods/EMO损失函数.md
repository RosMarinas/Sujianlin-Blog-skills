---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: EMO (Earth Mover Distance Optimization) 损失函数
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
source_ids:
  - 9797
method_summary: "用固定 token embedding 的余弦相似度作为最优传输成本，把交叉熵分类损失改写为按语义距离惩罚预测分布的 EMO 损失。"
typical_structure: |
  1. 获取预训练模型的词表 Token Embedding（通常使用预训练好的 LM Head 权重）并在此过程中保持固定。
  2. 使用余弦相似度计算真实标签 token 与所有其他 token 的距离（即传输成本）。
  3. 模型前向计算出预测概率分布 p。
  4. 计算 EMO 损失：计算预测概率与各 token 到目标 token 距离的加权和。
  5. 利用反向传播优化模型参数。
applicability: "大语言模型（LLM）的微调或二次预训练任务，特别是词表（vocab_size）较大时，旨在提升生成文本的主观质量和流畅度。不适用于从零开始的初始预训练。"
examples:
  - "[[article::9797]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::9797::EMO将交叉熵替换为基于最优传输的损失，利用Token Embedding的语义相似度分配更合理的传输成本。"
---

# EMO (Earth Mover Distance Optimization) 损失函数

## 适用问题
在训练和微调大语言模型（LLM）时，标准的交叉熵（Cross Entropy / MLE）损失将词表分类视为非黑即白的问题：只要预测的 token 不是标签 token，哪怕意思极为相近（近义词），模型受到的惩罚和预测成完全无关的词是一样的。我们需要一种能够反映 token 之间语义距离的损失函数，以提升生成的文本质量（即“说人话”的能力）。

## 核心变换
将度量预测概率分布与真实标签 One-hot 分布之间差异的 KL 散度（交叉熵），替换为两个分布之间的推土机距离（W距离 / EMD）。通过引入固定的 Token Embedding，将传输成本定义为余弦相似度的惩罚形式，从而将交叉熵损失重写为 EMO 损失：
$$ \mathcal{L}_{EMO} = \sum_i p_i \left( 1 - \left\langle \frac{\boldsymbol{e}_i}{\Vert\boldsymbol{e}_i\Vert}, \frac{\boldsymbol{e}_t}{\Vert\boldsymbol{e}_t\Vert} \right\rangle \right) $$
其中 $p_i$ 是预测第 $i$ 个词的概率，$\boldsymbol{e}_i$ 和 $\boldsymbol{e}_t$ 分别是第 $i$ 个词和目标标签词的预训练 Embedding 向量。

## 典型步骤
1. **获取先验 Embedding**：从一个预训练好的模型中取出 LM Head 或词向量层作为各个 token 的语义向量表示 $\boldsymbol{e}$，并在接下来的训练中将其**固定（冻结）**。
2. **计算成本矩阵**：定义预测成 token $i$ 时的代价为它与真实标签 token $t$ 的余弦距离 $c_{i,t} = 1 - \cos(\boldsymbol{e}_i, \boldsymbol{e}_t)$。
3. **输出预测分布**：模型输出当前位置关于整个词表的预测概率分布 $p$（通常经过 Softmax）。
4. **计算期望传输成本**：先将概率 $p$ 对所有被归一化后的 Token Embedding 进行加权求和，然后计算其与目标标签 Embedding 的内积，用 1 减去该内积得到最终损失。
5. **反向传播优化**：利用上述损失的梯度来更新模型参数（不包括第一步冻结的 Token Embedding）。

## 直觉
假设你要预测下一个词是“开心”，结果预测成了“快乐”或“悲伤”。在普通的交叉熵眼里，这俩全是0分，要挨一样的打。但最优传输（EMD）认为，你要把“快乐”搬运成“开心”，运费（成本）是很低的，因为它们在词向量空间里本来就挨得很近；而把“悲伤”搬运成“开心”运费就极高。EMO 损失函数就是把预测分布根据这些不同的“运费”进行计价，预测出来的近义词哪怕概率再高，也不会招致过于严重的惩罚，从而允许语言模型保持一定程度的表达多样性。

## 边界
1. **不能凭空训练**：因为需要语义合理的 Token Embedding 来计算距离成本，所以无法用于从零开始（随机初始化）的预训练阶段。
2. **收敛速度可能变慢**：因为错误方向的损失是有界的（最大值为2），不像交叉熵那样可以将错误方向的误差拉到无穷大，这可能导致在从零开始时收敛较慢（如果在预训练阶段使用，往往需要与 MLE 混合加权）。
3. 效果十分依赖预计算好的 Token Embedding 质量，词表（vocab_size）越大时“近义词”越多，收益通常越明显。

## 例子
在对 LLaMA-7B 或 13B 进行下游任务微调时，使用交叉熵会得到常规效果。改用 EMO 损失：固定其原有的语言建模头作为向量参考。当预测结果中与正确目标越相关的词占用更高概率时，Loss 下降得就越多，实验表明这极大提升了 MAUVE 指标（甚至困惑度 PPL 也有所降低），生成的文本在人工评价标准上更像真实人类写的。

## 证据
- 9797 介绍了最优传输损失和成本函数设计：“理想情况下应该根据相似度来给每个不同的 $i$ 设计不同的成本... $c_{i,t} = 1 - \cos(\boldsymbol{e}_i, \boldsymbol{e}_t)$”并推导出 $\mathcal{C}[p,\tau]= 1 - \left\langle \sum_i p_i \frac{\boldsymbol{e}_i}{\Vert\boldsymbol{e}_i\Vert}, \frac{\boldsymbol{e}_t}{\Vert\boldsymbol{e}_t\Vert}\right\rangle$。文章展示了其在继续预训练和微调中比 MLE 具有最高 10 个点的 MAUVE 指标提升。
