---
type: article_summary
title: 构造一个显式的、总是可逆的矩阵
article_id: "6407"
source_url: https://spaces.ac.cn/archives/6407
date: 2019-03-01
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2019-03-01-构造一个显式的-总是可逆的矩阵.md
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
  - ev::6407::内容摘要
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2019-03-01-构造一个显式的-总是可逆的矩阵.md
source_ids:
  - "6407"
status: stable
updated: 2026-06-12
---

# 构造一个显式的、总是可逆的矩阵

## 文章总结
在恒等式 $\det(\exp(A)) = \exp(\text{Tr}(A))$ 启发下，提出利用两个向量的乘积 $xy^T$ 代入矩阵指数函数，解析地推导得到一个构造显式且一定可逆的秩一偏移矩阵的形式：$\exp(xy^T) = I + xy^T \frac{e^{\langle x, y \rangle} - 1}{\langle x, y \rangle}$。该发现为神经网络等领域直接构造可逆模块提供了一种途径。
