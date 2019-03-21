### Python 爬取校徽图片

之前我开发过一个「校徽头像制作」的微信小程序，目前陆陆续续添加了有几百来所高效校徽，用户数也有 1w+ 了。

校徽之前都是自己手动一个一个添加到服务器的，效率很低，导致如今都还有很多校徽缺失，体验不好。

这几天偶然发现了另外一个小程序，里面的校徽图片很齐全，于是决定爬一爬。

#### 反编译小程序

要爬小程序里面的数据，需要知道小程序的接口地址以及参数。反编译小程序的主要目的就是是看到的 JavaScript 代码，这样就可以知道网络请求的 URL 以及 参数名称。

反编译小程序的过程比较复杂，这里可以直接参考文章[只需两步快速获取微信小程序源码](https://juejin.im/post/5b0e431f51882515497d979f)[^1]。

最后，我在代码中获取到如下关键信息：

```javascript
const url = `https://api.iamsaonian.com/index.php`；
const param = {
    'm': "Api",
    'c': "Xiaohuiavatar",
    'a': "xiaohui_list",
    'p': page
}
```

在 Postman 中进行请求，接口数据格式如下图，十分标准的 Json 格式数据，并且进行了分页。

![Postman 请求数据](https://ws4.sinaimg.cn/large/006tKfTcgy1g1ag5elvauj313j0u0n57.jpg)

下面就可以动手去爬去数据，并下载图片了。

#### 爬取图片

首先说一下爬取思路，请求上面的接口，并解析数据，获取图片的 URL，下载图片，保存 csv 格式数据。

使用到的包有下面几个：

```python
import json
import urllib.request
import requests
import csv
```

使用 urllib 下载图片至本地，图片命名使用 id 命名。

```python
# 获取图片格式
str_array = logo.split('.')
format = str_array[len(str_array) - 1]
# 通过urllib.request下载图片到本地
urllib.request.urlretrieve(logo, '本地地址'+id+'.'+format)
```

打开填写的地址，图片下载到了本地，共有 2728 个校徽图片。

![](https://ws1.sinaimg.cn/large/006tKfTcgy1g1af2d57puj316s0q0e2s.jpg)

#### 保存数据

以后想使用云开发重构小程序，因此将数据保存为 csv 格式，便于数据的插入。

```python
# 将数据保存为 csv 格式
with open('logo.csv', 'w', newline='', encoding='utf-8') as csvfile:
  # 设置表头
  fieldnames = ['id', 'name', 'logo']
  # 获得 DictWriter对象,使用，号分隔，便于云数据库导入
  dict_writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
  # 第一次写入数据先写入表头
  dict_writer.writeheader()
  dict_writer.writerows(list)
```

![导出的 csv 数据](https://ws4.sinaimg.cn/large/006tKfTcgy1g1aezy95cpj30ji0a80ut.jpg)

打开小程序云开发控制台，选择数据库，导入本地 csv 数据，这里我已经将爬去的数据导入到云开发数据库了。

![导入云开发数据库](https://ws3.sinaimg.cn/large/006tKfTcgy1g1agx147i4j318k0u0grm.jpg)



在公众号对话框回复**「爬取校徽」**可获取本次文章的代码。

![👆👆更多精彩文章](https://ws3.sinaimg.cn/large/006tKfTcgy1g1ah3pnc9hj306o055t91.jpg)


[^1]: https://juejin.im/post/5b0e431f51882515497d979f

