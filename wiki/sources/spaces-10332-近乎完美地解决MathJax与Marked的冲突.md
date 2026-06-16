---
type: article_summary
title: 近乎完美地解决MathJax与Marked的冲突
article_id: 10332
source_url: "https://spaces.ac.cn/archives/10332"
date: 2024-08-26
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-08-26-近乎完美地解决MathJax与Marked的冲突.md
series: []
topics:
  - [[Cool Papers工具生态]]
concepts: []
methods:
  - [[MathJax与Marked解析冲突解决方案]]
evidence_spans:
  - ev::10332::问题简述
  - ev::10332::逆向思路
  - ev::10332::强迫之症
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-08-26-近乎完美地解决MathJax与Marked的冲突.md
source_ids:
  - 10332
status: draft
updated: 2026-06-11
---

# 近乎完美地解决MathJax与Marked的冲突

## 文章核心问题

如何解决MathJax数学公式在网页前端（尤其是Cool Papers论文刷读场景下）与谷歌翻译、延迟加载以及Marked Markdown解析器的冲突和缩放自适应问题？

## 主要结论

- **问题简述**: Markdown与LaTeX语法冲突，导致Marked解析后破坏了LaTeX代码，MathJax渲染失败。
- **逆向思路**: 先用MathJax渲染公式以保护公式，然后用Marked渲染Markdown，可从根本上解决冲突。
- **强迫之症**: 在marked.parse前提取公式的script标签，parse后还原，再移除.MathJax类重新Typeset可恢复右键菜单并防止公式被破坏。

