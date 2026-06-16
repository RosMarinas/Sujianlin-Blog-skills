---
type: example
title: 网页翻译与延时加载兼容实现
article_id: 10320
article: '[[spaces-10320-让MathJax更好地兼容谷歌翻译和延时加载]]'
section: 总结一下
claim: 使用notranslate类在前端排版Queue中控制动态翻译与Typeset流程
notation_mapping:
  （待从源文章提取）: （待从源文章提取）
steps:
- 1. 在HTML中为含公式的段落添加class="notranslate"
- 2. MathJax.Hub.Queue中注册回调函数
- 3. 在Typeset完成后，给.MathJax加notranslate，并移除标题/段落的notranslate类以触发谷歌翻译
used_concepts:
- '[[（待从源文章提取）]]'
used_formulas: []
used_methods:
- - - MathJax翻译与延时加载兼容方法
source_span: ev::10320::逆向思维
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2024-08-15-让MathJax更好地兼容谷歌翻译和延时加载.md
source_ids:
- 10320
status: draft
updated: '2026-06-12'
---

# 网页翻译与延时加载兼容实现

该实例展示了如何在前端（如 Cool Papers）实现 MathJax 公式渲染与 Chrome 浏览器自带网页自动翻译（谷歌翻译）的完美结合。对于带有经 MathJax 2.7.9 渲染的数学公式的页面，由于公式在前端实时生成，普通的谷歌翻译通常会破坏公式的内部 DOM 结构从而导致页面乱码。

为了解决这一问题，核心的逆向思维方案是利用谷歌翻译的免翻机制：通过给特定的 DOM 元素添加 `class="notranslate"` 或 `translate="no"` 属性来阻止翻译引擎处理公式节点。具体的执行队列控制流程如下：

1. **预处理拦截**：在页面加载初期，直接为包含 LaTeX 公式代码的标题和摘要等父级段落容器添加 `class="notranslate"` 类，建立“免翻金牌”，避免在 MathJax 尚未渲染完成时被谷歌翻译提前处理而破坏原始内容。
2. **队列回调注册**：在前端逻辑中，利用 `MathJax.Hub.Queue` 注册自定义的回调函数，确保后续的 DOM 操作严格在 MathJax 的 `Typeset` 排版渲染流程彻底执行完毕后触发。
3. **精准保护与释放**：在公式渲染完成后，回调函数首先会遍历所有新生成的 `.MathJax` 公式节点，并为它们精准打上 `notranslate` 类属性；随后，安全地移除第一步中附加在父级标题或段落上的 `notranslate` 类。此操作会动态触发谷歌翻译的重新检测，从而使得周围的纯英文文本被正常翻译，而渲染好的数学公式本身则得到了完整保护。
