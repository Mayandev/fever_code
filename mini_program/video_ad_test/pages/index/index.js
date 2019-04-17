//index.js
//获取应用实例
var videoAd = null;

Page({

  onLoad() {
    if (wx.createRewardedVideoAd) {
      // 加载激励视频广告
      videoAd = wx.createRewardedVideoAd({
        adUnitId: 'adunit-5c7ca1173accce23'
      })
      //捕捉错误
      videoAd.onError(err => {
        wx.showModal({
          title: '提示',
          content: '视频广告拉取失败',
        })
      })
      // 监听关闭
      videoAd.onClose((status) => {
        if (status && status.isEnded || status === undefined) {
          // 正常播放结束，下发奖励

        } else {
          // 播放中途退出，进行提示
          wx.showModal({
            title: '提示',
            content: 'Sorry...您需要看完视频才能解锁～',
            showCancel: false,
            confirmText: '好的',
            success(res) {
              if (res.confirm) {
                videoAd.load()
                  .then(() => videoAd.show())
                  .catch(err => console.log(err.errMsg))
              }
            }
          })
        }
      })
    }
  },

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


})
