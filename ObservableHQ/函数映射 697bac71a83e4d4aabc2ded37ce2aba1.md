# 函数映射

本文在 Observable 提供了一个好用的函数可视化工具。

[Mathmatic notebook III](https://observablehq.com/@listenzcc/mathmatic-notebook-iii "Mathmatic notebook III")

---

-   [函数映射](#函数映射)
    -   [函数编辑](#函数编辑)
    -   [复数空间映射](#复数空间映射)
        -   [复数运算库](#复数运算库)

## 函数编辑

本工具提供了简单的函数编辑功能，但目前仅支持简单函数，即每个自变量对应一个且仅有一个因变量

$$
\begin{cases}
y=f(x)\\
f(x_1) - f(x_2) \neq 0 \\
\end{cases}
$$

编辑方式并不复杂，如下图即可。

![Input](%E5%87%BD%E6%95%B0%E6%98%A0%E5%B0%84%20697bac71a83e4d4aabc2ded37ce2aba1/Untitled.png)

Input

其对应的波形如下图，由于横纵坐标差异较大，因此自动在纵坐标使用更密集的网络线来表示。这样做的效果是横纵坐标网络线之间的尺寸是相同的。

![Pic](%E5%87%BD%E6%95%B0%E6%98%A0%E5%B0%84%20697bac71a83e4d4aabc2ded37ce2aba1/Untitled%201.png)

Pic

## 复数空间映射

接下来，通过 ChatGTP 写出一套 Javascript 的复数运算库。根据该库，只通过简单的定义传输函数就可以完成复变函数的相关计算

$$
((2+3i)+z)^p
$$

```jsx
convert = (x, y) => {
    const c = new complex(x, y);
    return c.add(new complex(2, 3)).power(power);
};
```

在指数为负数和正数时，映射后的坐标系和曲线如下图所示。

![Neg](%E5%87%BD%E6%95%B0%E6%98%A0%E5%B0%84%20697bac71a83e4d4aabc2ded37ce2aba1/Untitled%202.png)

Neg

![Pos](%E5%87%BD%E6%95%B0%E6%98%A0%E5%B0%84%20697bac71a83e4d4aabc2ded37ce2aba1/Untitled%203.png)

Pos

![Larger](%E5%87%BD%E6%95%B0%E6%98%A0%E5%B0%84%20697bac71a83e4d4aabc2ded37ce2aba1/Untitled%204.png)

Larger

### 复数运算库

```jsx
complex = {
  function complex(real, imag) {
    this.real = real;
    this.imag = imag;
  }

  complex.prototype.add = function (c) {
    return new complex(this.real + c.real, this.imag + c.imag);
  };

  complex.prototype.subtract = function (c) {
    return new complex(this.real - c.real, this.imag - c.imag);
  };

  complex.prototype.multiply = function (c) {
    return new complex(
      this.real * c.real - this.imag * c.imag,
      this.real * c.imag + this.imag * c.real
    );
  };

  complex.prototype.divide = function (c) {
    var denom = c.real * c.real + c.imag * c.imag;
    return new complex(
      (this.real * c.real + this.imag * c.imag) / denom,
      (this.imag * c.real - this.real * c.imag) / denom
    );
  };

  complex.prototype.power = function (n) {
    var r = Math.sqrt(this.real * this.real + this.imag * this.imag);
    var theta = Math.atan2(this.imag, this.real);
    var real = Math.pow(r, n) * Math.cos(n * theta);
    var imag = Math.pow(r, n) * Math.sin(n * theta);
    return new complex(real, imag);
  };

  return complex;
}
```
