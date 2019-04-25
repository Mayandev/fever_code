### 小程序插屏广告教程

这两天有读者在后台提醒我小程序可以添加插屏广告了，让我出一期教程。最近也在一直忙着毕业论文，抽空看了看小程序的插屏广告，插入广告并不难，但却有很多的条件限制。

还不会开通流量主或者不会插入 banner / 视频广告的先看下面两篇教程吧。

[小程序开通流量主](https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247484838&idx=1&sn=1ffc43c14cc8b7472adf6039508e485a&chksm=e80e577fdf79de695f6be6a82975786cf2783644c36f878e0382f3aac7575fc503a4dc87c767&token=1384912173&lang=zh_CN#rd)

[小程序插入激励视频广告](https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247485252&idx=1&sn=695560f88d80995093e7cb55b4749cbc&chksm=e80e559ddf79dc8b324ee0ada1b69e09ef4e25c841be5d3a2208c7a56795abc98377d88162eb&token=1384912173&lang=zh_CN#rd)

#### 插屏广告

用户触发小程序中的特定场景时，插屏广告将自动向用户展现，用户可以随时关闭插屏广告。广告触发场景由流量主自定义，广告按曝光计费（CPM）。

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2exzs1bu0j31t80q0k63.jpg)

官方建议在“有停顿感“的场景展现小程序插屏广告，例如`切换 tab、游戏回合结束、流程结束、视频播放停顿等等`，同时不建议在`一打开小程序或者操作过程中途`显示插屏广告。个人认为这个界定有些模糊了，拓展以及想象空间非常非常大。

![](https://ws4.sinaimg.cn/large/006tNc79gy1g2eyb26vvpj31ui0pgafz.jpg)

以上一些定义，各位可自行体会。下面进入正题，就教大家创建以及插入插屏广告。

#### 创建广告位

进入小程序的后台，点击**流量主**菜单，选择广告位管理，点击新建广告位。

![image-20190417171940076](https://ws3.sinaimg.cn/large/006tNc79gy1g25r4lefgsj31du0u0wp0.jpg)

现在这里的广告位类型有三个，选择插屏广告，并输入广告位名称，主要用于区分，方便管理，最后点击确定。

![](https://ws1.sinaimg.cn/large/006tNc79gy1g2eympoueej31h00u0gye.jpg)

创建成功后复制一下你的广告位 ID，并打开开发者工具。

#### 插入代码

插屏广告代码调用是 wx.createInterstitialAd 接口。接口返回一个广告对象，**该对象仅对单个页面有效，不允许跨页面使用**。与激励视频广告不同，多次创建，返回的是多个插屏广告对象。

下面以切换 tab 场景为例，教大家如何插入插屏广告。

首先 tabbar 的配置如下：

```json
"tabBar": {
    "color": "#707070",
    "selectedColor": "#6c63ff",
    "backgroundColor": "#ffffff",
    "list": [
      {
        "pagePath": "pages/home/home",
        "text": "home",
        "iconPath": "images/home.png",
        "selectedIconPath": "images/home-fill.png"
      },
      {
        "pagePath": "pages/bug/bug",
        "text": "bug",
        "iconPath": "images/bug.png",
        "selectedIconPath": "images/bug-fill.png"
      }
    ]
  }
```

官方不建议一打开小程序就显示广告，因此这里将广告插入在第二个页面中。

首先初始化插屏广告对象

```javascript
// 在页面中定义插屏广告对象
var interstitialAd = null;

Page({
    ...
})
```

由于广告对象仅对单个页面有效，官方建议开发者在页面加载后（onLoad事件）创建一个广告对象，并在该页面的生命周期内重复调用该广告对象。

```javascript
onLoad: function (options) {
  // 创建插屏广告实例
  if (wx.createInterstitialAd) {
    interstitialAd = wx.createInterstitialAd({
      adUnitId: 'adunit-你的广告id'
    })
    //捕捉错误
    interstitialAd.onError(err => {
      console.log(err);
    })
  }
},
```

由于 tabbar 的 onLoad事件 在整个应用生命周期中只会调用一次，因此这里选择在 onShow 中显示广告。

```javascript
onShow: function () {
  // 显示插屏广告
  if (interstitialAd) {
    interstitialAd.show().catch((err) => {
      console.error(err)
    })
  }
},
```

**目前调试工具无法正常显示视频广告，打开手机调试，插屏广告可以正常显示。**

如果视频不显示或者显示异常，可以参考表格中的异常信息代码，找到相应的解决方案。

![image-20190425173227222](https://ws1.sinaimg.cn/large/006tNc79gy1g2f0gdae4dj319a0sadnn.jpg)

另外，还有人问到如何实现切回主页面显示广告，这其实并不难，这里提供一个思路：在主页面设置一个布尔常量，**在 onShow 函数中通过这个布尔常量来判断当前页面是否为第一次显示即可**。代码就不展示了，不会的留言或者私聊问我吧。

#### 插屏广告限制

为保证良好的用户体验，插屏广告频率将受到如下限制，因此设计广告触发场景时需要考虑到以下的限制情况。

1. 用户每次打开小程序后的一段时间内，将不会展现插屏广告。
2. 两个插屏广告之间将会间隔一段时间。
3. 一个激励式视频与一个插屏广告之间将会间隔一段时间，展现次序不分先后。

另外，show方法返回rejected Promise时会有对应的错误码信息。因此，可以通过捕获的异常信息，来判断广告不显示的原因。

![image-20190425174858364](https://ws3.sinaimg.cn/large/006tNc79gy1g2f0xjxtcrj30pm0hejud.jpg)

这里吐槽一下，这么多限制，感觉也没啥地方可以展示的。


更多的信息请参考官方[小程序插屏广告流量主指引](https://wximg.qq.com/wxp/pdftool/get.html?post_id=741)。

上面的完整代码可以在公众号后台回复「**`插屏广告`**」获取。

---

**推荐阅读**
[小程序开通流量主](https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247484838&idx=1&sn=1ffc43c14cc8b7472adf6039508e485a&chksm=e80e577fdf79de695f6be6a82975786cf2783644c36f878e0382f3aac7575fc503a4dc87c767&token=1384912173&lang=zh_CN#rd)
[小程序插入激励视频广告](https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247485252&idx=1&sn=695560f88d80995093e7cb55b4749cbc&chksm=e80e559ddf79dc8b324ee0ada1b69e09ef4e25c841be5d3a2208c7a56795abc98377d88162eb&token=1384912173&lang=zh_CN#rd)

![](https://ws3.sinaimg.cn/large/006tNc79gy1g25xoimqxjj30jg0dwjtq.jpg)