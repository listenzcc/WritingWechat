# WebGL 页面中有用的 IDE 工具

虽然集成开发环境（IDE）这个概念有点大，但在 WebGL 开发和调试过程中，需要用到 C 和 JS 混合编程的技巧，因此顺手的开发工具有助于提升开发效率。
除此之外， 本文提供的样例渲染过程看上去是透过三角碎片观察一个完整的 HSV 调色板。为了强化这个过程，我在图上渲染了一个圆环，它的半径是 $0.3$。这种渲染思路可以解决一些科学绘图问题，这些问题满足如下条件

> 要绘制某个区域内的全部点，而这些点的颜色有解析的表达式，可以表示为 $color = f(x, y)$ 的形式。
> 

[WebGL's Simple Animation & Stats & Code-Prettify](https://observablehq.com/@listenzcc/webgls-template)

---
- [WebGL 页面中有用的 IDE 工具](#webgl-页面中有用的-ide-工具)
  - [代码高亮工具：****code-prettify****](#代码高亮工具code-prettify)
  - [性能统计工具：****stats-js****](#性能统计工具stats-js)
  - [透视的飘浮三角块](#透视的飘浮三角块)


## 代码高亮工具：****code-prettify****

由于 WebGL 的渲染过程是写成 C 代码之后再编译而完成的，因此需要开发过程中需要进行“在 JS 代码块中添加 C 代码片断”这样的操作，这个操作本身难度不大，但由于 JS 编辑器不提供 C 代码的语法高亮（syntax），因此会产生一种“盲人摸象”的尴尬感觉。

为了减轻这个过程造成的困扰，我使用 code-prettify 工具进行语法高亮，虽然它不是像 VS Code 一样万能，但至少能够让我看清楚代码的基本逻辑、宏定义和重要变量。

![Untitled](WebGL%20%E9%A1%B5%E9%9D%A2%E4%B8%AD%E6%9C%89%E7%94%A8%E7%9A%84%20IDE%20%E5%B7%A5%E5%85%B7%206d9f4c70cdba474a89445c11c87d6fa8/Untitled.png)

![Untitled](WebGL%20%E9%A1%B5%E9%9D%A2%E4%B8%AD%E6%9C%89%E7%94%A8%E7%9A%84%20IDE%20%E5%B7%A5%E5%85%B7%206d9f4c70cdba474a89445c11c87d6fa8/Untitled%201.png)

```jsx
const PR = require("https://cdn.jsdelivr.net/gh/google/code-prettify@master/loader/run_prettify.js"),
  d3 = require("d3"),
  frag= `Very useful fragmentrending c program...`,
  // Where to draw, whose <h2> tag is "Frag for REGL"
	div = document.getElementById("fragDivForREGL");

div.innerHTML = "";

d3.select(div)
  .append("pre")
  .attr("class", "prettyprint linenums lang-c")
  .append("code")
  .text(frag.trim());

// Very important,
// It prettifies the .prettyprint class.
PR.prettyPrint();
```

[npm: code-prettify](https://www.npmjs.com/package/code-prettify)

## 性能统计工具：****stats-js****

由于 WebGL 是高性能的渲染工具，因此我总想知道它的运行情况。我借助 stats-js 做到这一点。它是我在使用 three.js 时遇到的工具，用于显示实时显示运行时的系统性能情况。

![Untitled](WebGL%20%E9%A1%B5%E9%9D%A2%E4%B8%AD%E6%9C%89%E7%94%A8%E7%9A%84%20IDE%20%E5%B7%A5%E5%85%B7%206d9f4c70cdba474a89445c11c87d6fa8/Untitled%202.png)

```jsx
const Stats = require("https://cdn.jsdelivr.net/npm/stats-js@1.0.1/build/stats.min.js"),
  statsMonitor = new Stats(),
  { dom } = statsMonitor ;

// Very important,
// it places the dom on its embedding, instead of the top-left corner of the page
dom.style.position = "relative";

// Example of how to embed the monitor
<div id='statsMonitorDiv'>${statsMonitor.dom}</div>

// Operation for update the monitor's display after each frame rendering
statsMonitor.update();
```

[npm: stats-js](https://www.npmjs.com/package/stats-js)

## 透视的飘浮三角块

除了上述通用工具之外，我还添加了前端的颜色选择和拖动控件工具，把这些控件整合起来就得到了如下的集成效果。看上去是透视的飘浮三角块。

- 三角块的运动是用三个端点的坐标实时调整来实现的；
- 左上角的控件是性能监控，说明系统正以 60 帧进行渲染，内存空间约为 100 ~ 200 MB；
- 右侧是实现渲染的 C 代码，它具有语法高亮。

画面中心点坐标为 $(0, 0)$，整个画幅为 $(-1, -1), (1, 1)$。按照代码来看，渲染的 vertex 为位置不断变换的三角形端点；渲染的 fragment 颜色为 HSV 空间颜色，其中，中心点的饱和度（saturation）为 $0.0$，饱和度按与中心的距离呈线性关系不断增加到 $1.0$，色相（hue）值为到中心点的射线的反正切值。

因此，整个渲染过程看上去是透过三角碎片观察一个完整的 HSV 调色板。为了强化这个过程，我在图上渲染了一个圆环，它的半径是 $0.3$。这种渲染思路可以解决一些科学绘图问题，这些问题满足如下条件

> 要绘制某个区域内的全部点，而这些点的颜色有解析的表达式，可以表示为 $color = f(x, y)$ 的形式。
> 

这种渲染思路不能解决另一类问题，这些问题是这样的

> 要以三角为单位渲染某种仿射变换，这些变换是平移不变的。
> 

换句话说，如果我们不想透视什么东西，而只是渲染三角光栅的话，本例的方法就不太适用了。

![20230911-162458.gif](WebGL%20%E9%A1%B5%E9%9D%A2%E4%B8%AD%E6%9C%89%E7%94%A8%E7%9A%84%20IDE%20%E5%B7%A5%E5%85%B7%206d9f4c70cdba474a89445c11c87d6fa8/20230911-162458.gif)

![Untitled](WebGL%20%E9%A1%B5%E9%9D%A2%E4%B8%AD%E6%9C%89%E7%94%A8%E7%9A%84%20IDE%20%E5%B7%A5%E5%85%B7%206d9f4c70cdba474a89445c11c87d6fa8/Untitled%203.png)