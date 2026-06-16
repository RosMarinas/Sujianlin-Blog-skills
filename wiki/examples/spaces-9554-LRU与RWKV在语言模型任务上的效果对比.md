---
type: example
title: spaces-9554-LRU与RWKV在语言模型任务上的效果对比
article_id: 9554
article: |
  [spaces-9554-Google新作试图“复活”RNN-RNN能否再次辉煌](wiki/sources/spaces-9554-Google新作试图“复活”RNN-RNN能否再次辉煌.md)
section: 效果化
claim: 在语言模型任务上RNN变体的效果弱于同等量级的注意力机制模型且长程能力受限于hidden_size
notation_mapping:
  GAU: Gated Attention Unit Model
  SA: Rotary Self Attention Model
  LRU: Linear Recurrent Unit Model
  RWKV: RWKV RNN Model
steps:
  - 构建包含 GAU、SA、LRU、SLRU、RWKV 五种注意力或循环机制的 1 亿参数量级 base 版语言模型。
  - 利用 DeepNorm 初始化以及 Tiger 优化器对这五种模型在序列长度为 128 和 512 的任务上进行完全一致的数据集训练。
  - 在 128 序列长度下，测试集 Loss 的表现为：GAU > SA > RWKV > LRU > SLRU。
  - 当序列长度增加到 512 时，注意力模型（GAU、SA）的效果由于可以全局检索而明显变好，但由于RNN系列（LRU、SLRU、RWKV）的信息瓶颈受限于 hidden_size，其长程效果不增反降，拉大了与 Attention 模型的差距。
  - 实验证明 LRU 凭借复特征值优于实数 SLRU，而 RWKV 是当前最接近 SA 的 RNN，但在同等尺度下仍有明显性能差距。
used_concepts:
  - [LRU](wiki/concepts/LRU.md)
  - [SLRU](wiki/concepts/SLRU.md)
source_span: ev::9554::lm_comparison
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-03-28-Google新作试图-复活-RNN-RNN能否再次辉煌.md
source_ids:
  - 9554
status: draft
updated: 2026-06-12
---

# spaces-9554-LRU与RWKV在语言模型任务上的效果对比

## Claim
在语言模型任务上RNN变体的效果弱于同等量级的注意力机制模型且长程能力受限于hidden_size

## Section
效果化

## Notation Mapping
- $GAU$: Gated Attention Unit Model
- $SA$: Rotary Self Attention Model
- $LRU$: Linear Recurrent Unit Model
- $RWKV$: RWKV RNN Model

## Steps
1. 构建包含 GAU、SA、LRU、SLRU、RWKV 五种注意力或循环机制的 1 亿参数量级 base 版语言模型。
2. 利用 DeepNorm 初始化以及 Tiger 优化器对这五种模型在序列长度为 128 和 512 的任务上进行完全一致的数据集训练。
3. 在 128 序列长度下，测试集 Loss 的表现为：GAU > SA > RWKV > LRU > SLRU。
4. 当序列长度增加到 512 时，注意力模型（GAU、SA）的效果由于可以全局检索而明显变好，但由于RNN系列（LRU、SLRU、RWKV）的信息瓶颈受限于 hidden_size，其长程效果不增反降，拉大了与 Attention 模型的差距。
5. 实验证明 LRU 凭借复特征值优于实数 SLRU，而 RWKV 是当前最接近 SA 的 RNN，但在同等尺度下仍有明显性能差距。