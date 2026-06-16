---
type: method
operation_types:
  primary: Decompose / reduce dimension
  secondary: []
title: BERT-of-Theseus 模块替换压缩
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-07-17-BERT-of-Theseus-基于模块替换的模型压缩方法.md
source_ids:
  - 7575
method_summary: "将大 BERT 分块并随机用小模型对应模块替换，直接用下游任务损失训练小模块，逐步得到可独立使用的压缩模型。"
typical_structure: |
  1. 将已微调好的大模型（Predecessor）在层级上划分为与目标小模型（Successor）对应的几个模块。
  2. 固定 Predecessor 的权重参数。
  3. 在针对下游任务的训练过程中，以概率 $\varepsilon \sim U(\{0, 1\})$ 随机选择使用 Predecessor 还是 Successor 对应模块的输出送入下一层。
  4. 只使用下游任务本身的损失函数（不需要蒸馏的各种 KL loss）更新 Successor 的参数。
  5. 经过充分的混合训练后，分离出 Successor 独立进行进一步的微调，直到验证集指标收敛。
applicability: "在需要把效果好但速度慢的大模型（预训练模型）压缩为更快的小模型，并希望避免复杂的知识蒸馏目标函数设计时。"
examples:
  - "[[article::7575]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::7575::训练的时候，随机用Successor层替换掉Predecessor的对应模块，然后直接用下游任务的优化目标进行微调...训练充分后，再把整个Successor单独分离出来继续微调。"
---

# BERT-of-Theseus 模块替换压缩

## 适用问题
如何更简单、优雅地将大模型（如 6 层 BERT）压缩为小模型（如 3 层 BERT），使得小模型既具备大模型优秀的表征能力，又能避免传统知识蒸馏（Distillation）需要权衡大量不同损失函数的繁杂问题？

## 核心变换
在训练期间使用随机模块替换的混合网络结构：
$$ x^{(l)} = x_p^{(l)} \times \varepsilon^{(l)} + x_s^{(l)} \times (1 - \varepsilon^{(l)}), \quad \varepsilon^{(l)} \sim U(\{0,1\}) $$
其中 $x_p$ 为大模型模块输出，$x_s$ 为小模型模块输出。

## 典型步骤
1. 将已微调好的大模型（Predecessor）在层级上划分为与目标小模型（Successor）对应的几个模块。
2. 固定 Predecessor 的权重参数。
3. 在针对下游任务的训练过程中，以概率 $\varepsilon \sim U(\{0, 1\})$ 随机选择使用 Predecessor 还是 Successor 对应模块的输出送入下一层。
4. 只使用下游任务本身的损失函数（不需要蒸馏的各种 KL loss）更新 Successor 的参数。
5. 经过充分的混合训练后，分离出 Successor 独立进行进一步的微调，直到验证集指标收敛。

## 直觉
传统蒸馏试图通过复杂的 Loss 函数让小模型的输出去“对齐”大模型的中间层或最终输出。而“忒修斯之船”的思想是：与其费尽心思用数学公式对齐，不如在训练时直接让小模型的模块替代大模型的模块。如果在替换之后大模型仍能在下游任务中表现良好，就说明小模型的模块已经“学会”了履行大模型模块的职责。这就像一支新球队的成员轮流替换明星球队的成员上场练习，能更快地提升个人实力。

## 边界
这种方法虽然简洁并在不同模型大小压缩时有效，但实验表明：如果在结构完全一致的同模型之间应用此方法，最终 Successor 的性能并不会超越 Predecessor。这意味着它无法像某些自蒸馏技术那样进一步提升同等规模模型的性能。同时，它可能在某些需要精细模仿软标签（Soft Label）分布以提升特定泛化特性的场景下不如传统知识蒸馏精准。

## 例子
将一个 6 层的下游任务微调好的 BERT，压缩为 3 层的 BERT：将 6 层按每 2 层作为一个模块，与 3 层的每 1 层对应。每次前向传播时，对于某个模块，以 50% 的概率让数据走 6 层的大模型的 2 层，以 50% 概率走 3 层小模型的 1 层。只反向传播更新小模型的参数。训练完毕后，拿掉大模型模块，只使用这 3 层小模型。

## 证据
- 7575 提出该方法能消除中间层 loss、相关矩阵 loss 等多种蒸馏超参的设计。实验在 CLUE 的 iflytek 上证明，BERT-of-Theseus 的前 3 层能达到 59.36% 的准确率，优于直接使用原始 BERT 的前 3 层去微调的 57.96%。
