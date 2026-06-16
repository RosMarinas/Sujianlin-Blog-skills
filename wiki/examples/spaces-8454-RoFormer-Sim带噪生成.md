---
type: example
title: RoFormer-Sim带噪生成
article_id: 8454
article: SimBERTv2来了！融合检索和生成的RoFormer-Sim模型
section: 生成
claim: 在生成输入端随机遮蔽相似句并要求重构干净文本的计算步骤。
steps: 1. 读入问句对 (A, B)；\n2. 随机选取 A 的 15% token 替换为 [MASK]，得到带噪 A'；\n3. 构建掩码自回归注意力；\n4. 将带噪 A' 和 B 拼接送入 RoFormer 并在 B 的生成端计算交叉熵重构损失。
used_concepts: ["[[RoFormer-Sim]]"]
notation_mapping: {"[MASK]": "随机遮蔽占位符"}
source_span: ev::8454::检索蒸馏
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md"]
source_ids: ["8454"]
status: stable
updated: 2026-06-12
---

# RoFormer-Sim带噪生成

## 演示过程
本例演示了 RoFormer-Sim 模型的输入加噪与 Seq2Seq 重构生成过程。

1. 设输入同义句对为：
   - 句子 A: `今天天气真好`
   - 句子 B: `今日气候宜人`
2. 对 A 进行 15% 随机遮蔽，生成 A': `今天[MASK]真好`。
3. 拼接序列：`[CLS] 今天[MASK]真好 [SEP] 今日气候宜人 [SEP]`。
4. 模型在 `[SEP]` 之后执行自回归解码，逐步预测 `今`、`日`、`气`、`候`、`宜`、`人`，最大化生成干净句子 B 的概率。这促使 Context 编码器在 `[MASK]` 存在时仍能抽取核心句式向量。