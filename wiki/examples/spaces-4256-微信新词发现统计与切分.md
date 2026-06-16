---
type: example
title: 'spaces-4256: 微信新词发现统计与切分'
article_id: '4256'
article:
- - wiki/sources/spaces-4256-新词发现算法.md
section: 详细的算法
claim: 结合多阶内部凝固度筛选、粗糙切分频数统计以及回溯检查三步骤过滤出合格新词。
notation_mapping:
  ngrams: ngrams (各阶字串频数统计字典)
  ngrams_: ngrams_ (高内聚性片段的哈希集合)
  words: words (粗糙分词频数统计)
  w: w (最终回溯验证通过的新词字典)
steps:
- step: 1
  description: 遍历清洗后的文本，滑动窗口统计 1 到 4 字片段的频数并保存到 `ngrams` 中。
- step: 2
  description: 对所有频数大于阈值（如128）的片段，计算多阶内部凝固度。对 2-gram、3-gram、4-gram 分别用 5、25、125 的凝固度阈值进行筛选，得到高凝聚力集合
    `ngrams_`。
- step: 3
  description: 定义粗切分规则。使用 `ngrams_` 内的片段对句子做标记：在每个字符间隔，如果其前后字属于某个在 `ngrams_` 中的片段，则计数累加。累加大于
    0 的间隔在切分时不予断开，从而获得粗糙切分的词列表。
- step: 4
  description: 遍历语料执行上述粗切分，并统计切分出的词频，保存高频词至 `words` 中。
- step: 5
  description: 针对 `words` 中的每个高频候选词进行“回溯验证”：若词长 $\ge 3$，遍历检查其所有长度在 3 到 4 之间的连续子串是否都在
    `ngrams_` 中。
- step: 6
  description: 只要有一个子串不在 `ngrams_` 中（说明部分内部并不结实），则 `is_real` 返回 `False`。将不合格的拼接词（如“各项目”）剔除，输出最终精简干净的词典
    `w`。
used_concepts:
- - - concept::中文分词
- - - concept::新词发现
used_formulas:
- - - wiki/formulas/多阶凝固度公式.md
used_methods:
- - - method::多阶凝固度与回溯过滤新词发现
source_span: ev::4256::算法三步骤
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2017-03-11-中文分词系列-8-更好的新词发现算法.md
source_ids:
- '4256'
status: draft
updated: '2026-06-12'
---

# spaces-4256: 微信新词发现统计与切分

本例展示了利用多阶凝固度粗筛、粗匹配切分以及子串回溯过滤的完整代数步骤，用以验证如何以较低的计算成本快速提取出语料中的真实新词。

## 算法大意与凝固度公式

分词就是为了削弱相关性，降低对词序的依赖。本文就是在前文的基础上改进，那里只考虑了相邻字的凝固度，这里同时考虑多字的内部的凝固度（ngrams），比如，定义三字的字符串内部凝固度为：
$$
\min\left\{\frac{P(abc)}{P(ab)P(c)},\frac{P(abc)}{P(a)P(bc)}\right\}
$$
这个定义其实也就是说，要枚举所有可能的切法，因为一个词应该是处处都很“结实”的，4字或以上的字符串凝固度类似定义。一般地，我们只需要考虑到4字（4grams）就好（但是注意，我们依旧是可以切出4字以上的词来的）。

## 代码实现参考

下面给出一个参考的代码实现。首先，为了节约内存，写一个迭代器来逐篇输出文章：

```python
import re
import pymongo
from tqdm import tqdm
import hashlib

db = pymongo.MongoClient().weixin.text_articles
md5 = lambda s: hashlib.md5(s).hexdigest()

def texts():
    texts_set = set()
    for a in tqdm(db.find(no_cursor_timeout=True).limit(3000000)):
        if md5(a['text'].encode('utf-8')) in texts_set:
            continue
        else:
            texts_set.add(md5(a['text'].encode('utf-8')))
            for t in re.split(u'[^\u4e00-\u9fa50-9a-zA-Z]+', a['text']):
                if t:
                    yield t
    print u'最终计算了%s篇文章' % len(texts_set)
```

接着，直接计数：

```python
from collections import defaultdict
import numpy as np

n = 4
min_count = 128
ngrams = defaultdict(int)

for t in texts():
    for i in range(len(t)):
        for j in range(1, n+1):
            if i+j <= len(t):
                ngrams[t[i:i+j]] += 1

ngrams = {i:j for i,j in ngrams.iteritems() if j >= min_count}
total = 1.*sum([j for i,j in ngrams.iteritems() if len(i) == 1])
```

接着就是凝固度的筛选了：

```python
min_proba = {2:5, 3:25, 4:125}

def is_keep(s, min_proba):
    if len(s) >= 2:
        score = min([total*ngrams[s]/(ngrams[s[:i+1]]*ngrams[s[i+1:]]) for i in range(len(s)-1)])
        if score > min_proba[len(s)]:
            return True
    else:
        return False

ngrams_ = set(i for i,j in ngrams.iteritems() if is_keep(i, min_proba))
```

定义切分函数，并进行切分统计：

```python
def cut(s):
    r = np.array([0]*(len(s)-1))
    for i in range(len(s)-1):
        for j in range(2, n+1):
            if s[i:i+j] in ngrams_:
                r[i:i+j-1] += 1
    w = [s[0]]
    for i in range(1, len(s)):
        if r[i-1] > 0:
            w[-1] += s[i]
        else:
            w.append(s[i])
    return w

words = defaultdict(int)
for t in texts():
    for i in cut(t):
        words[i] += 1

words = {i:j for i,j in words.iteritems() if j >= min_count}
```

最后，回溯：

```python
def is_real(s):
    if len(s) >= 3:
        for i in range(3, n+1):
            for j in range(len(s)-i+1):
                if s[j:j+i] not in ngrams_:
                    return False
        return True
    else:
        return True

w = {i:j for i,j in words.iteritems() if is_real(i)}
