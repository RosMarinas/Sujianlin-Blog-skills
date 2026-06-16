---
type: article_summary
title: 不成功的尝试：将多标签交叉熵推广到"n个m分类"上去
article_id: "9158"
source_url: https://spaces.ac.cn/archives/9158
date: 2022-07-15
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2022-07-15-不成功的尝试-将多标签交叉熵推广到-n个m分类-上去.md
series:
  - [[多标签分类交叉熵]]
topics:
  - [[概率分布构建]]
concepts:
  - [[多标签分类损失]]
  - [[交叉熵]]
methods:
  - [[多标签交叉熵n×m推广尝试]]
evidence_spans:
  - ev::9158::loss-1类比推广形式
  - ev::9158::loss-3结果倒推形式
  - ev::9158::n×m不平衡自动调节
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2022-07-15-不成功的尝试-将多标签交叉熵推广到-n个m分类-上去.md
source_ids:
  - "9158"
status: draft
updated: 2026-06-10
---

# article-9158: 不成功的尝试：将多标签交叉熵推广到"n个m分类"上去

## 文章核心问题
如何将多标签分类（$n$个2分类）的自动平衡损失函数推广到"$n$个$m$分类"场景，并保持软标签解析解的存在性？

## 主要结论
1. 直接类比推广得到损失$l = \sum_j\log(1+\sum_{i,k\neq j} t_{i,j}e^{-s_{i,j}+s_{i,k}})$，硬标签下效果尚可，但软标签下无法求出解析解。
2. 从结果倒推得到损失$l = \sum_j\log(1+\sum_i t_{i,j}e^{-s_{i,j}+\bar{s}_i})$（$\bar{s}_i=\frac{1}{m}\sum_j s_{i,j}$），理论解析解为简单Softmax，但硬标签实际表现差，无法保证目标类logits最大。
3. 两种形式在$m=2$时都能退化为多标签交叉熵，但均未同时满足"自动调节类别不平衡"和"软标签解析解存在"两个理想特性。

## 推导结构
- 将多标签Softmax交叉熵做一阶截断推广到$n$个$m$分类，得loss-1
- 对loss-1求导尝试求解软标签解析解，发现方程无简单显式解
- 从结果倒推：假设解为$t_{i,j}=softmax(f(s_{i,j}))$，反推得loss-3需满足$\sum_j f(s_{i,j})$为常数
- 分析loss-3在硬标签下的缺陷：$s_{i,j}\gg\bar{s}_i$即可使损失接近0，无需$s_{i,j}$为最大值
- 讨论两种loss在$m=2$时退化为多标签交叉熵

## 关键公式
- loss-1（类比推广）：$l = \sum_j \log(1 + \sum_{i,k\neq j} t_{i,j}e^{-s_{i,j}+s_{i,k}})$
- loss-2（一般形式）：$l = \sum_j \log(1 + \sum_i t_{i,j}e^{-f(s_{i,j})})$
- loss-3（结果倒推）：$l = \sum_j \log(1 + \sum_i t_{i,j}e^{-s_{i,j}+\bar{s}_i})$，$\bar{s}_i=\frac{1}{m}\sum_j s_{i,j}$
- 理论最优解：$t_{i,j} = \frac{e^{s_{i,j}}}{\sum_j e^{s_{i,j}}}$
