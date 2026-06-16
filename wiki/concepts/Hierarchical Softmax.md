---
type: concept
title: Hierarchical Softmax
aliases:
- 层次Softmax
- Huffman Softmax
definition: 一种基于Huffman二叉树的Softmax近似提速算法，将输出层概率计算复杂度从 O(|V|) 降至 O(log_2 |V|)。
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-04-02-不可思议的Word2Vec-1-数学原理.md
source_ids:
- '4299'
prerequisites:
- '[[Softmax]]'
evidence_spans:
- ev::4299::训练提速
status: stable
updated: '2026-06-12'
---

# Hierarchical Softmax

Hierarchical Softmax（层次 Softmax）是 Word2Vec 中用于加速输出层多分类概率计算的经典技术。

## 基本原理
它根据词频构建一棵 Huffman 树，树的每个叶子节点代表词表中的一个词，而树的非叶子节点代表一个二分类器。预测词概率的问题从而转变为从根节点到对应叶子节点的二分类决策链条，将复杂度由 $\mathcal{O}(|V|)$ 降低为 $\mathcal{O}(\log_2 |V|)$。