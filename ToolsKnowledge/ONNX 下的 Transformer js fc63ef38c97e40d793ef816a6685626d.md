# ONNX 下的 Transformer.js

你的浏览器远比你想象的强大。比方说，它可以在 ONNX runtime 下直接跑通 transformer.js 进行 NLP。

本文代码可见我的前端笔记本

[Transformer.js in browser](https://observablehq.com/@listenzcc/transformer-js-in-browser)

---
- [ONNX 下的 Transformer.js](#onnx-下的-transformerjs)
  - [方法原理](#方法原理)
  - [Transformer.js](#transformerjs)
  - [ONNX Runtime](#onnx-runtime)
  - [附录：什么是 runtime](#附录什么是-runtime)


## 方法原理

Transformer.js使用ONNX Runtime来在浏览器中运行模型。ONNX Runtime是一个深度学习推理引擎，用于在不同硬件和软件平台上运行深度学习模型。Transformer.js借助ONNX Runtime的功能，能够在浏览器环境中加载、运行和推断Transformer模型，从而将最先进的机器学习技术引入到Web中，而无需依赖服务器端的计算资源。

## Transformer.js

[Transformers.js](https://huggingface.co/docs/transformers.js/index)

Transformer是一种用于自然语言处理（NLP）任务的深度学习模型，最初由Vaswani等人在2017年提出。它在机器翻译任务中取得了重大的突破，并在NLP领域广泛应用于各种任务，如文本生成、情感分析、问答系统等。

"transformer.js"是指一个JavaScript库或框架，它是为了在Web应用程序中实现Transformer模型而设计的。这样的库或框架可以提供在浏览器环境中加载、运行和推断Transformer模型的功能，从而使开发人员能够在前端应用程序中进行自然语言处理任务。

Transformers.js将最先进的机器学习技术引入到Web中，消除了对服务器的需求。受Hugging Face的transformers Python库的启发，Transformers.js由Xenova开发。它利用ONNX Runtime在浏览器中运行模型。

## ONNX Runtime

[ONNX Runtime | Home](https://onnxruntime.ai/)

ONNX Runtime是一个开源的深度学习推理引擎，用于在不同硬件和软件平台上运行深度学习模型。ONNX是"Open Neural Network Exchange"的缩写，是一个开放的深度学习模型表示格式。ONNX Runtime旨在提供高性能、可扩展性和跨平台的推理体验。

ONNX Runtime支持多种硬件和软件平台，包括CPU、GPU和专用加速器。它可以与各种深度学习框架集成，如PyTorch、TensorFlow和CNTK，以及其他支持ONNX格式的框架。通过将模型转换为ONNX格式，可以在不同框架之间无缝地共享和部署模型。

ONNX Runtime提供了一个统一的API，用于加载、优化和执行深度学习模型。它通过使用各种优化技术，如图优化、内核融合和量化，来提高推理性能。此外，ONNX Runtime还支持动态形状推理，使其能够处理具有可变输入大小的模型。

ONNX Runtime的目标是为开发人员提供一个高性能、灵活且易于使用的推理引擎，以便在各种应用场景中部署深度学习模型，包括计算机视觉、自然语言处理和推荐系统等。它的开源性质使得开发人员可以自由地使用、定制和贡献代码，从而不断改进和扩展ONNX Runtime的功能。

```jsx
/**
 * Demo of oonx runtime
 **/

import ai.onnxruntime.*;

// Load the model and create InferenceSession
String modelPath = "path/to/your/onnx/model";
OrtEnvironment env = OrtEnvironment.getEnvironment();
OrtSession session = env.createSession(modelPath);

// Load and preprocess the input image inputTensor
...

// Run inference
OrtSession.Result outputs = session.run(inputTensor);
System.out.println(outputs.get(0).getTensor().getFloatBuffer().get(0));
```

## 附录：什么是 runtime

Runtime是指程序在运行时的环境和执行状态。它是指程序在计算机上实际运行时所需要的支持和资源，包括操作系统、库文件、内存管理、线程管理、硬件驱动程序等。

在软件开发中，通常将程序分为编译时和运行时两个阶段。编译时是将源代码转换为可执行文件或库的过程，而运行时是指程序在计算机上被加载和执行的阶段。

Runtime环境提供了程序运行所需的各种功能和服务。它负责分配和管理内存，处理输入和输出，调度线程或进程，处理异常，以及与操作系统和硬件进行交互。运行时环境还可以提供各种库和工具，用于支持特定的编程语言、开发框架或应用程序。

不同的编程语言和框架通常有自己的运行时环境。例如，Java有Java Runtime Environment (JRE)，Python有Python运行时环境，而在深度学习中，ONNX Runtime就是一个针对深度学习模型推理的运行时环境。

总之，运行时是程序在计算机上实际执行的环境，它提供了程序运行所需的支持和资源，使得程序能够在特定的操作系统和硬件平台上正常运行。