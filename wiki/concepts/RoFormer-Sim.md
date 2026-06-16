---
type: concept
title: RoFormer-Sim
definition: SimBERTv2，以 RoFormer 为基础模型，在 UniLM 上融合了对比学习、BART 式加噪生成与检索几何蒸馏。
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md"]
source_ids: ["8454"]
aliases: ["SimBERTv2", "RoFormer-Sim-FT"]
status: stable
updated: 2026-06-12
---

# RoFormer-Sim

## 定义
RoFormer-Sim（SimBERTv2）是融合了检索和生成的多任务升级版模型。其骨干网升级为携带旋转位置编码（RoPE）的 RoFormer 结构。

## 主要更新
1. **句式扩展**：微调语料拓广至一般陈述句，不再局限于疑问句；
2. **生成抗噪**：输入端引入随机 `[MASK]`，并在输出端重构同义干净序列，属于困难形式的 BART 重构；
3. **检索蒸馏**：为了打破生成任务复杂度变大对对比特征造成的性能抑制，在微调尾声对输入批的句向量余弦相似度做 MSE 几何蒸馏，使检索表现不降反升。