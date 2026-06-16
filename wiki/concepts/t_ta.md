---
type: concept
title: T-TA (Transformer-based Text Autoencoder)
definition: T-TA（基于Transformer的文本自编码器）是一种重构自注意力连接方式的神经网络结构。它允许模型在不使用 `[MASK]` 标记的情况下，一次前向计算即能并行且不发生泄露地预测输入序列中的所有 Token。
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-07-修改Transformer结构-设计一个更快更好的MLM模型.md
source_ids:
  - "7661"
null_evidence_reason: Draft cognitive page retained for navigation; source-level evidence binding is deferred and the page must not be promoted until evidence_spans are attached.
status: draft
updated: 2026-06-12
---

# T-TA (Transformer-based Text Autoencoder)

## Definition
T-TA（基于Transformer的文本自编码器）是一种重构自注意力连接方式 of 神经网络结构。它允许模型在不使用 `[MASK]` 标记的情况下，一次前向计算即能并行且不发生泄露地预测输入序列中的所有 Token。

## Explanation
标准的Masked Language Model（MLM）为了防止信息泄露，只能mask掉15%的token，导致训练效率极低。T-TA通过改变Query、Key、Value的依赖路径解决了这一瓶颈：
- **第一层解耦**：第一层的 Query 只输入位置编码 $Q_0 = P$，去掉了词义信息。
- **对角线 Mask**：在第一层自注意力中将对角线得分设为 0，防止当前位置读取自身对应的输入。
- **共享 K, V 键值对**：为避免后续层将信息回传造成二次泄漏，规定所有 Attention 层的 $K$ 和 $V$ 均不随层进行变换，而是恒等于第一层的输入特征 $E+P$。
T-TA结构简化了特征流动，在训练中能充分利用所有token的自监督信号，大大提高了双向语言模型的预训练效率。
