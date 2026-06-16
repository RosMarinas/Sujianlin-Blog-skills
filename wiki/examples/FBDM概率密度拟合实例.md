---
type: example
title: FBDM概率密度拟合实例
article_id: "10007"
article: "article::用傅里叶级数拟合一维概率密度函数"
section: 一般结果
claim: FBDM通过自相关参数化构造非负傅里叶级数，实现一维概率密度的梯度优化拟合。
notation_mapping:
  - "$a_k \in \mathbb{C}$": 自由参数
  - "$c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*$": 自相关形式的傅里叶系数
  - "$p_\theta(x) = f_\theta(x)/(2c_0)$": 归一化概率密度
steps:
  - "设定自由复参数 $\{a_0,\dots,a_N\}$"
  - "构造 $c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*$ 保证Toeplitz矩阵正定"
  - "定义非负函数 $f_\theta(x) = \sum_{n=-N}^N c_n e^{i\pi n x}$"
  - "归一化得到 $p_\theta(x) = f_\theta(x)/(2c_0)$"
  - "通过最大似然和Adam优化器求解参数"
  - "使用高频正则项 $\gamma \sum 2\pi^2 n^2 |c_n|^2$ 防止过拟合"
used_concepts:
  - "concept::傅里叶级数概率密度"
used_formulas:
  - "formula::FBDM概率密度函数"
used_methods:
  - "method::傅里叶级数非负概率密度构造法"
problem_pattern: "problem_pattern::非光滑函数可导化"
source_span: ev::10007::一般结果
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2024-03-07-用傅里叶级数拟合一维概率密度函数.md
source_ids:
  - "10007"
status: draft
updated: 2026-06-12
---

## 示例说明

本示例展示了FBDM从参数化到优化的完整流程。核心创新在于利用自相关函数与Toeplitz正定矩阵之间的等价关系，巧妙解决了傅里叶级数非负约束这一关键困难。通过将 $c_n$ 参数化为 $c_n = \sum_{k=0}^{N-n} a_k a_{k+n}^*$，任意复参数 $\{a_k\}$ 自动保证截断傅里叶级数 $f_\theta(x)=\sum c_n e^{i\pi n x}$ 非负。归一化因子仅是 $2c_0$，使得整个模型简洁优雅。高频正则项 $\gamma\sum 2\pi^2 n^2|c_n|^2$ 有效防止过拟合。实验表明FBDM在KL散度和模态捕捉方面优于GMM和DFP。
