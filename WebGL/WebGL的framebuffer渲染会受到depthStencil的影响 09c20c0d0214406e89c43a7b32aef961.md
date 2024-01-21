# WebGL的framebuffer渲染会受到depthStencil的影响

简单来说，当使用framebuffer交互渲染时，应该关闭dephStencil选项。否则，会导致framebuffer无法按要求更新。这个经验是在绘制多个点的SDF时得到的。

---
[toc]

## 原因解释

在WebGL中，深度缓冲（depth buffer）和模板缓冲（stencil buffer）是与帧缓冲（framebuffer）紧密相关的概念。深度缓冲用于存储每个像素的深度值，而模板缓冲用于执行模板测试。这两者都可以影响帧缓冲的渲染结果。

1. **深度缓冲（Depth Buffer）**：
    - 深度缓冲通常用于处理遮挡关系。在渲染过程中，每个像素都有一个深度值，用于确定它在场景中的深度位置。深度测试（depth testing）会比较当前像素的深度值与深度缓冲中存储的值，以确定是否应该进行渲染。如果启用深度测试，而且当前像素在深度上小于深度缓冲中的值，那么该像素将被渲染，否则被丢弃。
2. **模板缓冲（Stencil Buffer）**：
    - 模板缓冲用于执行模板测试，这是一种可以根据像素位置执行的测试。模板测试通常涉及到对像素的模板值与模板缓冲中的值进行比较。模板测试的结果决定了是否要进行渲染，以及在渲染过程中执行什么样的操作。

当你创建帧缓冲对象时，可以配置它是否包含深度缓冲和模板缓冲。如果在创建帧缓冲对象时启用了深度缓冲和模板缓冲，它们会影响到后续的渲染操作。关闭depthStencil选项可能是为了在帧缓冲的渲染中不受深度和模板测试的限制，从而更自由地控制像素的渲染和更新。总的来说，深度缓冲和模板缓冲提供了一种控制渲染结果的手段，但在某些情况下，可能需要禁用它们以适应特定的渲染需求。

## 多个点的SDF示例

下图是多个点的SDF示例，图中有5个点，像素的颜色代表“与离它最近的点的距离”。在使用WebGL的绘制过程中，我需要逐一处理这些点，

- 每次处理一个点，只计算这个每个像素到该点的距离；
- 每次处理也称为一帧；
- 在处理下一个点时，通过简单的求小值的运算决定是否更新该点的SDF值。

$$
sdf_{xy} = min(sdf_{xy}, dist_{xy}(p))
$$

![Untitled](WebGL%E7%9A%84framebuffer%E6%B8%B2%E6%9F%93%E4%BC%9A%E5%8F%97%E5%88%B0depthStencil%E7%9A%84%E5%BD%B1%E5%93%8D%2009c20c0d0214406e89c43a7b32aef961/Untitled.png)

![Untitled](WebGL%E7%9A%84framebuffer%E6%B8%B2%E6%9F%93%E4%BC%9A%E5%8F%97%E5%88%B0depthStencil%E7%9A%84%E5%BD%B1%E5%93%8D%2009c20c0d0214406e89c43a7b32aef961/Untitled%201.png)

易见，这样的操作需要WebGL在framebuffer之间迭代。在迭代过程中，我遇到了无法按要求更新帧的问题。经过反复测试和印证，并查询了一些材料，获得了以上心得。

在本问题中，WebGL默认情况下是启用深度测试的。深度测试可能会导致新的像素值被丢弃，因为它们可能位于深度缓冲中的已渲染像素之后。你可以尝试在每一帧的渲染前禁用深度测试（**`gl.disable(gl.DEPTH_TEST)`**），并在渲染后启用它。

[配置Depth-Stencil功能 - Win32 apps](https://learn.microsoft.com/zh-CN/windows/win32/direct3d11/d3d10-graphics-programming-guide-depth-stencil)

[WEBGL_depth_texture extension - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_depth_texture)

[XRWebGLSubImage: depthStencilTexture property - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/XRWebGLSubImage/depthStencilTexture)