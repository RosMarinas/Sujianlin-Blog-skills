---
type: reading_path
title: LLM架构与上下文扩展阅读路径
aliases: []
goal: 从 Decoder-only 满秩性、LRU/RNN 并行化、RoPE-Bias、NBCE 到注意力稀疏度，理解 LLM 上下文与架构容量扩展。
audience: 需要从 series 层快速进入文章顺序、方法节点和检索关键词的读者。
ordered_nodes:
  - "[[spaces-9529]]"
  - "[[spaces-9547]]"
  - "[[spaces-9554]]"
  - "[[spaces-9577]]"
  - "[[spaces-9593]]"
  - "[[spaces-9617]]"
  - "[[spaces-9632]]"
  - "[[spaces-9648]]"
  - "[[spaces-9783]]"
  - "[[spaces-9889]]"
source_ids:
  - "9529"
  - "9547"
  - "9554"
  - "9577"
  - "9593"
  - "9617"
  - "9632"
  - "9648"
  - "9783"
  - "9889"
sources:
  - |
  - |
  - |
  - |
  - |
  - |
  - |
  - |
  - |
  - |
checkpoints:
  - Decoder-only 的满秩优势来自哪里？
  - NBCE 如何在不微调的情况下扩展上下文？
  - 非线性 RNN 并行化和 Attention 稀疏度分别回答什么问题？
next_paths:
  - [[Transformer架构与归一化阅读路径]]
  - [[Attention归一化与线性化阅读路径]]
status: draft
updated: 2026-06-14
---

# LLM架构与上下文扩展阅读路径

## 阅读顺序

1. 为什么现在的LLM都是Decoder-only的架构？
2. 《为什么现在的LLM都是Decoder-only的架构？》FAQ
3. Google新作试图“复活”RNN：RNN能否再次辉煌？
4. Bias项的神奇作用：RoPE + Bias = 更好的长度外推性
5. 注意力和Softmax的两点有趣发现：鲁棒性和信息量
6. NBCE：使用朴素贝叶斯扩展LLM的Context处理长度
7. 关于NBCE方法的一些补充说明和分析
8. Naive Bayes is all you need ?
9. 脑洞大开：非线性RNN居然也可以并行计算？
10. 注意力机制真的可以“集中注意力”吗？

## 读完应能回答

- Decoder-only 的满秩优势来自哪里？
- NBCE 如何在不微调的情况下扩展上下文？
- 非线性 RNN 并行化和 Attention 稀疏度分别回答什么问题？
