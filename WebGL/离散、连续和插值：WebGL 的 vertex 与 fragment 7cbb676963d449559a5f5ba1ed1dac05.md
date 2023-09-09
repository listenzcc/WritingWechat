# 离散、连续和插值：WebGL 的 vertex 与 fragment

本篇是对上篇的进一步解释和说明，尝试说明在 WebGL 的渲染过程中，程序是如何处理端点（vertex）和光栅片（fragment）之间的关系。这是一种离散、连续和插值之间的微妙关系，它们的背后是令人叹为观止的优秀工程实现。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

---
- [离散、连续和插值：WebGL 的 vertex 与 fragment](#离散连续和插值webgl-的-vertex-与-fragment)
  - [两种容器：ARRAY\_BUFFER 和 ELEMENT\_ARRAY\_BUFFER](#两种容器array_buffer-和-element_array_buffer)
  - [端点：vertex](#端点vertex)
  - [插值：fragment](#插值fragment)
  - [传递：varying](#传递varying)
  - [一个小问题：varying 的值是否受到仿射变换的影响](#一个小问题varying-的值是否受到仿射变换的影响)


## 两种容器：ARRAY_BUFFER 和 ELEMENT_ARRAY_BUFFER

在前文中我们可以看到，REGL 能够省去冗长的 WebGL 管道。但是，虽然步骤可以自动化，但变量绑定的物理内存和这些内存的抽象 buffer 却是实打实存在的，其中，vertex 和 fragment 的 buffer 种类不同

- vertex 使用 gl.ARRAY_BUFFER
- fragment 使用 gl.ELEMENT_ARRAY_BUFFER

它们的区别如下，ARRAY_BUFFER 负责将变量传递给 GPU，ELEMENT_ARRAY_BUFFER 则是一种引用（reference），引用的目标是另一个 ARRAY_BUFFER。要进一步理解这两种容器的用途，就需要从渲染的角度重新理解 vertex 和 fragment。虽然在形式上，它们都是 shader 的 C 代码，但其中变量的意义却截然不同。

> When dealing with OpenGL, the `ELEMENT_ARRAY_BUFFER` and `ARRAY_BUFFER` are both types of buffer objects used for efficient data storage and retrieval.
> 
> 1. **ARRAY_BUFFER**:
>     - `ARRAY_BUFFER` is a type of buffer object used to store vertex attribute data. This can include vertex coordinates, texture coordinates, normals, etc.
>     - It's typically used to pass data to the GPU for rendering.
> 2. **ELEMENT_ARRAY_BUFFER**:
>     - `ELEMENT_ARRAY_BUFFER` is used to store indices that reference vertices stored in an `ARRAY_BUFFER`.
>     - It allows for the reuse of vertices in different triangles or polygons, which can optimize memory usage.
> 
> In summary, `ARRAY_BUFFER` stores vertex attributes, while `ELEMENT_ARRAY_BUFFER` stores indices that reference those vertices.
> 

[WebGL - Geometry](https://www.tutorialspoint.com/webgl/webgl_geometry.htm)

## 端点：vertex

首先是 vertex 的渲染。所谓 vertex 就是渲染的端点，如下图中白色箭头指向的三个角点。下图右侧是处理这些端点的代码，它做以下的事情

- 端点的原始位置是 attribute vec2 position，先将它旋转 radian 个弧度，这里它的渲染位置被记录在 gl_Position 中，这是 main() 函数的“输出”；
- 端点的颜色由 attribute vec3 color 所指定，这里做的事情是将它传递给 fragment，传递的路径是 varying vec3 v_color，这是一个新的 varying 变量；
- 与颜色相似的，端点的位置信息也被传递到 varying vec2 v_pos 中，这也是一个新的 varying 变量；
- 由于这是一个三角光栅，因此这个过程对三个端点分别执行一次，总共执行三次。

这一系列操作只是在系统中设定了三个端点，接下来的工作是在这三个端点组成的三角区域之内进行渲染。

![Untitled](%E7%A6%BB%E6%95%A3%E3%80%81%E8%BF%9E%E7%BB%AD%E5%92%8C%E6%8F%92%E5%80%BC%EF%BC%9AWebGL%20%E7%9A%84%20vertex%20%E4%B8%8E%20fragment%207cbb676963d449559a5f5ba1ed1dac05/Untitled.png)

![Untitled](%E7%A6%BB%E6%95%A3%E3%80%81%E8%BF%9E%E7%BB%AD%E5%92%8C%E6%8F%92%E5%80%BC%EF%BC%9AWebGL%20%E7%9A%84%20vertex%20%E4%B8%8E%20fragment%207cbb676963d449559a5f5ba1ed1dac05/Untitled%201.png)

## 插值：fragment

为了在这三个端点组成的三角区域之内进行渲染，系统开始调用 fragment 的 main() 函数。这个函数的调用次数是可变的，而且数量很大，因为三角范围内的每个像素都要通过这个函数进行渲染。由于我没有将 uniform 参数传递进来，因此只考虑两个 varying 参数，v_pos 和 v_color。

- 首先，这个函数的“输出”是 gl_FragColor，顾名思义它是每个像素的颜色 RGB 值加上一个透明度通道；
- 随后，立即出现了一个矛盾，那就是 varying 变量在 fragment 中被进行了**插值**，从端点位置转换成了每个像素的实际渲染位置；
- 为了进一步说明这种情况，我定义了函数 dist，它用于计算两个点之间的欧氏距离。利用这个函数，我在整个 shader 上绘制了两个白色圆环，这说明在 fragment 渲染过程是在每个像素都执行的。

由此可见，上述过程虽然要执行多次，但每次都是确定的和排他的，因此可以由 GPU 进行并行计算，这也是 WebGL 的 shader 渲染算法能够进行 GPU 加速的核心原理。

![Untitled](%E7%A6%BB%E6%95%A3%E3%80%81%E8%BF%9E%E7%BB%AD%E5%92%8C%E6%8F%92%E5%80%BC%EF%BC%9AWebGL%20%E7%9A%84%20vertex%20%E4%B8%8E%20fragment%207cbb676963d449559a5f5ba1ed1dac05/Untitled%202.png)

![Untitled](%E7%A6%BB%E6%95%A3%E3%80%81%E8%BF%9E%E7%BB%AD%E5%92%8C%E6%8F%92%E5%80%BC%EF%BC%9AWebGL%20%E7%9A%84%20vertex%20%E4%B8%8E%20fragment%207cbb676963d449559a5f5ba1ed1dac05/Untitled%203.png)

## 传递：varying

从前文中我们还能看到，attribute 的作用域仅限于 vertex。从前两小节的分析中，可以看到这种分割是有道理的，其背后的逻辑是 attribute 只能控制 vertex 这类端点。为了让这些信息能够作用于后续的 fragment 插值，就需要使用 varying 关键词，将这些信息传递下去。

这就导致 vertex 和 fragment 的 shader 代码块中都包含相同的 varying 变量，但它们的意义是不同的。在 vertex 中，这些变量是与端点对齐的；而在 fragment 中，这些变量是与插值后的连续空间对齐的。

## 一个小问题：varying 的值是否受到仿射变换的影响

这并不是一个无厘头的问题，因为我的眼睛对颜色并不十分敏感，因此单从颜色无法判断varying 的值是否受到仿射变换的影响。于是我做了个实验，实验方法是在 vertex 渲染过程中进行右侧截断，也就是当端点位置横坐标超过 $0.1$ 时将它截断到 $0.1$。

经过截断后，两个白色圆圈并没有产生畸变，因此可以认为 varying 后的坐标是与端点位置相互独立的，不受端点坐标仿射变换的影响。

![20230908-161324.gif](%E7%A6%BB%E6%95%A3%E3%80%81%E8%BF%9E%E7%BB%AD%E5%92%8C%E6%8F%92%E5%80%BC%EF%BC%9AWebGL%20%E7%9A%84%20vertex%20%E4%B8%8E%20fragment%207cbb676963d449559a5f5ba1ed1dac05/20230908-161324.gif)

![Untitled](%E7%A6%BB%E6%95%A3%E3%80%81%E8%BF%9E%E7%BB%AD%E5%92%8C%E6%8F%92%E5%80%BC%EF%BC%9AWebGL%20%E7%9A%84%20vertex%20%E4%B8%8E%20fragment%207cbb676963d449559a5f5ba1ed1dac05/Untitled%204.png)