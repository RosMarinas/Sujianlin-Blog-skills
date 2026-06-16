---
type: example
title: spaces-9617-NBCE多段文档问答实例
article_id: 9617
article: |
  [spaces-9617-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度](wiki/sources/spaces-9617-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md)
section: 参考实现
claim: NBCE能实现无需微调、在7B模型上一次性输入万字长文本并正确回答多个问题
notation_mapping:
  contexts: 12 segmented news paragraphs
  questions: 8 reading comprehension questions
steps:
  - 准备 12 段相对独立的随机新闻文本段落，总字数约为 9000 多字，并设计 8 个针对这些段落的问题。
  - 选用一个预训练长度仅为 2048 字符的 OpenBuddy-7B 大模型，将该大模型与 NBCE 概率解算器结合，而不对参数进行任何微调。
  - 在每个生成步中，将 12 段上下文分别与已生成的 token 拼接，放入同一 batch 内并行计算转移概率。
  - 利用“最小熵 Pooling”从 12 个条件分布中筛选出当前不确定性最低的分布，并减去无 Context 预测，完成 Top-P 过滤后进行 Token 采样。
  - 模型能够以极高的流畅度，按顺序逐一准确无误地回答出全部 8 个问题，输入输出总字数超过 10000 字符，表现出超越预训练窗口的强大扩展性。
used_concepts:
  - [NBCE](wiki/concepts/NBCE.md)
source_span: ev::9617::nbce_demo
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-23-NBCE-使用朴素贝叶斯扩展LLM的Context处理长度.md
source_ids:
  - 9617
status: draft
updated: 2026-06-12
---

# spaces-9617-NBCE多段文档问答实例

## Claim
NBCE能实现无需微调、在7B模型上一次性输入万字长文本并正确回答多个问题

## Section
参考实现

## Notation Mapping
- $contexts$: 12 segmented news paragraphs
- $questions$: 8 reading comprehension questions

## Steps
1. 准备 12 段相对独立的随机新闻文本段落，总字数约为 9000 多字，并设计 8 个针对这些段落的问题。
2. 选用一个预训练长度仅为 2048 字符的 OpenBuddy-7B 大模型，将该大模型与 NBCE 概率解算器结合，而不对参数进行任何微调。
3. 在每个生成步中，将 12 段上下文分别与已生成的 token 拼接，放入同一 batch 内并行计算转移概率。
4. 利用“最小熵 Pooling”从 12 个条件分布中筛选出当前不确定性最低的分布，并减去无 Context 预测，完成 Top-P 过滤后进行 Token 采样。
5. 模型能够以极高的流畅度，按顺序逐一准确无误地回答出全部 8 个问题，输入输出总字数超过 10000 字符，表现出超越预训练窗口的强大扩展性。