在做前端开发的过程中，页面设计与排版往往成为一大拦路虎。抛开色彩的搭配不说，最让人头疼的无非就是如何让元素在水平或者垂直方向上进行布局排列，并以一定的方式对齐，使得页面显得简洁有序。

在这几周小程序开发工作当中，我也碰到了这样的问题，主要是因为自己CSS功底不扎实，只对几个常用的属性较为熟悉，因此布局起来相当吃力。每次写页面，都要先找一大堆模板，最后堆叠出来的代码我自己都看得恶心。但渐渐的，发现别人的代码中都有使用到flex布局，稍做了解后，确实好用，很快就可以自己编写出好看的页面。


### 1、flex布局

Flex是Flexible Box的缩写，意为"弹性盒子"。传统的布局解决方案是基于盒状模型，依赖 display、position、float这些属性。使用过的人就知道，用起来很不方便，没有响应式，并且对于一些特殊布局很难实现，比如，垂直居中。

![6](https://ws3.sinaimg.cn/large/006tKfTcgy1g1ai131wfij30jg0a8q30.jpg)

之后W3C提出了一种新的方案----Flex布局，可以简便、完整、响应式地实现各种页面布局。目前，它已经得到了所有浏览器的支持。下面的例子通过微信小程序实现，网页端同理。

### 2、布局拆解

在对页面进行编码前，通常需要对布局进行拆解，这也是关键的一步，我以下面的图片为例作讲解解。


![微信图片_20181130225547](https://ws4.sinaimg.cn/large/006tKfTcgy1g1ai3k3tsvj30u00a1ta2.jpg)

上面截图是我为某公司制作的官网小程序其中的一部分，布局并不复杂，由外至内进行分析。首先整体布局是一整行，其中有三个子项水平排列，每个子项又可再次进行拆分。

子项同样的由外至内分析，最外层为一个圆形，中间内容可以看作是一个图标和一行文字垂直居中排列，最后的组件拆解图如下。

![2](https://ws3.sinaimg.cn/large/006tKfTcgy1g1ai11l5s5j30rp0fkmxx.jpg)



### 3、编码实现

首先按找布局拆解的思路，先实现三个圆形组件的水平排列。平常我们想到的方式可能是使用浮动或者绝对布局进行定位，但是这样的方式对不同屏幕大小尺寸的设备不友好，容易出现布局错乱。下面使用flex布局看看是如何实现上面效果的。

小程序端页面代码如下，主要是定义几个容器，网页端同理（将view换成div即可）。

```xml
<view class="circle_line">
  <view class="circle"></view>
  <view class="circle"></view>
  <view class="circle"></view>
</view>
```
WXSS代码如下，网页端同理。
```css
.circle_line {
  /* 定义弹性布局，默认水平排列 */
  display: flex;
  /* 设置主轴对齐方式，space-around表示两端对齐，项目间间隔相等 */
  justify-content: space-around;
  /* 在交叉上的对齐方式 */
  align-items: center;
}
.circle {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background:linear-gradient(to right, #6372ff 0%, #5ca9fb 100%);
}
```

这时候页面的效果就如下图所示：

![3](https://ws1.sinaimg.cn/large/006tKfTcgy1g1ai1123zkj30bp03rglk.jpg)


首先注意的是flex布局默认排列方式是水平排列。如果对justify-content以及align-item这两个属性可能比较模糊，这里我将第一个属性的所有属性值试一遍，看看效果，另外一个同理，只不过是在交叉轴方向上的对齐方式。

![4](https://ws1.sinaimg.cn/large/006tKfTcgy1g1ai0zah3qj306y0c5my3.jpg)



有了上面布局的基础，很快的便可以将圆形内部的图标以及文字进行布局。实现思路就是将图标以及文字放入一个弹性盒子，并将排列方式设置为垂直方向，然后设置居中对齐。
wxml代码：
```xml
<view class="circle">
  ...
</view>
<view class="circle">
  <view class="circle_icon">
    <image class="circle_icon_image" mode="scaleToFill" src="/images/android.png" />
  </view>
  <view class="circle_txt">安卓开发</view>
</view>
<view class="circle">
  ...
</view>
```

wxss代码：
```CSS
.circle {
  ... 
  display: flex;
  flex-direction: column;
  align-items: center; 
  justify-content: center;
}
.circle_icon_image {
  height: 30px;
  width: 30px;
}
.circle_txt {
  color: #fff;
  text-align: center;
  font-size: 13px;
}
```

最后保存，就实现下面的效果啦！

![微信图片_20181130225547](https://ws4.sinaimg.cn/large/006tKfTcgy1g1ai3k3tsvj30u00a1ta2.jpg)

### 4、总结

希望上面过程，不仅仅说是学会了一个什么样的布局，最为关键的还是布局拆解的步骤，因为很多前端的编写都需要有类似的思想。

更多的相关flex布局可以去一些学习网站上做详细了解，祝学习愉快！

---

**推荐阅读**
[小程序学习资源整理](https://www.baidu.com)

![👆👆更多精彩文章](https://ws3.sinaimg.cn/large/006tKfTcgy1g1ah3pnc9hj306o055t91.jpg)