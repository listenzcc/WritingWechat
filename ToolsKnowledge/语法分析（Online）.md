## 语法分析（Online）

本文是前文《[英文苦手](https://mp.weixin.qq.com/s?__biz=MzkxNTI1MDc5NA==&mid=2247485066&idx=1&sn=486594ad89329b0a2f7e4de408a3c7f2&chksm=c1634d8ff614c499a753ee3c6423c6cc541a3eb8709a242bda55ac1d44602fed0b31a54675fc&token=537192075&lang=zh_CN#rd "英文苦手")》的前端实现方案。
主要解决两个问题，分别是
- 前端词性快速解析；
- 基于词性标签的文档可视化。

---

- [语法分析（Online）](#语法分析online)
- [效果呈现](#效果呈现)
- [词性分析](#词性分析)
- [文档可视化](#文档可视化)
- [未完成的工作](#未完成的工作)

## 效果呈现

可以登陆我的[Observable Notebook](https://observablehq.com/@listenzcc/pos-visualization-in-english-article "Observable Notebook")，
来尝试使用效果，
录了一个简单的视频如下

【这是一段棒到不行的视频】

下面分别介绍两个功能的实现方法。

## 词性分析

本文使用[POS](https://www.npmjs.com/package/pos "POS")在前端网页中实现词性分析。
这是个什么东西呢？

> pos-js is a Javascript port of Mark Watson's FastTag Part of Speech Tagger which was itself based on Eric Brill's trained rule set and English lexicon.
>
> pos-js also includes a basic lexer that can be used to extract words and other tokens from text strings.
>
> pos-js was written by Percy Wegmann and is available on Google code. This fork adds node.js and npm support.

它提供了一套高效计算包，
提供了文本提取与词性解析功能。
它的分析结果如下图所示

![POS Tag](./POS-tags.png)

其中，`word`是原词，
`tag`是解析出的词性，
`wordRoot`是我自己解析出的词根，
用于全文范围内的单词匹配。

为什么要进行全文范围内的单词匹配呢？
因为要进行简单的筛选，
便于进行文档可视化。

## 文档可视化

文档可视化主要具有三个方面的功能

- 实现了与用户输入相同步的解析与呈现；
  - The visualization is updated in **real time** as you type in the `CONTENT` textarea;- The visualization is updated in real time as you type in the `CONTENT` textarea;

- 根据词性对单词进行染色；
  - The words are **colored by the tag**.

- 用户可以选择特定单词，从而高亮呈现含有这些词的段落，方便用户了解文档结构。
  - And you can **select the word** to vague out the paragraphs that don't contain the selected word.

如图所示

![POS Highlight](./POS-highlight.png)

## 未完成的工作

右侧其实是一块预留的控制区域，
未来有时间的话会实现词性选择与颜色选择。

另外，还需要进行文本统计与词向量分析等功能。