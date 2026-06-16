---
type: example
title: 非方阵行列式计算示例
aliases: []
article_id: "6096"
article: "[[spaces-6096-再谈非方阵的行列式]]"
section: 定义
claim: 使用公式计算 $n \times 2$ 矩阵的行列式绝对值等于对应平行四边形的面积
notation_mapping:
  "A": "矩阵"
  "A": "矩阵"
steps:
  - 令 $Z = (x, y)$ 为 $n \times 2$ 的矩阵
  - 根据定义 $|\det Z| = \sqrt{\det(Z^T Z)}$
  - 计算 $Z^T Z = \begin{pmatrix} x^T x & x^T y \\ y^T x & y^T y \end{pmatrix}$
  - 计算行列式得 $\sqrt{(x^T x)(y^T y) - (x^T y)^2}$
  - 通过三角函数转换证明这正好是平行四边形面积 $|x||y|\sin\theta$ 的平方开根号
used_concepts:
  - "[[非方阵的行列式]]"
used_formulas:
  - "[[非方阵行列式公式]]"
used_methods:

problem_pattern: null
source_span: ev::6096::定义
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-10-16-再谈非方阵的行列式.md
source_ids:
  - "6096"
status: stable
updated: 2026-06-12
---

# 非方阵行列式计算示例

## 推导步骤
1. 令 $Z = (x, y)$ 为 $n \times 2$ 的矩阵
2. 根据定义 $|\det Z| = \sqrt{\det(Z^T Z)}$
3. 计算 $Z^T Z = \begin{pmatrix} x^T x & x^T y \\ y^T x & y^T y \end{pmatrix}$
4. 计算行列式得 $\sqrt{(x^T x)(y^T y) - (x^T y)^2}$
5. 通过三角函数转换证明这正好是平行四边形面积 $|x||y|\sin\theta$ 的平方开根号
