---
type: article_summary
title: Monarch矩阵：计算高效的稀疏型矩阵分解
article_id: "10249"
source_url: https://spaces.ac.cn/archives/10249
date: 2024-07-24
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-07-24-Monarch矩阵-计算高效的稀疏型矩阵分解.md
source_html: null
series: []
topics:
  - "[[矩阵计算]]"
concepts:
  - "[[Monarch矩阵]]"
  - "[[置换矩阵]]"
  - "[[分块对角矩阵]]"
  - "[[Butterfly矩阵]]"
  - "[[奇异值分解(SVD)]]"
  - "[[Eckart-Young-Mirsky定理]]"
methods:
  - "[[用Monarch分解实现结构化矩阵近似]]"
  - "[[用高维数组变换推导矩阵恒等式]]"
problem_patterns: []
evidence_spans:
  - ev::10249::SVD回顾
  - ev::10249::Monarch矩阵
  - ev::10249::Monarch分解
  - ev::10249::Monarch推广
  - ev::10249::蝶之帝王
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-07-24-Monarch矩阵-计算高效的稀疏型矩阵分解.md
source_ids:
  - "10249"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何构造一种兼具计算高效和表达能力的稀疏结构化矩阵分解——Monarch矩阵，作为低秩分解（SVD）的稀疏化替代方案。

## 主要结论

1. Monarch矩阵定义为$M=PLPR$，其中$P$是置换矩阵（reshape-transpose-reshape），$L,R$是分块对角矩阵。当$n=m^2$时，自由参数仅约$2n^{1.5}$个。
2. 矩阵-向量乘法复杂度$O(n^{1.5})$，求逆复杂度$O(n^2)$，均低于标准$O(n^2)$/$O(n^3)$。
3. Monarch分解可通过恒等式$M_{i,j,k,l}=L_{j,i,k}R_{k,j,l}$转化为$m^2$个秩-1近似问题，总复杂度$O(n^{2.5})$。
4. Monarch矩阵可推广到非平方阶（$\mathcal{M}^{(b,n)}$参数族），且严格包含Butterfly矩阵（$n>512$时）。
5. 可用于全连接层替换、事后模型压缩、PEFT微调等场景。

## 推导结构

SVD回顾（低秩近似和Eckart-Young-Mirsky定理）→ Monarch矩阵（三要素：置换矩阵P、分块对角L,R、计算效率分析）→ Monarch分解（转化为高维数组、推导恒等式$M_{i,j,k,l}=L_{j,i,k}R_{k,j,l}$、SVD求解）→ Monarch推广（非平方阶$\mathcal{M}^{(b,n)}$、灵活形式）→ 应用例子（全连接层替换、事后处理、PEFT）→ 蝶之帝王（与Butterfly矩阵的关系）。

## 关键公式

- Monarch矩阵形式：$M=PLPR$，$P$为置换矩阵（$P^2=I$）
- 高维表示恒等式：$M_{i,j,k,l}=L_{j,i,k}R_{k,j,l}$（固定$(j,k)$时退化为外积）
- Monarch分解算法：通过$4d\to 2d$变换+SVD求解$L,R$
- 一般Monarch矩阵：$\mathcal{M}^{(b,n)}=\{P_{(b,n/b)}LP_{(n/b,b)}R | L\in\mathcal{BD}^{(n/b,n)}, R\in\mathcal{BD}^{(b,n)}\}$

## 体现的方法

- **用Monarch分解实现结构化矩阵近似**：通过置换+P分块对角矩阵的乘积结构构造稀疏矩阵分解，将通用矩阵近似转化为子矩阵秩-1近似问题。
- **用高维数组变换推导矩阵恒等式**：将二维矩阵重新解释为四维数组，利用高维下标简化置换和分块结构的关系，得到简洁的分解恒等式。

## 所属系列位置

独立文章，是结构化矩阵领域的系统性介绍。

## 与其他文章的关系

- 与[[series::低秩近似之路]]系列互补（低秩vs稀疏两条路线）。
- Monarch矩阵的求逆和乘法运算与[[spaces-11072-对角-低秩-三角阵的高效求逆方法]]中结构化矩阵加速思路相通。
- 在LLM加速和PEFT方面有潜在应用价值。

## 原文证据锚点

- `ev::10249::SVD回顾`：SVD低秩近似和Eckart-Young-Mirsky定理回顾。
- `ev::10249::Monarch矩阵`：Monarch矩阵$M=PLPR$的定义、置换矩阵$P$和分块对角$L,R$的说明、计算效率分析。
- `ev::10249::Monarch分解`：通过高维数组变换推导恒等式$M_{i,j,k,l}=L_{j,i,k}R_{k,j,l}$，Monarch分解算法和代码实现。
- `ev::10249::Monarch推广`：$\mathcal{M}^{(b,n)}$推广到非平方阶，灵活形式。
- `ev::10249::蝶之帝王`：与Butterfly矩阵的关系，Monarch严格覆盖Butterfly。
