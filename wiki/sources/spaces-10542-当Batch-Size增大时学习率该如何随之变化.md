---
type: article_summary
title: 当Batch Size增大时，学习率该如何随之变化？
article_id: "10542"
source_url: https://spaces.ac.cn/archives/10542
date: 2024-11-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-11-14-当Batch-Size增大时-学习率该如何随之变化.md
source_html: null
series: []
topics:
  - "[[优化动力学]]"
concepts:
  - "[[SGD-SDE近似]]"
  - "[[优化动力学视角]]"
methods:
  - "[[用稳定性指标约束优化器缩放]]"
problem_patterns: []
evidence_spans:
  - ev::10542::平方根缩放
  - ev::10542::线性缩放SDE
  - ev::10542::单调有界
  - ev::10542::实践分析
  - ev::10542::数据效率
  - ev::10542::符号近似
  - ev::10542::涌现行为
  - ev::10542::效率关系
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-11-14-当Batch-Size增大时-学习率该如何随之变化.md
source_ids:
  - "10542"
status: draft
updated: 2026-06-10
---

## 文章核心问题

当Batch Size B增大时，学习率 η 该如何调整才能保持训练效果并最大化训练效率？

## 主要结论

1. **平方根缩放（$\eta\propto \sqrt{B}$）**：来自SGD增量方差保持不变的直观要求；Adam等自适应优化器在B较小时也适用平方根缩放。
2. **线性缩放（$\eta\propto B$）**：来自SGD-SDE对应分析，要求SDE形式在B变化时不变；仅在B较小时成立。
3. **单调有界（OpenAI 2018）**：SGD下最优学习率 $\eta^* = \eta_{\max} / (1 + \mathcal{B}_{\text{noise}}/B)$，随B增加单调递增但有上界 $\eta_{\max}$。
4. **Surge现象**：Adam下Hessian非对角项不可忽略时，最优学习率先增后减，存在使学习率最大的临界Batch Size。
5. **数据-步数双曲关系**：$(S/S_{\min} - 1)(E/E_{\min} - 1) = 1$，SGD和Adam共享此形式。

## 推导结构

平方根缩放（方差视角）→ 线性缩放（SDE对应）→ 直面损失（二阶展开求解最优学习率）→ 实践分析（$\mathcal{B}_{\text{noise}}$估计方法）→ 数据效率（导出的S-E关系）→ 自适应版（SignSGD近似Adam）→ 两个特例（对角Hessian等简化情形）→ 涌现行为（Surge现象与非对角Hessian）→ 效率关系（Adam下的S-E关系）。

## 关键公式

- SGD最优学习率：$\eta^* \approx \frac{g^\top g}{g^\top H g + \text{tr}(\Sigma H)/B} = \frac{\eta_{\max}}{1 + \mathcal{B}_{\text{noise}}/B}$
- 数据-步数关系：$(\frac{S}{S_{\min}} - 1)(\frac{E}{E_{\min}} - 1) = 1$
- Adam近似：$\eta^* \approx \frac{\sum_i \mu_i g_i}{\sum_i H_{ii} + \sum_{i\neq j} \mu_i \mu_j H_{ij}}$，其中 $\mu_i = \mathbb{E}[\text{sign}(\tilde{g}^{(i)}_B)]$
- Surge公式：$\eta^* \approx \frac{\eta_{\max}}{\frac{1}{2}(\frac{\beta_{\text{noise}}}{\beta} + \frac{\beta}{\beta_{\text{noise}}})}$，$\beta = (1 + \pi\kappa^2/2B)^{-1/2}$

## 体现的方法

- **用稳定性指标约束优化器缩放**：从损失函数二阶近似和SDE对应两种视角反推学习率随B的缩放规则。
- **SGD-SDE近似**：将SGD的离散迭代近似为连续SDE，由此导出的噪声-步长关系是线性缩放的理论基础。

## 所属系列位置

独立文章。但操作类型上与[[series::重新思考学习率与Batch Size]]共享"学习率与批量大小的缩放规律"的问题形态。

## 与其他文章的关系

- 被[[spaces-10770-初探MuP-超参数的跨模型尺度迁移规律]]引用其中的SignSGD近似方法用于Adam分析。
- 与系列[[series::从动力学角度看优化算法]]共享SDE视角和动力学分析框架。
- 在问题模式上与[[series::重新思考学习率与Batch Size]]系列高度相关，是该系列的前驱工作。

## 原文证据锚点

- `ev::10542::平方根缩放`：SGD增量方差保持给出$\eta\propto\sqrt{B}$，最初来自AlexNet并行训练。
- `ev::10542::线性缩放SDE`：SGD可近似为SDE，噪声项步长是梯度项的平方根，导出线性缩放$\eta\propto B$。
- `ev::10542::单调有界`：二阶展开损失函数求最优学习率，得$\eta^* = \eta_{\max}/(1+\mathcal{B}_{\text{noise}}/B)$。
- `ev::10542::实践分析`：$\mathcal{B}_{\text{noise}}$可通过简化的$\mathcal{B}_{\text{simple}}=\text{tr}(\Sigma)/(g^\top g)$近似估计。
- `ev::10542::数据效率`：由最优学习率下的损失下降导出S-E双曲关系$(S/S_{\min}-1)(E/E_{\min}-1)=1$。
- `ev::10542::符号近似`：用SignSGD近似Adam，假设梯度分量独立、正态分布，计算期望符号函数。
- `ev::10542::涌现行为`：Adam下Hessian非对角项显著时出现Surge现象，B过大时学习率应减小。
- `ev::10542::效率关系`：Adam下导出形式相同的S-E双曲关系，但$\mathcal{B}_{\text{noise-2}}$含义不同。
