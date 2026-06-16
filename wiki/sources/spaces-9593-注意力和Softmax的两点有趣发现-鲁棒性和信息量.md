---
type: article_summary
title: 注意力和Softmax的两点有趣发现：鲁棒性和信息量
article_id: 9593
source_url: https://spaces.ac.cn/archives/9593
date: 2023-04-25
category: Mathematics
source_markdown: |
  Data/Spaces_ac_cn/markdown/Mathematics/2023-04-25-注意力和Softmax的两点有趣发现-鲁棒性和信息量.md
sources:
  - Data/Spaces_ac_cn/markdown/Mathematics/2023-04-25-注意力和Softmax的两点有趣发现-鲁棒性和信息量.md
source_ids:
  - 9593
status: draft
updated: 2026-06-12
---

# 注意力和Softmax的两点有趣发现：鲁棒性和信息量

本文分享了作者关于Softmax注意力机制的两个有趣理论发现：
1. 鲁棒性：在注意力得分（logits）中加入独立同分布的噪声后，注意力输出值基本保持不变。这是因为在序列长度较大时，根据大数定律，乘性噪声期望在分子和分母中可以近似提取出来并相互抵消，展示了Softmax注意力的天然抗噪能力。
2. 信息量：从信息熵的角度解释了注意力机制的初始化和对比学习中的温度参数 $	au$。如果初始化使得logits过大，Softmax将退化为one-hot分布，此时信息熵（不确定性度量）为0，优化器“无利可图”导致梯度消失。因此应将模型初始化得尽量均匀以最大化可榨取的信息量。在对比学习中，缩小温度参数 $	au$ 能将信息熵的下界从约 $\log n - 0.4745$ 降低到接近 0，从而显著增加模型能获得的信息量。