---
type: method
operation_types:
  primary: Structure-expose by factorization
  secondary: []
title: 用AI Agent翻译编译LaTeX论文
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2026-01-28-一行代码将arXiv论文翻译成中文版.md
source_ids:
  - 11578
method_summary: "把 arXiv LaTeX 源码翻译交给 AI Agent，让其自动识别待翻译文件、保留公式结构、编译 PDF 并根据错误反馈迭代修复。"
typical_structure: |
  1. 为 AI Agent 提供系统级别的 Prompt 设定任务，以及可编译的本地环境。
  2. Agent 自动扫描源文件目录结构，确定需要翻译的 `.tex` 文件。
  3. 执行增量和并行翻译，忽略指定部分（如公式、人名）。
  4. 利用本地编译命令试错编译并根据 log 自动修复排版错误。
applicability: "将包含众多文件、复杂数学公式等特定非翻译元素的科研论文进行整体机器翻译和可读重现时。"
examples:
  - "[[article::11578]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::11578::展示了向kimi-cli发起包含下载、解压、规则约束、翻译、编译以及根据报错进行自修正的高级系统提示词和操作流（Lines 18-36）。"
---

# 用AI Agent翻译编译LaTeX论文

## 适用问题

传统的学术论文翻译软件无法保证长篇幅连贯性，并且很难兼顾到 LaTeX 源码中复杂的排版、公式和图表代码，导致翻译出来的版本版面混乱。需要一种自动化方法将英文学术论文转化为高度原汁原味的中文排版。

## 核心变换

$$ \text{LaTeX Source (En)} \xrightarrow{\text{Agent Prompt (Rules + Try-Catch)}} \text{LaTeX Source (Zh)} \implies \text{Compiled PDF} $$
利用 AI Agent 的自主分析、多轮推理和工具调用能力，将翻译的复杂工程流从“人力分块翻译”重构为“代理全托管”的试错-修复闭环。

## 典型步骤

1. 本地安装配备大模型接口的 CLI Agent（如 kimi-cli）与完整的 LaTeX 编译环境（如 MacTeX）。
2. 在终端传入精心设计的 Prompt，指定：保留公式和人名、翻译内容、保存的新目录、最终的编译命令。
3. Agent 自动分析源码目录，切分任务，开启子任务（Subagent）对不同 `.tex` 文件并行翻译。
4. Agent 执行 `xelatex` 编译，如果出错，Agent 会自主阅读报错日志，修正 LaTeX 源码错误，然后不断重试，直到生成无错的 PDF。

## 直觉

把翻译工作看作是带徒弟：不能只给学徒一堆英文段落让他翻译，而是要给他一本详细的指南，告诉他“公式不要碰”、“这里是注释”、“翻译完之后自己去运行编译看看有没有错”。有了具有执行能力的 Agent，我们就能扮演这个发号施令的“包工头”。

## 边界

- 高度依赖大模型的代码理解能力、多轮推理上下文长度和 API 额度，复杂论文易消耗巨大 Token。
- 需要在本地环境跑，且必须保证本地编译环境能够支持原始英文版和中文版（如 CTeX 或 xeCJK）的宏包。

## 例子

在终端中执行一段命令行：让 kimi-cli 下载某篇 arXiv 论文的源码，按规则翻译为中文，存入 `paper_cn` 文件夹，并用 `xelatex` 反复编译修复至输出最终中文化的 PDF。

## 证据

- ev::11578::展示了向kimi-cli发起包含下载、解压、规则约束、翻译、编译以及根据报错进行自修正的高级系统提示词和操作流（Lines 18-36）。
