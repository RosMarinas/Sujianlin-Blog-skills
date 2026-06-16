---
type: article_summary
title: 再谈非方阵的行列式
article_id: "6096"
source_url: https://spaces.ac.cn/archives/6096
date: 2018-10-16
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2018-10-16-再谈非方阵的行列式.md
series:
  - "[[新理解矩阵]]"
topics:
  - "[[矩阵代数]]"
  - "[[生成模型]]"
concepts:
  - "[[矩阵Capsule]]"
  - "[[高斯混合模型]]"
  - "[[非方阵的行列式]]"
  - "[[矩阵指数]]"
methods:
  - "[[带参求导构造ODE证明法]]"
  - "[[显式可逆矩阵构造法]]"
  - "[[EM路由算法]]"
problem_patterns:
  - "[[将经验判断转化为可计算命题]]"
evidence_spans:
  - ev::6096::内容摘要
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2018-10-16-再谈非方阵的行列式.md
source_ids:
  - "6096"
status: stable
updated: 2026-06-12
---
# article-6096: 再谈非方阵的行列式

## 文章核心问题
非方阵能否定义行列式？如何定义才能保留行列式的几何意义（向量张成超体积）？

## 主要结论
1. 对于$n\times k$（$n>k$）矩阵，将其视为$k$个$n$维列向量，它们张成$k$维超体积，此体积非平凡。
2. 合理的非方阵行列式定义为$|\det \boldsymbol{B}| = \sqrt{\det(\boldsymbol{B}^{\top}\boldsymbol{B})}$，该定义兼容方阵情形且保留行列式的几何意义。
3. 通过QR分解$\boldsymbol{B} = \boldsymbol{U}\boldsymbol{C}$可证明该定义等价于正交变换保持几何性质，且$n<k$时对应定义为$\sqrt{\det(\boldsymbol{B}\boldsymbol{B}^{\top})}$。

## 推导结构
- 回顾方阵行列式的几何意义：$n$维向量张成$n$维体的超体积
- 分析非方阵：$n>k$时$n$个$k$维行向量必线性相关，体积为0；但$k$个$n$维列向量张成$k$维体，体积非零
- 提出定义$|\det \boldsymbol{B}| = \sqrt{\det(\boldsymbol{B}^{\top}\boldsymbol{B})}$，验证$n\times 1$（向量模长）和$n\times 2$（平行四边形面积）情形
- QR分解证明：$\boldsymbol{B}_{n\times k} = \boldsymbol{U}_{n\times k}\boldsymbol{C}_{k\times k}$，正交变换不改变几何性质

## 关键公式
- $|\det \boldsymbol{B}| = \sqrt{\det (\boldsymbol{B}^{\top}\boldsymbol{B})}$，其中$\boldsymbol{B}_{n\times k}, n>k$
- $n\times 1$情形：$|\det \boldsymbol{X}| = \sqrt{x_1^2 + \cdots + x_n^2}$（向量长度）
- $n\times 2$情形：$|\det \boldsymbol{Z}| = \sqrt{\boldsymbol{x}^{\top}\boldsymbol{x}\boldsymbol{y}^{\top}\boldsymbol{y} - (\boldsymbol{x}^{\top}\boldsymbol{y})^2}$（平行四边形面积）
- 推广：$n<k$时$\sqrt{\det(\boldsymbol{B}\boldsymbol{B}^{\top})}$
