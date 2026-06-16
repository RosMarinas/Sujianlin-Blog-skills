---
type: article_summary
title: msign算子的Newton-Schulz迭代（上）
article_id: "10922"
source_url: https://spaces.ac.cn/archives/10922
date: 2025-05-11
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2025-05-11-msign算子的Newton-Schulz迭代-上.md
series: []
topics:
  - "[[矩阵优化]]"
concepts:
  - "[[矩阵符号函数(msign)]]"
  - "[[Newton-Schulz迭代]]"
  - "[[谱范数]]"
methods:
  - "[[用迭代逼近替代矩阵分解]]"
problem_patterns: []
evidence_spans:
  - ev::10922::msign定义
  - ev::10922::NS迭代格式
  - ev::10922::标量迭代分析
  - ev::10922::系数优化求解
  - ev::10922::初值分布分析
  - ev::10922::不同步系数方法
  - ev::10922::改良初值
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-05-11-msign算子的Newton-Schulz迭代-上.md
source_ids:
  - "10922"
status: draft
updated: 2026-06-10
---

# msign算子的Newton-Schulz迭代（上）

## 文章核心问题

如何为Muon优化器核心算子msign寻找更高效的Newton-Schulz迭代，使得在有限迭代步数内对msign的近似精度更高。文章围绕迭代系数(a,b,c)的优化和初值改进展开。

## 主要结论

- msign算子的Newton-Schulz迭代可简化为标量迭代 $x_{t+1} = a x_t + b x_t^3 + c x_t^5$ 的分析。
- 每一步使用不同的系数（解绑参数共享）能大幅提高收敛性质且不增加计算成本。
- 通过改良初值（用 $\sqrt[4]{\|(M^\top M)^2\|_F}$ 代替 $\|M\|_F$ 做归一化）可提高小奇异值的收敛速度。
- 对于当前LLM规模（hidden_size ~8192），msign算法需兼顾到0.001大小的奇异值。
- 小模型实验显示msign计算精度与最终模型效果无必然联系，仅影响前期收敛速度。

## 推导结构

1. 定义msign算子及其与SVD的关系。
2. 引入Newton-Schulz迭代格式，给出Muon作者KellerJordan的参考系数。
3. 将矩阵迭代简化为标量迭代分析。
4. 用Adam优化器求解最优系数(a,b,c)。
5. 分析初值奇异值分布，确定需关心的最小奇异值尺度。
6. 采用不同步系数方法（YouJiacheng思路）大幅提升收敛性。
7. 改良初值归一化方法：用高阶F范数逼近谱范数。

## 关键公式

- msign定义: $\text{msign}(M) = U_{[:,:r]} V_{[:,:r]}^\top = (M M^\top)^{-1/2} M$
- 最优正交近似: $\text{msign}(M) = \argmin_{O^\top O = I} \|M - O\|_F^2$
- NS迭代: $X_{t+1} = a X_t + b X_t(X_t^\top X_t) + c X_t(X_t^\top X_t)^2$
- 标量简化: $x_{t+1} = a x_t + b x_t^3 + c x_t^5$
- 初值归一化: $X_0 = M / \|M\|_F$，每步可重新用 $\sqrt[4]{\|(M^\top M)^2\|_F}$ 归一化

## 体现的方法

- **用迭代逼近替代矩阵分解**：将昂贵SVD替换为Newton-Schulz矩阵迭代，通过优化迭代系数提高收敛速度。
- **标量简化分析**：利用SVD将矩阵迭代分解为独立的标量迭代，降低分析难度。
- **不同步参数解绑**：每步使用不同系数，不增加计算量的免费午餐。
- **初值改良**：用近似谱范数替代F范数做归一化，改善小奇异值收敛。

## 所属系列位置

独立文章，与Muon优化器系列密切相关。是msign算子Newton-Schulz迭代研究的上篇。

## 与其他文章的关系

- 前置知识来自 Muon优化器赏析(10592) 和 Muon续集(10739)。
- 与 高阶MuP(10795) 中msign被视为奇异值裁剪极限版本的论述相关联。
- 下篇(10996) 给出更优雅的理论最优解证明。
- 后续mclip文章(11006, 11059) 建立在msign计算之上。

## 原文证据锚点

- ev::10922::msign定义: 第22-30行，msign的SVD定义和等价形式。
- ev::10922::NS迭代格式: 第44-58行，Newton-Schulz迭代格式和KellerJordan系数。
- ev::10922::标量迭代分析: 第85-96行，将矩阵迭代简化为标量迭代。
- ev::10922::系数优化求解: 第99-145行，用Adam优化求解系数的完整代码和结果。
- ev::10922::初值分布分析: 第147-155行，奇异值分布分析及需关注的尺度。
- ev::10922::不同步系数方法: 第159-282行，YouJiacheng不同步系数方法和作者自己的解。
- ev::10922::改良初值: 第287-317行，用高阶F范数改良初值归一化。
