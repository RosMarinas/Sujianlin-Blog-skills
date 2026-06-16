---
type: article_summary
title: NBCE：使用朴素贝叶斯扩展LLM的Context处理长度
article_id: 9617
source_url: https://spaces.ac.cn/archives/9617
date: 2023-05-23
category: Big-Data
source_markdown: |
  Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
source_ids:
  - 9617
status: draft
updated: 2026-06-12
---

# NBCE：使用朴素贝叶斯扩展LLM的Context处理长度

本文提出了一种名为NBCE（Naive Bayes-based Context Extension）的无微调、即插即用扩展LLM上下文长度的方法。
NBCE的思想是将超出模型训练长度的长上下文切分为多个较短的相对独立的段落（Contexts），在解码时将每个段落分别与当前生成的Task Tokens组合放入同一batch中并行计算预测概率。
利用朴素贝叶斯公式与条件独立假设，将联合概率分解为各个独立上下文概率的聚合，并减去无上下文预测概率以强化模型对证据的依赖（减少幻觉）。
为了改善由于独立性假设失效而导致随机采样不可读的问题，NBCE采用了一种一般化的Pooling聚合方式——“最小熵Pooling”，即只输出各上下文分布中信息熵最低（确定性最高）的那个概率分布。
实验表明，NBCE成功在7B模型上实现了包含12段不同段落、总长超1万字的长文本多问题阅读理解，展现了出色的外推生成能力。