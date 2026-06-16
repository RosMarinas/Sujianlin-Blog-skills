---
title: 用Numpy实现高效的Apriori算法
source_id: 5525
type: source
url: https://spaces.ac.cn/archives/5525
author: 苏剑林
date: 2018-05-10
category: 信息时代
tags: [apriori, association-rules, numpy, data-mining]
license: CC BY-NC-SA
abstract: 使用纯Numpy实现高效的Apriori关联规则挖掘算法。支持最小支持度和最小置信度阈值，通过0-1矩阵连乘快速计算项集支持度，按字典序排序的频繁项对组合策略生成候选项集。去掉了Pandas依赖，仅用Numpy实现，代码更加简洁高效。
key_contributions:
  - Numpy 0-1矩阵实现Apriori算法
  - 通过矩阵列连乘快速计算支持度
  - 字典序排序的频繁项对组合策略
  - 遍历所有排列计算置信度
  - 纯Numpy无Pandas依赖的轻量实现
---
