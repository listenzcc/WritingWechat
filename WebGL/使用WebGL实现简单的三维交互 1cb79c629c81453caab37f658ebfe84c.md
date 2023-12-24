# 使用WebGL实现简单的三维交互

本文是纯粹工程实现的用例，它呈现的是低阶球协函数（Spherical Harmonic, SH）的随机叠加，并且这个三维构型可以与观察者进行实时交互。工程的难点有二，一是如何将观察者的MPV（Module, Projection, View）映射（详见前文）与用户在canvas上的鼠标操作联系起来；二是如何将大量的球协函数计算用最高效的方法计算出来，从而实现实时叠加。

---
[toc]

## MVP矩阵的信息传递

为了解决如何将观察者的MPV（Module, Projection, View）映射（详见前文）与用户在canvas上的鼠标操作联系起来的问题，我采用了regl-camera插件，它的典型使用方式是将观察者绑定在canvas上，这样用户可以通过在canvas划动鼠标的方式实时改变观察者的位置，操作逻辑是鼠标上下移动调整观察者位置向量的俯仰，即$\theta$角度；鼠标左右移动调整观察者位置向量的偏转角度，即$\varphi$角度。

![Untitled](%E4%BD%BF%E7%94%A8WebGL%E5%AE%9E%E7%8E%B0%E7%AE%80%E5%8D%95%E7%9A%84%E4%B8%89%E7%BB%B4%E4%BA%A4%E4%BA%92%201cb79c629c81453caab37f658ebfe84c/Untitled.png)

```jsx
camera = reglCamera(regl, {
  element: regl._gl.canvas,
  center: [0, 0, 0],
  theta: (3.0 * Math.PI) / 4.0,
  phi: Math.PI / 6.0,
  distance: 40.0,
  damping: 0,
  noScroll: true,
  renderOnDirty: true
})
```

接下来，如果要显示的三维内容是“静态的”，那么可以使用如下方式进行帧绘制。其中，regl.frame负责控制帧绘制的时序，而camera负责**在视角改变时**进行重绘。它会将当前的projection和view矩阵传入regl的shader渲染器中。这是regl-camera的典型应用。

```jsx
regl.frame(() => {
  camera((state) => {
    if (!state.dirty) return;
    regl.clear({color: [0, 0, 0, 1]})
    drawBunny()
  })
})

vert: `
    precision mediump float;
    uniform mat4 projection, view;
    attribute vec3 position, normal;
    varying vec3 vnormal;
    void main () {
      vnormal = normal;
      gl_Position = projection * view * vec4(position, 1.0);
    }`,
```

[https://github.com/regl-project/regl-camera](https://github.com/regl-project/regl-camera)

## 实时变化的Vert信息

但是，当我们需要对绘制的物体三维结构进行实时改变时，以上方法就失效了。因为它绘图的逻辑需要camera位置发生变化，而我不能指望使用者不停地晃动鼠标。因此，我使用分体式的方案解决以上矛盾，核心代码如下所示，Step1用于监听鼠标动作并调整观察者位置；Step2用于实时绘制。注意，此时需要将projection和view信息手动传入shader。

![Untitled](%E4%BD%BF%E7%94%A8WebGL%E5%AE%9E%E7%8E%B0%E7%AE%80%E5%8D%95%E7%9A%84%E4%B8%89%E7%BB%B4%E4%BA%A4%E4%BA%92%201cb79c629c81453caab37f658ebfe84c/Untitled%201.png)

![20231224-200021.gif](%E4%BD%BF%E7%94%A8WebGL%E5%AE%9E%E7%8E%B0%E7%AE%80%E5%8D%95%E7%9A%84%E4%B8%89%E7%BB%B4%E4%BA%A4%E4%BA%92%201cb79c629c81453caab37f658ebfe84c/20231224-200021.gif)

接下来，为了实现形状的实时变化，我将低阶SH函数的叠加过程放在WebGL的shader阶段进行，这样可以实现毫秒级的计算渲染。而输入信息仅是围绕整个球面的极坐标信息。这些代码可见我的ObservahleHQ笔记本

[Spherical Harmonic (real-time)](https://observablehq.com/@listenzcc/spherical-harmonic-real-time)

```jsx
// Step1, Update camera in real-time based on mouse operation
regl.frame(() => {
  camera(function () {});
})

// Step2, Draw 3D model
while (true) {
    let { projection, view } = camera;

    regl.clear({ color: [0, 0.1, 0.26, 1] });

    drawSH({
      offset: [0, 0, 0],
      drawSphere: false,
      projection,
      view,
      secs: secs / 10
    });

    yield Object.assign(
      {
        secs: secs.toFixed(2)
      },
      camera
    );
  }
```

## 附录：本文中参与叠加的低阶SH函数

![Untitled](%E4%BD%BF%E7%94%A8WebGL%E5%AE%9E%E7%8E%B0%E7%AE%80%E5%8D%95%E7%9A%84%E4%B8%89%E7%BB%B4%E4%BA%A4%E4%BA%92%201cb79c629c81453caab37f658ebfe84c/Untitled%202.png)