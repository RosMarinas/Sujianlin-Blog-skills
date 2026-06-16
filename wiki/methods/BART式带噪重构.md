---
type: method
title: BART式带噪重构
operation_types: {"primary": "Construct auxiliary sequence", "secondary": []}
belongs_to: topic::句向量与对比学习
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md"]
source_ids: ["8454"]
aliases: ["带噪输入重构", "BART生成加噪"]
status: stable
updated: 2026-06-12
method_summary: 在 Seq2Seq 相似句生成任务的输入端加入随机 MASK 或删除等噪点，训练模型自回归重构出完整干净的目标同义句，以强化编码表示的语义抗噪与纠错鲁棒性。
typical_structure: 1. 读入同义句对 (A, B)；\n2. 随机对输入句子 A 进行 token 级别 MASK（如 15% 概率替换为 [MASK]）；\n3. 以带噪 A 作为输入，使用注意力控制自回归解码生成完整未损坏的句子 B；\n4. 计算生成端的交叉熵损失以端到端更新网络参数。
applicability: 适用于检索与生成多任务模型中，旨在利用生成支路强化特征表示向量的语义平滑性和噪声抵抗力的训练阶段。
examples: ["[[spaces-8454-RoFormer-Sim带噪生成]]"]
evidence_spans:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md#训练方式
---

# BART式带噪重构

## 适用问题

检索与生成多任务模型需要从相似句对中学习稳定语义表示，但普通 Seq2Seq 微调容易对输入字面形式过度依赖，生成支路的鲁棒性不足。

## 核心变换

BART式带噪重构（BART-style Noisy Reconstruction）是一种通过在输入端加入人工离散噪声，并强迫模型重构干净目标以提取稳定语义表征的数据增强生成方法。

在 RoFormer-Sim (SimBERTv2) 中，为了构建一个不仅能提取句向量、还能在更广泛陈述句中生成同义句的强鲁棒系统，普通的 Seq2Seq 微调很容易让模型产生对输入的字面过度依赖。

## 典型步骤

本方法在输入端序列 $S_{\\text{in}}$ 中，以一定的比例随机选取 Token 进行如下破坏：
- 替换为特殊的 `[MASK]` 占位符；
- 随机删除某些 Token 以造成词序残缺。

模型需要在 Decoder 生成端利用注意力重构出完整的、干净的目标相似句 $S_{\\text{out}}$。这可以看作是一种序列级的去噪自编码器（Denoising Autoencoder）策略，能够有效迫使 Context 表征向量编码更多的核心语义，而非简单的字面映射，显著提升了句向量检索与生成的双重鲁棒性。

## 直觉

带噪输入让模型不能只复制表面 token，而必须从上下文中恢复语义；输出相似句而不是原句，使任务比标准 BART 去噪更贴近相似句生成。

## 边界

原文同时记录了生成改动可能降低检索模型效果，原因可能是带噪或不同句式样本降低了对比学习负样本难度；因此该方法适合增强生成支路，不能无条件承诺提升检索支路。

## 例子

- [[spaces-8454-RoFormer-Sim带噪生成]]

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md#训练`
