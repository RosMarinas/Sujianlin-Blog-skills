---
type: method
title: GlobalPointer序列标注
aliases: []
operation_types:
  primary: Decompose / reduce dimension
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-10-31-bert4keras在手-baseline我有-CLUE基准代码.md
source_ids:
  - "8739"
method_summary: 将序列标注（NER、阅读理解）中首尾位置组合视为一个整体进行分类，用一个统一的结构同时处理嵌套和非嵌套情况，训练和推理行为一致，速度比CRF更快。
typical_structure: |
  1. 编码层（BERT/RNN）输出序列表示
  2. 使用两个线性变换得到start和end表示
  3. 计算所有(start, end)组合的交叉分数
  4. 用softmax多标签分类
  5. 匈牙利算法处理重叠预测的排他性
applicability: 适用于命名实体识别（嵌套和非嵌套）和抽取式阅读理解任务。作为CRF的替代方案，速度更快且效果相当。
tools:
  - 多头跨度打分
  - 多标签分类
related_methods:
  - [[线性链CRF构建]]
  - [[T-TA结构与共享键值防泄漏法]]
examples:
  - [[article::8739]]
status: draft
updated: 2026-06-14
---

## 适用问题

序列标注任务中，嵌套实体识别（如"北京大学"中的"北京"是一个地点、"北京大学"是一个机构）需要模型能够同时预测重叠的实体边界。传统 CRF 假设标签间为线性链依赖，无法处理嵌套结构；而基于序列标注的方式（BIO/BIOS 等）需要复杂的设计来处理嵌套。GlobalPointer 将实体识别转化为首尾位置对的分类问题，统一处理嵌套与非嵌套。

## 核心变换

**输入**：序列 $X = [x_1, \dots, x_n]$，编码器输出 $H \in \mathbb{R}^{n \times d}$
**输出**：所有 $(start, end)$ 组合的分类分数 $s(start, end)$
**参数**：起始和结束的投影矩阵 $W_s, W_e \in \mathbb{R}^{d \times h}$（$h$ 为实体类型数）

$$
\text{start\_logits} = H W_s \in \mathbb{R}^{n \times h}, \quad \text{end\_logits} = H W_e \in \mathbb{R}^{n \times h}
$$

位置 $(i, j)$ 属于实体类型 $k$ 的分数：
$$
s_k(i, j) = \text{start\_logits}_{i,k} + \text{end\_logits}_{j,k}
$$

对所有 $(i, j)$ 组合使用多标签 Softmax 分类：
$$
P_k(i, j) = \frac{e^{s_k(i,j)}}{\sum_{(i',j')} e^{s_k(i',j')}}
$$

## 典型步骤

1. **编码**：使用 BERT/RNN 编码输入序列，得到 $H \in \mathbb{R}^{n \times d}$
2. **投影**：通过两个线性变换分别得到 start 和 end 的 logits
3. **组合打分**：对每个实体类型 $k$，计算所有 $(i, j)$ 组合的分数
4. **多标签分类**：对 $n^2$ 个候选组合应用 Softmax 多标签分类
5. **后处理**：使用匈牙利算法处理重叠预测的排他性（同一实体内 span 不重叠）

## 直觉

核心思想：**实体的本质是连续区间，而非逐标签序列**。

传统 BIO 标注将"实体"这一整体概念拆解为逐 token 的标签序列，再通过 CRF 的转移矩阵重建实体边界。GlobalPointer 反其道而行，直接建模实体区间 $(start, end)$。

将实体识别转化为 (start, end) 对的分类问题有两大优势：
- **天然拟合一实体多 token**：每个实体是一个完整的区间，不需要通过"B-ORG, I-ORG, I-ORG"来拼凑
- **天然处理嵌套**：区间可以完全包含另一个区间，如 (1,4) 包含 (2,3)，在多标签分类框架下可以同时预测

## 边界

- 空间复杂度 $\mathcal{O}(n^2)$，序列极长时需考虑裁剪或分块
- 对实体长度的方差敏感——极长实体（如整个段落）的 start-end 距离很大，可能需要长度归一化
- 比 CRF 更适合嵌套 NER，但在非嵌套场景下两者效果相当
- 匈牙利算法虽然保证了排他性，但可能小幅增加推理时间

## 例子

- CLUE 中文 NER 任务上，GlobalPointer 达到与 CRF 相当的效果，但推理速度更快
- 在嵌套 NER 数据集上（如 ACE 2005），GlobalPointer 天然支持嵌套而无需额外设计
- 抽取式阅读理解同样可建模为 (start, end) 预测

## 证据

- ev::8739::GlobalPointer 公式：start_logits + end_logits 的组合打分方式
- ev::8739::多标签 Softmax 处理嵌套实体的方法
- ev::8739::在 CLUE 基准上的效果和速度对比
