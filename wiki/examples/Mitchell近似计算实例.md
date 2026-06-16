---
type: example
title: Mitchell近似计算实例
article_id: "7991"
article: "article::Mitchell近似：乘法变为加法，误差不超过1/9"
section: 一个乘法的例子
claim: 通过Mitchell近似将浮点数乘法转化为二进制位拼接和整数加法，最大相对误差仅1/9。
notation_mapping:
  - "$n$": 二进制表示中整数位数减1
  - "$x \in [0,1)$": 小数部分的数值
  - "$2^{n}(1+x)$": 浮点数的二进制科学计数法表示
steps:
  - "将 $12.3$ 和 $4.56$ 转化为二进制 $1100.0100110$ 和 $100.1000111$"
  - "提取 $n$（整数位数-1）和 $x$（小数部分），拼接得到 $\log_2$ 近似"
  - "将对数近似相加后应用指数近似，恢复为十进制乘积极近似值"
  - "结果 $53.625$ 与精确值 $56.088$ 的相对误差约 $4.39\%$"
used_concepts:
  - "concept::函数光滑化"
used_formulas:
  - "formula::Mitchell近似对数公式"
used_methods: []
problem_pattern: "problem_pattern::用简单运算替代复杂计算"
source_span: ev::7991::一个乘法的例子
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-12-14-Mitchell近似-乘法变为加法-误差不超过1-9.md
source_ids:
  - "7991"
status: draft
updated: 2026-06-12
---

## 示例说明

Mitchell近似利用 $\log_2(1+x) \approx x$ 将浮点数乘法转化为几乎仅含整数加法和二进制拼接的运算。对于 $12.3 \times 4.56$，近似结果 $53.625$ 与精确值 $56.088$ 相比误差可接受（相对误差 $4.39\%$）。这一近似在IEEE754硬件实现中可通过整数加减法和位操作完成，计算开销远低于标准乘法。NeurIPS 2020中已有工作验证了在ResNet50上使用Mitchell近似代替乘法仅带来轻微的准确率下降。
