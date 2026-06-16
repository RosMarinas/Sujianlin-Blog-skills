---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: PET范式
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-16-搜狐文本匹配-基于条件LayerNorm的多任务baseline.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-22-CAN-借助先验分布提升分类性能的简单后处理技巧.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-20-你的语言模型有没有-无法预测的词.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-16-随机分词浅探-从Viterbi-Decoding到Viterbi-Sampling.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-05-13-从EMD-WMD到WRD-文本向量序列的相似度计算.md
source_ids:
  - 7476
  - 8213
  - 8295
method_summary: 通过模版将下游任务转化为预训练任务（MLM/LM）形式，充分释放语言模型在小样本场景下的潜能
typical_structure: |
  1. 定义模版，将目标输入转换为包含挖空（Mask）的自然语言句子。
  2. 将下游任务标签映射到预定义的词汇（如[YES]/[NO]）。
  3. 利用语言模型或MLM模型对挖空处进行概率预测。
  4. 结合少量有标注数据和大量无标注数据进行联合训练或预测。
applicability: 小样本学习、零样本学习、半监督文本分类、短文本匹配等自然语言理解任务。
tools: 
related_methods: 
examples:
  - [[article::8213]]
  - [[article::8295]]
status: stable
updated: 2026-06-12
problem_patterns: 
evidence_spans: 
  - ev::7476::"PET主要是借助由自然语言构成的模版，将下游任务也转化为一个完形填空任务，这样就可以用BERT的MLM模型来进行预测了"
  - ev::8213::"用一个MLM模型来完成所有...同时做了句子对的分类任务（[CLS]的预测结果），也做了MLM的预训练任务...把分类、预训练和半监督都结合起来了"
---

# PET范式

## 适用问题

由于缺少标注样本，微调传统的分类器（加一个全连接层）容易过拟合且难以激活预训练模型中的知识，希望在零样本、小样本、半监督文本分类中充分释放预训练语言模型的潜能。

## 核心变换

将下游的监督分类问题形式化重写为预训练模型擅长的完形填空（Masked Language Modeling, MLM）或自回归语言模型（LM）问题，统一了预训练与微调任务形式。

## 典型步骤

1. **模版构造**：通过人工设计或自动搜寻一段包含自然语言前/后缀和掩码位置的模版（Pattern）。
2. **文本改写**：将输入文本通过模版进行包装。例如，将两句话拼接后接上“它们相似吗？[MASK]”。
3. **标签映射**：将原本下游任务的类别标签映射为词表中的具体 Token（如类别1对应“是”，类别2对应“否”）。
4. **模型预测**：直接通过预训练语言模型计算 MASK 位置对应 Token 的概率来得出最终分类。
5. **联合训练**：在训练阶段可以结合少量有标签数据和大量无标签数据，同时进行分类预测与遮蔽语言模型重构损失。

## 直觉

语言模型在预训练时学习到的是通过上下文填词的能力。下游分类任务如果是另外加入分类头，不仅引入了额外参数，且任务形式产生偏离。通过语言模版，让模型感觉依然是在做填空题，这样能够最快速、最直觉地调动起它学过的通用知识库。

## 边界

- 极其依赖模版的设计，人工构建费时且不同模版导致结果方差极大（这也是 P-tuning 试图解决的）。
- 当模型规模足够大且目标域数据极度丰富时，这种结构重写相较于直接微调带来的增益会边际递减。
- 难以直接应对目标标签无法简单地映射到单个或少数几个 Token 上的复杂预测任务。

## 例子

- **脱敏数据下的文本匹配**：利用 BERT MLM 任务结构，将需要匹配的两个短句重写后进行掩码预测，把分类和语言重构整合为单一的损失函数，有效运用了半监督学习的数据。
- **情感分类**：给待分类句子加上“满意吗？[MASK]”的前缀，将预测正/负面评价转换为让 BERT 预测在 `[MASK]` 位置填上 “满意” 或 “失望” 哪个词的概率更高。

## 证据

- ev::7476::"PET主要是借助由自然语言构成的模版，将下游任务也转化为一个完形填空任务，这样就可以用BERT的MLM模型来进行预测了"
- ev::8213::"我们同时做了句子对的分类任务（[CLS]的预测结果），也做了MLM的预训练任务（其他被mask掉的token），而且没有标签的样本（比如测试集）也可以扔进去训练...把分类、预训练和半监督都结合起来了"
