---
type: concept
definition: 一种直接优化余弦相似度的有监督句向量损失函数。核心为排序损失，只依赖句子对相似度的相对顺序，与Spearman系数评价指标一致。
aliases:
- Cosine Sentence
status: draft
updated: '2026-06-12'
title: CoSENT
source_ids:
- '8847'
- '9341'
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2022-01-06-CoSENT-一-比Sentence-BERT更有效的句向量方案.md
- Data/Spaces_ac_cn/markdown/Big-Data/2022-11-09-CoSENT-三-作为交互式相似度的损失函数.md
evidence_spans:
- ev::8847::CoSENT损失函数
---


# CoSENT

## 定义

CoSENT（Cosine Sentence）是一种有监督句向量训练方案，核心是直接优化句子对余弦相似度的相对顺序。源文 `8847` 指出，它比 InferSent 和 Sentence-BERT 更贴近预测阶段的余弦检索目标，并且训练只需要句子对样本。

## 损失函数

```tex
\log \left(1 + \sum_{\text{sim}(i,j)>\text{sim}(k,l)}
e^{\lambda(\cos(u_k,u_l)-\cos(u_i,u_j))}\right)
```

这里 $u_i,u_j,u_k,u_l$ 是句向量，$\lambda>0$ 是超参数。只要样本对 $(i,j)$ 的真实相似度应大于 $(k,l)$，就加入一项指数惩罚；因此它依赖标签顺序，而不依赖具体相似度数值。源文明确把这一点与 Spearman 系数联系起来，因为 Spearman 也只关心预测结果的相对顺序。

## 激活场景

CoSENT 适用于可以为句子对设计相似度顺序的监督数据，例如正负样本对、NLI 的蕴含/中立/矛盾顺序，或 STS-B 这类打分数据。若多类别之间没有序关系，源文提醒不能直接使用 CoSENT。系列第三篇还说明，把余弦函数替换为任意标量输出 $f(i,j)$ 后，CoSENT 可以作为交互式相似度模型的排序损失。

## 证据

- `ev::8847::CoSENT损失函数`
