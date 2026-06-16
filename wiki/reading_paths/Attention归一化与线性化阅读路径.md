---
type: reading_path
title: Attention归一化与线性化阅读路径
aliases: []
goal: 按机制递进理解 Attention 从标准 Softmax 到稀疏、线性、低秩、熵校准和 GAU 的演化。
audience: 需要从 series 层快速进入文章顺序、方法节点和检索关键词的读者。
ordered_nodes:
  - "[[spaces-4765]]"
  - "[[spaces-6853]]"
  - "[[spaces-7546]]"
  - "[[spaces-8180]]"
  - "[[spaces-8823]]"
  - "[[spaces-9019]]"
  - "[[spaces-9052]]"
source_ids:
  - "4765"
  - "6853"
  - "7546"
  - "8180"
  - "8823"
  - "9019"
  - "9052"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-01-06-Attention-is-All-You-Need-浅读-简介-代码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-07-27-为节约而生-从标准Attention到稀疏Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-04-线性Attention的探索-Attention必须有个Softmax吗.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-16-Nyströmformer-基于矩阵分解的线性化Attention方案.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-21-从熵不变性看Attention的Scale操作.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-07-听说Attention与Softmax更配哦.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-04-22-GAU-α-尝鲜体验快好省的下一代Attention.md
checkpoints:
  - 标准 Attention 的二次复杂度来自哪里？
  - 线性 Attention 牺牲了 Softmax 的哪些性质？
  - 熵不变性如何解释 scale？
next_paths:
  - [[Transformer架构与归一化阅读路径]]
  - [[LLM架构与上下文扩展阅读路径]]
status: draft
updated: 2026-06-14
---

# Attention归一化与线性化阅读路径

## 阅读顺序

1. 《Attention is All You Need》浅读（简介+代码）
2. 为节约而生：从标准Attention到稀疏Attention
3. 线性Attention的探索：Attention必须有个Softmax吗？
4. Nyströmformer：基于矩阵分解的线性化Attention方案
5. 从熵不变性看Attention的Scale操作
6. 听说Attention与Softmax更配哦～
7. GAU-α：尝鲜体验快好省的下一代Attention

## 读完应能回答

- 标准 Attention 的二次复杂度来自哪里？
- 线性 Attention 牺牲了 Softmax 的哪些性质？
- 熵不变性如何解释 scale？
