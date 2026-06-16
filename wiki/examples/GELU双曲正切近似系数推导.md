---
type: example
title: GELU双曲正切近似系数推导
article_id: "7309"
article: "article::GELU的两个初等函数近似是怎么来的"
section: 混合拟合
claim: GELU的tanh近似系数可以通过局部拟合加全局minimax优化混合求解。
notation_mapping:
  - "$\text{erf}(z)$": 误差函数
  - "$x$": GELU的输入
  - "$a,b$": 待拟合参数
steps:
  - "选取近似形式 $\tanh(a x + b x^3)$ 逼近 $\text{erf}(x/\sqrt{2})$"
  - "局部拟合：在 $x=0$ 处泰勒展开，令前两项匹配，解得 $a = \sqrt{2/\pi}$"
  - "固定 $a$，执行全局minimax优化 $\min_b \max_x |\text{erf}(x/\sqrt{2}) - \tanh(a x + b x^3)|$"
  - "解得 $b = 0.035677$，代入GELU公式得 $x^3$ 系数 $0.044715$"
used_concepts:
  - "concept::Minimax误差优化"
used_formulas:
  - "formula::GELU双曲正切近似公式"
used_methods:
  - "method::局部拟合与全局拟合法"
  - "method::Minimax误差优化法"
problem_pattern: "problem_pattern::用简单运算替代复杂计算"
source_span: ev::7309::混合拟合
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2020-03-26-GELU的两个初等函数近似是怎么来的.md
source_ids:
  - "7309"
status: draft
updated: 2026-06-12
---

## 示例说明

本示例展示了从局部泰勒展开匹配到全局minimax优化的完整系数求解流水线。关键在于先利用局部信息降低搜索维度（确定 $a$），再通过数值优化精调剩余参数（确定 $b$）。具体过程为：(1) 在 $x=0$ 处展开并令线性项和三次项系数匹配，得到 $a = \sqrt{2/\pi}$；(2) 固定 $a$ 后对 $b$ 执行 $\min_b \max_x |\text{erf}(x/\sqrt{2}) - \tanh(ax+bx^3)|$ 优化；(3) 最终得到 $b=0.035677$，折算到GELU标准形式后 $x^3$ 系数为 $0.044715$。
