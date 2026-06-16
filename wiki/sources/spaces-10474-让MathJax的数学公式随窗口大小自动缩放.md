---
type: article_summary
title: 让MathJax的数学公式随窗口大小自动缩放
article_id: 10474
source_url: "https://spaces.ac.cn/archives/10474"
date: 2024-10-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-10-15-让MathJax的数学公式随窗口大小自动缩放.md
series: []
topics:
  - [[Cool Papers工具生态]]
concepts: []
methods:
  - [[MathJax公式自适应窗口大小缩放方案]]
evidence_spans:
  - ev::10474::背景思路
  - ev::10474::代码参考
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-10-15-让MathJax的数学公式随窗口大小自动缩放.md
source_ids:
  - 10474
status: draft
updated: 2026-06-11
---

# 让MathJax的数学公式随窗口大小自动缩放

## 文章核心问题

如何解决MathJax数学公式在网页前端（尤其是Cool Papers论文刷读场景下）与谷歌翻译、延迟加载以及Marked Markdown解析器的冲突和缩放自适应问题？

## 主要结论

- **背景思路**: MathJax公式不支持类似图片的max-width缩放，但可以通过JS计算公式超出上级宽度的比例动态设置font-size。
- **代码参考**: 通过判断e.parentNode.className以区分行内和单行公式，动态调整其font-size以实现自适应缩放。

