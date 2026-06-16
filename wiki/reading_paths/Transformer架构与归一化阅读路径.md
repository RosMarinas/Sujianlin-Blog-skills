---
type: reading_path
title: Transformer架构与归一化阅读路径
aliases: []
goal: 按结构设计顺序理解 Transformer 的注意力低秩瓶颈、静态/门控注意力、RoFormerV2、Pre/Post Norm 和相对位置缺陷。
audience: 需要从 series 层快速进入文章顺序、方法节点和检索关键词的读者。
ordered_nodes:
  - "[[spaces-7325]]"
  - "[[spaces-7430]]"
  - "[[spaces-7661]]"
  - "[[spaces-8130]]"
  - "[[spaces-8610]]"
  - "[[spaces-8934]]"
  - "[[spaces-8990]]"
  - "[[spaces-8998]]"
  - "[[spaces-9009]]"
  - "[[spaces-9105]]"
source_ids:
  - "7325"
  - "7430"
  - "7661"
  - "8130"
  - "8610"
  - "8934"
  - "8990"
  - "8998"
  - "9009"
  - "9105"
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-04-13-突破瓶颈-打造更强大的Transformer.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-05-25-Google新作Synthesizer-我们还不够了解自注意力.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2020-08-07-修改Transformer结构-设计一个更快更好的MLM模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-02-03-让研究人员绞尽脑汁的Transformer位置编码.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2021-08-09-线性Transformer应该不是你要等的那个模型.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-02-25-FLASH-可能是近来最有意思的高效Transformer设计.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-11-门控注意力单元-GAU-还需要Warmup吗.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-21-RoFormerV2-自然语言理解的极限探索.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-03-29-为什么Pre-Norm的效果不如Post-Norm.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2022-06-07-相对位置编码Transformer的一个理论缺陷与对策.md
checkpoints:
  - 增大 key_size 与 Talking-Heads 分别修补什么瓶颈？
  - GAU/FLASH 如何把注意力和 FFN 融合？
  - Pre-Norm 深层退化为什么会发生？
next_paths:
  - [[Attention归一化与线性化阅读路径]]
  - [[Transformer升级之路阅读路径]]
status: draft
updated: 2026-06-14
---

# Transformer架构与归一化阅读路径

## 阅读顺序

1. 突破瓶颈，打造更强大的Transformer
2. Google新作Synthesizer：我们还不够了解自注意力
3. 修改Transformer结构，设计一个更快更好的MLM模型
4. 让研究人员绞尽脑汁的Transformer位置编码
5. 线性Transformer应该不是你要等的那个模型
6. FLASH：可能是近来最有意思的高效Transformer设计
7. 门控注意力单元-GAU-还需要Warmup吗
8. RoFormerV2-自然语言理解的极限探索
9. 为什么Pre-Norm的效果不如Post-Norm
10. 相对位置编码Transformer的一个理论缺陷与对策

## 读完应能回答

- 增大 key_size 与 Talking-Heads 分别修补什么瓶颈？
- GAU/FLASH 如何把注意力和 FFN 融合？
- Pre-Norm 深层退化为什么会发生？
