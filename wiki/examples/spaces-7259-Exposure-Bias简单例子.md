---
type: example
title: Exposure Bias简单例子
aliases: []
article_id: "7259"
article: "[[spaces-7259-seq2seq-zhong-exposure-bias-xian-xiang-de-qian-xi-yu-dui-ce]]"
section: 简单例子
claim: Exposure Bias导致Beam Search可能选出非最优序列，即使逐目标分类已训练好
notation_mapping: 标准符号: p(a), p(c)（第一步概率）；p(b|a)等（条件概率）；源文符号一致
steps:
  - "1. 设序列长度2，目标序列(a,b)，候选(a,b)和(c,d)"
  - "2. 训练后p(a)=0.6>p(c)=0.4，p(b|a)=0.55>p(d|a)=0.45"
  - "3. Beam size=1时：选a再选b，正确"
  - "4. Beam size=2时：计算所有组合概率，(a,b)=0.33,(a,d)=0.27,(c,b)=0.04,(c,d)=0.36"
  - "5. 错误的(c,d)胜出，原因是p(d|c)=0.9未经训练约束"
used_concepts: ["[[Exposure Bias]]", "[[Teacher Forcing]]", "[[束搜索]]"]
used_formulas: ["[[Seq2Seq概率分解]]", "[[交叉熵]]"]
used_methods: ["[[随机替换抗Exposure Bias]]"]
source_span: "ev::7259::简单例子"
sources:
  - Data/Spaces_ac_cn/markdown/...
source_ids:
  - "7259"
status: draft
updated: 2026-06-12
---
# Exposure Bias简单例子

**本文来源：** 文章 7259

**所属章节：** 简单例子

**核心观点：** Exposure Bias导致Beam Search可能选出非最优序列，即使逐目标分类已训练好

## 推导步骤
- 1. 设序列长度2，目标序列(a,b)，候选(a,b)和(c,d)
- 2. 训练后p(a)=0.6>p(c)=0.4，p(b|a)=0.55>p(d|a)=0.45
- 3. Beam size=1时：选a再选b，正确
- 4. Beam size=2时：计算所有组合概率，(a,b)=0.33,(a,d)=0.27,(c,b)=0.04,(c,d)=0.36
- 5. 错误的(c,d)胜出，原因是p(d|c)=0.9未经训练约束

## 符号映射
标准符号: p(a), p(c)（第一步概率）；p(b|a)等（条件概率）；源文符号一致
