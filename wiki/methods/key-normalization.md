---


type: method
operation_types:
  primary: Align / calibrate by invariance
  secondary: []
title: Key归一化长度外推方法 (KeyNorm)
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
  - Data/（待从源文章提取）
source_ids:
  - 9859
  - 9948
method_summary: KeyNorm是将Attention中Key向量的L2范数归一化为1的事前修改方法。通过消除Key向量长度带来的注意力缩放差异，使模型在长度外推时保持稳定。
typical_structure: |
  1. 在模型架构计算 Attention 权重之前，单独提取出 Key 向量序列。
  2. 对每个 Key 向量执行 L2 归一化：$k̃_j = k_j / ||k_j||$。
  3. Query 向量和 Value 向量不做改变。
  4. 对归一化后的 Key 向量进行旋转位置编码（RoPE）等正常运算。
  5. 继续后续常规的模型训练和推理步骤。
applicability: 在从零预训练的大语言模型中，希望仅通过极小的结构调整就能赋予模型自然的长文本外推能力，且不想在推理阶段引入诸如局部窗口、重叠计算等复杂修改的场景。
examples:
  - [[article::9859]]
  - [[article::9948]]
status: stable
updated: 2026-06-13
created: 2026-06-09
tags: 
related_articles: 
related_concepts: 
evidence_spans: 
  - ev::9859::提及“KNA不重复47.69% vs Baseline 23.16%”，证明其外推有效性。
  - ev::9859::提到“cos(q_i,k_j)训练不充分是长度外推失败的主因”。
---






## 适用问题
需要从零开始预训练 Transformer 或继续对模型进行长文本训练时，希望解决随着序列长度增加、Attention 发散导致模型困惑度崩溃的“长度外推”难题。并且希望方案极为轻量，在推理期完全没有额外的计算开销和特殊控制逻辑。

## 核心变换
在 Attention 中打破 Query 和 Key 在内积上的完全对称性，对 Key 强制约束为高维球面上的单位向量（**将 Key 的 L2 范数除以自身使其归一化**），而让 Query 自由承担其幅值变化的责任。

## 典型步骤
1. **获取特征**：在计算 Self-Attention 之前正常由全连接层映射得到 Query, Key, Value。
2. **强制归一**：对序列中所有的 Key 向量进行 L2 范数归一化操作，$k̃_j = k_j / ||k_j||$。
3. **位置编码**：对 Query 和新得到的单位向量 $k̃_j$ 同等地施加相对位置编码（如 RoPE）。
4. **注意力计算**：照常计算 $q_i \cdot k̃_j$，并计算后续的 Scaling、Softmax 以及与 Value 的加权和。
5. **一致部署**：该机制直接被当做原生模型结构的一部分，在预训练中学习，在推理时无差别应用，无需像 PI/ReRoPE 等那样在测试时根据目标长度动态调整参数或窗口。

## 直觉
Transformer 长度外推失败的本质原因之一是由于 $cos(q_i, k_j)$ 相关性学得不充分（距离远的词组合在短文本训练中很少见），如果此时 $q_i, k_j$ 本身由于幅值变大而导致乘积变大，Softmax 就会产生剧烈分布突变。Key 向量通常代表“词的固有身份或知识内容”。如果所有词语的名片（Key）在大小上都是等大的（即模长为1的向量），那么注意力机制判定远近和重要程度时，将纯粹依赖两者方向（余弦相似度）是否匹配，避免了某些被冷落但范数极大（“嗓门极大”）的 Key 在长文本中突然“喧宾夺主”抢走了注意力。

## 边界
这种属于“事前修改（Pre-train phase modification）”，无法作为“即插即用”的模块直接热更新到比如 LLaMA 等已经完成预训练且没有应用此修改的开源模型上，必须经过一定周期的继续训练或微调。且如果已经采用了 KeyNorm，在进一步需要突破更极端长度（如百万 token）时，如果叠加上其他的“事后”外推黑科技（如 NTK-aware、YaRN 等），其二次叠加的增益不会很显著。

## 例子
将此方法用于基准语言模型中（如 1 亿参数，训练长度 512）。将基准的普通 Attention 换为 KeyNorm Attention (KNA)，在 4096 的重复/不重复测试集上，Baseline 会衰减到近乎随机的 23.16%，而使用了 KeyNorm 的模型准确率能平稳保持在 47.69%，并且训练时长与正常模型完全一样。

## 证据
- ev::9859::展示了显著的外推增益：“KNA 不重复测试集达 47.69% （vs Baseline 23.16%）”。
- ev::9859::分析了理论机制：“cos(q_i,k_j)训练不充分是长度外推失败的主因”，而归一化缓解了该影响。
- ev::9948::系统梳理了方法论路线：“将 KeyNorm 置于事前修改路线的框架中...不需要像 PI 等那样事后动态调整”。
