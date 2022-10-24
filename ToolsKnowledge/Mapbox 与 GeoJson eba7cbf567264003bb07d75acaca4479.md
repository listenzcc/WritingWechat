# Mapbox 与 GeoJson

与 Canvas 相比，Mapbox 的原生 Layer 显然是更加优雅的解决方案，但它需要 GeoJson 的支持。

本文的代码可见我的开源前端库

[Mapbox with hex grids](https://observablehq.com/@listenzcc/mapbox-with-hex-grids)

---
- [Mapbox 与 GeoJson](#mapbox-与-geojson)
  - [图层与地理数据绑定](#图层与地理数据绑定)
  - [性能与畸变](#性能与畸变)

## 图层与地理数据绑定

GeoJson 是常用的地理数据规范，Mapbox 将它作为 Source，而 Source 可以与 Layer 进行绑定，从而实现地图绘制

```jsx
map.on("load", () => {
    // Init source
    map.addSource("gridGeometrySource", {
      type: "geojson",
      data: {
        type: "Feature",
        properties: {},
        geometry: mkGeometry()
      }
    });

    // Init grid line
    map.addLayer({
      id: "gridLine",
      type: "line",
      source: "gridGeometrySource",
      layout: {
        "line-join": "round",
        "line-cap": "round"
      },
      paint: {
        "line-color": gridColor,
        "line-width": 1
      }
    });
})
```

而 Source 可以是动态的，因此可以实现地图按需绘制。要达到这样做的目的，只需要在重绘函数中对 Source 进行修改，并且将它绑定在相应的操作上即可。

```jsx
// Generate reDraw function and bind it with mapbox interactions
reDraw = {
  // Update the gridGeometrySource source
  function reDraw() {
    map.getSource("gridGeometrySource").setData({
      type: "Feature",
      properties: {},
      geometry: mkGeometry()
    });
  }

  map.on("dragend", () => {
    reDraw();
  });

  map.on("zoomend", () => {
    reDraw();
  });

  map.on("pitchend", () => {
    reDraw();
  });

  return reDraw;
}
```

而 GeoJson 这个东西，几乎可以实现所有地图上的绘制操作，因此，这种方式相当实用。

## 性能与畸变

这样做的效果看上去很好，至少它解决了之前遇到的“由于覆盖在高度地图上的 Canvas 也同样被拉伸了，……因此线条在宽度方向会产生一定的畸变”的问题。在线条异常密集时，它产生的畸变也不至于让线过宽而混在一起。并且渲染的性能也有肉眼可见的提升。

![Untitled](Mapbox%20%E4%B8%8E%20GeoJson%20eba7cbf567264003bb07d75acaca4479/Untitled.png)