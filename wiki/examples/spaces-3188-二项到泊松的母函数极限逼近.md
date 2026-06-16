---
type: example
title: 二项到泊松的母函数极限逼近
aliases: []
article_id: '3188'
article: '[[spaces-3188-当概率遇上复变-从二项分布到泊松分布]]'
section: 泊松分布推导
claim: 离散二项分布的概率生成函数在样本极大且概率极小时极限收敛为泊松分布生成函数。
notation_mapping:
  p: 二项分布单次试验成功概率
  n: 试验次数
  \lambda: 均值参数，原文中为 \lambda = pn
  x: 生成函数自变量，在 wiki 常用记号中常为 z
steps:
- 写出二项分布生成函数 (q+px)^n，其中 q = 1-p
- 代入 p = \lambda/n：(1 + \lambda/n * (x-1))^n
- 取 n -> \infty 极限，利用极限等价公式 \lim_{n\to\infty} (1+y/n)^n = e^y
- 导出极限为 e^{\lambda(x-1)}
- 对极限函数展开为泰勒级数，读出各项系数即为泊松分布概率质量函数
used_concepts:
- '[[概率生成函数]]'
used_formulas:
- '[[二项分布生成函数]]'
- '[[泊松分布生成函数]]'
used_methods:
- '[[通过母函数做分布极限近似]]'
source_span: ev::3188::泊松分布推导
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2015-01-13-当概率遇上复变-从二项分布到泊松分布.md
source_ids:
- '3188'
status: draft
updated: '2026-06-12'
---

# 二项到泊松的母函数极限逼近

## 算例推导
在原文第23-34行中，详细展示了该渐近极限的代数变形步骤：
$$
\lim_{n\to\infty} \left(1 + \frac{\lambda}{n}(x-1)\right)^n = e^{\lambda(x-1)}
$$
对极限函数做泰勒级数展开：
$$
e^{\lambda x - \lambda} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k}{k!} x^k
$$
从而优雅地推出了泊松分布概率质量公式。