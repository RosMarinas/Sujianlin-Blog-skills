---
type: article_summary
title: 百度实体链接比赛后记：行为建模和实体链接
article_id: "6919"
source_url: https://spaces.ac.cn/archives/6919
date: 2019-09-03
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2019-09-03-百度实体链接比赛后记-行为建模和实体链接.md
series: []
topics:
  - [[联合抽取]]
concepts:
  - [[实体链接]]
  - [[标注行为建模]]
methods:
  - [[基于描述文本匹配的实体链接]]
status: stable
updated: 2026-06-12
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-03-百度实体链接比赛后记-行为建模和实体链接.md
source_ids:
  - "6919"
---

# 百度实体链接比赛后记：行为建模和实体链接

本文总结了百度2019实体链接比赛的参赛方案与心得。实体链接任务要求在输入问句中识别实体mention并将其消歧链接到知识库（KB）中的唯一实体。

在实体识别阶段，模型采用BiLSTM与“半指针-半标注”结构，并结合了基于训练集统计的最大匹配特征以拟合带有强主观色彩的标注习惯，即“标注行为建模”。在实体链接阶段，模型将候选实体在知识库中的属性键值对拼接为一整段描述文本，与query编码进行双向Attention交互，最后通过全连接分类器预测是否匹配。模型融合了字/词层面的语义匹配和基于实体频率分布的过滤规则，有效提升了链接准确度与运行效率。
