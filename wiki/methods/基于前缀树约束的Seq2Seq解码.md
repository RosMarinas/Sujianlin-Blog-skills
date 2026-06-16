---
type: method
operation_types:
  primary: "Dual / constraint rewrite"
  secondary: []
title: "基于前缀树约束的Seq2Seq解码"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2021-12-17-Seq2Seq-前缀树-检索任务新范式-以KgCLUE为例.md"
source_ids:
  - "8802"
method_summary: "把固定候选输出集合压缩成前缀树，在 Seq2Seq 每步解码时只允许当前前缀的合法后继 token，从而把生成限制为库内检索。"
typical_structure: |
  1. 把候选答案或三元组序列插入前缀树。
  2. 解码时根据当前已生成前缀查询合法后继 token。
  3. 将不在前缀树分支上的 token 概率置零或置为负无穷。
  4. 沿树生成到结束符，保证输出落在候选库中。
applicability: "适用于输出集合固定的生成式检索、知识图谱问答和实体/文档检索任务。"
examples:
  - "[[example::spaces-8802-前缀树解码算法实例]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8802::前缀树解码"
---

# 基于前缀树约束的Seq2Seq解码

## 适用问题

适用于输出集合固定的生成式检索、知识图谱问答和实体/文档检索任务。

## 核心变换

候选库 -> 前缀树约束 -> 合法路径内的 Seq2Seq 解码。

## 典型步骤

1. 把候选答案或三元组序列插入前缀树。
2. 解码时根据当前已生成前缀查询合法后继 token。
3. 将不在前缀树分支上的 token 概率置零或置为负无穷。
4. 沿树生成到结束符，保证输出落在候选库中。

## 直觉

Seq2Seq 负责根据输入选择路径，前缀树负责排除库外路径，因此生成过程变成受约束检索。

## 边界

原文指出遇到 UNK 或需要修正 bad case 时不如传统检索容易；该方法适合候选集可枚举的任务。

## 例子

- 8802 用“明月几时有”等句子构造前缀树，并说明每步把非法 token 概率置零可保证输出为数据库已有句子。

## 证据

- `ev::8802::前缀树解码`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-12-17-Seq2Seq-前缀树-检索任务新范式-以KgCLUE为例.md`
- 读取章节: 前缀解码、KgCLUE
