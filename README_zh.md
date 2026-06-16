# cognitive-knowledge-network

[English](README.md)

`cognitive-knowledge-network` 是一个面向 人类与Agent 的本地认知知识库与技能包，该仓库将Sujianlin的blog进行了整理，形成了一份面向概念与方法的“认知型知识网络”，并整理成了面向人类阅读友好的可视化wiki与面向agent阅读友好的skill。

这个公开仓库分发的是技能、schema、文档和派生知识层，不包含原始 `Data/`语料，`Data/`是对苏剑林博客材料进行本地采集、整理后形成的归档，包含从原始页面转换得到的 markdown 以及相关资源文件。但Data并不是必须的，graph下已经有足够的内容了。这个仓库的核心是启发式的关系，其次才是内容。

## 什么是 Cognitive Knowledge Network？

Cognitive Knowledge Network 是一个以“方法论”为中心的本地认知知识库。它建立在苏剑林（Scientific Spaces / 科学空间，`kexue.fm` / `spaces.ac.cn`）博客语料之上，充当一个知识编译层，把非结构化文章转换为结构化、可机器遍历、并带有证据支撑的数学概念与可迁移方法网络。

它不同于传统 wiki。传统 wiki 更偏向静态描述；普通 RAG 更偏向检索原始文本片段。这个网络试图把数学与模型设计中的想法编译成适合 AI Agent 和研究者使用的逻辑结构。

## 它解决什么问题？

- `浅层检索无法恢复推导链`：普通搜索能找到文章，但往往不能回答一个公式如何推导、
  一个优化器为什么有效、一个思想如何跨主题迁移。这个仓库通过
  `requires`、`derives`、`expresses_method`、`shares_pattern_with`、
  `verified_by` 等类型化关系来表达深层逻辑联系。
- `数学符号与记号不一致`：跨年份、跨主题、跨系列文章时，记号经常变化。这个网络
  采用双层策略：在 `concept` 和 `formula` 页面定义标准记号，在 `example`
  页面保留源文记号并通过映射关系连接二者。
- `概念膨胀与方法爆炸`：为了避免 Agent 随意发明重复概念或临时方法，仓库采用
  match-first, create-last 的分类策略，优先复用已有对象，再谨慎新增。
- `知识演化与修正`：科学观点会随时间变化。这个网络通过 `updates`、`corrects`、
  `refines`、`alternative_view_of` 等边来表达显式的时间演化与逻辑修订。

## 它能做什么？

整个系统可以理解为五层结构：

1. `源证据层`：保存不可变的原始材料，用于事实审计与回溯。公开 GitHub 版本中，
   这一层只保留边界说明，不直接打包。
2. `编译 wiki 层`：把内容组织成 `concept`、`method`、`formula`、
   `proposition`、`series`、`problem_pattern`、`example`、
   `reading_path` 等页面类型。
3. `认知图层`：把编译后的页面翻译为机器可遍历的节点与类型化边，支持图遍历、
   路径搜索和局部结构分析。
4. `质量闭环层`：通过 lint 和基于查询的 probes 检查孤立节点、缺少证据的断言、
   记号缺失等结构性问题。
5. `Agent 接口层`：提供 API 与 skill 接口，支持有界子图查询、源文定位、
   阅读路径恢复以及结构化研究产物生成。

## 对你有什么价值？

### 面向模型设计的深层数学洞见

你不需要只复制公式，而是可以沿着网络去理解高级深度学习设计背后的生成逻辑，
包括 Muon、MuP、RoPE、SSM、MoE、Diffusion 等相关主题。

例如：

- 为什么 embedding 或 LM head 矩阵不适合用 Muon 优化？
- 奇异值熵密度的推导链条是什么？
- RoPE 的几何表示如何转化为相对位置编码？

### 结构化学习与阅读路径

仓库会把系列文章编译成结构化阅读路径，用户可以按时间顺序和概念依赖学习一个主题，
而不是零散地阅读单篇博客。

### 面向 AI Agent 的本地数学工具

Agent 可以通过本地 API 查询有源文依据的数学知识、定位支持段落、检查假设条件，
从而在写代码、做笔记、生成解释时降低幻觉风险。

### 知识工程与 Agentic RAG 的参考实现

如果你在构建知识图谱、Agent 工作流或本地 RAG 系统，这个仓库也可以作为参考实现：
它展示了如何使用 JSONL 图 schema、类型化证据链接、验证循环和诊断 probes来构建一个可编译、可校验的本地知识库。

## 可视化界面

这个 skill 还提供了一个可视化界面，用于浏览图谱结构与查看节点详情。

![全局图谱视图](figures/Screenshot%202026-06-16%20at%2013.49.49.png)

_全局图谱视图，包含节点类型筛选与布局控制。_

![节点详情视图](figures/Screenshot%202026-06-16%20at%2013.50.27.png)

_聚焦局部图谱时，可在侧边栏查看方法级摘要、适用问题与步骤结构。_

## 仓库结构

- `SKILL.md`：skill 入口
- `skill/`：Python 辅助工具与 skill 文档
- `schema.md`：页面与图结构约束
- `wiki/`：派生知识页面
- `graph/`：结构化图谱内容
- `purpose.md`：仓库目标与边界（如果后续加入）
- `docs/`：设计与流程文档（如果后续加入）
- `probes/`：验证与诊断产物（如果后续加入）

`Data/` 有意不包含在公开 GitHub 包中。

## 许可

这是一个混合许可仓库。

### MIT 层

除非文件另有说明，MIT License 适用于软件与工程层，包括：

- `SKILL.md`
- `skill/`
- `visualize.py`
- `visualize.html`
- `schema.md`
- `README.md`
- `README_zh.md`
- `.gitignore`
- 构建、测试、打包相关文件
- 如果后续加入的 `purpose.md`
- 如果后续加入的 `docs/`

见 [LICENSE](LICENSE)。

### CC BY-NC-SA 4.0 内容层

除非文件另有说明，下列派生知识目录采用 CC BY-NC-SA 4.0：

- `figures/`
- `wiki/`
- `graph/`
- 如果后续加入的 `probes/`

这些目录不在 MIT 覆盖范围内。

见 [LICENSE-content.md](LICENSE-content.md)。

## 上游来源说明

本仓库围绕苏剑林博客语料的派生内容构建。

- 原作者：苏剑林
- 原站点：`https://spaces.ac.cn/` 与 `https://kexue.fm/`

`wiki/` 与 `graph/` 目录由本仓库维护者进行了整理、筛选和结构化表达，因此其中包含
维护者自己的组织性贡献。但它们仍然是基于上游博客语料形成的派生内容，因此按
CC BY-NC-SA 4.0 分发，而不是 MIT。

如果文件元数据或页面 frontmatter 中保留了上游署名与来源信息，下游再分发时应继续保留。
