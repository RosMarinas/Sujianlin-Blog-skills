---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: BytePiece Tokenizer
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-07-BytePiece-更纯粹-更高压缩率的Tokenizer.md
source_ids:
  - 9752
method_summary: 一种基于字节级别（Byte-level）和Unigram分词算法的无监督分词器，能够提供更高压缩率并保持语言无关性。
typical_structure: |
  1. 将输入文本编码为UTF-8字节序列。
  2. 进行n-gram计数，统计不同字节片段的出现频次。
  3. 执行n-gram剪枝，按照频数与目标词表大小进行初步过滤。
  4. 利用Viterbi算法计算最大概率路径，完成预分词。
  5. 对预分词结果进行剪枝，移除冗余子串，得到最终词表和分词模型。
applicability: 适用于需要训练高压缩率、语言无关且无需复杂预处理的通用Tokenizer场景，特别是构建大语言模型词表。
examples:
  - [[article::9752]]
status: stable
updated: 2026-06-13
evidence_spans:
  - ev::9752::BytePiece的训练本质上转化为n-gram语言模型的无监督训练，结合Viterbi算法求最大概率路径
---

## 适用问题

构建用于大语言模型等自然语言处理任务的底层分词器（Tokenizer），尤其是需要高压缩率、语言完全无关，且免去复杂文本预处理（如全半角转换、特殊字符处理）的场景。

## 核心变换

将传统的基于字符回退的BPE或Unigram模型，重写为完全基于UTF-8字节流（Byte-level）的Unigram语言模型。利用n-gram条件概率乘积最大化，将分词问题转化为寻找最大概率字节切分路径的隐马尔可夫/动态规划问题。

## 典型步骤

1. **字节编码**：将原始训练语料统一编码为UTF-8的字节序列，不作任何语言相关的过滤。
2. **频次统计**：扫描字节序列，统计不同n-gram片段的出现频次（通常n=6即可近似长序列）。
3. **初筛剪枝**：根据频数以及设定的目标词表大小（vocab_size），保留高频n-gram，剔除低频片段。
4. **Viterbi预分词**：基于当前的子词概率分布，使用Viterbi算法求解使得文本出现概率最大（或负对数似然最小）的分词路径。
5. **冗余剪枝**：排除那些在其组合概率上小于拆分部分概率的“永远不会被切分出来”的拼接词，精简词表。

## 直觉

任何文本最终在计算机中都是字节序列。如果抛弃字符概念直接在字节序列上做统计语言模型，那么所有语言、特殊符号、Emoji都能一视同仁。而Unigram分词本质上就是找到让该字符串在语言模型中概率最大的一条分割路径，这跟使用Viterbi算法进行解码的思想是完全同构的。

## 边界

1. 由于直接在字节级别进行暴力组合和统计，初期n-gram计数的内存消耗极大（内存限制了它可能不如 SentencePiece 的 BPE 容易在极低内存下运行）。
2. 在推理分词时，纯Python实现的Viterbi解码构建AC自动机速度比C++慢，可能成为大吞吐量生成时的短板。

## 例子

在处理包含中英混排、特殊符号和Emoji的文本时，直接按UTF-8展开为Bytes，然后统计高频Bytes片段。比如“学习”可能被直接统计为其对应的6个字节组合片段，而不是依赖于预先切分中文字符。

## 证据

- ev::9752::“对于Unigram分词，如果一个长度为l的字节串...概率乘积应该是所有切分中最大的。转化为n-gram语言模型的训练...并使用Viterbi求最大概率路径”
