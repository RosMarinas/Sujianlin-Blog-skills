---
type: concept
definition: RoPE-Tie（RoPE for Text-image）是一种结合RoPE-1D和RoPE-2D的图文混合位置编码方案。它给文本token分配(n,n)的二维坐标（退化为RoPE-1D），给图片patch分配传统的(x,y)二维坐标（RoPE-2D），通过缩放因子保证文本与图片间的对称性。
title: RoPE-Tie (Text-Image RoPE)
status: draft
created: '2026-06-09'
tags:
- 多模态
- RoPE-2D
- 图文混合
- 位置编码
related_articles:
- 10040
related_concepts:
- rotary-position-embedding
- 2d-rope
evidence_spans:
- 10040-合二为一
- 10040-延伸思考
updated: '2026-06-12'
source_ids:
- （待从源文章提取）
sources:
- （待从源文章提取）
---


## 核心定义

RoPE-Tie（RoPE for Text-image）是一种结合RoPE-1D和RoPE-2D的图文混合位置编码方案。它给文本token分配(n,n)的二维坐标（退化为RoPE-1D），给图片patch分配传统的(x,y)二维坐标（RoPE-2D），通过缩放因子保证文本与图片间的对称性。

## 关键设计

1. **文本位置**：文本token n的位置编码为(n,n)，即两个维度共享相同的位置标号——这等价于标准RoPE-1D。
2. **图片位置**：图片patch使用标准的RoPE-2D坐标(x,y)。
3. **缩放因子**：对于w×h的图片patch网格，缩放因子s=w+1, t=h+1保证图片前后的句子对称衔接。
4. **Special Token**：使用[IMG]、[/IMG]标记图片边界，避免图片直接相邻。

## 数学形式

对于w×h的图片位于位置L的文本之后：
- 图片第(i,j)个patch的位置：(L + i*s, L + j*t)，其中s=w+1, t=h+1
- 图片后第一个文本token的位置：(L + (w+1)(h+1), L + (w+1)(h+1))

## 优缺点

- 优点：直观模拟排版；保持图片位置的二维性；纯文本可退化为标准RoPE-1D，兼容预训练文本LLM。
- 缺点：
  - 复杂度较高，有"雕花"嫌疑
  - 图片等价于(w+1)(h+1)-1个token的数字不够自然
  - 实践中直接展平使用RoPE-1D可能同样有效

## 出现位置

- [第17篇](/archives/10040) "合二为一"和"延伸思考"节

## 原文证据

- 原文10040"合二为一"节：提出RoPE-Tie的核心设计——文本(n,n)退化为RoPE-1D，图片RoPE-2D加缩放
- 原文10040"延伸思考"节：讨论非整数位置、special token的使用等细节
- 原文10040"文章小结"节：总结"通过RoPE-2D支持图片的二维位置指标，通过适当约束使纯文本能退化为RoPE-1D"