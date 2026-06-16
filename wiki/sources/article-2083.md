---
type: article_summary
article_id: "2083"
source_url: https://spaces.ac.cn/archives/2083
date: 2013-09-26
category: Mathematics
series: [[数学基本技艺之23-24系列]]
source_markdown: Data/Spaces_ac_cn/markdown/Mathematics/2013-09-26-数学基本技艺之23-24-上.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2013-09-26-数学基本技艺之23-24-上.md
source_ids:
  - "2083"
status: draft
updated: 2026-06-10
---

# article-2083: 数学基本技艺之23、24（上）

## 文章核心问题

求解两个拟齐次微分方程：23题 dy/dx = x + x³/y 和 24题 ẍ = x⁵ + x²ẋ，通过变量代换技巧分离变量。

## 主要结论

1. 23题存在两个简单特解 y = x² 和 y = -x²/2（通过设 y=cxⁿ 找到）。
2. 通过变量代换 x = t√y 成功分离变量，得到通解 (2y+x²)(x²-y)² = C。
3. 当 C=0 时还原为两个特解，验证了通解的正确性。
4. 24题可通过设 ẋ = y 化为与23题相同形式来处理。

## 推导结构

- 先寻找 y=cxⁿ 形式的特解：n=2, c=1 或 c=-1/2
- 设变换 x = t√y，代入方程
- 将方程倒置并整理，分离变量 dt 和 dy
- 积分得通解

## 关键公式

- dy/dx = x + x³/y → (2y+x²)(x²-y)² = C
- 特解：y = x², y = -x²/2

## 体现的方法

- **拟齐次变量代换法** → 通过 x = t·y^k 形式的代换，将方程变为可分离变量形式

## 所属系列位置

数学基本技艺之23-24系列第1篇（上），求解23题并暗示24题的方法。

## 与其他文章的关系

- [[article-2096]]（下篇）从23题解中发现拟齐次方程通解的一般规律

## 原文证据锚点

- ev::2083::特解探索：设 y=cxⁿ 解得 n=2, c=1 或 -1/2
- ev::2083::变量代换：变换 x = t√y 并成功分离变量
- ev::2083::通解结果：(2y+x²)(x²-y)² = C
