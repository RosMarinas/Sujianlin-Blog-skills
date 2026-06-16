---
type: example
title: Basel问题欧拉解法
aliases: []
article_id: "3680"
article: article::3680
section: 伯努利级数
claim: "欧拉将有限韦达定理推广到无穷级数，从 sin(sqrt{x})/sqrt{x}=0 的根求和得到 sum 1/n^2 = pi^2/6"
notation_mapping:
  sin(sqrt{x})/sqrt{x}: 展开式为 1 - x/6 + x^2/120 - ...
  n^2*pi^2: 函数的零点
steps:
  - "将 sin(sqrt{x})/sqrt{x} 视为无限次多项式，零点为 n^2 pi^2 (n=1,2,3,...)"
  - "根据韦达定理推广：根倒数之和等于一次项系数相反数"
  - "由系数 -1/6 得 sum 1/(n^2 pi^2) = 1/6"
  - "两边乘以 pi^2 得 sum 1/n^2 = pi^2/6"
used_concepts:
  - "[[韦达定理推广]]"
  - "[[伯努利级数]]"
source_span:
  start: 30
  end: 57
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-03-20-欧拉数学-伯努利级数及相关级数的总结.md
source_ids:
  - "3680"
method: "[[欧拉无穷韦达定理法]]"
status: draft
updated: 2026-06-13
---

欧拉将 $\frac{\sin\sqrt{x}}{\sqrt{x}}$ 视为无限次"多项式"，其零点为 $n^2\pi^2$。根据韦达定理的无穷推广，根倒数和等于一次项系数的相反数，得 $\sum_{n=1}^\infty 1/n^2 = \pi^2/6$。此为数学史上著名的Basel问题。这个结果开启了无穷级数求和的严格理论，其思想后来被推广到一般形式的 $\sum 1/(n^2\pm\omega^2)$ 等含参级数。
