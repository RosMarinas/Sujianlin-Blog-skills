---
title: 增强typecho的搜索功能
source_id: 4797
type: source
url: https://spaces.ac.cn/archives/4797
author: 苏剑林
date: 2018-01-09
category: 信息时代
tags: [typecho, search, jieba, php, python]
license: CC BY-NC-SA
abstract: 通过Python+PHP混合编程增强typecho博客的搜索功能。核心方案：Python编写HTTP接口（bottle框架），使用jieba分词对查询语句进行分词，生成基于INSTR函数的SQL评分语句（标题匹配+2分，内容匹配+1分），按分数降序排列搜索结果。同时讨论了搜索排序覆盖默认时间排序的技术细节。
key_contributions:
  - Python+PHP混合编程的轻量级搜索增强方案
  - 基于jieba分词的SQL评分搜索
  - 标题/内容分别加权（2分/1分）
  - bottle框架的HTTP接口实现
  - typecho源码修改技巧
---
