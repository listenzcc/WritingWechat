# Learning WebGL

Learn WebGL in Baby's steps.

---
## REGL 简化了 WebGL 的什么？

WebGL 这类工具的学习曲线较为陡峭，因为它虽然工作在 javascript 上，但渲染过程中却会直接用到 C 代码。这样做的原因是由于它在渲染的实现过程中，需要用户自己定义每个 shader 的渲染行为。WebGL 的渲染过程是严格规范化的过程，因此 REGL 对它进行了包装。用户只需要调用这样的函数即可实现渲染。

[How does regl help?](https://observablehq.com/@listenzcc/how-does-regl-help)

## WebGL 的简要入门

优秀的 WebGL 工程代码是开源的，但除了好看之外几乎利用不上。这些没有注释、难以理解其复杂计算过程的代码满天乱飞，乍看起来它们已经足够酷炫和好用，导致继续花时间开发相似的功能就只有成本，但没有意义。而事实是，一旦落实到实际需求上，除了被抄一遍之外，它们无一例外地没有进一步修改的余地。因此，为了让我自己能够在将来的某一天，看得懂、改得动这些代码，我决定开始这个话题。

