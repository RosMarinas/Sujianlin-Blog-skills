---
type: example
title: 保守系统运动轨迹的Maupertuis几何化
aliases: []
article_id: "4046"
article: article::4046
section: 从作用量原理到黎曼几何
claim: 保守系统运动轨迹是Maupertuis度量ds²=(E-U)(dx²+dy²)的测地线
notation_mapping:
  "S": 作用量
  "E": 总能量
  "U": 势能
steps:
  - "最小作用量 S=∫(½v²-U)dt"
  - "能量守恒 E=½v²+U"
  - "消去dt: S=∫√{2(E-U)(dx²+dy²)}"
  - "定义 Maupertuis 度量 ds²=(E-U)(dx²+dy²)"
  - "测地线方程 ↔ 牛顿运动方程"
used_concepts:
  - 微分几何
  - 力学几何化方法
source_span: "ev::4046::测地线证力学"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2016-11-02-理解黎曼几何-8-处处皆几何-力学几何化.md
source_ids:
  - "4046"
status: draft
updated: 2026-06-13
---

# 保守系统运动轨迹的Maupertuis几何化

## 详细步骤

从最小作用量原理S=∫(½v²-U)dt出发，利用能量守恒E=½v²+U消去时间参数。导出等效作用量S=∫√{2(E-U)(dx²+dy²)}，定义Maupertuis度量ds²=(E-U)(dx²+dy²)。变分证明该度量的测地线方程等价于牛顿运动方程，实现了力学问题的几何化。该构造验证了变分原理与黎曼几何之间的深刻等价关系。
