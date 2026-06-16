---
title: 获取并处理中文维基百科语料
source_id: 4176
type: source
url: https://spaces.ac.cn/archives/4176
author: 苏剑林
date: 2017-01-06
category: 信息时代
tags: [wikipedia, corpus, nlp, data-preprocessing]
license: CC BY-NC-SA
abstract: 介绍如何获取和处理中文维基百科语料，通过结合gensim的Wikipedia Extractor和自写正则表达式处理脚本，将原始XML语料转化为干净的纯文本语料。最终从约91.9万个页面得到1.5G纯文本，并提取出维基重定向同义词表作为副产品。
key_contributions:
  - 基于gensim的wikicorpus库实现维基百科语料提取
  - 正则表达式处理特殊标记和{{}}标记的替换策略
  - 通过opencc实现繁简转换
  - 提取中文维基重定向表作为同义词资源
---
