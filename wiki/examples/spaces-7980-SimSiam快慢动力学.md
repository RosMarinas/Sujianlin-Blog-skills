---
type: example
title: spaces-7980-SimSiam快慢动力学
aliases: []
article_id: '7980'
article:
- - 从动力学角度看优化算法（六）：为什么SimSiam不退化？
section: 不退化的动力学
claim: predictor 与 stop_gradient 让 SimSiam 形成快慢动力学，减弱 encoder 退化力。
notation_mapping:
  phi: varphi
  theta: theta
  L: mathcal{L}
steps:
- 写出 predictor 与 encoder 的梯度流
- 比较 stop_gradient 去掉的项
- 识别 predictor 快变量与 encoder 慢变量
- 解释退化力在 encoder 退化前减弱
used_concepts:
- - - 优化快慢动力学
- - - 优化动力学视角
used_formulas:
- - - SimSiam快慢动力学公式
used_methods:
- - - 把优化算法解释为动力系统离散化
problem_pattern:
- - 把优化器经验现象改写为动力系统问题
source_span: ev::7980::不退化的动力学
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2020-12-11-从动力学角度看优化算法-六-为什么SimSiam不退化.md
source_ids:
- '7980'
status: stable
updated: '2026-06-12'
---

# spaces-7980-SimSiam快慢动力学

## 所在文章

[[从动力学角度看优化算法（六）：为什么SimSiam不退化？]]

## 原始问题

predictor 与 stop_gradient 让 SimSiam 形成快慢动力学，减弱 encoder 退化力。

## 推导步骤

1. 写出 predictor 与 encoder 的梯度流
2. 比较 stop_gradient 去掉的项
3. 识别 predictor 快变量与 encoder 慢变量
4. 解释退化力在 encoder 退化前减弱

## 证据锚点

- `ev::7980::不退化的动力学`