---
type: reading_path
title: Transformer升级之路阅读路径
aliases:
  - Transformer Upgrade Path reading path
goal: 按问题线索阅读Transformer升级之路，理解位置编码、长度外推、RoPE变体和MLA分析如何逐步连接。
audience: 已了解Transformer基本结构，希望系统掌握RoPE、长度外推或MLA设计脉络的读者或agent。
ordered_nodes:
  - "[[Sinusoidal位置编码追根溯源]]"
  - "[[博采众长的旋转式位置编码]]"
  - "[[Transformer升级之路：3、从Performer到线性Attention]]"
  - "[[Transformer升级之路：4、二维位置的旋转式位置编码]]"
  - "[[Transformer升级之路：5、作为无限维的线性Attention]]"
  - "[[Transformer升级之路：6、旋转位置编码的完备性分析]]"
  - "[[Transformer升级之路：7、长度外推性与局部注意力]]"
  - "[[Transformer升级之路：8、长度外推性与位置鲁棒性]]"
  - "[[Transformer升级之路：9、一种全局长度外推的新思路]]"
  - "[[Transformer升级之路：10、RoPE是一种β进制编码]]"
  - "[[Transformer升级之路：11、将β进制位置进行到底]]"
  - "[[Transformer升级之路：12、无限外推的ReRoPE？]]"
  - "[[Transformer升级之路：13、逆用Leaky ReRoPE]]"
  - "[[Transformer升级之路：14、当HWFA遇见ReRoPE]]"
  - "[[Transformer升级之路：15、Key归一化助力长度外推]]"
  - "[[Transformer升级之路：16、\"复盘\"长度外推技术]]"
  - "[[Transformer升级之路：17、多模态位置编码的简单思考]]"
  - "[[Transformer升级之路：18、RoPE的底数选择原则]]"
  - "[[Transformer升级之路：19、第二类旋转位置编码]]"
  - "[[Transformer升级之路：20、MLA好在哪里?（上）]]"
  - "[[Transformer升级之路：21、MLA好在哪里?（下）]]"
source_ids:
  - "8231"
  - "8265"
  - "8338"
  - "8397"
  - "8601"
  - "9403"
  - "9431"
  - "9444"
  - "9603"
  - "9675"
  - "9706"
  - "9708"
  - "9728"
  - "9731"
  - "9859"
  - "9948"
  - "10040"
  - "10122"
  - "10862"
  - "10907"
  - "11111"
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-03-08-Transformer升级之路-1-Sinusoidal位置编码追根溯源.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-03-23-Transformer升级之路-2-博采众长的旋转式位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-04-22-Transformer升级之路-3-从Performer到线性Attention.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2021-05-10-Transformer升级之路-4-二维位置的旋转式位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-06-Transformer升级之路-5-作为无限维的线性Attention.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-12-28-Transformer升级之路-6-旋转位置编码的完备性分析.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-12-Transformer升级之路-7-长度外推性与局部注意力.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-01-31-Transformer升级之路-8-长度外推性与位置鲁棒性.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-05-12-Transformer升级之路-9-一种全局长度外推的新思路.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-06-Transformer升级之路-10-RoPE是一种β进制编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-07-31-Transformer升级之路-11-将β进制位置进行到底.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-07-Transformer升级之路-12-无限外推的ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-14-Transformer升级之路-13-逆用Leaky-ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-08-24-Transformer升级之路-14-当HWFA遇见ReRoPE.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2023-11-20-Transformer升级之路-15-Key归一化助力长度外推.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-01-26-Transformer升级之路-16-复盘-长度外推技术.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-03-29-Transformer升级之路-17-多模态位置编码的简单思考.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2024-05-29-Transformer升级之路-18-RoPE的底数选择原则.md
  - Data/Spaces_ac_cn/markdown/Mathematics/2025-04-18-Transformer升级之路-19-第二类旋转位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-05-04-Transformer升级之路-20-MLA好在哪里-上.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2025-07-10-Transformer升级之路-21-MLA好在哪里-下.md
prerequisites:
  - "[[Attention]]"
  - "[[RoPE]]"
checkpoints:
  - Sinusoidal和RoPE如何用绝对编码实现相对位置效果？
  - 线性Attention的低秩瓶颈和标准Attention的无限维视角如何统一？
  - 长度外推失败分别来自位置越界和注意力熵变化中的哪一类不一致？
  - NTK-RoPE、ReRoPE、HWFA2、KeyNorm分别改变了位置编码、注意力结构还是训练约束？
  - Partial RoPE、NoPE和KV共享如何进入MLA的训练/解码折中？
next_paths:
  - "[[Transformer架构与归一化]]"
  - "[[Attention归一化与线性化阅读路径]]"
  - "[[LLM架构与上下文扩展]]"
status: draft
updated: 2026-06-14
---

# Transformer升级之路阅读路径

## 主线

1. `8231 -> 8265`：从Sinusoidal的相对距离解释进入RoPE构造。
2. `8338 -> 8601`：理解线性Attention的低秩/稀疏瓶颈，并回到标准Attention的无限维解释。
3. `9403 -> 10122`：沿RoPE完备性、β进制、混合进制和底数下界理解位置编码设计空间。
4. `9431 -> 9948`：沿长度外推诊断、HWFA、NTK-RoPE、ReRoPE、InvLeaky ReRoPE、HWFA2、KeyNorm和复盘建立技术谱系。
5. `10040 -> 11111`：从多模态/VO-RoPE进入Partial RoPE、NoPE、KV共享和MLA最优性分析。

## 使用方式

如果目标是RoPE理论，优先读 `8231, 8265, 8397, 9403, 9675, 10122, 10862`。如果目标是长上下文工程，优先读 `9431, 9444, 9603, 9675, 9706, 9708, 9728, 9731, 9859, 9948`。如果目标是MLA，先读 `10122, 10862, 10907, 11111`，再回看 `9675` 和 `9948` 补足位置编码与外推视角。
