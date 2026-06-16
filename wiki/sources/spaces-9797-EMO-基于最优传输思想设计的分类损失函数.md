---
type: article_summary
title: "EMO：基于最优传输思想设计的分类损失函数"
article_id: "9797"
source_url: https://spaces.ac.cn/archives/9797
date: 2023-10-13
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
topics:
  - [[topic::NLP语言模型与文本匹配]]
concepts:
  - [[concept::Earth Mover's Distance]]
  - [[concept::交叉熵损失]]
methods:
  - [[method::EMO损失函数]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-10-13-EMO-基于最优传输思想设计的分类损失函数.md
source_ids:
  - "9797"
status: draft
updated: 2026-06-10
---

# EMO：基于最优传输思想设计的分类损失函数

EMO将分类损失从KL散度替换为Earth Mover's Distance（最优传输距离）。对于one-hot标签，EMO退化为 $1 - \langle \sum_i p_i \frac{e_i}{\|e_i\|}, \frac{e_t}{\|e_t\|} \rangle$，利用固定的Token Embedding余弦相似度作为传输成本函数。实验表明EMO在LLM微调中显著优于交叉熵。
