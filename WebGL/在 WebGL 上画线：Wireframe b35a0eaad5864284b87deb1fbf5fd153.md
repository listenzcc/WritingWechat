# 在 WebGL 上画线：Wireframe

所谓曲线就是两个等值面互相吻合的边缘的点的集合。而 glsl-solid-wireframe 就是通过 WebGL 的微分库实现了这个点集的探测功能。本文试图从连续噪声图中找到等值线，并渲染它们。为了说明点集是如何被探测出来的，我还写了一些有用的数学推导。

开源代码可见我的 ObservableHQ 笔记本

[Contour demo of WebGL & glslify](https://observablehq.com/@listenzcc/contour-demo-of-webgl-glslify)

---
- [在 WebGL 上画线：Wireframe](#在-webgl-上画线wireframe)
  - [噪声及染色](#噪声及染色)
  - [等值线](#等值线)
  - [等值线的渲染](#等值线的渲染)
  - [附录：简要证明](#附录简要证明)


## 噪声及染色

将前文的内容进行整合，具体来说是将 glslify 的 simplex 噪声库不难绘制下图左侧的噪声。接下来，我引入 colormap 库，使用其中的 jet colormap 对它进行染色。染色的规则非常简单，该像素的值越大染色就越红，反之就越蓝。这个操作十分简单。接下来，我试图从图中找到等值线，就是右图中的黑色线。

![Untitled](%E5%9C%A8%20WebGL%20%E4%B8%8A%E7%94%BB%E7%BA%BF%EF%BC%9AWireframe%20b35a0eaad5864284b87deb1fbf5fd153/Untitled.png)

![Untitled](%E5%9C%A8%20WebGL%20%E4%B8%8A%E7%94%BB%E7%BA%BF%EF%BC%9AWireframe%20b35a0eaad5864284b87deb1fbf5fd153/Untitled%201.png)

```c
// Fragment shader rendering
void main () {
  float f = snoise(vec3(vPosition*noiseScale, t * 20.0 / ${refreshRatio}));

  float wf = 0.8 - wireframe(vec3(f * contours), gridWidth, gridFeather);

  // Draw the black-white graph (left)
  // gl_FragColor = vec4(vec3(f), 1.0);

  // Draw colorful graph (right)
  gl_FragColor = mix(jet(f * 0.5 + 0.5), vec4(vec3(0.3), 1.0), wf);
}
```

[https://github.com/glslify/glsl-colormap](https://github.com/glslify/glsl-colormap)

[GLSL noise library: Simplex and Perlin noise](https://stegu.github.io/webgl-noise/webdemo/)

## 等值线

等值线是在地理信息系统 (GIS) 和地图制图中常用的一种表示空间数据的方法。它们用于显示地理现象在地图上的分布情况，例如高程、温度、降雨量等。等值线通过连接具有相同数值的点来构建一条连续的曲线，这些点在地理空间上具有相同的属性值。这使得人们可以在地图上直观地理解数据的分布特征。例如，等高线图就是用等值线来表示地形高程的分布，这让人们可以看到山脉、谷地等地貌特征。此外，气象领域也常使用等值线来表示温度、压力、降雨量等变量在地图上的分布情况。

如下左图是较稀疏的等值线，图中黑色线的值为 $0$ 值，而右图则代表较多等值线的情况，它们是在 $(-1, 1)$ 范围内均匀分布的。

![Untitled](%E5%9C%A8%20WebGL%20%E4%B8%8A%E7%94%BB%E7%BA%BF%EF%BC%9AWireframe%20b35a0eaad5864284b87deb1fbf5fd153/Untitled%201.png)

![Untitled](%E5%9C%A8%20WebGL%20%E4%B8%8A%E7%94%BB%E7%BA%BF%EF%BC%9AWireframe%20b35a0eaad5864284b87deb1fbf5fd153/Untitled%202.png)

## 等值线的渲染

从数学意义的角度来说，线是存在的，但它无限细。因为线是一系列点的集合

$$
C=\{f(x, y) \mid f(x, y) = \hat{f}\}, f(x, y) \in (-1, 1)
$$

从概率论的角度上讲，点属于某条曲线的概率值满足如下积分关系。随着采样无限细分，其概率数值越来越难以计算。我们只能保证概率密度 $p_z$ 是可积的

$$
\begin{cases}
p_z &= p(f(x, y)=z) \\
1 &= \int_{-1}^{1}p_z dz \\
1 &\approx \lim_{n \rightarrow \infty} \sum_{i=1}^n p_{z_i} * \delta_{z_i} \\
2 &= \sum_{i=1}^n \delta_{z_i}
\end{cases}
$$

为了解决绕过这个难以计算的问题，我们转而考虑两个范围大一些的开空间

$$
\begin{cases}
A = \{f(x, y) \mid f(x, y) > \hat{f}\} \\
B = \{f(x, y) \mid f(x, y) < \hat{f}\} \\
A \cap B = \emptyset
\end{cases}
$$

利用这两个空间重新定义曲线，可得

$$
C = \{ (x, y) \mid \delta(x, y) \cap A \neq \emptyset, \delta(x, y) \cap B \neq \emptyset \}
$$

其中，$\delta(x, y)$ 代表点的任意邻域。由于我们在整个平面上只有这三个东西，且它们互不相交（证明见附录），因此一个和曲线的并是另一个的闭包（Closure）

$$
\begin{cases}
A \cup C = \overline{B}\\
B \cup C = \overline{A}
\end{cases}
$$

[Closure (mathematics)](https://en.wikipedia.org/wiki/Closure_(mathematics))

这样就得到了一句废话，那就是说，所谓曲线就是两个等值面互相吻合的边缘的点的集合。而 glsl-solid-wireframe 就是通过 WebGL 的微分库实现了这个点集的探测功能，分四步进行计算

1. looped 变量负责将 parameter 进行折叠，以 $1$ 为周期折叠成锯齿折线，因此整数位置被映射为 $0$，其他位置被映射为高值；
2. w1 变量是用户指定的曲线宽度；
3. d 变量是类似 varying position 变量的全微分，$dx + dy$，这个微分值得到了在这个位置上屏幕上相邻像素的位置信息，它是线宽的基线值；
4. a3 变量负责将以上信息整合，基于 looped 变量的零点判断 parameter 对应的点是否在曲线的点集上。

通过这些计算，我们找到了 parameter 包含整数的全部点的集合，这些点用 $0$ 值进行标记。

```c
#extension GL_OES_standard_derivatives : enable

float wireframe (vec3 parameter, float width, float feather) {
  vec3 looped = 0.5 - abs(mod(parameter, 1.0) - 0.5);

  float w1 = width - feather * 0.5;
  vec3 d = fwidth(parameter);

  vec3 a3 = smoothstep(d * w1, d * (w1 + feather), looped);

  return min(min(a3.x, a3.y), a3.z);
}
```

[https://github.com/rreusser/glsl-solid-wireframe](https://github.com/rreusser/glsl-solid-wireframe)

[fwidth - OpenGL 4 Reference Pages](https://registry.khronos.org/OpenGL-Refpages/gl4/html/fwidth.xhtml)

## 附录：简要证明

证明：$A, B, C$ 互不相交。

1. 由 $A \cap B = \emptyset$ 可知没有点兼属于两个集合。
2. 由 $\delta(x, y) \cap A \neq \emptyset$ 可知 $(x, y) \notin B$ ，否则与 1 矛盾，因为 $\forall (x, y) \in B \rightarrow \exists \delta(x, y) \notin A$ 。
3. 同理，由 $\delta(x, y) \cap B \neq \emptyset$ 可知 $(x, y) \notin A$ 。

证明毕。