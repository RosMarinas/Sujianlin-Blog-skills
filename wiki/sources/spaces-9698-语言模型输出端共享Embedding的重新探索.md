---
type: article_summary
title: 语言模型输出端共享Embedding的重新探索
article_id: "9698"
source_url: https://spaces.ac.cn/archives/9698
date: 2023-07-20
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2023-07-20-语言模型输出端共享Embedding的重新探索.md
series:
  - [[信息论工具]]
topics:
  - [[Transformer架构]]
  - [[信息论基础]]
concepts:
  - [[共享Embedding]]
  - [[Embedding输出头稳定性]]
  - [[JL引理]]
methods:

evidence_spans:
  - ev::9698::共享Embedding初始损失分析
  - ev::9698::初始化对策
  - ev::9698::随机投影解耦嵌入
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-07-20-语言模型输出端共享Embedding的重新探索.md
source_ids:
  - "9698"
status: draft
updated: 2026-06-10
---

# article-9698: 语言模型输出端共享Embedding的重新探索

## 文章核心问题
语言模型中共享Embedding权重（Tied Embeddings）为何会导致初始损失过大？如何有效初始化和参数化以缓解该问题？

## 主要结论
1. 共享Embedding导致初始损失过大的原因：残差分支初始近似恒等，输入token $i$的Embedding与自身内积$e^{\boldsymbol{w}_i\cdot\boldsymbol{w}_i/\sigma}=e^{d\sigma}$占主导，初始损失约为$d\sigma$量级，远超均匀分布的$\log n$。
2. 调整初始化标准差为$\sigma=(\log n)/d$可使初始损失降至$\log n$级别，但该方法收敛速度最慢。
3. 更有效的方案：在Normalization后接正交初始化的随机投影层（如BERT的做法），或通过维度打乱（如将向量对半拼接错位）破坏$\boldsymbol{w}_i$与自身的相关性。

## 推导结构
- 建立初始阶段模型近似恒等映射的假设（残差分支接近零）
- 推导共享Embedding下的初始条件概率$p(j|i) = e^{\boldsymbol{w}_i\cdot\boldsymbol{w}_j/\sigma}/\sum_k e^{\boldsymbol{w}_i\cdot\boldsymbol{w}_k/\sigma}$
- 用期望估计随机向量模长$\|\boldsymbol{w}\|\approx\sqrt{d}\sigma$和内积$\boldsymbol{w}_i\cdot\boldsymbol{w}_j\approx0$
- 得到初始损失估计$\log(e^{d\sigma}+(n-1))$，分析其远超$\log n$的原因
- 提出对策：调整初始化（$\sigma=(\log n)/d$）、正交投影层解耦、维度打乱操作

## 关键公式
- 初始条件概率：$p(j|i) = \frac{e^{\boldsymbol{w}_i\cdot\boldsymbol{w}_j/\sigma}}{\sum_k e^{\boldsymbol{w}_i\cdot\boldsymbol{w}_k/\sigma}}$
- 初始损失估计：$-\log p(j|i) \approx \log(e^{d\sigma} + (n-1))$
- 调整后的初始化标准差：$\sigma = (\log n)/d$
- 随机投影等价性质：$(\boldsymbol{w}_i\boldsymbol{P})\cdot\boldsymbol{w}_j \approx 0$（$\boldsymbol{P}$为正交随机矩阵）
