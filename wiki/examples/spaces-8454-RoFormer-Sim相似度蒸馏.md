---
type: example
title: RoFormer-Sim相似度蒸馏
article_id: 8454
article: SimBERTv2来了！融合检索和生成的RoFormer-Sim模型
section: 检索
claim: 计算并优化Student与Teacher余弦相似度矩阵均方误差的蒸馏步骤。
steps: 1. 提取 Batch 的文本分别送入新旧模型的 Encoder 得到表示；\n2. 计算新旧模型的余弦相似度矩阵 M_S 与 M_T；\n3. 计算两矩阵的均方误差损失 ||M_S - M_T||^2；\n4. 反向传播该几何距离对齐损失以更新 Student 模型。
used_concepts: ["[[RoFormer-Sim]]", "[[SimBERT]]"]
notation_mapping: {"M_T": "教师模型相似度矩阵", "M_S": "学生模型相似度矩阵"}
source_span: ev::8454::检索蒸馏
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md"]
source_ids: ["8454"]
status: stable
updated: 2026-06-12
---

# RoFormer-Sim相似度蒸馏

## 演示过程
本例演示了 RoFormer-Sim 检索蒸馏中对余弦几何距离进行均方误差对齐计算的过程。

对于大小为 $N$ 的 batch，教师模型 SimBERT 与学生模型 RoFormer-Sim 分别提取句向量集。
1. 计算相似度矩阵：
   $$
   \boldsymbol{A}_{ij} = \cos(\boldsymbol{u}_i, \boldsymbol{u}_j), \quad \boldsymbol{B}_{ij} = \cos(\boldsymbol{v}_i, \boldsymbol{v}_j)
   $$
2. 构建对齐损失：
   $$
   \mathcal{L}_{\text{sim}} = \frac{\lambda}{N^2} \sum_{i,j} (\boldsymbol{A}_{ij} - \boldsymbol{B}_{ij})^2
   $$
3. 联合优化自回归损失与该蒸馏损失，保留了特征检索维度的相对几何。