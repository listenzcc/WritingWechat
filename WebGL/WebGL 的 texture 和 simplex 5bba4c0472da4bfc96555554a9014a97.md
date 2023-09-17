# WebGL 的 texture 入门

缓冲器是 WebGL 的重要组成部分，它用来缓冲一张图像，本文说明它的基本使用逻辑。为了让本文不会过于无聊，本文实现了图像颜色空间的随机化，它保证了在原始图像上连续的颜色在新的颜色空间上还是连续的。又由于随机过程中含有时间变量，因此新的颜色空间是实时变化的。这就形成了一种奇怪的动态效果。得益于 WebGL 的优秀性能，这个过程是实时的，帧率可以达到显示器的刷新率。

[WebGL Texture Usage](https://observablehq.com/@listenzcc/webgl-texture-usage)

---
- [WebGL 的 texture 入门](#webgl-的-texture-入门)
  - [WebGL 的 texture 缓冲器](#webgl-的-texture-缓冲器)
  - [WebGL 的 simplex 噪声库](#webgl-的-simplex-噪声库)
  - [颜色空间映射](#颜色空间映射)


## WebGL 的 texture 缓冲器

缓冲器是 WebGL 的重要组成部分，它用来缓冲一张图像，这张图像的典型形式是三维矩阵$R^{width \times height \times 4}$ ，其中 $4$ 代表 RGBA 通道。从使用者的角度来讲，它的典型使用方式是将这个矩阵以各种形式“上传”到 WebGL 的 shader 中。上传的过程可以使用原生的 WebGL 语法直接完成，也可以使用 REGL 提供的包装器来完成，这个是小问题。

```jsx
image = new Image();
image.src = src;
image.crossOrigin = "anonymous";

image.onload = () => {
	const texture = regl.texture(image)
  // The texture is what I want.
}
```

> There are many ways to upload data to a texture in WebGL. As with drawing commands, regl consolidates all of these crazy configuration parameters into one function. Here are some examples of how to create a texture,
> 

[Texture2D | regl](https://stevebest.github.io/regl-typings/interfaces/regl.texture2d.html)

在 shader 接收到这个缓冲器后，我们可以在 fragment 中使用它，使用的逻辑是将它看作采样器（sampler2D）。在之前的文章中，我已经说明了在 fragment 中的位置参数（vPostition）是经过线性插值之后的像素位置，因此它代表要渲染的像素所对应的坐标。那么采样器所做的工作就是从缓冲器中获取该位置的 RGBA 值。

![Untitled](WebGL%20%E7%9A%84%20texture%20%E5%92%8C%20simplex%205bba4c0472da4bfc96555554a9014a97/Untitled.png)

```c
// Fragment shader
varying vec2 vPosition;
uniform sampler2D uSampler;

void main() {
  vec4 value = texture2D(uSampler, vPosition);
  gl_FragColor = value;
}
```

> In the fragment shader we declare a uniform sampler2D which lets us reference a texture. We use the texture coordinates passed from the vertex shader and we call `texture2D` to look up a color from that texture.
> 

[WebGL Textures](https://webglfundamentals.org/webgl/lessons/webgl-3d-textures.html)

[](http://regl.party/api#textures)

## WebGL 的 simplex 噪声库

为了让本文不会过于无聊，我引入了 glsl-noise 噪声库，它是基于 glslify 的开源代码的 webgl-noise 代码片断。它不是本文的重点，在此只是说明它能够以生成空间和时间连续的随机噪声，噪声是连续且有限的。

$$
\begin{cases}
f(x, y, z, t) \in (0, 1) \\
f(t=t_0) |_{xyz} = \lim_{t \rightarrow t_0} f(t) |_{xyz}
\end{cases}
$$

```c
// Fragment shader
varying vec2 vPosition;
uniform sampler2D uSampler;
uniform float t, mixRatio;

#pragma glslify: snoise = require('glsl-noise/simplex/4d')

void main() {
  vec4 tex= texture2D(uSampler, vPosition);
  float noise = snoise(vec3(value), t);
  vec4 color = vec3(noise, 1.0);
  gl_FragColor = mix(tex, color, mixRatio);
}
```

[GitHub - ashima/webgl-noise: Procedural Noise Shader Routines compatible with WebGL](http://github.com/ashima/webgl-noise)

[GitHub - hughsk/glsl-noise: webgl-noise shaders ported to work with glslify](https://github.com/hughsk/glsl-noise/tree/master)

[https://github.com/glslify/glslify](https://github.com/glslify/glslify)

## 颜色空间映射

接下来，我使用这个噪声库做了这样一件事情，这也是上述代码所做的事情

- 获取每个像素的 RGB 值；
- 根据这三个值再加上当时的时刻值 t 凑成 4 维向量，获取一个随机值；
- 将这个随机值复制为 RGB 颜色并进行灰度渲染；
- 另一个方法是将这个值转换为 HSV 值，并进行彩色渲染。

这样的操作实现了图像颜色空间的随机化，它保证了在原始图像上连续的颜色在新的颜色空间上还是连续的。又由于随机过程中含有时间变量（t），因此新的颜色空间是实时变化的。这就形成了如下的动态效果。
得益于 WebGL 的优秀性能，这个过程是实时的，帧率可以达到显示器的刷新率。

![Untitled](WebGL%20%E7%9A%84%20texture%20%E5%92%8C%20simplex%205bba4c0472da4bfc96555554a9014a97/Untitled%201.png)

![Untitled](WebGL%20%E7%9A%84%20texture%20%E5%92%8C%20simplex%205bba4c0472da4bfc96555554a9014a97/Untitled%202.png)

![Untitled](WebGL%20%E7%9A%84%20texture%20%E5%92%8C%20simplex%205bba4c0472da4bfc96555554a9014a97/Untitled%203.png)