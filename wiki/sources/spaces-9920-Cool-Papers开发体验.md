---
type: article_summary
title: 新年快乐！记录一下 Cool Papers 的开发体验
article_id: "9920"
source_url: https://spaces.ac.cn/archives/9920
date: 2024-01-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2024-01-01-新年快乐-记录一下-Cool-Papers-的开发体验.md
source_html: null
series: []
topics:
  - "[[Cool Papers工具生态]]"
concepts:
  - "[[LLM辅助开发]]"
  - "[[多优先级队列]]"
  - "[[Bottle框架]]"
  - "[[Atom订阅]]"
methods:
  - "[[用多优先级队列管理爬取和对话任务]]"
problem_patterns: []
evidence_spans:
  - ev::9920::大模型赋能
  - ev::9920::技术栈选型
  - ev::9920::队列设计
  - ev::9920::更新汇总
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-01-新年快乐-记录一下-Cool-Papers-的开发体验.md
source_ids:
  - "9920"
status: draft
updated: 2026-06-10
---

## 文章核心问题

Cool Papers网站开发过程中遇到的技术挑战（LLM辅助开发、前后端选型、队列设计）以及作者的个人开发体验反思。

## 主要结论

1. 大模型（GPT4、Kimi）极大降低了建站门槛，使非专业开发者也能完成全栈开发。
2. 网站后端采用Python+Bottle轻量框架，前端是作者"艺术细胞不足"下的勉强之作。
3. 所有网络通信（Arxiv爬取、PDF下载、Kimi对话）需通过有稳定间隔的队列完成，三部分队列需独立设计防相互拖累。
4. 队列中的进程必须加入值守功能，中断后自动重建。

## 推导结构

技术挑战（LLM解决"技术"问题）→ 艺术瓶颈（无法解决"美学"问题）→ 后端设计（队列为核心架构）→ 更新汇总（发布后的改进清单）。

## 关键公式

无定量公式。

## 体现的方法

- **用多优先级队列管理爬取和对话任务**：Arxiv论文列表获取、PDF下载、Kimi对话三个队列独立运行，防止互相阻塞。

## 所属系列位置

Cool Papers系列的首篇开发总结。后续文章包括Chrome扩展（9978）、站内搜索（10088）、搜索增强（10311）、扩展升级（10480）、Zotero适配（11250）等。

## 与其他文章的关系

- 被[[spaces-9938-Python重试代码更加优雅]]引用作为重试需求的背景。
- 被[[spaces-9978-Chrome重定向扩展]]引用作为Cool Papers开发基础。
- 被[[spaces-10088-站内检索系统]]引用作为前端能力限制的说明。

## 原文证据锚点

- `ev::9920::大模型赋能`：GPT4和Kimi在开发中的角色，几乎全部源码在其辅助下完成。
- `ev::9920::技术栈选型`：Python+Bottle后端，前端HTML+CSS+JS。
- `ev::9920::队列设计`：三部分网络通信需独立队列，进程需值守和自动重建。
- `ev::9920::更新汇总`：发布后增加的类别开放、Feed订阅、Markdown解析、点击次数等改进。
