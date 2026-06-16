---
type: method
title: "ZLPR多标签损失函数"
aliases:
  - "ZLPR Loss"
  - "多标签Softmax+交叉熵"
operation_types:
  primary: "Generalize from special cases"
  secondary: []
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-05-07-多标签-Softmax-交叉熵-的软标签版本.md
source_ids:
  - "9064"
method_summary: "将多标签分类损失ZLPR推广到软标签版本：log(1+sum t_i e^{-s_i})+log(1+sum (1-t_i)e^{s_i})。"
typical_structure: |
  1. 硬标签损失: log(1+sum e^{s_i})+log(1+sum e^{-s_j})
  2. 软标签版本: log(1+sum t_i e^{-s_i})+log(1+sum (1-t_i)e^{s_i})
  3. 最优解: t_i = sigma(2s_i)
applicability: "多标签分类，支持label smoothing和mixup"
tools:
  - 软标签
  - label smoothing
  - mixup
related_methods: []
examples:
  - [[article::9064]]
status: draft
updated: 2026-06-13
---

## 适用问题

多标签分类问题，特别是存在正负类不平衡的场景。当需要对标签使用label smoothing、mixup等软标签增强技巧时，ZLPR的软标签版本提供了统一的损失函数。

## 核心变换

**输入**：各类别得分$s_i$ + 软标签$t_i \in [0,1]$
**输出**：软标签多标签损失

硬标签ZLPR：
$$
\log\left(1 + \sum_{i\in\Omega_{neg}} e^{s_i}\right) + \log\left(1 + \sum_{j\in\Omega_{pos}} e^{-s_j}\right)
$$

软标签版本：
$$
\log\left(1 + \sum_i t_i e^{-s_i}\right) + \log\left(1 + \sum_i (1-t_i)e^{s_i}\right)
$$

## 典型步骤

1. **计算类别得分**：模型输出每个类别的logit $s_i$
2. **应用软标签**：$t_i = 1$（正类）、$t_i = 0$（负类），或使用混合标签（label smoothing/mixup）
3. **计算损失**：$loss = \log(1 + \sum t_i e^{-s_i}) + \log(1 + \sum (1-t_i)e^{s_i})$
4. **反向传播**：标准梯度下降优化
5. **预测**：取$\sigma(2s_i) > 0.5$的类别为正类（最优决策阈值）

## 直觉

多个"sigmoid+二分类交叉熵"展开后包含高阶项（如$e^{s_i}e^{s_j}$等），在正负类不平衡时这些高阶项使负类的损失被过度放大。ZLPR去掉了高阶项，使每个类别的损失贡献与类别数线性相关而非指数相关。

软标签版本的推导逻辑：从软标签多二分类交叉熵展开，去掉高阶项后自然得到软标签ZLPR。推导还证明了最优分类器满足$t_i = \sigma(2s_i)$——即预测值需经双倍sigmoid才能重建软标签。

## 边界

- 软标签$t_i$不能恰好为0或1时需在实现中防止$\log(0)$（加epsilon平滑）
- 最优决策阈值是$\sigma(2s_i) > 0.5$，而非标准的$\sigma(s_i) > 0.5$
- 支持label smoothing和mixup，但需配合软标签版本使用
- ZLPR硬标签版本即为原始的"多标签Softmax+交叉熵"推广

## 例子

- 硬标签多标签分类：正类得分>0，负类得分<0，ZLPR正常工作
- 混合标签（mixup）：标签为$0.3$或$0.7$时，软标签ZLPR自动适配
- label smoothing：标签从0/1平滑为0.05/0.95，使用软标签版本

## 证据

- ev::9064::硬标签ZLPR公式：$\log(1 + \sum_{neg} e^{s_i}) + \log(1 + \sum_{pos} e^{-s_j})$
- ev::9064::软标签版本推导：从sigmoid二分类交叉熵展开到去掉高阶项的ZLPR软标签形式
- ev::9064::最优解条件：$t_i = \sigma(2s_i)$，即双倍sigmoid决策阈值
