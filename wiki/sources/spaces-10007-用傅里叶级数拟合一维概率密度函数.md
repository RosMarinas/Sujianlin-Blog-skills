---
type: article_summary
title: 用傅里叶级数拟合一维概率密度函数
article_id: "10007"
source_url: https://spaces.ac.cn/archives/10007
date: 2024-03-07
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
source_ids:
  - "10007"
status: stable
updated: 2026-06-12
---

## 概述

本文介绍了一种基于傅里叶级数拟合概率密度函数的新方法（Fourier Basis Density Model, FBDM）。与高斯混合模型（GMM）和深度因子化概率（DFP）相比，FBDM通过精巧的参数化构造解决了傅里叶级数非负约束这一核心难题。

关键创新在于利用 Toeplitz 正定矩阵与自相关系数的等价关系：将傅里叶系数 $c_n$ 构造为 $c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*$，使得对应的截断傅里叶级数 $f_{\theta}(x) = \sum_{n=-N}^N c_n e^{i\pi n x}$ 自动满足非负性。归一化因子为 $2c_0$，因此最终的概率密度函数为 $p_{\theta}(x) = f_{\theta}(x)/(2c_0)$。

文章还讨论了：
1. **扩展到 $\mathbb{R}$**：通过 $\tanh$ 变换将实数轴压缩到 $[-1,1]$，并代入链式法则修正密度。
2. **正则项**：用 $\gamma \int |df_{\theta}/dx|^2 dx = \gamma \sum 2\pi^2 n^2 |c_n|^2$ 对高频项施加惩罚以防止过拟合。
3. **实验对比**：相比GMM和DFP，FBDM在KL散度和模态捕捉方面均表现更优。
4. **缺点**：不直观、不易采样（需逆累积概率函数）、高维推广成本高。

## 关键数学公式

- **截断傅里叶级数**：$f_{\theta}(x) = \sum_{n=-N}^N c_n e^{i\pi n x}, \quad x\in[-1,1]$
- **非负性构造**：$c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*$（自相关形式）
- **归一化**：$p_{\theta}(x) = \dfrac{f_{\theta}(x)}{2c_0}$
- **正则项**：$\gamma\int_{-1}^1 |f_{\theta}'(x)|^2 dx = \gamma\sum_{n=-N}^N 2\pi^2 n^2 |c_n|^2$
