# Learning WebGL

Learn WebGL in Baby's steps.

---
## REGL 简化了 WebGL 的什么？

WebGL 这类工具的学习曲线较为陡峭，因为它虽然工作在 javascript 上，但渲染过程中却会直接用到 C 代码。这样做的原因是由于它在渲染的实现过程中，需要用户自己定义每个 shader 的渲染行为。WebGL 的渲染过程是严格规范化的过程，因此 REGL 对它进行了包装。用户只需要调用这样的函数即可实现渲染。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

## WebGL 的 texture 入门

缓冲器是 WebGL 的重要组成部分，它用来缓冲一张图像，本文说明它的基本使用逻辑。为了让本文不会过于无聊，本文实现了图像颜色空间的随机化，它保证了在原始图像上连续的颜色在新的颜色空间上还是连续的。又由于随机过程中含有时间变量，因此新的颜色空间是实时变化的。这就形成了一种奇怪的动态效果。得益于 WebGL 的优秀性能，这个过程是实时的，帧率可以达到显示器的刷新率。

[WebGL Texture Usage](https://observablehq.com/@listenzcc/webgl-texture-usage)

## WebGL 的简要入门

优秀的 WebGL 工程代码是开源的，但除了好看之外几乎利用不上。这些没有注释、难以理解其复杂计算过程的代码满天乱飞，乍看起来它们已经足够酷炫和好用，导致继续花时间开发相似的功能就只有成本，但没有意义。而事实是，一旦落实到实际需求上，除了被抄一遍之外，它们无一例外地没有进一步修改的余地。因此，为了让我自己能够在将来的某一天，看得懂、改得动这些代码，我决定开始这个话题。

## WebGL 页面中有用的 IDE 工具

虽然集成开发环境（IDE）这个概念有点大，但在 WebGL 开发和调试过程中，需要用到 C 和 JS 混合编程的技巧，因此顺手的开发工具有助于提升开发效率。
除此之外， 本文提供的样例渲染过程看上去是透过三角碎片观察一个完整的 HSV 调色板。为了强化这个过程，我在图上渲染了一个圆环，它的半径是 $0.3$。这种渲染思路可以解决一些科学绘图问题，这些问题满足如下条件

> 要绘制某个区域内的全部点，而这些点的颜色有解析的表达式，可以表示为 $color = f(x, y)$ 的形式。
> 

[WebGL's Simple Animation & Stats & Code-Prettify](https://observablehq.com/@listenzcc/webgls-template)

## 三角 shader 的重心坐标系

前文遗留了一个问题，那就是如何使用 WebGL 渲染平移不变的三角 shader。本文尝试使用重心坐标系解决这个问题。为了体现重心坐标的意义和作用，我还增加了 wireframe 的线绘制方法。另外，前文的三角形端点移动方法并不令人满意，因此本文更换成 simplex-noise 方法，它使端点的运动看上去更加自然、柔和。

[Barycentric coordinate in WebGL](https://observablehq.com/@listenzcc/barycentric-coordinate-in-webgl)

## 离散、连续和插值：WebGL 的 vertex 与 fragment

本篇是对上篇的进一步解释和说明，尝试说明在 WebGL 的渲染过程中，程序是如何处理端点（vertex）和光栅片（fragment）之间的关系。这是一种离散、连续和插值之间的微妙关系，它们的背后是令人叹为观止的优秀工程实现。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)
