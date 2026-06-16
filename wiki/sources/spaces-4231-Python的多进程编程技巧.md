---
title: Python的多进程编程技巧
source_id: 4231
type: source
url: https://spaces.ac.cn/archives/4231
author: 苏剑林
date: 2017-02-19
category: 信息时代
tags: [python, multiprocessing, parallel-computing]
license: CC BY-NC-SA
abstract: 介绍Python多进程编程的进阶技巧，特别是如何在类（对象方法）中正确使用multiprocessing.Pool进行并行计算。对比了多进程与多线程（multiprocessing.dummy）的区别，并参考gensim的ldamulticore实现，总结出一种通过Pool+Queue在类中启动多进程的通用写法。
key_contributions:
  - 对象方法中多进程编程的Pickling错误原因分析
  - 基于Pool+Queue的对象内多进程通用写法
  - multiprocessing与multiprocessing.dummy的对比
  - 参考gensim源码实现的并行模式
---
