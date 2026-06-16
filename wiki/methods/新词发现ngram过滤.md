---
type: method
title: 新词发现ngram过滤
aliases: []
operation_types:
  primary: Decompose / reduce dimension
  secondary:
    - Estimate / sample instead of compute
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-09-09-重新写了之前的新词发现算法-更快更好的新词发现.md
  - Data/Spaces_ac_cn/markdown/Big-Data/2018-05-31-基于最小熵原理的NLP库-nlp-zero.md
source_ids:
  - "6920"
  - "5597"
method_summary: 通过统计ngram频数和互信息从大规模语料中无监督提取候选词，使用KenLM的count_ngrams高效统计，Trie树加速搜索，多级过滤（频数+互信息）控制质量。
typical_structure: |
  1. 使用KenLM的count_ngrams统计各长度ngram
  2. 按互信息阈值过滤低质量ngram
  3. 构建Trie树
  4. 利用Trie树进行预分词获取候选词
  5. 频数过滤+互信息回溯过滤
applicability: 适用于需要从大规模无标注语料中构建词库的场景。对以字为基础单位的语言（如中文）特别有效。需要Linux环境和KenLM编译支持。
tools:
  - KenLM count_ngrams
  - Trie 树
  - 互信息过滤
related_methods:
  - [[基于最小熵原理的无监督分词]]
  - [[线性链CRF构建]]
examples:
  - [[article::6920]]
  - [[article::5597]]
status: draft
updated: 2026-06-14
---

## 适用问题

中文等以字为基础单位的语言中，词的边界不明确。从大规模无标注语料中自动发现新词（未登录词）对分词、关键词提取等任务至关重要。传统方法依赖手工规则或标注数据，效率低且覆盖面有限。基于 ngram 统计和互信息的无监督新词发现方法可在千万级语料中高效提取候选词。

## 核心变换

**输入**：大规模无标注语料（纯文本）
**输出**：候选新词列表（含频数和互信息得分）
**核心**：统计 ngram 频数 + 互信息过滤 + Trie 树加速

### 互信息计算

对于长度为 $n$ 的 ngram $w_1 w_2 \dots w_n$，其互信息衡量内部凝聚度：

对于 2-gram，点互信息：
$$
PMI(w_1, w_2) = \log \frac{p(w_1 w_2)}{p(w_1)p(w_2)}
$$

对于更高阶 ngram，使用最小互信息：
$$
MI_{min} = \min_{k} \log \frac{p(w_1 \dots w_n)}{p(w_1 \dots w_k)p(w_{k+1} \dots w_n)}
$$

### Trie 树加速

构建所有候选 ngram 的 Trie 树，在语料上利用 Trie 树进行最大匹配预分词，快速筛选出可能的词边界。

## 典型步骤

1. **ngram 统计**：使用 KenLM 的 count_ngrams 高效统计语料中各长度 ngram（1-gram 到 6-gram）的频数
2. **互信息过滤**：计算每个 ngram 的互信息，低于阈值的 ngram 被过滤
3. **Trie 树构建**：将剩余候选 ngram 构建为 Trie 树
4. **预分词匹配**：在语料上用 Trie 树进行预分词匹配，获取候选词
5. **回溯过滤**：结合频数阈值和互信息得分进行多级过滤，控制输出质量

## 直觉

核心思想：**真正的词内部成分之间应该紧密结合**。

新词发现的核心假设是：如果一个 ngram 是一个真正的词，其内部字符应该"紧密结合"，而不会被外部字符"拆散"。

互信息量化了这个直觉：$p(AB) \gg p(A)p(B)$ 意味着 A 和 B 经常一起出现，它们是一个词的可能性高。反之，如果 $p(AB) \approx p(A)p(B)$，则 A 和 B 只是碰巧相邻，不是词。

Trie 树的作用是加速——在数千亿字符的语料中，暴力计算所有 ngram 的频数是不现实的。Trie 树可以将匹配过程从 $\mathcal{O}(n^2)$ 降到 $\mathcal{O}(n)$，同时支持最大匹配分词。

## 边界

- 需要 Linux 环境和 KenLM 编译支持（`count_ngrams` 是 KenLM 工具）
- 仅输出频数+互信息得分，不保证 100% 召回所有真实新词
- ngram 窗口通常限制在 2-6 字，超过此范围的词汇（如成语、专业术语）可能遗漏
- 互信息阈值需根据语料规模和语言特点调参
- 对低频新词（语料中出现次数少于阈值）天然不敏感

## 例子

- 从千万级新闻语料中提取新词："新冠""健康码""双减"等时代热词
- nlp-zero 库中基于最小熵原理的新词发现实现
- 改进版算法将处理速度提升数倍，可在数小时内完成千万级语料的新词发现

## 证据

- ev::6920::KenLM count_ngrams 高效统计 ngram 的方法
- ev::6920::Trie 树加速预分词匹配
- ev::6920::频数 + 互信息多级过滤流程
- ev::5597::基于最小熵原理的新词发现理论基础
