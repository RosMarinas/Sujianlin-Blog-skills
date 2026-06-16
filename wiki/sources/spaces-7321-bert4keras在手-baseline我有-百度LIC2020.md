---
type: article_summary
title: bert4keras在手，baseline我有：百度LIC2020
article_id: "7321"
source_url: https://spaces.ac.cn/archives/7321
date: 2020-04-02
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2020-04-02-bert4keras在手-baseline我有-百度LIC2020.md
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-02-bert4keras在手-baseline我有-百度LIC2020.md
source_ids:
  - "7321"
status: draft
updated: 2026-06-11
---

# bert4keras在手，baseline我有：百度LIC2020

本文介绍了基于 `bert4keras` 搭建百度 2020 语言与智能技术竞赛（LIC2020）三个赛道（阅读理解、关系抽取、事件抽取）的 Baseline 模型的思路和关键技术。

## 主要内容

1. **赛道任务与设计**：
   - **阅读理解**：常规 BERT 后接首尾指针预测（两个全连接层 + Softmax）。
   - **关系抽取**：升级版的三元组抽取。处理 predicate 多义性时，通过将 predicate 与 object 前缀（如 `饰演_@value`）拼接，转化为普通的三元组抽取问题，采用“半指针-半标注”设计。
   - **事件抽取**：由于评测指标仅考察三元组 `(event_type, role, argument)`，任务可退化为普通的序列标注问题来解决。

2. **匹配原序列的 `rematch` 方法**：
   - **分词对齐问题**：抽取任务输出必须是原文中的片段。然而，BERT Tokenizer 分词后由于大小写转换、空格变化等因素，Token 序列与原始字符序列可能存在不对齐。
   - **解决方案**：在 `bert4keras` 的 `Tokenizer` 中增加了 `rematch` 方法。通过传入原始文本和分词后的 Token 序列，该方法能够自动建立并返回 Token 到原始文本字符位置的映射关系，实现无损的原文切片和抽词。
