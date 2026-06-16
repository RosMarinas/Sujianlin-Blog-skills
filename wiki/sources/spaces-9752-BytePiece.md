---
title: BytePiece：更纯粹、更高压缩率的Tokenizer
source_id: 9752
type: source
url: https://spaces.ac.cn/archives/9752
author: 苏剑林
date: 2023-09-07
category: 信息时代
tags: [tokenizer, byte-level, unigram, compression]
license: CC BY-NC-SA
abstract: 介绍BytePiece，一个纯Python实现的Byte-based Unigram分词器。直接操作UTF-8字节序列，压缩率高于SentencePiece，训练速度在并行条件下可媲美SP-Unigram。
key_contributions:
  - 理想Tokenizer五大特性：无损重构、高压缩率、语言无关、数据驱动、训练友好
  - Byte-based vs Char-based的分析（信息熵均匀性）
  - BNLM（Byte-based N-gram Language Model）训练算法
  - 剪枝策略排除永远不会被切出的冗余词
  - 与SP-BPE/SP-Unigram的全面对比（训练时间、内存、压缩率）
  - 大语料场景下BytePiece的压缩率优势（同源5.39 vs SP-BPE 4.52）
