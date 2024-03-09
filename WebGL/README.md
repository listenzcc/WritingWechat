# Learning WebGL

Learn WebGL in Baby's steps.

---
## Hessian 与梯度结合

本文讲述了利用 Hessian 提供的二阶信息确定梯度下降最优步长的方法，这种梯度下降法只进行了 10 次迭代即可找到极小值，这说明该方法大大提高了寻优效率，并且有机会跳出局部最优值，受起始点影响更小。

本文代码还是在我的 ObservableHQ 笔记本上。

[Searching maximum by Hessian (Improve)](https://observablehq.com/@listenzcc/searching-maximum-by-hessian-improve)

## Hessian 粗解

Newton 法是一种迭代优化算法，用于求解非线性优化问题。它利用目标函数的二阶导数信息（Hessian 矩阵）来进行迭代，以更快地收敛到局部最小值。尽管 Newton 法在很多情况下具有快速收敛的特性，但也存在一些问题，其中之一是它的稳定性可能较差，也更容易陷入鞍点。

本文将其与梯度方法进行平行对比，开源代码可见我的 ObservableHQ 笔记本

[Searching maximum by Hessian](https://observablehq.com/@listenzcc/searching-maximum-by-hessian)

## REGL 简化了 WebGL 的什么？

WebGL 这类工具的学习曲线较为陡峭，因为它虽然工作在 javascript 上，但渲染过程中却会直接用到 C 代码。这样做的原因是由于它在渲染的实现过程中，需要用户自己定义每个 shader 的渲染行为。WebGL 的渲染过程是严格规范化的过程，因此 REGL 对它进行了包装。用户只需要调用这样的函数即可实现渲染。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

## REGL提供的上下文机制

阅读regl源码的时候看到一个非常有趣的机制。在regl.frame中，可以通过上下文迭代的机制实现varying变量的复用，从代码中可以看到，这个变量是透过函数调用传递下去的。这好像是一种闭包机制，非常好用。它可以保证vert中变量的一致性，有效减少开发成本。

[Game of Life](https://observablehq.com/@listenzcc/game-of-life)

## SDF中有趣的几何问题

最近在看SDF（****Sign Distance Function****），但没看懂，不过发现了一些有意思的边角东西。我在学习SDF的过程中遇到它GeoGebra，更准确地讲，我是在学习如何绘制正五边形的SDF时遇到它的。再进一步讲，在绘制正五边形的SDF时，为了避免SHADER过于复杂，需要将任意位置的点映射到正五边形中的某个三角形中。在前人的经验中，这种映射“总是”能通过有限次的“翻转”来做到，而对于正五边形来说，翻转的次数不超过四次。

## SDF在WebGL中的实现：以三角为例

本文以三角为例，在WebGL中实现SDF计算和实时渲染。

[SDF in WebGL](https://observablehq.com/@listenzcc/sdf-in-webgl)

## WebGL 中 buffer 的进一步理解

借用出差的间隙想了 4 天，我似乎把 buffer 这个东西想明白了一些。但由于出差过程中实在摸不着电脑，所以基本上属于闭门造车。 但是万幸的是，从效果上看，我的理解似乎没什么大问题。

感兴趣的话可以留意我的开源代码

[Image histogram using the buffer in WebGL (II)](https://observablehq.com/@listenzcc/image-histogram-using-the-buffer-in-webgl-ii)

## WebGL 初涉 buffer：像素的颜色直方图

本文利用 WebGL 的 buffer 机制实现了图像的像素级颜色直方图绘制，虽然能实现功能，但我仍然没有弄透这个东西。

[Image histogram using the buffer in WebGL](https://observablehq.com/@listenzcc/image-histogram-using-the-buffer-in-webgl)

## WebGL 实现线积分卷积（1）：framebuffer 基础

在现代图形编程中，Framebuffer 更常指代图形硬件或 API 中的一个对象，用于存储图像的像素数据。Framebuffer 可以包含颜色缓冲区、深度缓冲区、模板缓冲区等。在渲染流水线中，图形数据首先渲染到帧缓冲区，然后再传递到屏幕。通过反复渲染到不同的帧缓冲对象，可以实现图像像素的累积效果，达到一种积分计算的效果。这种技术在一些图形效果和计算中经常被使用，例如模糊效果、光照效果等。

代码可见我的 ObservableHQ 笔记本。

[Accumulate in the framebuffer](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer)

## WebGL 实现线积分卷积（2）

本文使用 WebGL 实现了线积分的基本前序功能。在迭代中，我使用局部梯度 $dFdx, dFdy$ 更新点的位置，让它沿梯度方向向下运动。并且采取了采用了双 framebuffer 耦合的方法，避免点的痕迹造成的影响。

本文的开源代码可见我的 ObservableHQ 笔记本

[Accumulate in the framebuffer (II)](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer-ii)

## WebGL 实现线积分卷积（3）：改变像素形态

前文实现了像素点沿梯度方向的移动，并且能够实时绘制它们。这距离实现线积分卷积的绘制还有一步之遥，那就是如何画线。具体来说是”如何改变像素形态，实现将像素绘制成成小线段“的功能。

功能代码可见我的 ObservableHQ 笔记本

[WebGL pixel shape](https://observablehq.com/@listenzcc/webgl-pixel-shape)

## WebGL 实现线积分卷积（4）：组合

终于把之前的东西组合起来，形成了完整的线积分渲染程序。开源代码可见我的 ObservableHQ 笔记本

[Accumulate in the framebuffer (III)](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer-iii)

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

## WebGL的framebuffer渲染会受到depthStencil的影响

简单来说，当使用framebuffer交互渲染时，应该关闭dephStencil选项。否则，会导致framebuffer无法按要求更新。这个经验是在绘制多个点的SDF时得到的。

## WebGL绘制球协函数

由于表面与球面对应关系的存在，我们总能用球面建模和绘制的方式进行物体建模和绘制。这是物体表面建模及绘图的基本原理之一。球协函数是三维函数，它可以用极坐标表示。为了说明它与球的对应关系，我对将它与一个球绘制在一起，用球的颜色表示它表面的各个点，用HSL颜色空间表示，其中，Hue表示$\varphi \in (0, 2\pi)$，Lightness表示$\varphi \in (0, \pi)$。绘图的代码可见我的ObservableHQ笔记本。

[Spherical Harmonic](https://observablehq.com/@listenzcc/spherical-harmonic)

## WebGL 面与点的绘制方式对比

绘制一个场景有两种方式，分别是按照面和按照点进行绘制。在 webgl 中，两种模式具有相似的形式。本文解释了两种绘图方式的差异。

[WebGL Template](https://observablehq.com/@listenzcc/webgl-template)

## 三维视角的vert变换

本文用极简的语言说明如何在opengl的语境中实现vert的三维视角变换。再简单一点说，它可以表示为矩阵连乘的计算结果。

## 三角 shader 的重心坐标系

前文遗留了一个问题，那就是如何使用 WebGL 渲染平移不变的三角 shader。本文尝试使用重心坐标系解决这个问题。为了体现重心坐标的意义和作用，我还增加了 wireframe 的线绘制方法。另外，前文的三角形端点移动方法并不令人满意，因此本文更换成 simplex-noise 方法，它使端点的运动看上去更加自然、柔和。

[Barycentric coordinate in WebGL](https://observablehq.com/@listenzcc/barycentric-coordinate-in-webgl)

## 任意三角形的SDF组合与阴影投射

将之前的内容组合起来就得到了这样一个“利用SDF进行实时投影计算”的样例程序。
在我的ObservableHQ开源笔记本可以找到它，

[SDF and Ray Tracing (Dev. III)](https://observablehq.com/@listenzcc/sdf-and-ray-tracing-dev-iii)

## 使用WebGL实现简单的三维交互

本文是纯粹工程实现的用例，它呈现的是低阶球协函数（Spherical Harmonic, SH）的随机叠加，并且这个三维构型可以与观察者进行实时交互。工程的难点有二，一是如何将观察者的MPV（Module, Projection, View）映射（详见前文）与用户在canvas上的鼠标操作联系起来；二是如何将大量的球协函数计算用最高效的方法计算出来，从而实现实时叠加。

## 在 WebGL 上画线：Wireframe

所谓曲线就是两个等值面互相吻合的边缘的点的集合。而 glsl-solid-wireframe 就是通过 WebGL 的微分库实现了这个点集的探测功能。本文试图从连续噪声图中找到等值线，并渲染它们。为了说明点集是如何被探测出来的，我还写了一些有用的数学推导。

开源代码可见我的 ObservableHQ 笔记本

[Contour demo of WebGL & glslify](https://observablehq.com/@listenzcc/contour-demo-of-webgl-glslify)

## 在SDF的基础上绘制光源投影

本文介绍了基于 Signed Distance Field (SDF) 的光源追踪方法。通过动态确定迭代步长，使用 SDF 可以有效地判断光线是否经过物体，并避免了传统方法的采样问题和大量物体信息的输入。另外，还在迭代过程中记录最小 SDF 值用于绘制光线颜色，并展示了样例场景的光线强度图和彩色结果。末尾还附上了追踪的核心代码。

[SDF and Ray Tracing (Dev. II)](https://observablehq.com/@listenzcc/sdf-and-ray-tracing-dev-ii)

## 将任意三角形规范化：简化计算SDF的尝试

由于计算任意三角形SDF的代码显得过于臃肿，所以我想将它简化一下。仅通过一次映射将任意三角形转换为规范的三角形，在这个规范的二维空间中进行近似计算，似乎可以提升代码的简洁性。

[Regular triangle](https://observablehq.com/@listenzcc/regular-triangle)

## 平面在三维中旋转：REGL解决实际问题之一

这是一个平面在三维空间中旋转并通过仿射变换反映在二维空间的问题。通过对平面进行维度扩展和仿射变换的数学建模，介绍了如何处理三维空间中的旋转问题，并尝试从二维空间的信息中反推三维空间的信息。然而，由于信息的不完整性，这个问题成为了一个欠定问题，特别是当只能从二维空间中提取到部分信息时。

为了解决这个问题，采用了REGL进行模拟实验，设计了一个二维矩形在三维空间中的旋转模拟，并记录下角点的位置变化。通过对这些数据进行回归分析，我尝试了解是否可以仅通过仿射变换后的三个角点的二维坐标来推断出第四个角点的二维坐标。实验结果显示，虽然无法准确推测出第四个角点的第三维$z$成分，但如果只关注二维平面内的位置，通过三个角点的信息反推第四个角点的二维坐标是可行的。

实验代码可见：

[Geometry Dim 2 to 3](https://observablehq.com/@listenzcc/geometry-dim-2-to-3)

分析代码可见：

[https://github.com/listenzcc/geometry-dim-2-to-3](https://github.com/listenzcc/geometry-dim-2-to-3)

## 开源，就是随取随用

程序员的生产工具和工作对象是二进制代码，但这是个很扭曲的群体，他们是最不喜欢敲代码的一群人，是能复制粘贴的就绝不多写一个字的一群人。这是把人从工具中解放出来的懒惰，这种极度的懒惰就是开源。

WebGL 的 shader 渲染过程需要“编写” c 代码，由于实现了开源代码的随取随用，我们可以使用 promise 机制临时下载它们。

[Glslify](https://observablehq.com/@listenzcc/glslify)

## 梯度粗解

梯度就是局部效用最大的变化方向。对于给定的标量场，我们总能让某个点沿着它的梯度进行“移动”。移动的过程中，该点的值会不断增加。因此这个过程称为梯度上升。如果将这个场倒过来，那么不断增大的过程会转换成不断减小的过程，这个过程就是“梯度下降”。

开源代码可见我的 ObservableHQ 笔记本

[Searching maximum by gradient ascending](https://observablehq.com/@listenzcc/searching-maximum-by-gradient-ascending)

## 流浪像素：逐像素的微分偏移

本文以前文这基础，在 WebGL 上实现了逐像素的微分偏移，使图像看上去像是在“流动”。

[Image histogram using the buffer in WebGL (III)](https://observablehq.com/@listenzcc/image-histogram-using-the-buffer-in-webgl-iii)

## 离散、连续和插值：WebGL 的 vertex 与 fragment

本篇是对上篇的进一步解释和说明，尝试说明在 WebGL 的渲染过程中，程序是如何处理端点（vertex）和光栅片（fragment）之间的关系。这是一种离散、连续和插值之间的微妙关系，它们的背后是令人叹为观止的优秀工程实现。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

## 继续SDF：简单压倒一切

本文尝试一种计算简单，且适用于任意凸多边形SDF计算的快速算法。在这个算法中，对于每条边只需要计算二次内积即可，因此这是一种复杂度为$N$的算法。

[Easy to compute the SDF of triangle](https://observablehq.com/@listenzcc/easy-to-compute-the-sdf-of-triangle)

## 随机三角形的SDF

SDF（Signed Distance Field）是多边形空间中任意点到最近边缘的最短距离标量。通过重心坐标系，类似于三角形Shader的技巧，可实现三维模型的SDF。利用重心坐标化，可在片元着色器中计算距离场，用于绘制三角形边缘，实现视觉效果。

