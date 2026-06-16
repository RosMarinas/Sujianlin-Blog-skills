---
type: method
operation_types:
  primary: "Rewrite / identity transform"
  secondary: []
title: "FlatNCE损失计算"
sources:
  - "Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md"
source_ids:
  - "8586"
method_summary: "将小 batch 对比学习中接近 0 的交叉熵项改写为去掉正样本得分的 logsumexp 形式，使梯度等效但数值尺度更稳定。"
typical_structure: |
  1. 分析 InfoNCE 在正样本得分远大于负样本时的 xi 近零问题。
  2. 用一阶近似把 log(1+xi) 的有效梯度聚焦到 xi。
  3. 通过 stop_gradient 或 log xi 变换放大近零损失的数值尺度。
  4. 实现为 logsumexp(负样本得分) - 正样本得分的 FlatNCE 损失。
applicability: "适用于小 batch 对比学习中正负样本差距明显、常规交叉熵损失长期接近 0 并可能受浮点误差主导的训练。"
examples:
  - "[[example::spaces-8586-FlatNCE小批次优化]]"
status: stable
updated: 2026-06-13
evidence_spans:
  - "ev::8586::FlatNCE等效"
---

# FlatNCE损失计算

## 适用问题

适用于小 batch 对比学习中正负样本差距明显、常规交叉熵损失长期接近 0 并可能受浮点误差主导的训练。

## 核心变换

InfoNCE 近零交叉熵 -> 梯度等效的 log xi / FlatNCE -> 更稳定的小 batch 更新信号。

## 典型步骤

1. 分析 InfoNCE 在正样本得分远大于负样本时的 xi 近零问题。
2. 用一阶近似把 log(1+xi) 的有效梯度聚焦到 xi。
3. 通过 stop_gradient 或 log xi 变换放大近零损失的数值尺度。
4. 实现为 logsumexp(负样本得分) - 正样本得分的 FlatNCE 损失。

## 直觉

当损失真实值已经非常小，浮点误差可能比有效信号还大；FlatNCE 不改变理论梯度方向，而是把有效项从 log(1+xi) 中显式抽出来。

## 边界

该页只支持对比学习损失的数值稳定改写；损失值可能为负，不能按普通非负交叉熵解释。

## 例子

- 8586 推导 xi/sg(xi) 与 log xi 的梯度一致，并指出 logsumexp 中去掉正样本得分后可得到 FlatNCE。

## 证据

- `ev::8586::FlatNCE等效`
- `Data/Spaces_ac_cn/markdown/Big-Data/2021-07-26-FlatNCE-小批次对比学习效果差的原因竟是浮点误差.md`
- 读取章节: 变微为著
