---
type: example
title: NL2SQL的动态表头编码实例
article_id: "6771"
article: [[spaces-6771-基于Bert的NL2SQL模型-一个简明的Baseline]]
section: 模型结构
claim: 利用BERT同时编码问题和动态表头进行联合特征学习
notation_mapping:
  BERT(Q, H): BERT(Q, H)
steps:
  - 步骤1：输入问句 Q 和该表头对应的所有列名 H，构造形如 [CLS] Q [SEP] [CLS] H_1 [SEP] [CLS] H_2 [SEP] 的联合输入。
  - 步骤2：输入BERT获取编码序列。问句开头的 [CLS] 向量用于判断条件联结符（AND, OR, NIL）。
  - 步骤3：对每个 H_i 开头的 [CLS] 向量进行 7 分类预测，同时确定该列是否被选中以及被选中的 Aggregator 函数类型。
  - 步骤4：通过字标注抽取出条件值，利用字表征与各列名表征的内积相似度对条件值进行列匹配。
used_concepts:
  - [[NL2SQL]]
source_span: ev::6771::联合编码
sources:
  - Data/Spaces_ac_cn/markdown/Big-Data/2019-06-29-基于Bert的NL2SQL模型-一个简明的Baseline.md
source_ids:
  - "6771"
status: stable
updated: 2026-06-12
---

# NL2SQL的动态表头编码实例

本实例说明了基于哈工大/谷歌 BERT 模型在中文首届 NL2SQL 挑战赛中的基线构建过程。

例如，输入自然语言问句为“世茂茂悦府新盘容积率大于1，请问它的套均面积是多少？”，该句对应的数据库表格列名有 `项目名称`、`容积率`、`套均面积` 等。模型通过联合输入编码后，`套均面积` 列对应的特征向量预测分类为“SELECT 且无 AGG”（前 6 类之一），`项目名称` 预测为不选（第 7 类）。字标注提取出条件值 `世茂茂悦府`，其与列名 `项目名称` 的编码特征相似度计算值最高，因而被正确归类到该列的约束中。
