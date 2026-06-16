---
type: article_summary
title: Transformer升级之路：12、无限外推的ReRoPE？
article_id: "9708"
source_url: https://spaces.ac.cn/archives/9708
date: 2023-08-07
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
series: [Transformer升级之路]
topics: [位置编码, 长度外推, ReRoPE, 相对位置矩阵]
concepts: [rerope, leaky-rerope]
methods: [rerope-window-extension, leaky-rerope]
problem_patterns: [长度外推, 相对位置越界, 局部性保持]
evidence_spans:
  - 9708-重温
  - 9708-融合
  - 9708-计算
  - 9708-实验
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
source_ids:
  - "9708"
status: draft
updated: 2026-06-09
---

## 文章核心问题

在NTK-RoPE-mixed已接近上限的背景下，寻找一种更大幅度的免微调长度外推方案。

## 主要结论

1. ReRoPE（Rectified RoPE）通过在窗口w内保持标准间隔、窗口外截断为常数w，实现了理论上无限的长度外推能力。
2. Leaky ReRoPE是ReRoPE的一般化——窗口外使用1/k的步长间隔进行位置内插，k取有限值。
3. 在1亿参数GAU模型上，ReRoPE-w256+log n在4096不重复测试中达49.07%，显著超过NTK-RoPE-mixed的45.41%和HFWA的48.15%。
4. 在LLAMA2-13b上，ReRoPE实现了"longer context, lower loss"的理想特性（4096→8192→16384，loss持续下降）。
5. 主要代价：需计算两次Attention矩阵，不兼容Flash Attention。

## 推导结构

1. 回顾RoPE的相对位置矩阵及直接外推、位置内插、NTK-aware Scaled RoPE的局限
2. 提出"保近压远"思想——窗口内保持1间隔、窗口外使用更小间隔或直接截断
3. 给出Leaky ReRoPE（一般形式）和ReRoPE（k→∞极限）的相对位置矩阵
4. 讨论实现：需算两次Attention再依据条件拼接
5. 详尽实验验证

## 关键公式

ReRoPE相对位置矩阵：窗口内用原RoPE步长1，窗口外全部截断为w（eq:rerope）

Leaky ReRoPE相对位置矩阵：窗口内步长1，窗口外步长1/k（eq:leaky-rerope）

Attention矩阵合并：a_{i,j} = a^{(1)}_{i,j} (i-j<w), a^{(2)}_{i,j} (i-j≥w)

## 体现的方法

- ReRoPE窗口截断方法
- Leaky ReRoPE分段线性方法
- 两次Attention合并实现

## 所属系列位置

第12篇，在第11篇指出NTK系列已达上限后提出的全新方案。

## 与其他文章的关系

- 前驱：第11篇（β进制位置编码）结论NTK-RoPE已达上限
- 后续：第13篇讨论其逆用，第14篇讨论与HWFA结合
- ReRoPE借鉴了HFWA的实验结果作为比较基准

## 原文证据锚点

- 重温: 原文"重温"节，回顾RoPE相对位置矩阵（eq:rope）及各方法局限
- 融合: 原文"融合"节，给出Leaky ReRoPE和ReRoPE的矩阵定义（eq:leaky-rerope, eq:rerope）
- 计算: 原文"计算"节，给出两次Attention的公式及合并逻辑
- 实验: 原文"实验"节，GAU实验表格显示ReRoPE-w256+log n达85.12%（4096重复）；LLAMA2-13b实验显示loss从1.4967(4096)降至1.4001(16384)
