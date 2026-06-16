---
type: example
title: 网页数学公式自适应窗口缩放
article_id: 10474
article: '[[spaces-10474-让MathJax的数学公式随窗口大小自动缩放]]'
section: 代码参考
claim: 通过判断公式父类区分行内和单行，计算溢出宽度并缩放其font-size
notation_mapping:
  （待从源文章提取）: （待从源文章提取）
steps:
- 1. 在MathJax初始化配置中移除公式自动折行配置
- 2. 遍历所有MathJax-Element开头的公式节点
- 3. 根据endsWith('isplay')判断是否为单行公式，相应测量父或祖父容器宽度
- 4. 若公式偏宽，动态计算比例设置其style.fontSize百分比
used_concepts:
- '[[（待从源文章提取）]]'
used_formulas: []
used_methods:
- - - MathJax公式自适应窗口大小缩放方案
source_span: ev::10474::代码参考
sources:
- Data/Spaces_ac_cn/markdown/Big-Data/2024-10-15-让MathJax的数学公式随窗口大小自动缩放.md
source_ids:
- 10474
status: draft
updated: '2026-06-12'
---

# 网页数学公式自适应窗口缩放

该示例展示了在网页环境中，如何通过结合 MathJax 初始化配置与自定义的 JavaScript 逻辑，使数学公式能够如同设置了 `max-width: 100%` 的图片一样，根据可用容器宽度自适应屏幕与窗口缩放。

具体实现中，首先在 MathJax 的配置中移除了基于 `linebreaks: {automatic: true}` 的自动折行机制。移除该项是因为在面对超长公式时，强行折行往往会破坏预排版公式的结构与美观度，而本文方案旨在保持公式原有排版连贯性的前提下，通过整体比例缩放其尺寸来适配移动端或窄视口。

核心的动态缩放逻辑依赖于 `MathJax.Hub.Queue`，在所有公式完全渲染完毕后触发执行。脚本通过 `document.querySelectorAll('span[id^="MathJax-Element"]')` 抓取页面上所有被 MathJax 渲染出的公式节点，并对每个节点（`e`）依次进行容器宽度与内容宽度的比对：

1. **容器可用宽度判定**：判断公式的直接父节点的 `className` 是否以 `'isplay'` 结尾（例如 `.MathJax_Display`、`.MJXc-display` 及其它包含 Display 标识的类）。如果符合，说明该公式是独立成行的“单行公式”，且外围多嵌套了一层区块容器 `div`，因此真正的可用容器宽度应取其祖父节点 `e.parentNode.parentNode.offsetWidth`；否则为“行内公式”，可用宽度直接取其父节点 `e.parentNode.offsetWidth`。
2. **计算溢出并设置字体大小**：通过对比判定，如果公式内容自身的真实宽度 `e.offsetWidth` 严格大于获取到的可用宽度 `parentWidth`，表明公式在当前视口发生溢出。此时，计算缩放比 `parentWidth * 100 / e.offsetWidth`，并将计算所得的百分比动态附加 `%` 符号后赋值给公式节点的 `e.style.fontSize`。

借由这一 CSS/JS 混合控制逻辑，无论是行内嵌套的局部长公式还是占据整行的大型等式块，都能避免横向溢出视口界限的问题。公式基于文字大小调整自动等比缩小，无需依赖于容易造成混乱的自动换行（reflow），在底层实现了与图片相似的响应式自适应特性。
