---
title: 有限内存下全局打乱几百G文件（Python）
source_id: 8662
type: source
url: https://spaces.ac.cn/archives/8662
author: 苏剑林
date: 2021-09-08
category: 信息时代
tags: [shuffle, big-data, file-processing, python, disk-based-algorithm]
license: CC BY-NC-SA
abstract: 介绍在内存有限的情况下对几百GB大文件进行全局随机打乱的算法和Python实现。核心思路：将文件切分为m个小文件，每个小文件内部随机打乱，然后按行横向混排（依次读取每个文件的第k行随机写入输出文件）。性能测试280G文件约3.5小时（Python）vs 2.7小时（C++ terashuf）。支持多文件混合打乱和分割输出。
key_contributions:
  - "先竖后横"的两阶段大文件打乱算法
  - 基于分片-内部打乱-横向混排的策略
  - 拒绝采样解决尾部不均问题
  - 与terashuf的性能对比
  - Python实现的完整shuffle工具
---
