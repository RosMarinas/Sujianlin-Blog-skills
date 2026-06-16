---
type: method
operation_types:
  primary: "Align / calibrate by invariance"
  secondary: []
title: "基于条件LayerNorm的实体关系抽取"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md"
source_ids:
  - "7161"
method_summary: "先预测主实体 s，再把 s 的首尾编码向量作为条件注入 LayerNorm，调节整句编码后预测该主实体对应的客实体 o 和关系 p。"
typical_structure: |
  1. 用 BERT 编码原始句子并预测主实体 s。
  2. 抽取 s 的首尾位置编码作为条件向量。
  3. 以 s 的条件向量对编码序列执行条件 LayerNorm。
  4. 在条件化后的序列上预测对应的 o 和 p。
applicability: "适用于三元组抽取中先确定主实体、再按主实体条件抽取客实体和关系的半指针-半标注模型。"
examples:
  - "[[article::7161]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md#模型简介"
---

# 基于条件LayerNorm的实体关系抽取

## 适用问题

适用于三元组抽取中先确定主实体、再按主实体条件抽取客实体和关系的半指针-半标注模型。

## 核心变换

句子编码与主实体 s -> 条件 LayerNorm 调制 -> o,p 联合预测。

## 典型步骤

1. 用 BERT 编码原始句子并预测主实体 s。
2. 抽取 s 的首尾位置编码作为条件向量。
3. 以 s 的条件向量对编码序列执行条件 LayerNorm。
4. 在条件化后的序列上预测对应的 o 和 p。

## 直觉

同一句中不同主实体对应不同关系查询；把主实体向量作为条件注入 LayerNorm，相当于让编码空间随当前 s 重新校准。

## 边界

该页只支持 7161 的三元组抽取结构；条件 LayerNorm 多任务文本匹配属于相邻方法，不是本页主证据。

## 例子

- 7161 的模型步骤写明：先预测 s，再根据传入的 s 抽取其首尾编码，并以该编码作为条件做条件 LayerNorm 来预测 o、p。

## 证据

- `Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md#模型简介`
- `Data/Spaces_ac_cn/markdown/Big-Data/2020-01-03-用bert4keras做三元组抽取.md`
- 读取章节: 模型简介
