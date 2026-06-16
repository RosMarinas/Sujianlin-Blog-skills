---
type: article_summary
title: 更便捷的Cool Papers打开方式：Chrome重定向扩展
article_id: "9978"
source_url: https://spaces.ac.cn/archives/9978
date: 2024-02-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-02-02-更便捷的Cool-Papers打开方式-Chrome重定向扩展.md
source_html: null
series: []
topics:
  - "[[Cool Papers工具生态]]"
  - "[[浏览器扩展开发]]"
concepts:
  - "[[Chrome扩展]]"
  - "[[重定向机制]]"
  - "[[多优先级队列]]"
methods:
  - "[[用重定向扩展实现曲线救国搜索]]"
problem_patterns: []
evidence_spans:
  - ev::9978::借花献佛
  - ev::9978::使用说明
  - ev::9978::放开历史
  - ev::9978::其他更新
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-02-02-更便捷的Cool-Papers打开方式-Chrome重定向扩展.md
source_ids:
  - "9978"
status: draft
updated: 2026-06-10
---

## 文章核心问题

在Cool Papers暂时无法实现完整站内搜索的情况下，如何通过Chrome重定向扩展"曲线救国"，让用户能从任意页面跳转到Cool Papers。

## 主要结论

1. 写Chrome重定向扩展（Cool Papers Redirector v0.1.0），从任意页面右键快速跳转到Cool Papers。
2. 扩展自动检测所选文字、超链接或页面路径中的论文ID，三选一检测到即跳转。
3. 放开所有历史Arxiv论文访问，采用三级优先级队列保证当天论文优先处理。
4. 扩展开发简单（HTML+JS+GPT4/Kimi辅助），但放开历史论文的压力管理是核心挑战。

## 推导结构

搜索需求分析（"做搜索不是笔者的强项"）→ 曲线救国思路（Chrome重定向）→ 使用方式（右键菜单）→ 放开历史论文压力（多优先级队列）→ 其他更新汇总。

## 关键公式

无定量公式。

## 体现的方法

- **用重定向扩展实现曲线救国搜索**：当直接实现搜索功能不可行时，通过Chrome浏览器扩展让用户借用外部搜索引擎（Google、arXiv原生搜索），再通过右键重定向到Cool Papers，绕过站内搜索的缺失。

## 所属系列位置

Cool Papers系列的一部分。前一篇文章是[[spaces-9920-Cool-Papers开发体验]]，后一篇是[[spaces-10088-站内检索系统]]。

## 与其他文章的关系

- 被[[spaces-10088-站内检索系统]]引用，指出搜索功能后续已实现。
- 被[[spaces-10480-浏览器扩展v0-2-0]]引用作为v0.2.0升级的基础版本。
- 与[[spaces-10311-站内搜索新尝试]]共同构成Cool Papers搜索/筛选功能演化线。

## 原文证据锚点

- `ev::9978::借花献佛`："借花献佛"思路——写Chrome重定向扩展绕过站内搜索缺失。
- `ev::9978::使用说明`：扩展的使用方式——右击菜单自动检测论文ID。
- `ev::9978::放开历史`：三级优先级队列设计（超级VIP > 当天论文 > 历史论文）。
- `ev::9978::其他更新`：一个月来的功能改进列表（PDF.js预览、日期选择、英文输出等）。
