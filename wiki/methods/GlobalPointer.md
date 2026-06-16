---
type: method
operation_types:
  primary: Rewrite / identity transform
  secondary: []
title: GlobalPointer
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-05-01-GlobalPointer-用统一的方式处理嵌套和非嵌套NER.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-05-10-Transformer升级之路-4-二维位置的旋转式位置编码.md
source_ids:
  - 8373
method_summary: "把 NER 改写为对所有连续片段的实体级多标签分类，用 query-key 片段打分和 RoPE 相对位置统一处理嵌套与非嵌套实体。"
typical_structure: |
  1. 将长度为 n 的输入序列枚举为 n(n+1)/2 个连续候选片段。
  2. 为每个实体类型生成起点向量 q 和终点向量 k。
  3. 用内积打分 s_alpha(i,j)=q_i^T k_j，并用 RoPE 注入相对位置信息。
  4. 用多标签分类损失训练，解码时输出得分超过阈值的片段。
applicability: "适用于嵌套和非嵌套命名实体识别，尤其适合实体长度和跨度多样化的场景"
examples:
  - "[[article::8373]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8373::GlobalPointer公式"
  - "ev::8373::RoPE重要性"
  - "ev::8373::实验对比"
---

# GlobalPointer

## 适用问题
需要在命名实体识别中统一处理非嵌套实体与嵌套实体，并希望训练、评估、解码都以实体片段为基本单位，而不是逐 token 标签序列。

## 核心变换
把长度为 $n$ 的文本中所有连续片段视为候选实体，将 NER 改写为每个实体类型上的 $n(n+1)/2$ 选 $k$ 多标签分类问题；用 $s_\alpha(i,j)=q_{i,\alpha}^\top k_{j,\alpha}$ 给片段打分，并用 RoPE 注入相对位置信息。

## 典型步骤
1. 编码输入序列，得到每个位置的上下文向量 $h_i$。
2. 对每个实体类型 $\alpha$ 生成起点向量 $q_{i,\alpha}$ 与终点向量 $k_{j,\alpha}$。
3. 对所有 $i \le j$ 的连续片段计算 $s_\alpha(i,j)$，作为该片段属于类型 $\alpha$ 的 logits。
4. 加入 RoPE 相对位置，使模型区分片段长度与跨度。
5. 用多标签分类损失训练，并在解码时输出所有得分大于阈值的实体片段。

## 直觉
NER 的评测对象是完整实体片段，而不是单个位置标签。GlobalPointer 直接对候选片段打分，使训练目标、解码输出和实体级 F1 更一致；RoPE 则补上跨度位置感，避免任意起止位置被错误组合。

## 边界
该方法需要枚举 $O(n^2)$ 个候选片段，空间开销随序列长度平方增长；虽然在 Transformer 场景中通常可并行承受，但超长文本仍需截断、滑窗或其他压缩策略。

## 例子
- `article::8373` 中，GlobalPointer 在人民日报非嵌套 NER 上可媲美 CRF，在 CMeEE 嵌套 NER 上优于 CRF；去掉 RoPE 时 F1 明显下降。

## 证据
- `ev::8373::GlobalPointer公式`：用 $s_\alpha(i,j)=q_{i,\alpha}^\top k_{j,\alpha}$ 作为连续片段打分。
- `ev::8373::RoPE重要性`：有无 RoPE 的 GlobalPointer F1 差距可达 30 个百分点以上。
- `ev::8373::实验对比`：非嵌套 NER 上媲美 CRF，嵌套 NER 上显著优于 CRF。
