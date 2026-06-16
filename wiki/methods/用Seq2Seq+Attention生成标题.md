---


type: method
operation_types:
  primary: Structure-expose by factorization
  secondary: []
title: 用Seq2Seq+Attention生成标题
aliases: 
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-09-01-玩转Keras之seq2seq自动生成标题.md
source_ids:
  - 5861
method_summary: 用 Encoder-Decoder 序列模型加 Attention 局部回看长文本，生成更短的标题序列。
typical_structure: |
  1. 使用双向 RNN（如 LSTM/GRU）作为 Encoder 处理输入长文本。
  2. 使用 RNN 作为 Decoder。
  3. 在 Decoder 生成每一步时引入 Attention 机制，计算当前隐状态对原输入序列中每一处的注意力分布并加权求和，拼接到隐状态中。
  4. 解码输出端接 Softmax 以预测单词概率，并使用交叉熵训练模型。
applicability: 适用于文本摘要、自动拟写文章标题等需要将长序列映射为短序列且长程依赖较强的自然语言生成任务。
examples:
  - [[article::5861]]
status: stable
updated: 2026-06-12
evidence_spans:
  - ev::5861::介绍了基于Seq2Seq框架并结合注意力机制进行中文文章标题自动生成的应用与Keras层面的构建方法。
---

# 用Seq2Seq+Attention生成标题

## 适用问题

仅仅通过提取现成的句子作为文章摘要或标题（抽取式摘要）有时显得生硬且无法高度概括。我们希望利用深度学习生成全新且语义连贯的总结性标题（生成式摘要），这就需要解决长文章压缩到短文本时容易“遗忘”关键信息的问题。

## 核心变换

$$ c_t = \sum \alpha_{ti} h_i,\quad \alpha_{ti} = \text{Softmax}(score(s_{t-1}, h_i)) $$
在将输入转换为隐空间表示的纯序列映射过程中，插入 Attention（注意力）软对齐，使得解码生成步骤动态“关注”原始文本的不同位置。

## 典型步骤

1. **词向量映射**：将输入的正文文本序列以及目标标题序列转换为固定维度的词向量。
2. **编码器构建**：通过一层或多层双向 GRU/LSTM，充分读取输入文本并生成蕴含全局上下文的高维隐特征序列。
3. **注意力计算**：在解码阶段的每一步，解码器都计算自身当前内部状态与编码器所有词的隐含状态之间的相似度（Attention），得到加权上下文向量 $c_t$。
4. **解码生成**：将加权上下文向量 $c_t$ 与当前预测时间步的输入拼接，送入解码器 GRU，并通过 Softmax 给出当前词的输出概率。
5. **推断策略**：由于推断时不具有真实目标信息，需要采用贪婪搜索或 Beam Search 来循环输出序列直到遇到结束符。

## 直觉

Seq2Seq 就像是把一本长书的内容用记忆压缩成一串脑电波，然后再根据脑电波讲一个新故事。如果书太长，单纯的脑电波可能会丢三落四。加上 Attention 机制，就像是给讲故事的人发了一份原书的副本，每讲一个词他都可以回过头翻一翻副本里对应的核心段落，从而讲出极其凝练又不会跑偏的标题。

## 边界

- 相比于现代 Transformer 架构，基于 RNN 的 Seq2Seq+Attention 在处理超长文本和并行计算效率上处于劣势。
- 文本生成的通用通病，容易出现内容重复（复读机现象）或语义幻觉现象，有时需要加入诸如 coverage penalty 等防重复机制。

## 例子

在 Keras 下训练自动标题生成网络，编码器将一段几百字的新闻正文加工后，配合加入的单头注意力层，解码器准确输出了十几个字的标题。即使文章主题有转变，注意力图也能反映出不同词汇对生成标题单词的对应程度。

## 证据

- ev::5861::介绍了基于Seq2Seq框架并结合注意力机制进行中文文章标题自动生成的应用与Keras层面的构建方法。
