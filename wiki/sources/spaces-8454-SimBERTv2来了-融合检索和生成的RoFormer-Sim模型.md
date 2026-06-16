---
type: article_summary
title: SimBERTv2来了！融合检索和生成的RoFormer-Sim模型
article_id: 8454
source_url: https://spaces.ac.cn/archives/8454
date: 2021-06-11
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md
sources: ["Data/Spaces_ac_cn/markdown/Big-Data/2021-06-11-SimBERTv2来了-融合检索和生成的RoFormer-Sim模型.md"]
source_ids: ["8454"]
status: draft
updated: 2026-06-12
---

# SimBERTv2来了！融合检索和生成的RoFormer-Sim模型

## 文章核心问题
如何对第一代 SimBERT 进行全面技术迭代，构建在通用句式（陈述句）上同样表现优异、检索与生成能力均有突破的 RoFormer-Sim（SimBERTv2）模型。

## 主要结论
推出了 RoFormer-Sim 模型。在骨干网上使用结合旋转位置编码（RoPE）的 RoFormer 结构。在训练层级引入了无监督通用相似句挖掘、BART 式输入带噪重构生成。针对“由于生成语料复杂化和噪声增大导致对比检索效果意外受损”的问题，在后处理阶段创新性地引入了相似度矩阵几何蒸馏，使得相似度打分精度基本持平或优于初代模型。

## 推导结构
1. 对比 SimBERT 与 RoFormer-Sim 结构差异，展示通用相似句对抽取方案。
2. 提出结合 BART 遮蔽噪声的相似句重构生成模式。
3. 揭示生成难度增加导致检索空间被句式特征干扰的缺陷，为此提出将原有 SimBERT 检索表示蒸馏至新模型的双向几何约束算法。
4. 汇总 STS-B、ATEC 等测试集的多 Pooling 白化性能，确认检索能力的成功恢复。

## 关键公式
- 相似度蒸馏损失：$\\mathcal{L}_{\\text{sim}} = \\frac{\\lambda}{n^2}\\sum_{i=1}^n\\sum_{j=1}^n (\\cos(u_i,u_j)-\\cos(v_i,v_j))^2$

## 体现的方法
- [[BART式带噪重构]]：在生成输入端随机 `[MASK]`，要求重构其相似句目标以强化表示鲁棒。
- [[句向量相似度几何蒸馏]]：利用均方差蒸馏 Teacher 模型句向量两两相似度几何，修复多任务冲突下的特征退化。

## 与其他文章的关系
- 继承了 [[鱼与熊掌兼得：融合检索和生成的SimBERT模型]] 的核心逻辑。
- 采用有监督蒸馏技术，后续通过 [[用开源的人工标注数据来增强RoFormer-Sim]] 进一步扩充。

## 原文证据锚点
- `ev::8454::检索蒸馏`：对应原文中为了弥补对比学习中由于生成任务加噪导致检索性能下降，进而设计余弦相似度均方误差（MSE）矩阵蒸馏损失的完整数学公式与表述。