---
type: article_summary
title: 【不可思议的Word2Vec】 4.不一样的“相似”
article_id: "4368"
source_url: https://spaces.ac.cn/archives/4368
date: 2017-05-01
category: Big-Data
source_markdown: Data/Spaces_ac_cn/markdown/Big-Data/2017-05-01-不可思议的Word2Vec-4-不一样的-相似.md
series:
  - [[不可思议的Word2Vec]]
concepts:
  - [[Word2Vec]]
  - [[Skip-Gram]]
  - [[Hierarchical Softmax]]
  - [[点互信息PMI]]
methods:
  - [[基于Word2Vec计算相关词]]
formulas:
  - [[词向量余弦相似度]]
  - [[基于点互信息PMI的相关词度量]]
examples:
  - [[spaces-4368-广州相关词计算]]
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2017-05-01-不可思议的Word2Vec-4-不一样的-相似.md
source_ids:
  - "4368"
status: draft
updated: 2026-06-11
---

# 【不可思议的Word2Vec】 4.不一样的“相似”

## 内容概要
文章探讨了词语“相似”在不同应用场景下的不同数学定义。除了常规的余弦相似度（衡量搭配的一致性或可替换性）之外，作者提出用“点互信息（PMI）”来定义“相关性”，并利用 Skip-Gram 模型的条件概率输出来寻找与输入词最相关的词汇。

## 关键内容
1. **余弦相似度的局限性**：余弦相似度只反映两个词的上下文平均分布是否一致，代表了句子结构上的“可替换性”（如“广州”的最相似词是“东莞”、“深圳”）。
2. **点互信息（PMI）度量相关度**：在推荐系统、多义词推断等场景中，用户往往希望获得的是地理或语义强相关的关联词（如“广州”的相关词为“白云机场”、“光孝寺”）。互信息定义为：
   $$\text{PMI}(x, y) = \log \frac{P(x, y)}{P(x)P(y)} = \log P(y|x) - \log P(y)$$
3. **基于词频调节的修正指标**：为提高高频词的可读性，引入调节常数 $\alpha$（通常取 0.9）：
   $$\text{Score}(y|x) = \log P(y|x) - \alpha \log P(y)$$
   在代码实现中，利用 Skip-Gram 的 Huffman Softmax 近似预测条件概率对数 $\log P(y|x)$，结合频数对数进行计算。
4. **劣势**：在预测阶段，当需要遍历整个词典寻找最大互信息词汇时，层次 Softmax 的求概率步骤比原生 Softmax 更慢。
