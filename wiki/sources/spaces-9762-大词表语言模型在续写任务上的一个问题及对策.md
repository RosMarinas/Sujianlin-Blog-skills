---
type: article_summary
title: "大词表语言模型在续写任务上的一个问题及对策"
article_id: "9762"
source_url: https://spaces.ac.cn/archives/9762
date: 2023-09-13
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::Tokenizer]]
  - [[concept::语言模型]]
methods:
  - [[method::Token Healing]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-09-13-大词表语言模型在续写任务上的一个问题及对策.md
source_ids:
  - "9762"
status: draft
updated: 2026-06-10
---

# 大词表语言模型在续写任务上的一个问题及对策

大词表Tokenizer将常见短语压缩为单个token（如"import numpy as np"），导致用户输入不完整前缀时无法续写完整短语。对策：回退一步对最后一个token做词表前缀搜索，再用LLM计算候选词的条件概率后采样，将缺点转化为优点。
