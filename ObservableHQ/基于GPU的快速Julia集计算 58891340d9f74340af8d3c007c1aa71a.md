# 基于GPU的快速Julia集计算

本文记录一个利用GPU计算的前端程序，它用来在PC上快速计算和实时渲染大量迭代的 Julia 集。由于 GPU 算的实在是太快了，因此我决定让它成为一个实时计算和渲染程序。开源代码可见我的前端笔记本
[The Fractal (Julia Set) on GPU](https://observablehq.com/@listenzcc/the-fractal-julia-set-on-gpu "The Fractal (Julia Set) on GPU")

或GITHUB页面
[JuliaSet-GPUIO](https://listenzcc.github.io/JuliaSet-GPUIO/ "JuliaSet-GPUIO")

---
- [基于GPU的快速Julia集计算](#基于gpu的快速julia集计算)
  - [Julia集](#julia集)
  - [GPU计算和渲染](#gpu计算和渲染)


## Julia集

Julia集是在复数空间上的著名自相似集。它的生成过程是求解如下迭代方程，并且记录每次得到的复数值。再将这些值以概率密度的形式绘制在复数平面上。

$$
z_n = z_{n-1}^2 + c, z \in \mathbb{C}
$$

其中，参数$c$值可以用来控制图像的形状。

[Julia Set -- from Wolfram MathWorld](https://mathworld.wolfram.com/JuliaSet.html "Julia Set -- from Wolfram MathWorld")

## GPU计算和渲染

由于计算过程非常简单，因此乘下的工作就是使用 GPU-IO 工具进行快速计算，并将概率密度函数用采样的方法渲染在图像上。在计算和渲染过程中，有一个因素比较关键的，它就是“迭代次数”（Iterations）和“渲染振幅”（Render Amplitude）选项之间的平衡。“迭代次数”选项对可视化效果至关重要，值越小，绘图越模糊，扩展范围越大。较大的值提供了集合的更多细节。当“迭代次数”选项足够大时，您可能会对相邻参数之间的快速变化感到惊讶。“渲染振幅”选项控制集的增强部分，值越小，集的渲染效果越好，而值越大，集的边缘渲染效果越好。

由于 GPU 算的实在是太快了，因此我决定让它成为一个实时计算和渲染程序。因此我提供了一个可以通过鼠标拖动来改变参数的控制板（Touch Pad of Parameter），并且为了增强它的可用性，我在触摸板上放置了一些预定义的参数，拖动它们附近的红色点以使用这些参数。开源代码可见我的前端笔记本

[The Fractal (Julia Set) on GPU](https://observablehq.com/@listenzcc/the-fractal-julia-set-on-gpu "The Fractal (Julia Set) on GPU")

当然，该集合具有自相似性，您可以缩放绘图以查看它，下面是一些渲染的样例。

![Parameter-1](%E5%9F%BA%E4%BA%8EGPU%E7%9A%84%E5%BF%AB%E9%80%9FJulia%E9%9B%86%E8%AE%A1%E7%AE%97%2058891340d9f74340af8d3c007c1aa71a/Untitled.png)

Parameter-1

![Parameter-2](%E5%9F%BA%E4%BA%8EGPU%E7%9A%84%E5%BF%AB%E9%80%9FJulia%E9%9B%86%E8%AE%A1%E7%AE%97%2058891340d9f74340af8d3c007c1aa71a/Untitled%201.png)

Parameter-2

![Parameter-3](%E5%9F%BA%E4%BA%8EGPU%E7%9A%84%E5%BF%AB%E9%80%9FJulia%E9%9B%86%E8%AE%A1%E7%AE%97%2058891340d9f74340af8d3c007c1aa71a/Untitled%202.png)

Parameter-3

![Parameter-3-zoom-in](%E5%9F%BA%E4%BA%8EGPU%E7%9A%84%E5%BF%AB%E9%80%9FJulia%E9%9B%86%E8%AE%A1%E7%AE%97%2058891340d9f74340af8d3c007c1aa71a/Untitled%203.png)

Parameter-3-zoom-in