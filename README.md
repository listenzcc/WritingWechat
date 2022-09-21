# The Daily Writing NoteBook

Visit
[Writing](https://listenzcc.github.io/WritingWechat/ "Writing")
to see all the contents.

Everyday, I would like to write something down in this **PROJECT**.

To convert the materials to WeChat Publication Area,
the website of [mdnice](https://mdnice.com/ "mdnice") will be used.

The 2nd level titles refer the topics.
I hope you readers like them.

## The Structure of the Project

In the project, the folders are the separated **Topics**.

The `readme.md` files in the folders will be used as the summary of the **Topic**.
They are listed as following.

---
# File = Content + Coding

In Computer System, the files are the real-world content in coding.

The **Subject** will explain the process.

The folder contains following md files:

---
## 三维模型解析及渲染

解析`GLTF`文件的代码。

## 三维模型的同胚变换

对于特定的三维模型，
我们总是希望它与单位球体具有连续的变换关系。

用数学语言来说，
这叫做“同胚”。

这种变换关系可以用于多个三维模型之间的配准等等。

本文给出了一个简单的实例，
以便对这种变换进行直观说明。

## 文件 = 内容 + 编码 （之一）

在目前主流的电脑系统中，所有的数据都可以看作一组二进制数所构成的具体的流。
如果你拿一个示波器去看，你是能够在主板的合适位置上观测到这一列数字的。
另一方面，这组数据的内容往往对应现实世界中的一张图像、或者是一段文字。
这就构成了一种两端的结构，一端是计算机要处理的物理世界，另一端是计算机的具体硬件，而把这两个具体端联系起来的，我们可以理解成是抽象的编码过程。
本文将解析这一过程。

## 文件 = 内容 + 编码 （之三）

本部分接上文《文件 = 内容 + 编码 （之二）》。

> 我们重新审视编码纠正的工作，会发现 PS 操作过程中，至少暗含着两个未经考察的问题，这两个问题都是针对字节解码的问题，它们分别对应着在纠正代码中所使用的`utf-16`和`latin1`编码协议。
> ……如果我们轻易放过这两个编码问题，我们将错过 W 系统进行中文编码的重要细节，给之后的代码工作留下后患。
> 因此，在接下来的一篇文章，我将对此进行分析。

本文将跳出图像矩阵编码的范畴，讨论在计算机系统中较为一般的符号编码问题。
但是由于该问题过于繁杂，本文将集中讨论 Python 语言环境下的二进制编码问题，以及中文符号加入后，给原先的拉丁字母表达系统造成的麻烦。
另外，由于本部分内容可能包含过多的细节，为了避免失于细碎，我们不妨先将其中容易出现理解偏差的关键节点列写出来，再逐一作出解析。

## 文件 = 内容 + 编码 （之二）

本部分接上文《文件 = 内容 + 编码 （之一）》。

> 至此，我们已经可以将矩阵图像等价成一列数字，之后的工作将专注于对这一列数字进行编码。……这一工作将等同于对矩阵图像本身进行编码。

本文将介绍基本的矩阵图像编码方法，并且给出一个 PS 进行网络请求图像的例子，来具体说明图像矩阵与二进制序列之间互相转换的关系。

## 文件 = 内容 + 编码 （之四）

在《文件 = 内容 + 编码 （之三）》中，我们提到

> 目前，最主流的兼容包括中文在内的多种语言字符的解决方案，是称为 Unicode 的字符集。
> ……为了比 utf-8 更加完整地覆盖 Unicode 字符集（Unicode 的范围为`0x0~0x10FFFF`，可以用来表示大量的特异性字符），计算机系统必须做出广度和效率之间的妥协。

​ 本部分是《文件 = 内容 + 编码》的最后部分，其目的是对之前的遗留问题进行说明，可以当作附录来使用。
但本部分内容也有其自然的逻辑，即同样的内容在计算机系统中，可以具有不同的表达或存储方式。

# Invariance

There are several invariance by math.
Knowing them means knowing everything.

---
## 一些不变性（之一）

函数的本质是映射。
而“不变性”是规范映射变量之间关系的重要渠道。
本文试图从不变性的角度，
探索描述惯性系之间坐标变换的“洛仑兹变换”。

## 一些不变性（之二）

之前提到双曲余弦函数，
它在复数空间内的性质十分有趣。

## 三年以下五年以上

开大会，
重要的议题是立法。
所以本文就尝试对《刑法》的刑期进行可视化。

当然，本文的目的不是要试图说明一个什么事情，
而是举一个反例，
说明数据可以被怎样误用。

## 事件地图

这个统计是基于一个外国小哥分享的地图数据制作的。
从这个统计地图上看，
事件几乎是瞬间发生，
并且一直保持在那里了。

本工程的代码可以见[我的在线代码](https://observablehq.com/@listenzcc/russia-ukraine-war-incidents-over-time "我的在线代码")。

## 卷积及傅立叶变换的矩阵计算

傅氏变换与卷积都可以用矩阵乘法的形式进行表达。
图神经网络的优化正是以这种矩阵形式为基础的，
从信号连续空间到图拓扑空间的拓展。

本文是其中的第一步，
用矩阵的形式表达信号的傅氏变换与卷积。

本文只涉及必要的原理解释，
具体实现代码可见我的[GitHub 仓库](https://github.com/listenzcc/JupyterScripts.git "GitHub 仓库")。

## 合适的统计检验方法

统计检验是个非常复杂的话题。

它在形式上通常非常简单，
对于任何统计检验方法，
你都能喂给它任意两组数，
然后它反馈给你一个$p$值。

因此，如何选择合适的统计检验方法，
让$p$值能够具有明确的统计意义，
就成了问题的关键。

本文将以转换检验的例子出发，
尝试引出一些有意思的检验方法。

## 咬文嚼字

我唯一知道的是我什么都不知道。

哲学从本体论退化到认识论，
再退化到现在的语言哲学，
导致这种情况的根本原因是

> 在语言不恰当的情况下，
> 我们其实什么也说不清楚。

## 四维时空

对于同一个“事件”，
不同的参考系会给出不同的“描述”。
而在光速不变原理的约束下，
空间和时间都是相对的，
它们之间甚至没有差别。

## 卷积定理的矩阵巧合

从矩阵的角度来看“卷积定理”，
仿佛它只是数字角频率完备正交基下的一个特例。

## 数列

数列的存在是为了解决如何表达不那么自然的实数的问题。

## 方差分析（一）

本系列将逐步涉及方差分析的一些概念。
但在此之前，需要厘清一个更基本的问题，
为什么需要对数据进行方差分析。

## 方差分析（三）

本文对随机数据的方差与分割之间的关系进行简要的可视化。
通过可视化的结果可以看到，
建立线性模型的过程，可以形象地看作是一种规划过程；
而方差分析，是对这种规划过程的合理性进行判定。

## 方差分析（二）

上文描述了二阶统计量的稳定性，
本文将基于二阶统计量的计算方式，
对它的变动来源进行分析。

## 方差分析（五）

除了之前介绍的情况之外，
样本变量之间的协方差也是影响方差分析的难点之一。
本文继续进行实验。

## 方差分析（四）

本篇将考察方差分析何时会给出错误的判断，
这种问题很有用，却鲜有人提及。

## 旋转构成不可交换群

辛辛苦苦做了一个多轴联动的系统，
但发现它不能归零。

郁闷半天，发现多轴旋转竟然是不可交换的。

好在我可以用度量张量来证明这件事情。

## 旋转的坐标系

三维空间中，点的运动有平移和旋转两种方式。
因此，需要为点建立自身的笛卡尔坐标系，
从而描述它的旋转过程。

## 有图必有谱

谱聚类是针对“图”的节点分割算法。
理想的谱聚类需要解决 NP-Hard 问题：
分割导致解空间不连续；
而节点搜索导致计算规模随着数据规模而扩大。
因此，谱聚类算法是寻找一个可行的近似解。

## 有限循环群

偶然发现，似乎在所有有限的循环群中，
幺元是群内生的禀赋，
而不需要额外的假设。

这说明，
如果宇宙中先有某种法则的话，
只要我们观测到了自然数，
就无法否定在某个地方，
它能够把原本极大的，映射为极小的，
从而把终点变成起点。

## 样本均衡

在分类研究中，如果待分类的样本数量不均衡，
会给分类准确性度量造成极大的影响。
本文将使用可视化方法对这种影响进行量化。

## 椭圆周长

椭圆与圆有本质的区别，
它的周长没有初等表达式的闭式解，
这是一个很神奇的现象。

## 江山不改

我就知道普大帝不会让人失望，
在我
[之前的文章](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485087&idx=1&sn=1d3e649125bf9d24a7d979a74a0dbd14&chksm=c1634d9af614c48c68e4406b27088e8bb49c1abebce8bdd0524d0e88c0b7ccb14c9912c9d18f&token=856934625&lang=en_US#rd "之前的文章")
就觉得他一定要在乌克兰搞事情。

![Putin 1](./putin-1.png)

因为江山不改，本性不移。
他不搞事情，整个俄罗斯的文化脉络也会推着他搞。

但从个人角度讲，
请德先生先靠边，
我要是俄罗斯人，
这个总统我也想让他当到天荒地老。

## 没头没尾的事

一个方程组摆在面前，
你猜我想让你干点啥？

## 群

群是个神奇的概念。

## 群的例子（之一）

本文将给出一个简单的例子，
试图说明如何从变换的角度理解群。

## 质能方程

所谓伟大分为两种，
一曰为天下之大不韪；
一曰开启天下之先。

上个世纪由爱因斯坦博士提出的相对论就是后者的典型代表。
它否定时空不变性，时间和空间是什么？

-   是描述速度的参考系；
-   是度量物理量的载体；
-   换句话说，只是观念里的一把尺子。

一则，它提出时空的尺度受速度影响；
二则，它暗示质量和能量也并非物体的禀赋，而只是用来度量空间弯曲程度的变量。

本文是对“质能方程”的一些思考，
描述它与速度之间的关系。

奇怪的是，
在速度之外，
质能方程还有一个副产品，
就是**预言**了物体的质量和能量能够相互转化。

## 车枪球-四冲程

天下大事，无非车枪球三样而已，今天先说车。

众所周知，汽缸越多车越稳，
而好车通常采用直列八缸发动机，
本文将解释这是因为什么，以及如何使用群进行分析。

## 群的边界

从《群》的第一篇不难看出，
群是一个包罗万象的概念。
但越是面对这样的东西，
就越需要谨慎。

本文将通过一个例子说明哪些元素不在群里，
从而厘定群的边界。

## 知识、经验和随机性

本文试图说明为什么以及如何使用线性模型对随机变量进行解构。

# Observable HQ

JAVASCRIPT gives HTML amazing Abilities to present Things.

The **Subject** tries to explain the benefits of the environment.

The folder contains following md files:

---
## Perlin 噪声与随机地形

在许多情况下，需要生成随机的地形或者空间连续的随机变量。

这里 Perlin 噪声往往是很好的选择。

比如我在前端页面做的一个小demo [Perlin Noise Contours with GeoProjection](https://observablehq.com/@listenzcc/perlin-noise-contours-with-geoprojection "Perlin Noise Contours with GeoProjection")

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

## 今天的风儿有些喧嚣

今天刮大风，刮的建筑像要被吹跑似的。
所以趁着机会做一个简单的粒子运动模拟。

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

## 历代君王

刷B站看到一条弹幕，
它说雍正和华盛顿是一个时代的人。
于是我就统计了一下，
还真是。

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

## 地图工具 V0.1

地图是一个让人能够更加理解地缘的好东西。

于是我决定一点一点地做一套自己的地图工具。

## 均贫富

本文是使用 Atomic Agents 分析另一个有意思的问题。

> 在平等交易的前提下，贫穷和富裕是如何诞生的？

本文的分析结果偏向于认为贫穷和富裕是在自由交易的市场中自发形成的，动态平衡的经济学现象。

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

## 机械臂运动控制的位置和角度关系及其可视化

本文是记录一个交互式可视化工程，
它对二维二轴机械臂的平面运动过程中，
控制角度与机械臂端点位置的相互关系进行可视化，
并且允许用户通过鼠标模拟二者之间的对应关系。

## 三轴机械臂运动的逆解

在`THREE.js`的支持下，我们可以做出一些有意思的应用。
比如模拟一个三轴机械臂的运动。
于是有了这个缝合怪。

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

## 滤波及失真

针对信号进行滤波是信号处理的基本操作之一，它可以用来提取信号中我们感兴趣的特定成分。

但操作必然会导致信息量的损失，失真就是这种损失的直观表现。

这个话题很大，我就遇到哪写到哪。

## 物以类聚

都说物以类聚，人以群分。但又都说要兼容并包，兼收并蓄。

后一个说教其实大家都不怎么喜欢听，因为它天然的假定物以类聚这个现象，是因为个体微观的不够包容而造成宏观现象。

也就是说错在个人，社会是个人意愿的加和。

而群体行为的研究却有证据认为，群体行为往往不是个体行为的简单累积，而是具有混沌属性，往往与参与者的主观意愿相悖。

落实在本问题上，即使每个人都很大程度的包容自己的邻居，在群体层面也会呈现出极其严重的分类和隔离。

## 瞎画的艺术

数据科学往往能在不经意间诞生艺术创作。

但这个过程可能有点过于不走心了，所以称为瞎画的艺术。

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

## 长津湖

这篇很俗，但值得一写。

# oh-my-image

The oh-my-image project.

The folder contains following md files:

---
## image

## tensorflow-1to2

# OpenGL

OpenGL Details on developing.

---
## B 样条

一般来说，立体渲染需要首先获取物体的三维模型。

而在有限信息的情况下，完全的三维模型往往难以取得，这就需要进行估计。

本系列将一步一步来，先从 B 样条开始。

B 样条是一种经典的物体表面估计方法。

## 三个火枪手

立体渲染是一个充斥着工程师卓越智慧的领域。它的科学问题不多，但工程上的困难几乎无处不在。因此，这也是一个大坑。

## 张量的缩并

张量，Tensor，是个数学概念。在计算机应用中，它可以用来极大地对计算进行提速。

本实验的结论表明，在样本规划大于 1 万的时候，张量计算快；在样本规模小于 1 万的时候，张量计算又装 X 又快。

## 搬砖小能手

常见的三维数据有两种，
一种是高度结构化的点集和面元数据，易于使用`3D`渲染工具，如`OpenGL`绘制；
另一种是单纯的体素数据，就让人很头疼。
本文提出的解决方法是像砖墙一样，将体素垒起来。

## 浅析 Ref-NeRF

NeRF 是目前比较流行的三维渲染网络，本文以新的 RefNeRF 为契机，
尝试说明三维表面中的法线与渲染之间的紧密联系。

## 超级加倍-反直觉的计算机视觉

计算机视觉算法实现过程中，
会遇到一系列相当“反直觉”的问题。
当然，这里的“直觉”指的是过于“想当然”的直觉，
而不是基于纯几何分析的理性推断。

事实上，这些问题的解决方式，通常是以几何分析为突破口的。
本文将描述如何正确处理计算机视觉三维呈现过程中，
如何生成一个正确的“表面”的问题。

# Power Shell

Powershell is a **Object Oriented Programming** programming environment.

The **Subject** tries to explain the benefits of the environment.

The folder contains following md files:

---
## PowerShell 与 LinuxShell 之不同

[PowerShell](https://www.powershellgallery.com/ "PowerShell") 是微软自带的交互软件，与类 Linux 系统的 Shell 具有一定的平行替代关系。
但使用起来，二者却给人以完全不同的感觉。

当然，PowerShell （PS）令人智熄的蓝色界面有一定影响，这却不是主要原因。
其根源在于 Windows 系统（W）与类 Linux 系统（L）的不同构建哲学。
一句话来说，L 是以文件为基础而构建的系统，W 是以抽象为基础而构建的系统。
在 L 系统中，用户所看见和所操作的都是具体的文件，所谓“一切皆文件”；
而在 W 系统中，用户始终处于抽象构建的类结构中，所见的都是一望无际的抽象概念。
孰优孰劣我们不去评价，具体和抽象的区别却是在实际使用中产生直观的感受。

## 用 PowerShell 寻找你找不到的文件

继续说 PowerShell （PS）的事情，通过本文档，希望你能够获得一个在 Windows （W）系统中高效找到你想要的文件的方法。能够开始使用 W 系统中提供的 PS 终端，并且习惯用键盘打字的方式而不是鼠标乱点的方式操作你的电脑。
当然，本文档的目的还是深入理解 PS 的抽象类模式，并提供一个非常工程化的视角来阐述这一特性。

# Random Analysis

Learn the way to obtain the world, using the **Random View**.

The **Topic** is the handbook for the random analysis methods.

The folder contains following md files:

---
## 从检验到瞎编

本文将正式介绍统计检验的基本方法，并简要说明它的适用范围，以及它是怎么被玩坏的。

## 屈打成招

本文将用一个简单的例子说明前文《从检验到瞎编》与《通往显著之路》中介绍的校正方法之必要性。


## 我们与真相的距离

俗话说“众口难调”，要摸底某个群体的真实情况往往是十分困难和意义重大的事情。
那么，我们需要调研多少个样本，才能在较高的置信度下，确定该群体的真实情况呢？
本文将通过概率分析方法，尝试分析并解决这一问题。
那么，这个调研样本的数量要求，就是“我们与真相的距离”。

## 概然而非必然的世界（之一）

阿甘正传里有个寓言，说是人生就像一盒巧克力，你永远不知道下一块是什么。
很浪漫地说明了这个世界是概然的而不是必然的，随机和有序是这个世界的基本特征。
因此，随机变量及其统计分析，是解释世界的基本工具之一。

## 概然而非必然的世界（之误差的估计与估计的误差）

本文可以总结成一句绕口令，

> 误差的估计与估计的误差

将从马尔可夫不等式开始，尝试涉及参数估计的重要思想。
并且，通过本文您将看到，估计出的参数，天然地具有误差，而这些误差范围也需要合理的估计。

## 概然而非必然的世界（之二）

本文之标题有“世界”二字，但笔力其实撑不起来。
为了避免过于高开低走，本文将进行一个简单的实验，并且尝试以可视化的方式，展示一个非常简单的动力学模型。
通过该模型，我们似乎可以涉足一个可爱的问题，即我们是否可能通过提高生产力的路径，达到均贫富的目标？

## 概然而非必然的世界（之五）

本文将续前文《[概然而非必然的世界（之四）](http://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247483914&idx=1&sn=72609edc3197161a25d727a0f56f65f1&chksm=c163490ff614c019abf7f49717edcb3cdf60a1e7b27d3ff2e32b43ab6a483b0972327fb2306d&token=135658256&lang=zh_CN#rd "概然而非必然的世界（之四）")》。
继续介绍“卡方分布”与“T分布”。

## 概然而非必然的世界（之六）

本文将解决上篇文章所遗留的待证明问题。

## 概然而非必然的世界（之善战者无赫赫之功）

“欧洲杯”开始了，本文暂时应个景，尝试用概率分析方法解决一个长久以来的思考，即

> 冠军比亚军强多少？

通过分析我们可以看到，在“联赛”体系下，其实二者差不多；但在“杯赛”体系下，亚军则有大概有$25\%$的概率“德不配位”。
现在的很多商业理论，如“弯道超车”、“差异化经营”等，都是在这样的概率体系下，才得以成立。
许多竞技或商业的“奇迹”，不过是这种概率行为的具体表现而已。

## 概然而非必然的世界（之四）

本文将以“二项分布”为起点，分别引申出“泊松分布”、“正态分布”、“卡方分布”与“T分布”。
虽然名目众多，但通过本文的分析可以看到，这些分布完全是一脉相承的关系，并不难理解。
这些分布在实际应用中，可以解决$90\%$以上的统计分析问题。

## 概然而非必然的世界（之杠精总动员）

本文将从概率角度试图解释一个令人十分糟心的现象。

> 为什么互联网会放大个人的极端观点，而持有极端观点的人往往并不自知。

有人说，这是因为互联网提供了一个远程沟通的渠道，使参与者不必在乎对方的反馈。
但我认为事实远不止如此简单。

通过本文的分析，您将看到。
互联网提供了一个“百家争鸣”的密集型话语环境。
正是这样的环境，使得每个参与者，无论其观点有多极端，都能够找到属于自己的一个“小圈子”，使自己处于圈子的中心。
个人处于这样安逸的位置上，当然不会承认，自己的观点之“极端”。

## 概然而非必然的世界（之三）

本文是针对“概然而非必然的世界（之二）”的数学原理解释和说明。

> 我将从“二项分布”和“正态分布”的角度，来对以上实验结果进行解释，……并顺理成章地，引出参数估计与统计检验的基本概念。

相信通过本文的论述，我们可能对随机变量的“均值”、“方差”及“均值的方差”这些拗口的概念，具有直观的理解。

## 通往显著之路

上文《从检验到瞎编》介绍了统计检验的基本方法。
并引出了多重比较校正的概念和经典的FWE校正方法，本文将介绍另一种多重比较校正方法。

# Sun at Four

Have you saw the Beautiful Sun at 4:00?

The folder contains following md files:

---
## 你见过早上四点钟的太阳吗？

我没见过，因为教育部不太允许我四点起床。
我们这疙瘩在四点钟也不是很经常能看见太阳。

不过我现在每天只需要写`1`个小时的作业了，补课也不用去了。

## 卷起来

中国人太过聪明。
似乎一切既定的规则，只要有中国人的参与，就都将成为内卷的源动力。
人更像是手段，而不是目的。
甚至，连出生年份都能卷。

## 搭建 GIT 服务器

如果你拥有一台服务器的使用权限，就可以将它作为你的 GIT 服务器，像使用 GITHUB 一样来使用它。

要达到这个目的并不难，但中文互联网技术（IT）的经验分享，可能会让这个过程变得有些艰难。

## 诗人和远方

网传麦克阿瑟在西点的演讲被收入了语文教材的爱国篇。这让我有点想吐，难道中国文人这两千多年来什么都没干，竟然沦落到要一个美国人教中国孩子怎么爱国吗？你这与XX做XX的XX。

当然，单纯的抱怨没有任何用处，就写写相关的东西吧。

中国文人重游历，足迹遍及海内。充耳不闻天下事，一心只读圣贤书？你寒碜谁呐？

# Talk with Picture

The Topic will try to create **Pictures** for **Key Ideas**.

The folder contains following md files:

---
## COCO图像类别空间的简单可视化

本文将分别使用`PCA`、`TSNE`和`SOM`三种方法对`COCO`数据图像的类别信息进行映射。
从而以较低的维度对数据进行呈现。

## Coco数据集

Coco数据集是通用较强的数据集，
它的全称为“Common Objects in Context”，
里面包含了各种日常物品，可以细分为`80`类。
对这些图像中的物品进行统计，
也许可以帮助我们了解一般的图像的统计特性。


## Linux User Cookbook

<aside>
💡 To whom wants to, but never got a chance to try Linux Server.

</aside>

## Quick Start

- [ ]  🌐Download & Install MobaXterm
- [ ]  🙂Ask admin to make you account (Login IP, Username, Password)
- [ ]  🤖Establish the remote session of MobaXterm to log in the server with SSH
- [ ]  ⌨️(Optional) Establish the remote development environment with VSCode or Pycharm or something like
- [ ]  🆗(Optional) Set up your Key Authorization of SSH login without password

## Movie in Machine Learning

如果你实在是没有时间看电影，不妨让算法把相似的信息提取出来。

当然，目前的算法很粗糙，提取的信息也很朴实。

## 一种线性反馈的多输出零点控制方式

本文将试图说明一种面向线性反馈系统的，
基于共模差模控制的，
双输入、双输出反馈控制方式。
这只是第一个版本，
只给出定性分析，并不列出系统方程。

## 丙子双十二

1936年12月12日，西安事变。
我们被揍得鼻青脸肿，
国家元首还被自己人给绑了。

如今75年过去了，
我们却在购物。

## 从词向量的角度理解COCO

上一篇从类别标签的角度介绍了`COCO`数据集的基本情况，
本文将从“词向量”的角度理解这组数据。


## 全面开往小康社会

过年嘛，既然日子也就那么回事，
所以就畅想些美好的未来。

今年据说是全面建成小康社会的一年。
它标志着我们也许可以开始畅想着买小汽车的事情了。

## 初五迎财神

一晃已经初五，
假期余额严重不足。

正好今天的习俗是祭灶，
就索性写写发财的事。

> 从概率统计的角度来分析，
> 麻将怎么打才能赢？

本文可以带来三条建议

- 牌局进行到大概`14`轮时，就要警惕赢家的出现了；
- 如果你会赢的话，尽量基于起始的牌，不要大换血；
- 尽量留中间的牌，这样赢的概率更大。

## 商业精神

《潜伏》里的谢若林同学曾说过一句名言，
嘴里都是主义，眼里全是生意。
如今流行的WEB3.0自然也是商业逻辑催生的产物。

## 降维打击-四元数

欧拉四元数简直是神迹，
用四维的形式解决三维的问题。

在四元数规范下，
我们将看到内积和外积对应同一个方程的实部和虚部，
也因此，三维世界的解析几何经典公式在四维世界中成对出现。

这也是目前主要的计算机视觉工具在处理三维空间几何计算问题时，
使用四元数对空间坐标进行表示的原因。

## 图像的颜色风格化

神经网络的非线性映射方法能够方便地进行各种有效的计算机视觉设想。
本文尝试使用SOM与KMEANS相结合的方式，对图像进行有效的颜色风格化。

## 图解FDR

鉴于写字没人看，于是决定改成图。
这个系列争取一张图讲明一个故事。
本图是对`FDR`校验过程及原理进行图解。

后面的简要说明，您可以选择看或不看，因为它是为了凑足300字的最低字数要求，完全不影响疗效。

## 图解HSV空间

以颜色空间的“舌形图”为蓝本，我们可以在RGB空间之外，得到更加符合人眼观感的HSV空间。
本文对其进行图解。

## 图解图论分析

本文是标题党，因为一文和一图无法解释清楚图论的概念。
但是，结合《图解词向量》的相关分析，并且使用相同的语料，我们可以进行简要分析，并帮助我们从图的角度理解文章内容。

## 图解审美（一）

本系列将试图通过可视化方法，解释图画审美的问题。

本文将图画打散并嵌入到颜色空间中，用来剖析一个问题

> 什么样的图，是好看的图？

祝我好运吧。


## 图解审美（二）

本文接上文《图解审美（一）》。
本文试图说明，可以通过在`HSV`颜色空间中的变换，对图像进行风格化变换。

## 图解审美（三）

本文将对《图解审美（二）》中的线性变换问题进行图解说明。
并且还将提供一种基于非线性映射的改进方法，用于提升颜色分布变换的效果。

## 图解词向量

本文将对`NLP`的重要概念“词向量”进行图解。
并且以“重要讲话”为语料，通过简单的可视化分析，对其内容进行“数据驱动”的解析。

## 图解词向量与图论的代码

本文是列出以上两篇文章《图解词向量》与《图解图论分析》的相关代码。

## 图解贝斯公式

本文对贝叶斯公式进行图解。
并且说明，在先验知识存在的情况下，观测样本只能在一定范围内对后验概率进行修正。
而不是直接进行数据驱动地估计。
这即是贝叶斯公式背后的精湛哲学。

## 图解颜色空间

不知道你是否和我一样，对颜色空间的形状有些好奇。
它之所谓是个“舌头”的形状，是与眼睛感光的机制有关。
本文将进行适当图解。

## 地图映射

同志你好，请问基辅怎么走？

克里米亚属于山区，而旁边的基辅是个大平原。
怎么说呢，它们就相当于中原腹地与燕云十六州之间的关系。
因此，我不觉得普大帝在装腔作势，毕竟换谁能忍得住？

所以问题来了，
为什么俄罗斯在地图上显得这么大？

## 声音的谱

本文对英文中易混淆发音的单词进行谱分析，
从谱分析结果中，
可以看出一些不容易听出来的东西。

## 她是活的人，而不是尸体

长太息以掩涕兮，哀民生之多艰。

## 如果时间是条河

尽管空间旅行的速度越来越快，但人类目前的技术还无法跨越时间。如果时间是条河，那么人们只能随波逐流，因此，你的起点就决定了你的终点。

## 按需分配

那个啥的核心奥义是实现按需分配，
所以请拥抱`HTML`吧，
这里啥都有。

当然，有时候你需要一些`JS`提供的帮助。

## 文化自信

自信就是相信自己，进而相信自己的邻居和同胞能够成就伟大的生活和事业。

但是国人近期对谷爱凌的关注，反映出了国人目前普遍崇拜美国归来的游子。

所谓中国是世界上最大的美分，这句话似乎没有原则上的错误。

## 星链

马斯克搞的这个星链就很有意思，它既依靠大量小卫星覆盖全球，又让这些卫星的使用和发射成本足够小，像蜂群一样为地球服务。

## 泡沫

习惯了经济学价值叙事的我发现，价值叙事解释不了时下很多的经济学现象。
其中一个重要的缺失是它解释不了经济泡沫的成因。

本文借用《再售期权理论（Resale Option Theory）》中的一个例子，
试图说明经济泡沫也许可以解释成异质信念条件下的资产交易属性。

## 科里奥利力

本体论追求并提炼万物的本源，
在遇到抽象现象时往往会遇到阻碍。

比如“科里奥利力”，这个找不到施力物的，
甚至受力物体都感受不到的，无形的力。

认识论就简单很多，
只要认识它就可以了。

## 素描

这是一段将图片转换为铅笔素描版本的小程序。

## 纹理与着色

如果你喜欢某一张图的配色，想把颜色方案应用到另一张图上。本文提供的方法和代码可以帮你一把。

## 记一个神奇的BUG

今天遇到一个神奇的BUG，
解决方式虽然非常简单。
但它暴露出来一个问题，
即，我已经被弱类型语言给惯坏了。

## 运动反解算法

本文将综合之前的“四元数”计算、“机械臂”运动和“THREE”可视化的代码，
构建了一个仿“人体骨骼”的运动反解工程。

## 配色方法

如果你经常纠结于怎么为自己的PPT或其他什么东西配色的话。
本文将介绍一种基于`HSV`空间的配色方法，也许能解决你的问题。

## 酸葡萄

这一篇酸臭味道很冲的文章。

## 鱼眼看世界

很好奇鱼眼镜头里的“扭曲”是如何生成的，于是就有了这个模拟计算。

## 鱼眼看世界-V2

很好奇鱼眼镜头里的“扭曲”是如何生成的，于是就有了这个模拟计算。

本文对之前的内容进行了两个方面的扩展，一是考虑了空间角的影响；二是通过变换还原真实的视野内容。

# Tools Knowledge

The Topic is about how to use software tools better.

The folder contains following md files:

---
## GIT-bug

GIT 是常用的版本管理软件，它偶尔也会出问题。

## how covid-19 is becoming

如果 a 比 b 快，
那么 b 就永远都追不上 a。
这是小学生都知道的事情。

那么如果病毒感染的速度比人类生育的速度快呢？

## Tools Knowledge

The Topic is about how to use software tools better.

The folder contains following md files:

## Tensor flow 踩坑记

Tensor flow 删除了 contrib 模块，这是万恶之源。

## 三维大脑展示页面

本文是介绍大脑标准模板的一站式展示工具。

不用装任何软件，打开网页即可。

我很奇怪，都2022年了，竟然还没有人做这个事情。

[Brain Atlas Gallery](https://observablehq.com/@listenzcc/brain-atlas-gallery)

## We are So Strong

As a whole.

## WebSocket 实用记录

手头的项目需要用到 WebSocket。

你敢相信吗，这个破玩意的通信功能已经集合了 HTTP，WebSocket 和 Parallel Ports，诚可谓五毒俱全。

本文将记录使用 WebSocket 的一些实用方案，比如如何建立和测试连接，如何判断失联并实现重联等。

## 今天你过得如何

今天可是个大日子。
因为现在地球上大概有7,975,447,402，这么多人。
其中，今年出生的有55,713,877，这么多人。
很值得庆祝，不是吗？

所以你，
70多亿分之一，
今天过得怎么样？

## notion和飞书

## 一种面向脑电信号包的无损压缩思路

脑电信号一般具有较高的采样率，因此在实时系统中，如何对它进行快速传输是比较棘手的问题。

本文提供了一个高效的、轻量化的压缩思路，能够在信号源头减少传输开销。

## 不仅仅是播放器

大家都熟悉播放器，它可以把视频播放出来。

但抖音模式的播放没有任何价值，因为它只是放了一遍，却没有任何东西留下来。

我想要是功能更多一点的播放器，比如看到好玩的东西可以把它们留下来，然后自动生成一份报告，方便以后查看。

但这个功能市面上好像是没有，于是我就自己做了一个。


所以它并不是一个简单的播放器，
而是一个电影写作器，
它可以你在看电影的同时，
自动生成一份摘要。
这个摘要是图文并茂的，
之后你无须再看电影，
就可以回顾起当时的感觉。
当然也方便分享。

## 中日颜色风格

这两网站是配色苦手的福音。

## 借助深度估计的点云场景重建

所谓身怀利器，X心自起。

当你手上有 GPU 服务器的时候，总会想用它来弄点东西。

这次的东西就是借助深度估计网络的点云生成的尝试。

## 冷

一场秋雨一场凉，一到十月特别冷。
于是我开发了一个 `IPython` 笔记本，
它能够实时获取一个气象数据网站上的历史气温数据，
并以合适的方式把它们绘制出来。

看历史温度图，我们或许就能够解释为啥九、十月份时，体感会这么冷。
其实很简单，

> 在时间进入九、十月的这一段时间，
> 气温在经历了`8`个月的上升之后，
> 首次开始下降。

另一个问题，今年比往年“热”或“冷”吗？

> 数据告诉我们每年的气温基本上都差不多，
> 那些说往年并不如此的言论，
> 就是十足的“活在当下”而已。

## 功能连接分析

功能连接（Functional Connectivity Analysis）分析是认知神经科学重要的分析方法。

> 它是研究各个体素、各个体素之间”共变“关系的重要计算工具。

何为共变关系以及如何对它进行度量，就是功能连接分析的重要课题。

更进一步地，共变关系可以解决什么问题，以及如何利用这些共变特性，就是另外的故事了。

## 功能连接可视化

本文介绍另一个大脑功能可视化工具，还是不用装任何软件，打开网页即可。

要说明的是目前的版本是一个半成品，更完整一点的工具应该是与之前的工具产生联动的一个玩意。

[https://observablehq.com/@listenzcc/functional-connectivity-explorer](https://observablehq.com/@listenzcc/functional-connectivity-explorer)

## 双目视觉

双目视觉是立体感知的重要途径。
然而，从双目视觉的原理来看，
也许，我们所认为自己所“看到”的图像或场景，
其实都是脑补出来的。
当然，本文也可以看作是自动景深算法的一个粗糙实现。

## 和光同尘

人眼观测到的是现象，而背后的逻辑可能比看上去要简单许多。
比如，光沿直线传播。

## 图像分割

这是一个最近做的东西的副产品。
能够实现按照图像的自动分割。

## 图像缩放工具

本例提供了一个批量图像缩放工具，用于指定目录下的图像统一缩放。
源码可见[GITHUB](https://github.com/listenzcc/resizeImages "GITHUB")

## 天气热不热，取决于记性好不好

人往往囿于眼前的苦难，却淡忘过往的悲伤。

就好像每年都在说“今年天气热，胜过往年”。

## 如何安装一个机械臂

这是一篇极其无聊的工作记录。
它涉及如何固定一个机械臂，让它在固定的平台上安全地自由运动。

## 小程序开发记录

微信小程序是基于微信的独特交互方式，

> **小程序简介**
>
> 小程序是一种全新的连接用户与服务的方式，它可以在微信内被便捷地获取和传播，同时具有出色的使用体验。

鉴于微信生态在中国的巨大体量，可以这样说，它是任何工作走向大众、走向互联网的不可或缺的一环。

本文是这样一个记录，是我这样一个互联网门外汉，试图了解其开发方式所做的一些尝试和分享。恰恰是因为我对这个领域什么不都懂，所以可能会闹一些笑话，写出一些不太专业的描述，不是用各种专业名词，而是用自己的语言和逻辑对其中涉及的概念进行一定程度的抽象和归并。

当然，我还是希望最终呈现出来的逻辑是简明和自洽的，并且希望对读者您是有些用的。

## 干点正事

了解一个领域最快捷的方式就是读文献。

本文借助`Scopus`和`VOSViewer`两个工具联合来帮你捋清文献的脉络。

## 快速序列视觉呈现

快速序列视觉呈现是很折磨人的脑-机接口实验范式。
它拖着一串问题，是视频编码算法的天敌。

## 房贷那点事

如果你背上了房贷，那么是否应该提前还呢？这是个问题，但没有答案。

不过分析这个事情是挺有意思的，因为我得出了一个挺有意思的事实，那就是你越有钱，你使用钱的自由越大（比如不着急用它归还银行贷款），在一段长时间之后，你的财富就越多。相反，如果你被贷款追着跑，那么就要背负庞大的债务。所谓富的越来越富，穷的越来越穷是也。

## 机场的密度分布

能一飞冲天的东西，我们叫做飞机。
本位文对世界范围内的机场分布的密度图进行估计和可视化。
结果表明，我国配不上所谓的“基建狂魔”的称号，
甚至可以说，扩大内需没有尽头，大国工匠大有可为。

## 永远干不完的工作

之前做了一个​面向视频的整理工具，
[不仅仅是播放器](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485688&idx=1&sn=d7b4ff708ab4587910bf7e0089066798&chksm=c16343fdf614caebda9e81c5777f31c609509ab6b517f235724e9e66afd40d9ac0c6e600bfbf&token=1683679924&lang=zh_CN#rd "不仅仅是播放器")。

但转念想想，
这个思路用来整理琐碎的调研工作似乎更合适。

## 狭义相对论的简单图解

偶然看到一个狭义相对论的简单图解，很有意思

## 神经网络的表达能力

人工神经网络是近年来火热的模式识别算法，
在计算机视觉领域应用广泛。

本文是一个例子，
表明如何使用一个结构异常简单的神经网络，
在随机参数的情况下，
对一只兔子进行剖析。

可以看到，
如此简单的神经网络，
即使未经训练，也具有表达兔子各个部位的能力。

至于如何对它进行训练和优化，则是另一个问题。

## 科学还贷

本文是对提前还贷是否合算的科学计算。

我首先假设了绝对公平的比较方法，比较了提前还贷与否，在 25 年后造成的盈亏。如果你选择按月还款，你需要向银行支付 88 或 76 万元；如果你选择提前还款，你需要向银行支付 33 或 29 万元。

之后，对有些不尽人情的假设进行修正，因为没有人会为了不存在的月供利息压力，而把钱按月放在银行里存着。这样算下来，如果按当期来说，提前还款只能省下 5 到 6 万元，因为明天的钱没有今天值钱。

## 立体渲染

要渲染一个立体结构，除了将它解析成表面之外，还可以通过体渲染的方式来解决问题。

## 简洁带来的麻烦

`Python`是十分简洁的计算机语言，但是简洁会不避免地带来歧义。
这些歧义则会导致一些麻烦。

## 粗看ERD和ERS

ERD和ERS是信号随机叠加的两种不同的现象，
它们的差异更多地是体现在叠加的波形上，
而在它们的幅度上，不容易看到较大的差异。

## 纹理增强

由于上述图像过于“模糊糊”，因此尝试使用“空间滤波”的方式进行纹理增强。

人生如树花同发，随风而堕。自有拂帘幌坠于茵席之上，自有关篱墙落于粪溷之中。坠茵席者，殿下是也。落粪溷者，下官是也。贵贱虽复殊途，因果竟在何处？

## 线性模型的实例之一

线性模型是解析观测变量的有效手段。
但它实在是太庞大了，所以只能蚂蚁式的、慢慢地啃下来。

## 股价预测

本文是使用**机器学习**方法对股票价格进行预测的实用方法。

但如果想用它来赚钱，
猜猜你会赔多少？

## 脑成像数据的标准空间

脑成像设备和数据都需要进行一定程度的标准化才能进行后续分析。
本文是对其基本概念的一些介绍。

## 英文苦手

作为英文苦手，
语法几乎是遥不可及的玩意，
从来就没有弄明白过。
但也许可视化的方法可以帮助解决这个问题。

## 蒙特卡洛方法

蒙特卡洛（Monte Carlo）方法是一种无奈，
却高效的遍历方法。
本文是该方法的一个样例。

## 视角渲染

不同的视角下看到同一个东西通常会得到不同的图像。我就搭建了这样一个场景，即模拟高空俯瞰一小片陆地的场景。

这算是一个框架上的尝试，它是在渲染过程中，尝试对同一个三维场景进行多次渲染。

## 计时精度

都说`LINUX`比`WINDOWS`操作系统更适合做工程开发，
这也许是谣言，
但绝非空穴来风，
本文就是一例。

设想一个典型场景，
你需要让计算机每隔一段时间做一件事情，
比如显示一张图片什么的，
那么就要用到计时器。

当这段时间短到毫秒级的时候，
问题就来了。

## 语法分析（Online）

本文是前文《[英文苦手](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485066&idx=1&sn=486594ad89329b0a2f7e4de408a3c7f2&chksm=c1634d8ff614c499a753ee3c6423c6cc541a3eb8709a242bda55ac1d44602fed0b31a54675fc&token=537192075&lang=zh_CN#rd "英文苦手")》的前端实现方案。
主要解决两个问题，分别是
- 前端词性快速解析；
- 基于词性标签的文档可视化。

## 运动轨迹分析

这是一个纯工程的方法，
尝试解决多轴连动的运动参数与终点轨迹之间的关系。

## 魑魅魍魉

互联网世界中的奇奇怪怪的符号通常是用 Unicode 符号表达的，因此，我做了一个 Unicode 符号的速查表，来看看奇怪字符的奇怪表达。

欢迎访问我的
[Github 主页](https://listenzcc.github.io/home-page-2/unicodes/ "Github 主页")

## 鸡同鸭讲的 BUG

Python-opencv 遇到了一个中文支持的 BUG，它不能读取目录中带有中文的图像文件。

这背后的原因是编码和解码过程不一致所导致的乱码现象。

# Traffic Analysis

The Topic is about Analysis the Traffic Situations.

The folder contains following md files:

---
## 以空间换时间

为了解决《私人订制》一文中遇到的，由于计算规模扩大所导致的，
寻路计算负担问题。
我们将从寻路算法的原理出发，对动态规划算法进行改进。

## 学而不思则罔

这是解决寻路问题代码的最后一篇，尝试让算法再快一点。
天知道我在贪婪算法上已经水了多少天。
水日常到此为止。

## 图的谱聚类

本文将继续介绍图的谱聚类方法，不纠结方法，只尝试说明它的用途。

## 图的距离度量

本文将在上文《最小连通图》的基础上，介绍图距离度量理念及方法。

## 所谓路径依赖

继续图论。
本文将借用之前“过于简单粗暴”的图示来说明所谓“路径依赖”的问题。
往大了说，它代表一种全局和局部的矛盾关系。

## 改出路径依赖

上文我们介绍了“路径依赖”现象，本文将继续介绍通过添加捷径的方法，改出路径依赖的肤浅思路。
并给出一个例子，尝试利用数值化分析方法对该思路其进行说明。

另外，添加捷径的方法综合利用了前文中谱娶类和最小连通图的方法，
并且引入了图论中“超节点”和“超边”的概念。

由于本文说理性较强，相关代码也有不少需要说明的内容。
因此，相关代码和具体算法的体量将在下一篇文章继续完成。

## 最小连通图

本文将介绍最小连通图原则，及其在图构建过程的应用。

## 私人订制

为解决上文《贪婪算法及其困境》中遇到的困难。
我们在本文中对算法进行改进，从而使其能够用来解决一般性的“寻路”问题。

## 行路难

过分追求全局最优会降低局部效率。
那么这种情况有多严重呢？本文是基于图分析对该问题进行量化。
通过分析，我们可以看到以下现象，

1. 全局最优解往往会陷于路径依赖困境；
2. 可以通过极少的“捷径”开销，提升总体效率；
3. 但全局最优往往已然促成“天然垄断”；
4. 总体效率的提升会造成“垄断”权益的稀释，从而受到阻碍。

虽然修建捷径是利国利民的好事，但会损害天然垄断的利益。
不难想见，垄断权益受到损害的体量，就是修建捷径的成本。
其值甚至与社会总收益相当，甚至可能产生“投鼠忌器”级别的阻力。
所谓“行路难”是也。

## 贪婪算法及其困境

本文将详述形成最小连通图的贪婪算法。
在此基础上，我们才能说明捷径加入之后，原始算法是如何失效的。
从而解决《改出路径依赖》一文所提出的问题。

