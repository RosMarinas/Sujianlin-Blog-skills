---
type: article_summary
title: 让MathJax更好地兼容谷歌翻译和延时加载
article_id: 10320
source_url: "https://spaces.ac.cn/archives/10320"
date: 2024-08-15
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-08-15-让MathJax更好地兼容谷歌翻译和延时加载.md
series: []
topics:
  - [[Cool Papers工具生态]]
concepts: []
methods:
  - [[MathJax翻译与延时加载兼容方法]]
evidence_spans:
  - ev::10320::免翻金牌
  - ev::10320::延时加载
  - ev::10320::混合双殇
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-08-15-让MathJax更好地兼容谷歌翻译和延时加载.md
source_ids:
  - 10320
status: draft
updated: 2026-06-11
---

# 让MathJax更好地兼容谷歌翻译和延时加载

## 文章核心问题

如何解决MathJax数学公式在网页前端（尤其是Cool Papers论文刷读场景下）与谷歌翻译、延迟加载以及Marked Markdown解析器的冲突和缩放自适应问题？

## 主要结论

- **免翻金牌**: 给MathJax渲染后的公式节点加上class="notranslate"可防止谷歌翻译将其误翻译。
- **延时加载**: 在延时加载新内容后需要手动调用MathJax.Hub.Typeset()以渲染新公式。
- **混合双殇**: 当翻译与延时加载共存时，先给内容块加notranslate，等公式渲染完后再移除，可确保公式渲染后才触发翻译。

