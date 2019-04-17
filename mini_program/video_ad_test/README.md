

### 在小程序中添加激励视频广告


今天登陆小程序的后台，收到了官方通知，小程序激励式视频广告组件日前已上线，也就是说可以在小程序中插入激励视频广告了。

![image-20190417170702711](https://ws3.sinaimg.cn/large/006tNc79gy1g25qrhvfyyj31es0aggo9.jpg)

早在今年年初的微信公开课上，微信团队就曾透露「2019 年，微信小程序将在三方面发力商业化变现：`小程序激励视频，插屏广告，个人小程序变现`」，现在看来正在一步一步的实现。


#### 激励式视频广告

用户在小程序中主动触发激励式广告，并达成奖励下发标准（完整播放视频广告，并手动点击“关闭广告”按钮），将获得该小程序下发的奖励。广告触发场景与奖励内容均由流量主自定义。

![image-20190417173443740](https://ws3.sinaimg.cn/large/006tNc79gy1g25rkbunczj31u40u01kx.jpg)

下面就教大家如何在小程序中添加视频激励广告。

开通小程序流量主的步骤请先参考这篇文章：[小程序中开通流量主](https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247484838&idx=1&sn=1ffc43c14cc8b7472adf6039508e485a&chksm=e80e577fdf79de695f6be6a82975786cf2783644c36f878e0382f3aac7575fc503a4dc87c767&token=1716683574&lang=zh_CN#rd)

#### 	1、新建广告位

进入小程序的后台，点击**流量主**菜单，选择广告位管理，点击新建广告位。

![image-20190417171940076](https://ws3.sinaimg.cn/large/006tNc79gy1g25r4lefgsj31du0u0wp0.jpg)

这里的广告位类型有两个，选择激励式视频，并输入广告位名称，主要用于区分，方便管理，最后点击确定。

![image-20190417172057347](https://ws1.sinaimg.cn/large/006tNc79gy1g25r5xnyl9j31du0u0n9t.jpg)

创建成功后复制一下你的广告位 ID，并打开开发者工具。

#### 2、插入广告代码

视频激励广告代码插入略微复杂，不像 banner 广告，直接获取广告组件代码插入即可显示。视频激励广告代码调用是 wx.createRewardedVideoAd 接口。接口返回一个单例对象，该对象仅对单个页面有效。多次创建，返回的是同一个激励式视频广告对象。

下面直接来看看是如何插入的：

首先在 js 文件中定义一个全局作用域的视频广告对象

```javascript
// 代码来自公众号「嗜码」
// 在页面中定义激励视频广告对象
var videoAd = null;

Page({
    ...
})
```
由于广告对象是单例，且对单个页面有效，因此官方建议在页面加载后（onLoad 事件）中创建广告对象，并在该页面的生命周期内重复调用该广告对象。

因此在 onLoad 函数中调用广告接口，并监听广告关闭。

```javascript
// 代码来自公众号「嗜码」
onLoad() {
  if (wx.createRewardedVideoAd) {
    // 加载激励视频广告
    videoAd = wx.createRewardedVideoAd({
      adUnitId: '你的 adUnitId'
    })
    //捕捉错误
    videoAd.onError(err => {
    // 进行适当的提示
    })
    // 监听关闭
    videoAd.onClose((status) => {
      if (status && status.isEnded || status === undefined) {
        // 正常播放结束，下发奖励
		// continue you code
      } else {
        // 播放中途退出，进行提示
      }
    })
  }
}
```
注意这里需要对错误进行捕捉，否则会报下面的错误。

![image-20190417202431550](/Users/phillzou/Library/Application Support/typora-user-images/image-20190417202431550.png)

然后，在合适的位置展示广告，例如我这在一个 button 的 tap 事件进行广告显示。

```javascript
// button 点击事件
openVideoAd() {
  console.log('打开激励视频');
  // 在合适的位置打开广告
  if (videoAd) {
    videoAd.show().catch(err => {
      // 失败重试
      videoAd.load()
        .then(() => videoAd.show())
    })
  }
}
```

目前调试工具无法正常显示视频广告，打开手机调试，视频广告可以正常显示。


如果视频显示异常，可以参考下表，对应的异常代码都有解决方案。

![image-20190417204139584](https://ws4.sinaimg.cn/large/006tNc79gy1g25wysyn4wj31920s87c1.jpg)



####  3、接入场景

小程序不知道以哪种形式接入？可以参考以下几种接入场景：

- 内容类。观看视频广告查看更多内容（文字、视频）。
- 工具类。部分功能观看视频后使用，或者限制使用词数。
- 电商类。观看视频广告获取一些优惠。
- 更新中。。。

更多的信息请参考官方[小程序激励式视频广告流量主指引 ](https://wximg.qq.com/wxp/assets/pdf/reward0415.pdf)。

上面的完整代码可以在公众号后台回复「**视频广告**」获取。

---

**推荐阅读**

[「微软」推出的那些好用的微信小程序](<https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247485140&idx=1&sn=65a5f6f67119d485731857e16e35ad9d&chksm=e80e540ddf79dd1b62b3c51352cc33d1384c7bb102cc4d90ed37405a5fd3c92fb7a801358522&token=1078153792&lang=zh_CN#rd>)

[小程序中添加广告并获取收益](https://mp.weixin.qq.com/s?__biz=MzIyNDQzMDAwNg==&mid=2247484838&idx=1&sn=1ffc43c14cc8b7472adf6039508e485a&chksm=e80e577fdf79de695f6be6a82975786cf2783644c36f878e0382f3aac7575fc503a4dc87c767&token=1078153792&lang=zh_CN#rd)