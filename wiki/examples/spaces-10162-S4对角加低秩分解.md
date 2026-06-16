---
type: example
title: S4对角加低秩分解
aliases: []
article_id: '10162'
article:
- - 重温SSM（三）：HiPPO的高效计算（S4）
section: 点睛之笔
claim: 展示 S4 如何把 HiPPO-LegS 矩阵转为酉相似下的对角减秩1形式。
notation_mapping:
  A: source A
  U: source U
  Lambda: "source \Lambda"
  u_v: source uv*
steps:
- 识别 A 的对角减 vv* 影子
- 构造 A+1/2vv*+1/2I 为反对称矩阵
- 利用酉对角化得到 A=U*(Lambda-uv*)U
used_concepts:
- - - HiPPO-LegS
- - - 对角加低秩分解
used_formulas:
- - - 对角加低秩分解公式
used_methods:
- - - 对角加低秩与Woodbury加速
problem_pattern:
- - 将矩阵幂卷积转为生成函数求值
source_span: ev::10162::点睛之笔::dlr
sources:
- Data/Spaces_ac_cn/markdown/Mathematics/2024-06-20-重温SSM-三-HiPPO的高效计算-S4.md
source_ids:
- '10162'
status: stable
updated: '2026-06-12'
---
## 问题

源文“点睛之笔”要解决 S4 中 HiPPO-LegS 矩阵 $A$ 的高效计算问题。直接对角化 $A$ 数值不稳定，但若能把它转成对角加低秩结构，就可用 Woodbury 恒等式加速递归和卷积核计算。

## 推导

源文先利用 $A$ 中已有的 $vv^*$ 影子，构造
$$
A+\frac12vv^*+\frac12I.
$$
该矩阵的非对角项一上一下符号相反，对角线为 0，因此是反对称矩阵。反对称矩阵可被酉矩阵稳定对角化，于是存在酉矩阵 $U$ 和对角矩阵 $\Lambda$，使
$$
A+\frac12vv^*+\frac12I=U^*\Lambda U.
$$
整理得
$$
A=U^*\left(\Lambda-\frac12I-\frac12(Uv)(Uv)^*\right)U,
$$
最终可简写为
$$
A=U^*(\Lambda-uv^*)U.
$$

## 方法与证据

本例体现“绕开不稳定直接对角化，构造可酉对角化的反对称矩阵，再得到对角减秩 1 表示”的方法。证据锚点为 `ev::10162::点睛之笔::dlr`，源文还说明 $(\Lambda-uv^*)x=\Lambda x-u(v^*x)$ 可在 $\mathcal{O}(d)$ 内完成。
