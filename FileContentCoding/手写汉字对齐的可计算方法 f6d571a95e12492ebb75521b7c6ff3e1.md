# 手写汉字对齐的可计算方法

本人从小就困扰于一个问题，那就是写字不好看。家长对我的评价是写字大小不一，不够整齐。但我一直不服，主要是不解“什么叫整齐” 。本文尝试对这个问题进行计算，顺便解决 OpenCV 如何使用本地 TTF 字体的技术问题。

开源代码如下

[https://github.com/listenzcc/opencv-play-with-ttf](https://github.com/listenzcc/opencv-play-with-ttf)

---
- [手写汉字对齐的可计算方法](#手写汉字对齐的可计算方法)
  - [计算方式](#计算方式)
  - [重排结果](#重排结果)


## 计算方式

今天偶然看到一个视频说，所谓整齐不是每个字都一样大，而是保持每个字的“留白”看上去是一样的比例，笔画复杂的字就要写得大，笔画简单的字就要写得小。这样一来，每个字看上去就是一样大的。我是理工科出身，因此开始用计算的方法验证这个说法。

我的做法是使用 OpenCV 工具，加载 TTF 字体，之后通过获取每个字的 bbox 并进行 canny 滤波来获取每个字的笔画边缘。边缘像素占总像素的比例（ratio）就代表字的复杂程度，根据这个值对全篇文章的字进行缩放即可，缩放尺度为 scale 列，如下图所示。

![Untitled](%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E5%AF%B9%E9%BD%90%E7%9A%84%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%96%B9%E6%B3%95%20f6d571a95e12492ebb75521b7c6ff3e1/Untitled.png)

![Untitled](%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E5%AF%B9%E9%BD%90%E7%9A%84%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%96%B9%E6%B3%95%20f6d571a95e12492ebb75521b7c6ff3e1/Untitled%201.png)

## 重排结果

下面是用上述方法进行文字重振的对比结果，左侧列代表重新排版的效果，右侧列代表原始大小的效果。虽然左侧看上去更乱，但却更像是手写的。下文的两例分别为晁错的《**[论贵粟疏](https://so.gushiwen.cn/shiwenv_a09860c14994.aspx)**》和贾谊的《**[治安策](https://so.gushiwen.cn/shiwenv_ec737382cf4a.aspx)**》首段。字体为随手下载的 [云峰静龙行书字体免费下载和在线预览-字体天下 (fonts.net.cn)](https://www.fonts.net.cn/font-40592408336.html)。

![Untitled](%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E5%AF%B9%E9%BD%90%E7%9A%84%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%96%B9%E6%B3%95%20f6d571a95e12492ebb75521b7c6ff3e1/Untitled%202.png)

![Untitled](%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E5%AF%B9%E9%BD%90%E7%9A%84%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%96%B9%E6%B3%95%20f6d571a95e12492ebb75521b7c6ff3e1/Untitled%203.png)

![Untitled](%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E5%AF%B9%E9%BD%90%E7%9A%84%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%96%B9%E6%B3%95%20f6d571a95e12492ebb75521b7c6ff3e1/Untitled%204.png)

![Untitled](%E6%89%8B%E5%86%99%E6%B1%89%E5%AD%97%E5%AF%B9%E9%BD%90%E7%9A%84%E5%8F%AF%E8%AE%A1%E7%AE%97%E6%96%B9%E6%B3%95%20f6d571a95e12492ebb75521b7c6ff3e1/Untitled%205.png)