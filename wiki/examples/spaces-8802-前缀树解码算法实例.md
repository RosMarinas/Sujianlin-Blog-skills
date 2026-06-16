---
type: example
title: 前缀树解码算法实例
article_id: "8802"
article: [[spaces-8802-Seq2Seq-前缀树-检索任务新范式-以KgCLUE为例]]
section: 前缀解码
claim: 利用前缀树在解码时将不合规Token概率置零以限制输出处于合法库中
notation_mapping:
  Trie(Prefix): Trie(Prefix)
steps:
  - 步骤1：对目标数据库中的合法短句集合构建前缀树嵌套字典结构。
  - 步骤2：模型自回归生成下一个字符时，使用当前已生成的 Prefix 字符串查询前缀树字典。
  - 步骤3：过滤出合法的后继单字列表，将当前预测中所有不属于此列表的 Token 的 Logits 覆写为负无穷。
  - 步骤4：对 Logits 计算 Softmax 获得受限概率分布，采样输出下一步 Token 并继续，确保路径连通直至结束。
used_concepts:
  - [[前缀树约束解码]]
source_span: ev::8802::前缀树解码
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-12-17-Seq2Seq-前缀树-检索任务新范式-以KgCLUE为例.md
source_ids:
  - "8802"
status: stable
updated: 2026-06-12
---

# 前缀树解码算法实例

本实例展示了在 KgCLUE 知识问答任务中利用前缀树（Trie）规范生成三元组的过程。

假定知识库中包含“明天会更好”和“明年见”两句话，前缀树首字分支为 `明`。解码第一步，前缀树限制候选首字只能为 `明` 或 `今` 等合法字，预测概率中其他不相干字被强设为零；若采样首字为 `明`，则第二步查询前缀树得到可选的下接字符仅为 `月`、`天`、`年`，排除了其他任何不合法字符的可能。这使得解码序列必然落在树的路径内，防止了检索生成时的幻觉。
