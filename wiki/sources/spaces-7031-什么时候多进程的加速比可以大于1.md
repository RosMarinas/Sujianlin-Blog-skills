---
title: 什么时候多进程的加速比可以大于1？
source_id: 7031
type: source
url: https://spaces.ac.cn/archives/7031
author: 苏剑林
date: 2019-10-27
category: 信息时代
tags: [multiprocessing, parallel-computing, python, word-count, performance]
license: CC BY-NC-SA
abstract: 通过词频统计任务分析多进程加速比超线性加速的现象。单进程直接统计20分钟，而10进程分批统计+合并仅55秒（加速比2）。分析原因是单进程版本中dict操作随元素增多越来越慢，多进程版本每批只处理少量样本保持高效。同时指出单进程分批统计同样能提升效率（20分钟→8分钟），说明分批处理在单进程中也有价值。
key_contributions:
  - 超线性加速比（>1）的原因分析
  - 封装parallel_apply多进程通用函数
  - 分批处理+合并的统计策略
  - 单进程分批处理同样有效的发现
  - 字典操作随规模增大的性能退化问题
---
