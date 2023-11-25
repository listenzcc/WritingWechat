# Fastapi + tailwindcss = 各司其职

最近要写个功能稍微复杂的 APP，所以需要搭微型网络服务。出于好奇，我选择了时下流行的 fastapi 作为后台；选择了 tailwindcss 让我的 APP 免得过于难看。本系统将逐步记录开发过程。

本文的主旨在于澄清一个误会。由于以上两个框架都较为流行，因此不免存在大量的网络文档试图将它们结合在一块来讲。但我觉得似乎并无必要：因为它们干的是不同的事情，让它们各司其职就好，二者不应该有太多的交互。

本系列对应的开源代码位于我的 Github 仓库

[https://github.com/listenzcc/eeg-for-everyone](https://github.com/listenzcc/eeg-for-everyone)

---
- [Fastapi + tailwindcss = 各司其职](#fastapi--tailwindcss--各司其职)
  - [Fastapi](#fastapi)
  - [Tailwindcss](#tailwindcss)
  - [各司其职](#各司其职)


## Fastapi

这是一个 python 的敏捷开发的 web 框架，我目前感觉它与 flask 有相似性，但又显得更简洁一些。选择它的起因是 flask 用腻了，尝试一下新东西。另外，我最看重的是它的**异步支持：** FastAPI 支持异步编程，可以利用 Python 3.7+ 的 **`async`** 和 **`await`** 关键字来编写异步代码，从而提高性能。当然，承载其网络服务的是 python 的另一个 ASGI（Asynchronous Server Gateway Interface） 模块，称为 unicorn，我需要再弄懂一些才能写写它。

> FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.
> 
> 
> The key features are:
> 
> - **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](https://fastapi.tiangolo.com/#performance).
> - **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
> - **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
> - **Intuitive**: Great editor support.  everywhere. Less time debugging.
>     
>     Completion
>     
> - **Easy**: Designed to be easy to use and learn. Less time reading docs.
> - **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
> - **Robust**: Get production-ready code. With automatic interactive documentation.
> - **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

[FastAPI](https://fastapi.tiangolo.com/)

[Uvicorn](https://www.uvicorn.org/)

## Tailwindcss

这是一个便于使用的样式库，它的使用逻辑与传统 CSS 略微不同。不同点主要体现在它需要根据页面内容现场“编译”，这样做的好处是能够按需加载已有的样式，而忽略用不到的样式。另外，这种机制也能根据页面对样式进行局部优化。

与手写或使用预处理器（如Sass或Less）不同，Tailwind 提供了一组预定义的类名，每个类名都对应于一个具体的样式。通过在 HTML 中使用这些类名，你可以轻松地构建样式，而不需要编写自定义的 CSS。我希望利用这次机会，熟悉这一框架。

另外，它的编译过程提升了使用门槛，具体来说，它需要通过 node 应用进行编译，编译方法原理不难，但说起来实在麻烦，所以我就先贴一张图在这里，日后有机会再补充。

![Untitled](Fastapi%20+%20tailwindcss%20=%20%E5%90%84%E5%8F%B8%E5%85%B6%E8%81%8C%20af299241bce2422c8996e8d9556b3d9a/Untitled.png)

> “Tailwind CSS is the only framework that I've seen scale on large teams. It’s easy to customize, adapts to any design, and the build size is tiny.”
> 
> 
> Sarah Dayan
> 
> Staff Engineer, Algolia
> 

[Tailwind CSS - Rapidly build modern websites without ever leaving your HTML.](https://tailwindcss.com/)

## 各司其职

由于以上两个框架都较为流行，因此不免存在大量的网络文档试图将它们结合在一块来讲。但我觉得似乎并无必要，因为它们干的是不同的事情，让它们各司其职就好，二者不应该有太多的交互。其中 fastapi 负责维护 static （静态文件目录）和 template （模板文件目录）；而 tailwindcss 负责在外围更新 style.css。

![Untitled](Fastapi%20+%20tailwindcss%20=%20%E5%90%84%E5%8F%B8%E5%85%B6%E8%81%8C%20af299241bce2422c8996e8d9556b3d9a/Untitled%201.png)

![Untitled](Fastapi%20+%20tailwindcss%20=%20%E5%90%84%E5%8F%B8%E5%85%B6%E8%81%8C%20af299241bce2422c8996e8d9556b3d9a/Untitled%202.png)