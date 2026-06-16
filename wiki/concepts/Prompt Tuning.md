---
type: concept
title: Prompt Tuning
aliases:
- 提示调优
- P-tuning
definition: 通过可学习的连续向量模版替代自然语言模版，将下游任务与预训练任务对齐的参数高效微调方法。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
source_ids:
- '8295'
prerequisites:
- - - concept::语言模型
related_methods:
- - - method::P-tuning
- - - method::PET范式
- - - method::Adapter
status: draft
updated: '2026-06-14'
---

# Prompt Tuning (P-tuning)

Prompt Tuning (P-tuning) 是一种自动构建模版的方法，它重新审视了关于模版的定义，放弃了“模版由自然语言构成”这一常规要求，从而将模版的构建转化为连续参数优化问题。它在输入中插入可学习的连续向量（而非离散的自然语言 token），通过梯度下降优化这些向量的 Embedding，将下游任务转化为 MLM/LM 的预训练任务形式。

## 核心定义与优化原理

本质上来说，P-tuning 并不关心模版由什么自然语言词汇构成，只关心模版的长度、插入位置、输出候选空间等。它直接使用预训练模型词表中的未见 token（如 `[unused1]` 到 `[unused6]`）来构成模版。
在代码实现层面，P-tuning 的参数更新可以通过 `stop_gradient` 算子实现，仅使得部分控制模版的 token 在反向传播时梯度不为零：
```python
embeddings_sg = K.stop_gradient(embeddings)
mask = np.zeros((K.int_shape(embeddings)[0], 1))
mask[1:9] += 1  # 只优化特定 id 的 token
self.embeddings = embeddings * mask + embeddings_sg * (1 - mask)
```

## 关键属性与优化策略

根据标注数据量的多少，P-tuning 的优化策略分为两种主要情况：
1. **标注数据较少时**：固定整个预训练模型的权重，只优化模版对应 token 的 Embedding。由于要学习的参数很少，训练速度快且不容易过拟合，能够有效实现小样本学习。
2. **标注数据充足时**：放开所有模型权重进行全量微调。此时由于仅优化几个 token 会导致欠拟合，开放全量微调能够提供更大的优化空间。

**增强相关性（连续模版的自然语言近似）**：
为了让新插入的连续 token 之间具有更强的相关性（更贴近自然语言分布），P-tuning 可以通过一个小型且可学习的 LSTM 模型来生成这些 Embedding，这有助于防止局部最优并加快收敛。另一种更自然的方法是引入辅助目标：在训练下游任务时，不仅仅预测下游任务的目标 token，还同时随机 mask 并预测其他的 token，通过重构序列来引导连续模版向自然语言靠拢。

## 与其他概念的关系

* **PET（Pattern-Exploiting Training）范式**：PET 使用离散的自然语言模版进行提示，而 P-tuning 将离散的模版搜索转变为连续的参数优化，解决了人工构建自然语言模版困难且效果差异大的痛点。
* **Adapter**：如果将新插入的连续 token 视为模型本身的一部分，P-tuning 固定原模型权重而只在 Embedding 层插入并优化少量新参数的做法，与 Adapter 机制（只优化新插入的残差模块）有颇多异曲同工之处。
* **单向语言模型（LM vs MLM）**：P-tuning 成功地使得单向语言模型（如 GPT）能以生成任务的形式胜任自然语言理解（NLU）任务，有效释放了 GPT 等模型的潜能。

## 典型案例与性能表现

在具体的模型应用中，可以使用 `[unused*]` token 作为前缀或后缀拼接到输入文本两侧。实验表明，配合 P-tuning 的 GPT 能够克服以往“不擅长 NLU”的固有印象，在 SuperGLUE 上的成绩首次超过了同等级别的 BERT 模型。
在中文情感分类的小样本实验中：
* “BERT + P-tuning” 方案在测试集上取得了 $89.75\%$ 的准确率。
* “GPT + P-tuning” 方案在测试集上取得了 $88.51\%$ 的准确率。
这充分验证了通过连续参数优化构建模版的有效性，且为有限算力下调用大型预训练模型提供了一种全新的微调思路。
