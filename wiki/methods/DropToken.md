---
type: method
operation_types:
  primary: Construct auxiliary sequence
  secondary: []
title: DropToken 正则化
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-11-29-Dropout视角下的MLM和MAE-一些新的启发.md
source_ids:
  - 8770
method_summary: "从 MAE 的 Dropout 视角出发，在训练时随机删除部分 token 但保留剩余 token 原始位置，用更短序列实现正则化和加速。"
typical_structure: |
  1. 在每次训练前向传播时，设定一个丢弃比例 p (如 0.1~0.15)。
  2. 随机选中输入序列中 p 比例的 Token 位置进行丢弃。
  3. 将被丢弃的 Token 从序列中移除（或将对应的 Attention 列置零）。
  4. 关键：必须保留剩余 Token 的原始绝对位置编码（Position Embedding）。
  5. 将缩短后的序列输入 Transformer 进行处理。
  6. 在预测/微调阶段（测试时），不再进行丢弃，所有 Token 输入模型。
applicability: "在 Transformer 模型的训练或微调阶段，当模型遇到过拟合问题，且希望在施加正则化的同时还能加快训练速度（由于缩短了实际序列长度）时。"
examples:
  - "[[article::8770]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8770::在训练阶段，我们可以随机扔掉一些token，但要保持剩余token的原始位置，我们暂且称之为“DropToken”...DropToken由于显式了缩短了序列长度，是可以提高训练速度的"
---

# DropToken 正则化

## 适用问题
如何为 Transformer 等长序列模型提供一种防止过拟合的正则化手段，且不像常规 Dropout 那样仅仅带来计算开销，而是能够实质性地减少输入长度，从而加快训练速度？

## 核心变换
将全序列的完全特征输入转化为“位置对齐的不完整特征输入”。这等效于在 Self-Attention 矩阵上施加了一种特殊的列掩码（即被丢弃 token 所在的那一列强制置 0）。

## 典型步骤
1. 在数据预处理或前向传播之初，设定丢弃比例 `drop_ratio`（最佳范围约在 0.1 到 0.15 之间）。
2. 从输入序列中随机选取 `drop_ratio` 比例的 Token 位置。
3. 从序列中删除这些被选中的 Token。
4. 在分配位置编码时，绝对位置编码必须对应 Token 在**原始序列**中的真实位置，不能因前方 Token 被丢弃而前移。
5. 将这个更短、但不连续的序列送入 Transformer 层训练。
6. 推理时，不丢弃任何 Token，恢复正常预测过程。

## 直觉
由于 Transformer 是一个完全无序的集合计算模型，其顺序仅由位置编码提供。当我们随机丢弃掉几个词，但保留剩余词的原始位置编码时，这就好比我们给人看一段缺字漏词但排版不变的文章。模型不仅不能依赖某个特定的上下文线索，还必须利用残缺的全局信息进行推断。此外，这实际上可以看作是 MAE (Masked Autoencoder) 模型的一个特例视角，它在微调时关闭丢弃操作，理论上与预训练阶段具有良好的一致性。

## 边界
由于 DropToken 具有很强的破坏性，其效果对具体任务的依赖性较强。在部分分类任务（如 IFLYTEK）上表现出明确的正则提升，但在其他任务（如 WSC / CSL）上可能会导致性能下降。特别是不适合那些对位置或细粒度上下文信息极其敏感的任务。

## 例子
假设一句话是“今 天 天 气 真 好”，对应的位置编号是 0,1,2,3,4,5。使用 0.3 的比例丢弃了“天(1)”和“气(3)”。输入序列变成“今”、“天”、“真”、“好”，但它们带入模型的位置编码依然强制设为 0、2、4、5。

## 证据
- 8770 指出：“我们可以随机扔掉一些token，但要保持剩余token的原始位置，我们暂且称之为‘DropToken’”，以及“DropToken虽然删除了一些Token，但依然保留了剩余token的原始位置，这个实现依赖于Transformer结构本身。”
