---
type: article_summary
title: 一行代码将arXiv论文翻译成中文版
article_id: "11578"
source_url: https://spaces.ac.cn/archives/11578
date: 2026-01-28
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2026-01-28-一行代码将arXiv论文翻译成中文版.md
source_html: null
series: []
topics:
  - "[[AI翻译工具]]"
concepts:
  - "[[AI Agent]]"
  - "[[kimi-cli]]"
  - "[[LaTeX编译]]"
  - "[[论文翻译]]"
methods:
  - "[[用AI Agent翻译编译LaTeX论文]]"
problem_patterns: []
evidence_spans:
  - ev::11578::一行命令
  - ev::11578::AI Agent优势
  - ev::11578::效果对比
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-01-28-一行代码将arXiv论文翻译成中文版.md
source_ids:
  - "11578"
status: draft
updated: 2026-06-10
---

## 文章核心问题

如何利用AI Agent（以kimi-cli为例）实现arXiv论文的自动翻译和编译，对比传统手工规则方案。

## 主要结论

1. 一行命令即可翻译arXiv论文：使用kimi-cli加翻译prompt，AI自动分析目录结构、翻译源码、编译成PDF。
2. LaTeX翻译适合AI Agent而非人工规则，因为LaTeX语法自由度极高，"抽取-翻译"难以拆解为有限步骤（幻觉翻译团队仍在持续修bad case）。
3. AI Agent自动处理编译错误并调整文档，人工编写编译错误处理规则难度不亚于重写LaTeX编译器。
4. 相比逐段翻译的幻觉翻译（hjfy.top），kimi-cli带全局上下文，翻译质量更好，但速度偏慢且存在大模型幻觉问题。

## 推导结构

方法（kimi-cli一行命令）→ 效果对比（kimi vs hjfy翻译质量）→ 多扯几句（AI Agent优势分析）。

## 关键公式

无定量公式。

## 体现的方法

- **用AI Agent翻译编译LaTeX论文**：利用AI Agent（kimi-cli）自动分析LaTeX源码目录、逐文件翻译、编译PDF并修复编译错误，将传统需要海量人工规则的"抽取-翻译"流水线转化为Agent自主任务。

## 所属系列位置

独立文章，属于AI工具应用类别。

## 与其他文章的关系

- 引用kimi-cli作为AI翻译工具示例，与该系列其他AI/工具话题相关。
- 翻译论文的需求与Cool Papers生态相关（同为论文阅读工作流的一部分）。

## 原文证据锚点

- `ev::11578::一行命令`：kimi-cli一行命令翻译arXiv论文并编译成PDF的具体使用方法。
- `ev::11578::AI Agent优势`：LaTeX语法灵活性导致"人工拆解成可枚举步骤"极为困难，AI Agent天然适合此类任务。
- `ev::11578::效果对比`：kimi-cli翻译质量与幻觉翻译（hjfy.top）的对比。
