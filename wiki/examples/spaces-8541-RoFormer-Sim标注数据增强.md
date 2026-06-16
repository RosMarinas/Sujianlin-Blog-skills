---
type: example
title: RoFormer-Sim标注数据增强
article_id: 8541
article: 用开源的人工标注数据来增强RoFormer-Sim
section: 鱼与熊掌
claim: Sentence-BERT 拼接 [u, v, |u-v|] 特征并用于分类层微调的步骤。
steps: 1. 提取匹配句对特征 u 与 v；\n2. 计算逐维度绝对差值 |u - v|；\n3. 拼接得到综合向量 [u, v, |u-v|]；\n4. 送入全连接线性层进行相似度分类 Softmax 联合优化。
used_concepts: ["[[RoFormer-Sim]]"]
notation_mapping: {"|u-v|": "绝对语义紧邻度"}
source_span: ev::8541::特征拼接
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-07-19-用开源的人工标注数据来增强RoFormer-Sim.md"]
source_ids: ["8541"]
status: stable
updated: 2026-06-12
---

# RoFormer-Sim标注数据增强

## 演示过程
本例演示了 Sentence-BERT 特征拼接结构如何对有标签数据进行解耦分类微调。

设共享编码器输出两句子的表示向量 $\boldsymbol{u}, \boldsymbol{v} \in \mathbb{R}^d$。
1. 计算逐维度差值绝对值：
   $$
   \boldsymbol{d} = |\boldsymbol{u} - \boldsymbol{v}|
   $$
2. 拼接为综合向量：
   $$
   \boldsymbol{h} = [\boldsymbol{u}, \boldsymbol{v}, \boldsymbol{d}] \in \mathbb{R}^{3d}
   $$
3. 计算三分类概率（相似、不相似、中立）：
   $$
   \boldsymbol{p} = \text{Softmax}(\boldsymbol{h}\boldsymbol{W} + \boldsymbol{b})
   $$
4. 优化交叉熵损失，解耦了主题相关度与语义相似度。