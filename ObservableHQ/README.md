# Observable HQ

JAVASCRIPT gives HTML amazing Abilities to present Things.

The **Subject** tries to explain the benefits of the environment.

The folder contains following md files:

---
## 2023 年北京中考成绩的按区分布

东城、海淀和朝阳三个区的加权平均成绩高于 600 分。

虽然东城区的加权平均值最高，但主要得益于参考人数较少。初中阶段教育质量最高的属海淀区，从分布上看属于遥遥领先。另外，朝阳区和西城区处于二者之间。

至于其他的区，洗洗睡吧。

本文很无聊，代码可见我的 ObservableHQ 笔记本

[Beijing high school entrance exam](https://observablehq.com/@listenzcc/beijing-high-school-entrance-exam)

## Bunny Render

本文尝试通过 WebGL 渲染 Bunny 兔子模型，它的颜色受到一个简单的神经网络的控制。

从结果上来看，虽然实验用的神经网络极其简单，但它可以用来高亮模型表面的任何区域。

本文代码可见我的前端笔记本

[Demo of Neural Network](https://observablehq.com/@listenzcc/demo-of-neural-network "Demo of Neural Network")

## Delaunay 算法的边界风险和规避

在边界处发生未连接的Delaunay邻居存在一些特定的风险，它是由于算法“误认为”两个点之间的有邻居关系，但它们的连接点又位于边界之外。本文对这种现象进行解释，并尝试进行规避。

本文开源代码可见我的 ObservableHQ 笔记本

[Delaunay neighbours / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/delaunay-neighbours)

## Delaunay算法与应用一例

本文尝试使用Delauney算法进行快速次近邻检索。该方法在d3.js库的帮助下，能够在数十毫秒内解决10000个点的次近邻问题求解。本文的开源代码可见我的在线开源笔记本

[Find the closest Two points using the delaunay](https://observablehq.com/@listenzcc/find-the-closest-two-points-using-the-delaunay)

## EEG 和 LFP 相互关系的动态展示

本文对 LFP（局部场电位）和EEG（脑电图）的理解进行简单的可视化，要表达的信息是 LFP 是大脑内部 $Na^+, Ca^{2+}$等离子有序迁移引起的局部电位变化，而 EEG 是在头皮表面，以无创的方法采集到的电场强度变化。

本文通过一段代码直观地展示了这一过程，你可以在这里找到它

[LFP & EEG](https://observablehq.com/@listenzcc/lfp-eeg)

## Enigma 的原理示意

Enigma（译为恩尼格码）密码机是一种使用配对设备进行同步加密和解码的机械式密码机，本文是在前人代码的基础上，通过添加着色的方法使其原理更加便于理解。本文的开源代码可见我的 ObservableHQ 笔记本

[Enigma machine demo](https://observablehq.com/@listenzcc/enigma-machine-demo)

## Gabor 函数的参数空间-1

Gabor 函数是常用的数学函数，可以用来对多种物理现象进行表达。

> 函数在参数空间沿最短线移动时，与目标的距离先上升后下降，这导致梯度方法无法用于寻找到这条路径。

换句话说，Gabor 函数在参数空间中是非凸的。

开源代码可见我的前端笔记本

[Parameter Space of Gabor](https://observablehq.com/@listenzcc/parameter-space-of-gabor "Parameter Space of Gabor")

## Gabor 函数的参数空间-2

本文是接续前文的拓展，探讨在估计最优参数时，梯度下降方法是否能够得到最优解。

梯度下降可能有三种结果

1. 能够得到几乎正确的结果，但过程曲折；
2. 能够得到几乎正确的结果，过程也与理想轨迹大致吻合；
3. 梯度下降轨迹与理想轨迹南辕北辙。

本文代码可见我的前端笔记本

[Parameter Space of Gabor (Gradient)](https://observablehq.com/d/e5f15050d1568991 "Parameter Space of Gabor (Gradient)")

## NBA 赛季投篮数据可视化

我使用开源工程下载典型的投篮数据库，记录的信息非常丰富，从表中可以查到这样的信息

> 在某一节的某一分钟，某名球员在某场比赛中，在球场上的某个位置进行投篮。投篮的结果是投中 | 未中。

我据此绘制了投篮出手的球场位置分布图和时间分布图，开源代码可见我的 ObservableHQ 笔记本

[NBA Player Shot Statistic (2022-23 Regular Season)](https://observablehq.com/@listenzcc/nba-player-shot-statistic-2022-23-regular-season)

## NBA 赛季投篮数据可视化（二）

本文对 NBA 2022-23 赛季常规赛部分球员的投篮数据进行细化统计，开源代码可见我的 ObservableHQ 笔记本。

[NBA Player Shot Statistic (2022-23 Regular Season)](https://observablehq.com/@listenzcc/nba-player-shot-statistic-2022-23-regular-season)

## Perlin 噪声与随机地形

在许多情况下，需要生成随机的地形或者空间连续的随机变量。

这里 Perlin 噪声往往是很好的选择。

比如我在前端页面做的一个小demo [Perlin Noise Contours with GeoProjection](https://observablehq.com/@listenzcc/perlin-noise-contours-with-geoprojection "Perlin Noise Contours with GeoProjection")

## Observable HQ

JAVASCRIPT gives HTML amazing Abilities to present Things.

The **Subject** tries to explain the benefits of the environment.

The folder contains following md files:

## THREEJS 的三阶魔方

春去江花红胜火，春来江水绿如蓝，能不忆江南。这个周末气温回暖，草木发芽，于是在家有前端做了个虚拟化的三阶魔方。本文的开源代码可见我的前端笔记本

[Rolling magic cube with THREE.js](https://observablehq.com/@listenzcc/rolling-magic-cube-with-three-js)

## WebGL的实时渲染

本文提供一个前端样例，用于实时捕捉流数据并进行计算和渲染。

开源代码可见我的前端笔记本

[Image Cookbook](https://observablehq.com/@listenzcc/image-cookbook "Image Cookbook")

## WebGL绘图（之一）

`WebGL`是重要的前端技术之一，
是高性能的像素级渲染工具。

## WebGL绘图（之三）

我在之前的基础上添加了一点点细节。
现在能够呈现一个动态的复数空间。

## WebGL绘图（之二）

不得不说`WebGL`是个坑，坑在哪呢？
一是计算机语言，二是高等数学。

## 一个简单的动力学模型

借助JAVASCRIPT的实时计算工具，HTML（也就是网页）具有强大的​呈现能力。
而以D3为代表的工具进一步简化了这一过程。
本文借助该平台，建立了一个简单的动力系统。
该系统可以在一定程度上显示出“混沌”现象。

## 一种莫名其妙的自组织结构

我的初衷是在某个图形之内构造一组致密点云，我最初的设想是这个点云应该会**像水波一样，从一个中心向外不断扩张。**但事与愿违，这些点似乎有他们自己的想法，**他们开始自组织起来，以一种匪夷所思的像下围棋一样的方式向外扩张**。这是出乎我意料的，因此记录下来。本文的开源代码如下

[Plot population](https://observablehq.com/@listenzcc/plot-population)

## 万有引力与第一只手

万有引力定律是个伟大的定律，它从数学原理上描述了这个“有序的”宇宙。

然而这个定律并没有保证这个宇宙一定是有序的，甚至不需要要“三体”，最简单的地-日系统都可能直接把地球弹出去流浪。

于是我尝试用模拟的方法解释日-地式的双星系统可以不稳定到什么程度。欢迎访问我的前端笔记本

[Play ground: Law of universal gravitation](https://observablehq.com/@listenzcc/play-ground-law-of-universal-gravitation "Play ground: Law of universal gravitation")

## 不圆的轮子：Reuleaux 三角

人总要摆脱经验造成的路径依赖，比如能够稳定转动的东西不一定就是轮子。本文介绍一种不是圆形的轮子 Reuleaux 三角，它是一种“等宽闭曲线”，能够像圆轮子一样平稳转动。

本文尝试以数据驱动的方式解决解析几何问题，让人可以不依赖几何知识就可以验证以上结果。由于我得到的 Reuleaux 三角是纯数值的，不依赖于几何公式推导，因此，我可以用工程学的方法来模拟它在等宽范围内的转动。结果发现，即使这种曲线能够在水平方向上进行平稳转动，但其转速却并不平稳。另外，曲线不同位置的线速度和轨迹也不尽相同。

这说明这种三角轮子的转动稳定性并不理想。路径依赖虽然有保守的风险，但至少可以规避一些创新风险。本文的开源代码可见我的 ObservableHQ 开源代码库

[Reuleaux triangle](https://observablehq.com/@listenzcc/reuleaux-triangle)

## 乌合之众

系统中多个成员的复杂关系一般可以用网络进行描述，
在该网络中的信息传递效率是值得关注的关键点。

通过本文的模拟可以看到，
一个无中心的，
单纯依靠节点之间的互信进行信息传递的网络，
其网络容量令人难以置信的低。

本文是之前“行路难”系列的延伸，
与之不同的是，本文提供了一个实时模拟和显示代码，
让读者可以“看到”网络中消息“流动”和“迟滞”的动态过程。

## 二维场及其可视化

这是一个进行二维场生成和可视化的前端工具，
但还是初版。

## 云图

最近科研圈出了个大事，就是一度非常火热的老年痴呆与一种知名蛋白沉淀之间的关联指控是数据造假的结果。

简单来说，它等价于这样一种行为，就是我可以通过各种 CG 方法生成一张图，然后把这张图给地球披上，然后指着它说，看吧，这就是之后 30 年的地球气候的云图。

虽然这张图实际上没有一点儿意义。

## 云雾效果

本文是在之前“等高线图”的基础上，
开发了一个类似“云雾效果”或“封冻效果”的渲染生成方法。

## 人口曲线再挖掘⛏️

有的数据不公布了，这不是什么好事儿。虽然上面总有自己的考量，但这提醒我要学学如何从已知的数据进行猜测性分析。本文开始尝试从人口普查的年龄分布数据开始进行分析，初步代码可见我的 ObservableHQ 笔记本

[How many females will have no child](https://observablehq.com/@listenzcc/how-many-females-will-have-no-child)

## 人口曲线再挖掘⛏️【2】

书接上回，继续从人口分布数据中估计未来丁克的女性数量。结论是，未来十数年内，我国不选择生育的女性数量约为 2500 万人。这是相当保守的估计，因为我目前的假设是所有新生儿都是一人一胎，杜绝多胞胎和一人多胎的情况。因此，未来 5 千万到 1 亿不生育的年轻人将是我国必将面临的新常态。开源代码还是在这里

[How many females will have no child](https://observablehq.com/@listenzcc/how-many-females-will-have-no-child)

## 人口红利

姜文电影有一句名言

> 我就是为了这碟醋，才包的这顿饺子。

我让 ChatGPT 给我编了一段解释兰彻斯特方程的代码，于是我给它加了一个可视化的壳，现在已经说不清谁是饺子谁是醋了。代码可见我的前端笔记本

[The Lanchester function explaining by ChatGPT](https://observablehq.com/@listenzcc/the-lanchester-function-explaining-by-chatgpt "The Lanchester function explaining by ChatGPT")

## 今天的风儿有些喧嚣

今天刮大风，刮的建筑像要被吹跑似的。
所以趁着机会做一个简单的粒子运动模拟。

## 从地理交互看 Walmart 的时间线

本文是结合地理数据与 Walmart 经营数据的可视化尝试，尝试使用可交互的手段提升对数据的理解。从静态图中可以明显看出 Walmart 发迹于美国中东部，而后逐渐向东、西两个海岸发展。虽然这个趋势非常明显，但会忽略它发展轨迹中的一些细节，这些细节可以从可交互的可视化分析中得到生动的补充。

[An animation demo of Walmart in America / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/an-animation-demo-of-walmart-in-america)

## 使用二维拓扑表示三维魔方

二维拓扑是指在平面上表示物体的形状和关系，而三维魔方是一个由小立方体组成的立体结构。虽然二维拓扑无法直接表示三维魔方的立体性质，但我们可以使用映射的方法通过二维拓扑表示魔方的交换群特性。

本文的可交互代码可见我的 ObservableHQ 在线笔记本

[Magic cube in 2D space](https://observablehq.com/@listenzcc/magic-cube-in-2d-space)

## 便携的深度网络

最近 ChatGPT 从实验室走到了千家万户，这说明虽然深度网络是极其依赖于计算资源的服务方式，但只要通过合适的技术途径，是可以实现轻计算终端接入的。在神经网络计算功能日益强大的今天，这是复杂计算落地的必由之路。因此，本文提供一个 DEMO，将预训练好的轻量图像计算网络直接放在前端进行图像识别计算。

本文开源代码可见我的前端代码库

[The TensorFlow in Javascript](https://observablehq.com/@listenzcc/the-tensorflow-in-javascript "The TensorFlow in Javascript")

## 保守场的最短路径估计

本文将“最速降线的蒙特卡洛逼近”一文的方法推广到任意的保守场。

开源代码可见我的前端笔记本

[Estimate the Brachistochrone using Monte Carlo Simulation V2](https://observablehq.com/@listenzcc/brachistochrone-using-monte-carlo-simulation-v2 "Estimate the Brachistochrone using Monte Carlo Simulation V2")

## 信息茧房

都说互联网是个信息茧房，所以我们就来试试。

其实什么也没试出来。

## 像上网一样使用FSL

`FSL`是个好软件，
它强在皮层水平的各种统计计算。
但缺点同样明显，
它太难用了，
如此功能强大的软件却将数据格式过度封装，
导致除了它给定的几种算法之外，
想要做出一点扩展都艰难异常。
让人非常费解。

本工程做出一些尝试，
希望让它的分析和呈现能够变得像“上网”一样简单。
目前，离这个目标还相当之遥远。

## 光场渲染的 MRI 点云

Nerf 是用深度神经网络表达某个物体，虽然我没有这个本事构造深度神经网络，但好在我并不需要这么做，因为我只要能根据已知的点云，把 MRI 数据渲染出来就达到目的了。本文开源代码可见我的在线代码笔记本

[3D MRI volume rendering in slices with WebGL](https://observablehq.com/@listenzcc/3d-mri-volume-rendering-in-slices-with-webgl)

## 全国铁路站点

本文尝试使用 mapbox，force graph 和 sankey diagram 对全国铁路车站进行可视化。

本文绘图代码可见我的前端库

[Railway stations](https://observablehq.com/@listenzcc/railway-stations "Railway stations")

本文数据预处理的代码可见我的 Github 库

[China-rail-way-stations-data](https://github.com/listenzcc/China-rail-way-stations-data "China-rail-way-stations-data")

效果看着还行，所以最后还有一点碎碎念。

## 函数映射

本文在 Observable 提供了一个好用的函数可视化工具。

[Mathmatic notebook III](https://observablehq.com/@listenzcc/mathmatic-notebook-iii "Mathmatic notebook III")

## 刹车对车流造成的持续性影响

由于汽车的加速能力远不及刹停能力，因此在密集车流中，前车的刹车会对后车造成持续性影响。本文动态仿真了这一过程。本文构造了一个循环的车流系统，不许超车。在系统中，多辆小车沿圆形轨道自主行进，所有小车均**在恰好不与前车相撞的最佳车距的最佳时刻选择制动**。

开源形码可见我的 ObservableHQ 笔记本

[How can a break slow down the running cars](https://observablehq.com/@listenzcc/how-can-a-break-slow-down-the-running-cars)

## 前端是个好东西，但需要数据支撑

前端是个好东西，但需要数据支撑。所谓产业赋能就是强大的后台+好用（好看）的前端。本文以地铁为例做一次眼高手低的尝试。

## 前端的GPU渲染库

GPU是强大的计算单元，擅长进行较大规模的并行计算。

本文通过一款优秀的前端GPU渲染库，提供几个GPU渲染的前端样例。

[Learning GPU-IO](https://observablehq.com/@listenzcc/learning-gpu-io "Learning GPU-IO")

## 前端输入微调交互样例

Figma 是一个十分漂亮和高效的原型设计辅助软件，在使用它的过程中，遇到了很多提升用户交互效率的小 Trick。

本文复现了 Figma 上的一个十分用户友善的应用，它在前端输入时，允许用户采用鼠标拖动的方式对数值型输入进行微调。

## 北京中考成绩的统计分析，我仿佛看到了城乡差异

本文对 2023 年中考成绩分布，我仿佛看到了城乡差异。从成绩上看，北京的高中似乎只对东城、海淀、朝阳和西城区的初中生开放。其中，前 4 区的学生成绩明显优于其他区。另外，东城区没有海淀区名气这么大，但东城区的 CDF 曲线与另外三区之间有一定的间隔，说明这个区的学生成绩更高。

另外，在 625 分以上的学生中，他们“均匀”来自 18 个区的假设不能成立。这说明成绩好的区在高成绩方面有近乎垄断的优势。

本文涉及的理论内容见附件，本文的代码可见我 ObservableHQ 笔记本

[Beijing high school entrance exam](https://observablehq.com/@listenzcc/beijing-high-school-entrance-exam)

## 北京西北水系与万里长城

前两天跟老同学聊天儿，聊起北京洪灾。我说那边的地势比较容易受山洪影响，还给他画了张图。他看地图不错，于是想在上面看看长城。但我惊讶地发现，现在的地图工具没有提供这个功能，于是我就画了一个，在我的 ObservableHQ 笔记本上。

[Great wall display](https://observablehq.com/@listenzcc/great-wall-display)

## 历代君王

刷B站看到一条弹幕，
它说雍正和华盛顿是一个时代的人。
于是我就统计了一下，
还真是。

## 变异 Covid-19

人年纪大了就会不自觉地思考最后的归宿，死 Covid-19 可乎？

不停地变异是病毒的特点之一，感染数量和范围可以看作是变异的直观反应。

本文从 **pango_lineage** 分类学数据库出发，试图对 Covid-19 如何变异提供一个可视化视角。

代码可见我的前端程序库

[The pango-lineage of Covid-19](https://observablehq.com/@listenzcc/the-pango-lineage-of-covid-19 "The pango-lineage of Covid-19")

## 后验概率的暴力计算

本文提供一种后验概率的暴力计算思路，但很遗憾，暴力计算解的精度低于解析解，这也许就是数据驱动的机器学习和数据分析之间的差距。

本文的开源代码可见我前端代码库

[Simulation of Maximized Posterior Probabilities](https://observablehq.com/@listenzcc/simulation-of-maximized-posterior-probabilities "Simulation of Maximized Posterior Probabilities")

## 吹气球

`FreeSurfer`是将功能磁成像数据映射到大脑皮层空间的软件。
它的计算原理就像吹气球。

## 图神经网络的计算和收敛

图神经网络是考察节点关系的模式识别方法。
多用于解决复杂系统中，
针对节点之间的关系进行运算的模式识别问题。

本文是对它的运算过程进行模拟，
并且尝试通过简单的例子，
说明这类网络的收敛性。

本样例的代码可见[我的开源代码](https://observablehq.com/@listenzcc/graph-network "我的开源代码")

## 在太阳内部航行

真空中的光速为每秒30万公里，
但太阳最内部发出的光则需要10万年才能到达太阳表面，
这是由于那里的光子需要不停的与其他光子发生碰撞。

## 在线实验的信号边缘频率失真

所谓在线实验就是将连续信号不断切断，并且在断口处进行实时分析的苦逼过程。然而信号的有些频率成分会在断口处出现较大的失真，这是离线算法不能直接移植到在线实验场景的重要原因之一。

本文直观地显示了这一点，开源代码可见我的ObservableHQ 笔记本

[EEG filters](https://observablehq.com/@listenzcc/eeg-filters)

## 地图工具 V0.1

地图是一个让人能够更加理解地缘的好东西。

于是我决定一点一点地做一套自己的地图工具。

## 地铁密度对比

在某个神奇的国度，不是每个人都有把握方向盘的权力，因此，地铁就是出行的主力。

本文试图通过蜂窝状的网格进行计数，用来对各个地区的地铁方便程度进行量化。

本文代码可见我的前端笔记本 

[Subway stations in hex grids](https://observablehq.com/@listenzcc/mapbox-with-hex-grids-version-3 "Subway stations in hex grids")

## 均贫富

本文是使用 Atomic Agents 分析另一个有意思的问题。

> 在平等交易的前提下，贫穷和富裕是如何诞生的？

本文的分析结果偏向于认为贫穷和富裕是在自由交易的市场中自发形成的，动态平衡的经济学现象。

## 基于Delaunay算法的自组织纹理

本文将“人以群分”的原则应用在随机分布的点集中，其中Delaunay算法用于确定每个点的邻居及其阶数。如果某个点类别不是其邻居点集的简单多数时，他就选择搬家。无数个这样的个体会导致整体上呈现某种纹理，实验结果说明多样性越低，邻居的外延性越强，越容易生成较大的连片”集合“。

[Crazy neighbours by delaunay](https://observablehq.com/@listenzcc/crazy-neighbours-by-delaunay)

## 基于GPU的快速Julia集计算

本文记录一个利用GPU计算的前端程序，它用来在PC上快速计算和实时渲染大量迭代的 Julia 集。由于 GPU 算的实在是太快了，因此我决定让它成为一个实时计算和渲染程序。开源代码可见我的前端笔记本
[The Fractal (Julia Set) on GPU](https://observablehq.com/@listenzcc/the-fractal-julia-set-on-gpu "The Fractal (Julia Set) on GPU")

或GITHUB页面
[JuliaSet-GPUIO](https://listenzcc.github.io/JuliaSet-GPUIO/ "JuliaSet-GPUIO")

## 基于人口普查数据的性别比例分析

出于偶然，本文尝试对第七次人口普查的公开数据进行分析，尝试将表 1-5 和 1-6 中的性别差异进行可视化。**本工程的特点是形成的数据更加像是数据库，因此更加便于进行可视化分析。**得到初步结论如下

- 天津户籍人口，他参加高中入学考虑并考上高中的概率约为 $66 \% \sim 77 \%$；
- 按照地区和年龄进行区分可知，我国男性青年多于女性，大约多 $10 \%$；老年女性多于男性，且二者差异随年龄不断扩大；
- 如果中国有“重男轻女”的观点的话，那么它造成的恶果是小学升初中阶段失学女童数量多。而是之后的教育阶段中，除了攻读博士研究生女性较少之外，女性均强于男性。

开源代码可见

[https://github.com/listenzcc/population-by-gender-1](https://github.com/listenzcc/population-by-gender-1)

[Population by gender - 1](https://observablehq.com/@listenzcc/population-by-gender-1)

## 增长方程的两个不变性

本文将在前文的基础上，对增长方程的性质进行简要分析，即从矩阵的行和列观点来看，分析它的两个不变性。分析和演示代码可见我的前端代码库

[Generating the Optimized Production Matrix II](https://observablehq.com/@listenzcc/generating-the-optimized-production-matrix-ii)

## 增长的最优系数

在前文中，我们论述了在指定生产矩阵的条件下，如何确定初始化资源比例，以及在这种比例下增长会如何发生。

本文将这个过程反过来，尝试解决在给定初始条件和期望增长的前提下，如何选择生产方程的问题。

## 大事记

最近有同志去世，比较好奇他在任期间有哪些大事，于是找到了官方的权威文档，但这个文档看起来有点麻烦，于是我尝试把它们整合在一个页面里。

[中华人民共和国大事记（1949 年 10 月－2009 年 9 月）*历史概况*中国政府网](http://www.gov.cn/guoqing/2009-10/09/content_2582666.htm "中华人民共和国大事记（1949年10月－2009年9月）_历史概况_中国政府网")

[Story of China](https://observablehq.com/@listenzcc/story-of-china "Story of China")

## 大新闻

号外号外，真有文化人说别人是犬子了。

## 大风扯乎

最近在知乎上看到一篇奇文，
算是“地摊文学”的上乘之作，
隐隐然有种《细菌、病毒与钢铁》的扯淡气魄。

于是找了点材料，
看上去还真是这么回事。
本文的分析代码可见
[我的代码本](https://observablehq.com/d/4037ab90a91424a7 "我的代码本")

## 天津中考成绩的数值分析

本文尝试对2023年度天津中考成绩进行分析，讨论学生和郊区学生在不同分数范围下的表现以及估计他们进入高中和大学的情况。

市区学生在高分范围（>750）表现更好，而郊区学生在中等分数范围（~700）表现更好。高中录取方面，市区学生的录取要求分数约为580，而郊区学生为560。

进入大学的情况根据高中入学考试成绩进行估算，其中郊区学生在985211工程大学录取中略处于劣势，而在总计录取中表现出优势。综合而言，学生的地区背景可能会对录取结果产生一定影响，

本文的数据图可见我的 ObservableHQ 笔记本

[High school entrance exam in TianJin](https://observablehq.com/@listenzcc/high-school-entrance-exam-in-tianjin)

## 好界面是拖出来的

本文提供一个大道至简的界面编辑框架，解决的痛点是普通人如何把“我要把这个框框画在那个位置”这个朴素的审美需求转化成程序员能看懂并用程序实现的设计需求。本工程的代码可见我的 ObservableHQ 笔记本

[Layout player](https://observablehq.com/@listenzcc/layout-player)

## 字体比较工具

这是一个字体比较工具，它的优势是快捷和风格可调。

目前确有这样的在线工具，但它们可能 ​ 没办法像我这样实时调整背景。

## 宇宙为何空空荡荡

这是标题党，但又不全是标题党，因为我有实验。

## 将FSL统计结果映射到FreesSurfer皮层上

这是一个工作过程记录。
总的目的是将`FSL`的预处理及统计分析结果，
映射到`FreeSurfer`的皮层空间上。

工作流可见我的[GITHUB工程](https://github.com/listenzcc/freesurferAnalysisScripts "GITHUB工程")，
可视化代码可见我的[ObservableHQ工程](https://observablehq.com/@listenzcc/free-surfer-cortex-v2 "ObservableHQ工程")。

## 局部最优如何随机地填满整个空间

本文继续用 Delaunay 算法构造一个二维连通图，一些点按照局部最优的规则进行随机游走，我记录了整个连通图中各个节点数量密度的动态变化，并且记录了这些点从源到漏的可能路径。我原本的假设是这些有一定自主性的点会自发地形成较短或较稳定的通路，但事实并不是这样。相反，这些局部最优的点会随机地填满整个空间，并且整个分布模式随时间变化。

本文的开源代码可见的 ObservableHQ 笔记本

[Random walkers](https://observablehq.com/@listenzcc/random-walkers)

## 布朗桥噪声的三种可视化方法

布朗桥噪声具有回归性质，该特性使得布朗桥噪声在金融建模和信号处理等领域中有广泛的应用。本文通过可视化的方法说明，随着时间的变化，一系列布朗桥的时序变化是统一的，都呈现了先扩散、再收敛的趋势。

另外，我使用 Plotly 工具将全部点绘制在三维图上，用来表示其在三维空间中可以更加全面地展示整体分布。本文的开源代码可见的 ObservableHQ 笔记本

[Simulate diffusion using Brownian Bridge](https://observablehq.com/@listenzcc/simulate-diffusion-using-brownian-bridge)

## 布朗桥（Brownian Bridges）

在建立某个随机动力过程时，我们虽然希望其随机性尽可能大，但又要防止它的范围过分扩张。通过使用合适的约束手段，我们可以达到这一目的，Brownian bridge 是其中之一。

本文的开源代码可见我的 ObservableHQ 笔记本

[Brownian Bridges](https://observablehq.com/@listenzcc/brownian-bridges)

## 弯道超车

滑冰也好，赛车也好，
都是速度的游戏。
而弯道既是速度的瓶颈，
更是超越的机遇，
所以是比赛的关键。

本文是使用**动态规划**的方法，
对通过弯道的**最快方案**进行估计。
该方法简单和粗糙的不可理喻，
但它的结果似乎又有点靠谱。
气不气人。

经过一通分析告诉我们一个道理，
玩赛车或者滑冰等竞速游戏，
遇到弯道要记得

> 早刹车、切内弯，然后油门焊死，你就赢了。

所以，在冬奥会看滑冰，
他们那帮人才会在入弯时拼了命地使小动作，
毕竟谁占内弯，谁就赢。

## 形式逻辑的陷阱

最近 ChatGTP 火出圈了，但和小伙伴交流发现，大家都认为这种语言模型可能会让人误会他说的是有道理的，即使它们只符合形式逻辑。因此，不能简单地拿它当作搜索引擎用，并且只有明确地知道它返回结果的意义，才能更好地让它为人服务。

本文以容易理解的二维场作例子，试图说明在采用不同的计算方法时，场的叠加可能会得到截然不同的结果，即使这些结果看上去都还行，但是否能够反映实际情况，则有待分析。本文的例子可见我的前端笔记本

[The gravity field of two stars III](https://observablehq.com/@listenzcc/the-gravity-field-of-two-stars-iii "The gravity field of two stars III")

## 扩散模型-1

最近扩散模型比较火，所以本文尝试用前向计算尝试对它进行解释。

本文的代码可见我的前端笔记本

[Diffusion Model Demo (Forward)](https://observablehq.com/@listenzcc/diffusion-model-demo-forward "Diffusion Model Demo (Forward)")

## 扩散模型-2

本文尝试将扩散过程反过来，即从随机噪声“生成”有意义的图像或者数据。

## 色块拼图

计算机里的图像一般是方方正正的，
由像素组成的矩形集合。

而人描述一个场景或图像时，
所使用的往往不是这样规矩的矩形，
而是这样的话语

> 这里有山有云，在夕阳下，
> 山和云都显出很好看的红色。

因此，我们或许可以尝试使用“色块”对场景进行描述。

【这是一段棒到不行的视频】

本样例的代码可见我的[在线笔记本](https://observablehq.com/@listenzcc/quadtree-art "在线笔记本")。

## 数据截断及估计

继上文“滤波及失真”之后，我们还需要考察的问题是，是否能够使用被截断的信号来估计出原始信号。当然，这里的反推并不是完全的还原，因为对于随机信号来讲，我们往往更关注它的统计特性，而非具体取值。这就要在频谱上做文章。

## 文件结构树

现代计算机操作系统往往会用目录树的结构来维护用户的文件。

但用户面对这个树形的结构往往需要四处翻找，才能找到他想要的文件。

因此，本文尝试用交互式圆饼图展示文件结构，力图用最简洁的方式来帮助用户找到他需要的文件。

## 新冠地图

本文是简单的染色地图，
染色的数据是新冠疫情爆发以来，
世界各国的感染人数、死亡人数和死亡率。

## 无限上升的卡农

交变电场产生磁场，
而为了产生稳定的磁场，
就需要建立时刻变化的电场，
就像《GEB》书中写到的所谓“无限上升的卡农”。

## 日地月-2

本文是上文《日地月》的补足。
我用`THREE.js`建立了一个三维模型，还是太阳-地球-月亮互相转动的故事。

## 日地月

我用`ObservableHQ`平台搭建了一个好玩的`DEMO`。
它形象地展示了为啥一个月有大约`30`天，
以及为什么月相会呈现一种奇妙的周期性。

## 时间的漩涡

在时间的河流中，日子容易过得头昏脑涨。我觉得时间像个齿轮令人眩晕，人在眩晕中顾不上看年华老去。本工程希望通过螺旋的时间线来传达我的感受。怎么说呢，反正看上去可能有点晕。

开源代码如下

[How do the time pass?](https://observablehq.com/@listenzcc/how-do-the-time-pass)

## 最速降线的蒙特卡洛逼近

本文进行了一次尝试，尝试通过简单粗暴的蒙特卡洛方法逼近一条“最速降线”。

本文代码详见我的前端仓库

[Estimate the Brachistochrone using Monte Carlo Simulation](https://observablehq.com/@listenzcc/estimate-the-brachistochrone-using-monte-carlo-simulatio "Estimate the Brachistochrone using Monte Carlo Simulation")

## 机械臂运动控制的位置和角度关系及其可视化

本文是记录一个交互式可视化工程，
它对二维二轴机械臂的平面运动过程中，
控制角度与机械臂端点位置的相互关系进行可视化，
并且允许用户通过鼠标模拟二者之间的对应关系。

## 三轴机械臂运动的逆解

在`THREE.js`的支持下，我们可以做出一些有意思的应用。
比如模拟一个三轴机械臂的运动。
于是有了这个缝合怪。

## 树形数据结构的表形管理

这篇东西仍然比较无聊，它描述了如何用表对一种树形数据结构进行表达。

树形数据结构支持深度和广度遍历，优点是使用灵活，缺点是内容偶合度过高，导致难以单独存储；

而表形数据结构则更贴近数据库，优点是条目清晰，易于存储。

本文尝试在牺牲一定存储空间的条件下，用数据库的形式对树结构进行一定程度的表达。

## 每日一图

不得不说`BING`的每日一图是真的好看。
不妨以为契机，记录一下前端绘图的一些经验和坑点。

## 气温地图

接着上回的温度数据，再做一点工作。

具体来说，我关注一个温度指标，它就是

> 今年 7 月的温度比去年同期高多少？

能看得出来，我国西南今年是真的热，

> 有多热？比去年高 9 度的那种热。

## 水球效果

这是一个在真空中的水球效果的模拟。
不是物理模拟，
而是看上去相似的一个动画。

## 涂鸦玩具

窗外在下雨，这种天气特别适合在家写程序。正好学一下 pixi.js，并与 perfect-freehand.js 结合，写了一个特别跟手的涂鸦绘板 demo。源程序可见我的 ObservableHQ 页面

[Hand writing with Pixi.js & perfect-freehand](https://observablehq.com/@listenzcc/hand-writing-with-pixi-js-perfect-freehand)

## 滤波及失真

针对信号进行滤波是信号处理的基本操作之一，它可以用来提取信号中我们感兴趣的特定成分。

但操作必然会导致信息量的损失，失真就是这种损失的直观表现。

这个话题很大，我就遇到哪写到哪。

## 漂移变道

最近常做梦，梦到买了辆车，车牌号很吉利，叫做 BJHJYD。

买了车咱就开，那么问题就来了，为啥超车变道的时候需要后车刹车呢？

为了回答这个问题，我写了个前端程序

[Over taking](https://observablehq.com/@listenzcc/over-taking "Over taking")

## 激活函数的功率谱密度

本文从量化的角度解释双曲正切激活函数对信号的 FFT 造成的影响。
本文开源代码可见我的前端笔记本
[FFT for Activation](https://observablehq.com/@listenzcc/fft-for-activation)

## 点集的着色及其生成顺序分析

我们之前在给定图形之内构造了一组致密点云，本文进一步解决如何对这些点进行分类着色的问题，并分析点集的类别与生成顺序之间的关系。如果我们稍微放飞一下自我，也许它可以作为一个 demo，用于解释机器学习中的“涌现”现象。

开源代码位置仍为

[Plot population](https://observablehq.com/@listenzcc/plot-population)

## 物以类聚

都说物以类聚，人以群分。但又都说要兼容并包，兼收并蓄。

后一个说教其实大家都不怎么喜欢听，因为它天然的假定物以类聚这个现象，是因为个体微观的不够包容而造成宏观现象。

也就是说错在个人，社会是个人意愿的加和。

而群体行为的研究却有证据认为，群体行为往往不是个体行为的简单累积，而是具有混沌属性，往往与参与者的主观意愿相悖。

落实在本问题上，即使每个人都很大程度的包容自己的邻居，在群体层面也会呈现出极其严重的分类和隔离。

## 特斯拉阀水管的粗糙模拟

特斯拉阀（又称 fluid diode）是一种单向阀门，也被称为流体二极管。

出于好奇，我用之前的粒子模拟程序做了一个简单的 demo，实验结果表明顺向流动的出口流速大于逆向流动，在一定程度上模拟了 fluid diode 的特性。

开源代码可见我的 ObservableHQ 笔记本

[LiquidFun Tesla Fluid Diode explain](https://observablehq.com/@listenzcc/liquidfun-tesla-fluid-diode-explain)

## 生产与增长

最近看到一个东西，叫做“增长方程”。它可以在一定程度上解决两个问题，一是在生产开始之前预知增长能否持续，二是预知生产的最优初始条件。它附带地解决了另一个问题，那就是为什么总有人说增长一旦停滞，就意味着 some thing is going very wrong.

[Growth equation](https://observablehq.com/@listenzcc/growth-equation)

## 瞎画的艺术

数据科学往往能在不经意间诞生艺术创作。

但这个过程可能有点过于不走心了，所以称为瞎画的艺术。

## 程序员的格子

我用 Mapbox 做了一个地图玩具，可以对地图进行精准定位，并且方便比较。

工程可见我的代码笔记本

[map-grid-by-mapbox](https://observablehq.com/@listenzcc/map-grid-by-mapbox "map-grid-by-mapbox")

## 等高线图

等高线图，又称为等势线图，
是对样本点的场的势面进行可视化的制图方法。

数学上，等高线图需要根据边界条件，
对连续函数进行求解。
但由于实际上并不可行，
因此本文提供一个的生成式的离散逼近方法。

## 素描

花鸟鱼虫皆入笔下，魑魅魍魉信手拈来。绘画素描应该是个挺有意思的事情，但可惜我并不会。

但不妨碍我看到一张图，就看看它用素描的方法画出来，是个啥样子。纯属好奇。

## 统计检验工具-F分布的可视化和速查工具

本文构造了一个方便的前端工具，能够以可交互的方式展示 F 检验中 F 值与 p 值之间的关系。这种工作本身没有意思，因为它除了根据已有的知识构造一个工具之外别无科学价值。

但本文在代码方面能够解决两个问题，首先它提供了 javascript 标准库引用的方法，其次它以更直观的方式展示了 F 分布在实数域的全貌。

本文开源代码与可交互页面如下：

[Stats of F Distribution](https://observablehq.com/@listenzcc/stats-of-f-distribution)

## 三维场景的受力模拟

本文还是基于`THREE.js`的三维场景呈现。
但缝合了`D3`的力模拟功能。

## 脑皮层的褶皱渲染

大脑皮层是高度卷曲的褶皱状结构。本
[前端工具](https://observablehq.com/@listenzcc/vertices-render "前端工具")
试图展示这一点。

## 腿部运动轨迹重建

这一个基于`THREE`的可视化工程尝试。
基于`IMU`角度信号对行走过程中的腿部运动轨迹进行重建。

## 致最可爱的天津地铁

虽然规模不大，但换乘可是一点都不方便。

与北京和上海相比，它会给你带来物超所值的通勤体验。

本文开源代码可见

[Subway stations v2](https://observablehq.com/@listenzcc/subway-stations-v2 "Subway stations v2")

## 艺术细菌

用了三种方法对图片进行艺术化渲染，分别是低分辨率化、马赛克化和动态化。
工科狗的艺术细菌就长到这了。。

## 蓝队加油

INTEL新近发布了第`12`代CPU，
在长时间挤牙膏之后，终于爆发了一次。
虽然没有了当前“默秒全”的统治力，
但新产品确实是让人大呼NB。

本文是十分应景的一文，
正好有一个良好的实验，
来说明“睿频”这个功能为计算资源的释放提供了怎样颠覆性的贡献。

## 贷款与存款

这是在不考虑通胀的条件下，按揭、月供和储蓄之间相爱相杀的故事。
首先，它回答了贷款一定金额时，其本息相当于在银行存了多少钱；
之后，它回答了“等额本息”月供的计算方式，以及当确定首月还款特定数量的本金时，多少个月后能够结清贷款。

[Saving & Loan Curve](https://observablehq.com/@listenzcc/saving-loan-curve)

## 跳舞火柴人

本文以 Openpose 的骨架识别能力为基础，从视频中解析出人体关节的实时位置，并进行绘制。

解析代码可见我的 GitHub 仓库

[https://github.com/listenzcc/dancing-body](https://github.com/listenzcc/dancing-body "https://github.com/listenzcc/dancing-body")

绘制代码可见我的前端笔记本

[Dancing Body](https://observablehq.com/@listenzcc/dancing-body "Dancing Body")

## 辛普森悖论

在统计学中有一个挺神奇的悖论，称为辛普森悖论（Simple’s Paradox）。

简单来说，就是“在分组比较中都占优势的一方，在总评的时候有时反而是失势的一方。”

本文试图通过交互式的可视化方法，对它进行解释。

并且试图说明这种矛盾的情况并不是很偏僻的角落，甚至在合适的构造方法下，这种矛盾总能发生。

## 那些弃籍的美国人

根据一些奇奇怪怪的美国法律，
它的国务院会公开一些奇奇怪怪的信息，
其中就有放弃了美国国籍的人的名单。

本文对这些“不穷”的美国人用脚投票的结果进行可视化。

## 那抹五彩斑斓的黑

感谢 Apple，让我们见识到了传说中五彩斑斓的黑。

## 钢笔大厂的产品特点一览

我下载了一份关于钢笔的统计文档，里面收录了不同品牌钢笔的长度及重量信息，稍作统计如下。为了增强分析的可视性，我将派克笔厂现在仍然在产的较为经典的 Duofold International 系列作为参考，用红色十字线来表示，并且对大笔厂产品的重量分布也稍做统计，本文的可交互分析图可见我的前端笔记本

[Fountain pen database / Chuncheng | Observable (observablehq.com)](https://observablehq.com/@listenzcc/fountain-pen-database)

## 长津湖

这篇很俗，但值得一写。

## 随机游走片段的距离度量

本文尝试对随机游走过程得到的随机时间序列进行度量分析，通过分析这些时间序列之间的欧氏距离建立度量空间，并对该空间进行呈现。本文的开源代码可见我的 ObservableHQ 笔记本

[Distance between the brownian bridges](https://observablehq.com/@listenzcc/distance-between-the-brownian-bridges)

## 雨滴打在窗户上

本文使用 Canvas 模拟了雨滴打在窗户上的视觉效果。

实现这个玩意需要在前端实现三个功能，分别是图像的径向模糊、Canvas 绘图的遮罩方式和动态帧动画。

实现过程可见我的前端笔记本

[Rain drop simulation](https://observablehq.com/@listenzcc/rain-drop-simulation "Rain drop simulation")

## 颜色空间映射

本文试图解释一个可视化现象，那就是在单独改变某一个颜色通道的条件下，得到的颜色序列在颜色空间中如何分布。

## 风雨

风雨送人来，风雨留人住。草草杯盘话别离，风雨催人去。

泪眼不曾晴，眉黛愁还聚。明日相思莫上楼，楼上多风雨。

## 黄金分割探测器

所谓闭门造车，出门合辙。如果你遇到一个构图问题，比如摄影或者做 PPT 什么的，那么黄金分割律就是你要合的辙。本文提供了一个可交互的前端工具，用来从好看的图中找到其中的黄金分割律

[Golden Ratio in Image](https://observablehq.com/@listenzcc/golden-ratio-in-image)

