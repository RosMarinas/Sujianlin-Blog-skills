---
type: reading_path
title: "SGD收敛与学习率调度阅读路径"
aliases:
  - "scientific alchemy SGD path"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2023-12-19-让炼丹更科学一些-一-SGD的平均损失收敛.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-12-让炼丹更科学一些-二-将结论推广到无界域.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-16-让炼丹更科学一些-三-SGD的终点损失收敛.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2025-12-26-让炼丹更科学一些-四-新恒等式-新学习率.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2026-01-09-让炼丹更科学一些-五-基于梯度精调学习率.md"
  - "Data/Spaces_ac_cn/markdown/Mathematics/2026-01-16-让炼丹更科学一些-六-自上而下的精妙构造.md"
source_ids:
  - "9902"
  - "11469"
  - "11480"
  - "11494"
  - "11530"
  - "11540"
assumed_reader_state: "了解梯度下降、凸函数和基本期望符号，但不要求熟悉随机优化证明。"
ordered_nodes:
  - "article::9902"
  - "article::11469"
  - "article::11480"
  - "article::11494"
  - "article::11530"
  - "article::11540"
checkpoints:
  - "能解释平均损失界的假设"
  - "能说明无界域推广为什么需要期望"
  - "能复述终点恒等式的作用"
  - "能解释线性衰减和 Warmup-Decay 的理论来源"
status: draft
updated: "2026-06-09"
---

# SGD收敛与学习率调度阅读路径

## 读者状态

适合已经知道 SGD 更新式、凸函数一阶条件和数学期望含义的读者。

## 阅读顺序

1. 先读 9902，建立 [[SGD平均损失收敛]] 和投影 SGD 的基本假设。
2. 再读 11469，理解 [[无界域SGD收敛]] 为什么需要期望形式。
3. 接着读 11480，关注 [[终点平均恒等式]] 如何把平均损失转成终点损失。
4. 继续读 11494，理解 [[加权终点恒等式]] 和 [[线性衰减学习率]] 的关系。
5. 读 11530，把梯度规模纳入 [[梯度自适应学习率]]。
6. 最后读 11540，看 [[自上而下构造辅助序列]] 如何证明 [[Warmup-Decay最优学习率]]。

## 检查点

- 读完第一篇后，应能列出平均损失界的四个主要假设。
- 读完第二篇后，应能说明为什么加期望能消去采样变量依赖。
- 读完第四篇后，应能说明为什么终点最优学习率依赖总步数。
- 读完第六篇后，应能解释 Warmup-Decay 中 Warmup 与 Decay 分别来自哪个因子。
