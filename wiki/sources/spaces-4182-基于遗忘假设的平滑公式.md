---
type: article_summary
title: 基于遗忘假设的平滑公式
article_id: "4182"
source_url: https://spaces.ac.cn/archives/4182
date: 2017-01-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2017-01-07-基于遗忘假设的平滑公式.md
series:
  - "[[概率与统计模型]]"
topics:
  - "[[概率与统计推断]]"
concepts:
  - "[[平滑公式]]"
  - "[[遗忘假设]]"
  - "[[艾宾浩斯遗忘曲线]]"
methods:
  - "[[遗忘假设平滑法]]"
evidence_spans:
  - "ev::4182::forgetting_based_smoothing"
  - "ev::4182::smoothing_taylor_expansion"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2017-01-07-基于遗忘假设的平滑公式.md
source_ids:
  - "4182"
status: draft
updated: 2026-06-13
---

## 文章核心问题

如何从人脑遗忘过程的数学建模出发，推导出一种具有清晰参数含义的统计平滑公式，并揭示它与经典加1平滑法的联系？

## 主要结论

1. 假设记忆量服从递推 $A_{n+1}=\beta A_n+1$，其极限 $A=1/(1-\beta)$ 可作为平滑后的统计结果。
2. 遗忘规律按指数下降，即 $\beta=\alpha^{N/F}$（$\alpha$ 为遗忘常数），带入得平滑公式 $\hat{F}=N(1-\alpha)/(1-\alpha^{N/F})$。
3. 固定 $\alpha$ 导致所有低频词获得相同概率，更合理的方式是固定未出现项的频数 $\gamma$，得 $\alpha=1-\gamma/N$。
4. 泰勒展开 $\hat{F} \approx F+\gamma/2+\gamma^2/(12F^2)+\cdots$ 表明其效果与加1平滑类似，为加1平滑法提供了遗忘假设的理论依据。

## 推导结构

1. 记忆量递推模型及其极限
2. 指数遗忘假设 $\beta=\alpha^{N/F}$
3. 平滑公式的推导和修正
4. 泰勒展开与加1平滑的关联

## 关键公式

$$\hat{F} = \frac{\gamma}{1-(1-\gamma/N)^{N/F}} \approx \frac{\gamma}{1-e^{-\gamma/F}} \approx F + \frac{\gamma}{2} + \cdots$$

## 体现的方法

- **遗忘假设平滑法**：从认知科学的遗忘曲线出发，将统计平滑问题建模为指数衰减递推过程。

## 所属系列位置

属于《概率与统计模型》系列的应用文章，将统计平滑与认知过程建模相结合。

## 与其他文章的关系

- [[4277 梯度下降和EM算法：系出同源，一脉相承]]：同为统计推断主题的不同侧面。
- [[5239 从最大似然到EM算法：一致的理解方式]]：自然语言处理中的统计基础。
