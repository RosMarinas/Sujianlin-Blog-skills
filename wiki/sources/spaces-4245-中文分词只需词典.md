---
type: article_summary
title: "【中文分词系列】 7. 深度学习分词？只需一个词典！"
article_id: "4245"
source_url: https://spaces.ac.cn/archives/4245
date: 2017-03-06
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-03-06-中文分词系列-7-深度学习分词-只需一个词典.md
series:
  - [[wiki/series/中文分词系列.md]]
concepts:
  - [[concept::中文分词]]
  - [[concept::字标注分词]]
methods:
  - [[method::基于词表随机组合语料训练]]
evidence_spans:
  - ev::4245::伪语料生成
  - ev::4245::BiLSTM分词
  - ev::4245::算法学习能力
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-03-06-中文分词系列-7-深度学习分词-只需一个词典.md
source_ids:
  - "4245"
status: draft
updated: 2026-06-11
---

# 【中文分词系列】 7. 深度学习分词？只需一个词典！

本文介绍了一种仅基于带词频词典、无需人工标注真实语料来训练深度学习分词器的半监督/无监督方法。通过基于词典词频随机拼凑生成虚假句子并附带标签，训练 BiLSTM 标注模型，使其隐式学习到动态规划的解码过程。

## 核心内容

- **伪语料生成算法**：
  - 基于一个大型带词频词典，将词频取整以减少权重分组类别，加速随机采样。
  - 按正比于词典词频的概率随机挑选词语拼凑成“句子”（如长度 1 到 16 个词）。
  - 根据拼凑结构自动生成字级 SBME 标签，并将句尾用填充标记（和对应的掩码）补齐。
- **BiLSTM 分词器**：
  - 输入：48维变长字 ID。经过字 Embedding（128维） $\to$ 双向 LSTM（64隐藏单元） $\to$ TimeDistributed Dense 层 $\to$ Softmax 激活输出 5 类标签概率（包含填充掩码类别）。
  - 在 Bakeoff 2005 评测集上，没有接触过任何真实训练语料的模型取得了 $85\%$ 的 F1 值，证明了其出色的新词与长词泛化能力。
- **动态规划逼近假说**：
  - 基于词典的分词算法假设句子是词的随机组合，并用 Viterbi 算法求解全局概率最大路径。
  - 通过让神经网络在以词频加权生成的伪语料上进行拟合，LSTM 的强记忆能力使其学到了这一“动态规划”的寻优机制，从而能在面对类似“结婚的和尚未结婚的”这样的交叉歧义时，给出符合词典概率规律的正确切分。
