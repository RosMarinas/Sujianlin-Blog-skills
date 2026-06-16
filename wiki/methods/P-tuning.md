---

type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: P-tuning
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-06-10-无监督分词和句法分析-原来BERT还可以这样用.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-05-短文本匹配Baseline-脱敏数据使用预训练模型的尝试.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-03-P-tuning-自动构建模版-释放语言模型潜能.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-22-CAN-借助先验分布提升分类性能的简单后处理技巧.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-20-你的语言模型有没有-无法预测的词.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
source_ids:
  - 8295
method_summary: 将模版构建转化为连续参数优化问题，使用[unused*] token的Embedding作为可学习参数，通过梯度下降自动构建模版
typical_structure: |
  1. 将原有自然语言模版替换为几个伪标记符（如 `[unused*]`）。
  2. 初始化这些标记的Embedding。
  3. 冻结预训练模型的大部分或全部参数，仅对这几个标记的Embedding进行梯度下降训练（或微调整个模型）。
  4. 使用学到的模版应用到具体的预训练或下游任务预测。
applicability: 小样本学习、零样本学习、参数高效微调、有限算力下调用大型预训练模型。
tools: 
related_methods: 
examples:
  - [[article::8295]]
status: stable
updated: 2026-06-12
problem_patterns: 
evidence_spans: 
  - ev::8295::"放弃了“模版由自然语言构成”这一常规要求，从而将模版的构建转化为连续参数优化问题"
---

# P-tuning

## 适用问题

缺少人工构建模版的精力或难以寻找最优模版，在小样本学习或有限算力微调大型预训练模型时，如何自动寻找最优的提示（Prompt/Pattern）。

## 核心变换

将离散自然语言模版的搜索过程，松弛转化为对连续向量（`[unused*]` 的 Embedding）的优化问题，通过反向传播自动学习出最佳模版表示。

## 典型步骤

1. **模版初始化**：在输入中插入一组未使用的特殊Token（如 `[unused1]` 到 `[unused6]`）来构成模版的前缀或后缀。
2. **冻结参数（少样本场景）**：在标注数据很少时，固定预训练模型的全部权重，只将这些新插入的Token的Embedding设为可学习。
3. **连续优化**：通过目标任务的监督信号，利用反向传播直接计算新Embedding的梯度并进行更新（也可使用一个小型的LSTM辅助生成这些Embedding以增强相关性）。
4. **联合训练（多样本场景）**：在数据充足的情况下，可选择放开所有模型参数进行端到端的联合微调。

## 直觉

我们本质上不关心模版必须是“自然语言”形式的，只要这几个Token插进去之后能促使语言模型输出正确的下游任务结果即可。把离散的词变成可以求导的连续Embedding，神经网络就可以自己学到提取特定知识的“探针”。

## 边界

- 只优化几个Token的参数容易在参数空间上受限。在全量数据场景下，可能不如放开全部权重或需通过额外的LSTM辅助收敛。
- 前缀与后缀的使用方式对不同模型（如单向LM与双向MLM）的敏感性不同，LM严重依赖前缀。

## 例子

- **SuperGLUE测评超越BERT**：借助自动优化的连续模版，只通过少量可学习参数便将 GPT 在 SuperGLUE 的分类成绩提升并超越了同级 BERT，证明 GPT 并非不擅长 NLU，只是需要合适的模版提取知识。

## 证据

- ev::8295::"P-tuning重新审视了关于模版的定义，放弃了“模版由自然语言构成”这一常规要求，从而将模版的构建转化为连续参数优化问题"
- ev::8295::"这种情况下，我们固定整个模型的权重，只优化[unused1]～[unused6]这几个token的Embedding...因为要学习的参数很少，因此哪怕标注样本很少，也能把模版学出来，不容易过拟合。"
