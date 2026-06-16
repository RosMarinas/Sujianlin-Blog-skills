---
type: example
title: SimBERT掩码自回归
article_id: 7427
article: 鱼与熊掌兼得：融合检索和生成的SimBERT模型
section: SimBERT
claim: 利用注意力掩码实现Context双向编码与Target单向自回归生成的步骤。
steps: 1. 构建输入序列 [CLS] Context [SEP] Target [SEP]；\n2. 构建注意力掩码矩阵，使前 $L_1$ 个 token 互相可见，后 $L_2$ 个 token 仅可见 Context 及自身历史；\n3. 将输入序列与掩码矩阵送入 Transformer；\n4. 在 Target 序列的各位置上预测下一个 token 并计算交叉熵损失。
used_concepts: ["[[UniLM]]", "[[SimBERT]]"]
notation_mapping: {"Context": "输入文本问句", "Target": "相似生成目标"}
source_span: ev::7427::检索部分
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2020-05-18-鱼与熊掌兼得-融合检索和生成的SimBERT模型.md"]
source_ids: ["7427"]
status: stable
updated: 2026-06-12
---

# SimBERT掩码自回归

## 演示过程
本例演示了 SimBERT 模型的注意力掩码自回归生成过程。

假定输入为：`[CLS] 我喜欢看电影 [SEP] 我爱看电影 [SEP]`。
Context 长度为 $L_1 = 8$，Target 长度为 $L_2 = 7$。

1. 构建注意力掩码 $M \in \mathbb{R}^{(L_1+L_2) \times (L_1+L_2)}$：
   - 对于前 $L_1$ 行，前 $L_1$ 列元素为 0，其余为 $-\infty$；
   - 对于后 $L_2$ 行，前 $L_1$ 列为 0，后 $L_2$ 列仅下三角区域（含对角线）为 0，其余为 $-\infty$。

2. Transformer 内部进行 Self-Attention 计算：
   $$
   \text{Attention}(\boldsymbol{Q}, \boldsymbol{K}, \boldsymbol{V}) = \text{Softmax}\left(\frac{\boldsymbol{Q}\boldsymbol{K}^{\top}}{\sqrt{d}} + \boldsymbol{M}\right)\boldsymbol{V}
   $$

3. 在 Target 序列中，利用前向输出的表征计算交叉熵损失，拟合相似问句的生成概率。