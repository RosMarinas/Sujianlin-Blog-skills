---
type: method
operation_types:
  primary: "Structure-expose by factorization"
  secondary: []
title: "UniLM自回归掩码编码"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md"
source_ids:
  - "7427"
method_summary: "通过特殊 Attention Mask 让输入段内部双向可见、输出段只能单向自回归可见，使同一 Transformer 同时承担理解编码和生成解码。"
typical_structure: |
  1. 把输入句与目标句拼接为 [CLS] 输入 [SEP] 输出 [SEP]。
  2. 设置输入段内部双向 Attention。
  3. 设置输出段对历史 token 单向可见，并阻断其影响输入段编码。
  4. 用输入段 CLS 表示做检索，用输出段做 Seq2Seq 生成。
applicability: "适用于希望同一个 BERT 式模型同时支持句向量检索和相似句生成的 Seq2Seq/检索融合任务。"
examples:
  - "[[article::7427]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::7427::检索部分"
---

# UniLM自回归掩码编码

## 适用问题

适用于希望同一个 BERT 式模型同时支持句向量检索和相似句生成的 Seq2Seq/检索融合任务。

## 核心变换

拼接序列 -> 分段自回归/双向 Attention Mask -> 同时获得 NLU 句向量与 NLG 输出。

## 典型步骤

1. 把输入句与目标句拼接为 [CLS] 输入 [SEP] 输出 [SEP]。
2. 设置输入段内部双向 Attention。
3. 设置输出段对历史 token 单向可见，并阻断其影响输入段编码。
4. 用输入段 CLS 表示做检索，用输出段做 Seq2Seq 生成。

## 直觉

Mask 决定了信息流；只要输入段不看输出段，它的 CLS 就仍可作为原输入句向量，而输出段又能按自回归方式生成。

## 边界

证据来自 SimBERT 使用 UniLM 的训练结构；不覆盖所有 UniLM 预训练任务细节。

## 例子

- 7427 说明输入部分内部可做双向 Attention，输出部分只做单向 Attention，并用 CLS 向量训练检索任务。

## 证据

- `ev::7427::检索部分`
- `Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md`
- 读取章节: UniLM、SimBERT
