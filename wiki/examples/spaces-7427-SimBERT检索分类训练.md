---
type: example
title: SimBERT检索分类训练
article_id: 7427
article: 鱼与熊掌兼得：融合检索和生成的SimBERT模型
section: SimBERT
claim: 基于Batch内负采样的检索相似度分类Softmax训练步骤。
steps: 1. 提取 Batch 中各相似问对的首个 token [CLS] 向量作为表征；\n2. 对表示矩阵进行 L2 归一化；\n3. 计算内积矩阵，并乘以温度系数（Scale=30）；\n4. 将对角线位置作为多分类交叉熵的目标类别进行优化。
used_concepts: ["[[SimBERT]]"]
notation_mapping: {"Scale": "预测相似度放大系数"}
source_span: ev::7427::检索部分
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md"]
source_ids: ["7427"]
status: stable
updated: 2026-06-12
---

# SimBERT检索分类训练

## 演示过程
本例演示 SimBERT 模型如何通过 Batch 内多分类 Softmax 实现特征式检索优化。

对于包含 $N$ 个相似句对的 Batch，提取归一化的 `[CLS]` 向量矩阵 $\tilde{\boldsymbol{V}} \in \mathbb{R}^{N \times d}$：

1. 计算相似度矩阵：
   $$
   \boldsymbol{S} = 30 \times \tilde{\boldsymbol{V}}\tilde{\boldsymbol{V}}^{\top}
   $$
2. 由于第 $i$ 行代表第 $i$ 个句子与 Batch 内所有句子的内积，其自身与相似配对句的打分应为对角线最高值。
3. 对对角线设置掩码，执行交叉熵分类：
   $$
   \mathcal{L} = -\sum_{i} \log \frac{e^{\boldsymbol{S}_{i, i+1}}}{\sum_{j} e^{\boldsymbol{S}_{i, j}}}
   $$