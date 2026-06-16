---
type: proposition
title: Short Conv通过改变TTT配对解决键值同源瓶颈
aliases:
  - Short Conv Solves Key-Value Homology
statement: 线性注意力中Short Conv的核心作用是将TTT的(K,V)配对从"预测自己"(k_t,v_t)转化为NTP式"预测周围"(k_{t-1},v_t)，从而解决键值同源（K=V或同源输入）导致的TTT表达能力瓶颈。
assumptions:
  - "线性注意力采用TTT框架"
  - "键值同源时TTT的可学信息有限"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-10-05-为什么线性注意力要加Short-Conv.md
source_ids:
  - "11320"
evidence_spans:
  - "ev::11320::键值同源"
  - "ev::11320::卷积救场"
status: draft
updated: 2026-06-10
---

# Short Conv通过改变TTT配对解决键值同源瓶颈

## 内容

TTT框架中，如果K=V则MesaNet等模型直接退化为单位变换，即使K不等于V但同源（k_t和v_t同出一源x_t）时，可学信息也有限。Short Conv（kernel_size=2）相当于将配对改为(k_{t-1}, v_t)，与NTP任务一致，使模型能学出n-gram等非平凡模式。
