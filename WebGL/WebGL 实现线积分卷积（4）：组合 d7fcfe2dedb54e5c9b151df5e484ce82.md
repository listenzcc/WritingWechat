# WebGL 实现线积分卷积（4）：组合

终于把之前的东西组合起来，形成了完整的线积分渲染程序。开源代码可见我的 ObservableHQ 笔记本

[Accumulate in the framebuffer (III)](https://observablehq.com/@listenzcc/accumulate-in-the-framebuffer-iii)

---
- [WebGL 实现线积分卷积（4）：组合](#webgl-实现线积分卷积4组合)
  - [组合的内容](#组合的内容)
  - [呈现效果](#呈现效果)


## 组合的内容

1. **Framebuffer 的使用：** Framebuffer是在渲染管线中用于存储渲染结果的内存区域。我利用了两个不同的framebuffer，通过交替使用它们，实现了点轨迹的算数积分。这种技术被广泛应用于图形学中，可以有效地进行多步渲染，每一步都在前一步的基础上进行。
2. **点移动的轨迹：** 点的轨迹是通过计算局部梯度得到的。在图形学中，梯度表示的是图像中像素值的变化率。使用**`dFdx`**和**`dFdy`**函数可以获取在每个像素点上的局部梯度，这些梯度信息用于确定点的移动方向。这种方法常用于流线可视化和仿真等应用。
3. **使用 gridArrayBuffer 访问像素：** 在vertex渲染过程中使用gridArrayBuffer是一种高效的方式，通过这种方式，我能够访问图像中的每个像素。通过增加**`linePosition`**和**`count`**，将像素转换为线条微元，为后续的线积分卷积操作做好准备。这种精细的像素访问是实现高级图形效果的基础。
4. **Shader 渲染过程的设计：** 设计了不同shader的输入和输出，特别是在framebuffer交替的过程中。这一做法允许你在线条渲染时直接利用这些信息，确定线条的方向和长度。这些数据传递和处理方式经过仔细的计算和调试，确保每个步骤都能够正确地协同工作。

## 呈现效果

下图是针对随机变化的连续标量场的线积分绘图，上图是单一颜色的渲染结果；下图是按局部梯度方向渲染的结果；右图是叠加标量场的结果。

![Untitled](WebGL%20%E5%AE%9E%E7%8E%B0%E7%BA%BF%E7%A7%AF%E5%88%86%E5%8D%B7%E7%A7%AF%EF%BC%884%EF%BC%89%EF%BC%9A%E7%BB%84%E5%90%88%20d7fcfe2dedb54e5c9b151df5e484ce82/Untitled.png)

![Untitled](WebGL%20%E5%AE%9E%E7%8E%B0%E7%BA%BF%E7%A7%AF%E5%88%86%E5%8D%B7%E7%A7%AF%EF%BC%884%EF%BC%89%EF%BC%9A%E7%BB%84%E5%90%88%20d7fcfe2dedb54e5c9b151df5e484ce82/Untitled%201.png)

![Untitled](WebGL%20%E5%AE%9E%E7%8E%B0%E7%BA%BF%E7%A7%AF%E5%88%86%E5%8D%B7%E7%A7%AF%EF%BC%884%EF%BC%89%EF%BC%9A%E7%BB%84%E5%90%88%20d7fcfe2dedb54e5c9b151df5e484ce82/Untitled%202.png)

![Untitled](WebGL%20%E5%AE%9E%E7%8E%B0%E7%BA%BF%E7%A7%AF%E5%88%86%E5%8D%B7%E7%A7%AF%EF%BC%884%EF%BC%89%EF%BC%9A%E7%BB%84%E5%90%88%20d7fcfe2dedb54e5c9b151df5e484ce82/Untitled%203.png)