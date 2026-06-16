---
type: article_summary
title: Mitchell近似：乘法变为加法，误差不超过1/9
article_id: "7991"
source_url: https://spaces.ac.cn/archives/7991
date: 2020-12-14
category: Mathematics
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2020-12-14-Mitchell近似-乘法变为加法-误差不超过1-9.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-12-14-Mitchell近似-乘法变为加法-误差不超过1-9.md
source_ids:
  - "7991"
status: stable
updated: 2026-06-12
---

## 概述

本文介绍了John N. Mitchell于1962年提出的Mitchell近似算法，该算法在二进制下将对数运算$\log_2(1+x) \approx x$近似为简单的移位拼接操作，从而将乘法转化为加法。文章从快速对数与指数的近似计算出发，给出了详细的数值算例，并展示了利用IEEE754浮点数表示法实现的极其简洁的C++代码。误差分析证明了该算法的最大相对误差不超过$1/9$。文章还介绍了该算法在NeurIPS 2020中的深度学习应用——在ResNet50上验证了用Mitchell近似替换乘法后准确率仅轻微下降。

## 关键数学公式

- **对数近似**：$\log_2 p \approx n + x$，其中 $p = 2^n(1+x)$，$x \in [0,1)$
- **指数近似**：$2^{n+x} \approx 2^n(1+x)$
- **误差上界**：$\text{相对误差} \leq 1/9$，在 $x_1 = x_2 = 0.5$ 时达到
