# wx-weather-py

[![morning](https://github.com/saozimian/wx-weather-py/actions/workflows/main.yml/badge.svg)](https://github.com/saozimian/wx-weather-py/actions/workflows/main.yml)

## 介绍

项目地址：https://github.com/saozimian/wx-weather-py

Gitee：https://gitee.com/zhanghuan08/wx-weather-py

> 通过 微信公众号定时发送模板消息~~

![img.png](https://image.codehuan.com/image/202208242046885.png)

## 食用方法

### 1、Fork 本项目

![img.png](https://image.codehuan.com/image/202208242046822.png)

### 2、注册测试微信公众号

注册地址：https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

![image-20220824204559401](https://image.codehuan.com/image/202208242046231.png)

#### 2.1、微信公众号测试参数获取

扫码注册登录之后，可以看到下面的 `appID` 和 `appsecret` 参数，这个我们待会用到。

![img6.png](https://image.codehuan.com/image/202208242046456.png)

#### 2.2、创建模板

![image-20220824205152299](https://image.codehuan.com/image/202208242051657.png)

**模板样例**

感兴趣可以自己花点时间调整一个好看的。

```xml
臭宝所在的城市：{{cityname.DATA}}
        天气：{{weather.DATA}}
        温度：{{temperature.DATA}}
        风向：{{winddirection.DATA}}
        今天是我们的第{{love_days.DATA}}天
        距离臭宝生日还有{{birthday_left.DATA}}天

        {{words.DATA}}
```

#### 2.3、获取模板ID

![img.png](https://image.codehuan.com/image/202208242046594.png)

#### 2.4、二维码

**使用者必须先让他/她扫描关注这个二维码，关注之后右侧列表会显示对应的人员openid，
我们也可以通过接口获取这个人员id，也可以写在我们的配置文件中。**

![image-20220824205904029](https://image.codehuan.com/image/202208242059523.png)

有了上面的信息，我们返回到第一步，在我们`Fork`下来的项目中进行配置。

## 3、申请天气接口

高德开放平台：https://lbs.amap.com/

1、我们这边使用高德开放平台的天气查询接口。没有账号首先进行注册。

![image-20220824211053139](https://image.codehuan.com/image/202208242110590.png)

2、来到控制台创建应用。

`应用名称` 和`应用类型`可以随便填写。

![image-20220824211252800](https://image.codehuan.com/image/202208242112938.png)

3、添加`Key`

Key名称：任意填写。

服务平台选择 ：`Web服务`。

![image-20220824211434237](https://image.codehuan.com/image/202208242114560.png)

3、完成之后获取我们的`Key`

![image-20220824211610758](https://image.codehuan.com/image/202208242116977.png)

## 4、修改配置

来到我们项目首页，按照图中的顺序进行选择。①、②、③。

![img.png](https://image.codehuan.com/image/202208242046704.png)

第三步是进行我们的参数修改，选择`New Repository secret`。

![image-20220824210442601](https://image.codehuan.com/image/202208242104799.png)

`Name`：对应的Key

`Value`：对应的值

完成之后如下图。

![image-20220824210254552](https://image.codehuan.com/image/202208242103796.png)

## 5、查看我们的定时任务

![img.png](https://image.codehuan.com/image/202208242119166.png)

### 5.1、修改定时任务时间

`cron`: github的时区为GMT，他们的0点对应我们时区的8点。

`0 0 * * *`：表示每天的早上8点执行一次。

可自行修改定时任务规则（github的cron没有秒）

**需要注意：**
*因为毕竟是免费的服务器，所以如果选择的定时任务执行的时间节点可能存在很多个任务，我们的任务可能就会被加入到队列中进行排队，所以不一定是按照当时的时间去执行，我们可以错开时间去执行我们的定时任务。*

或者添加 `workflow_dispatch:` 在我们的定时任务列表会出现一个按钮，可以手动去执行

![image-20220825121735027](https://image.codehuan.com/image/202208251217399.png)

`main.yml样例`
```yaml
name: morning

on:
  schedule:
    - cron: '50 1 * * *'  #每天的9点50执行 （国内时间）  
  workflow_dispatch:

jobs:
  send_message:
    runs-on: ubuntu-latest
    name: send morning to your girlfriend

    steps:
      - name: checkout
        uses: actions/checkout@v3
        with:
          ref: master

      - uses: actions/checkout@v3
      - name: checkout
        uses: actions/setup-python@v3
        with:
          python-version: "3.10"
      - name: sender
        run: pip install -r ./requirements.txt && python ./main.py

    env:
      APP_ID: ${{ secrets.APP_ID }}
      APP_SECRET: ${{ secrets.APP_SECRET }}
      KEY: ${{ secrets.KEY }}
      TEMPLATE_ID: ${{ secrets.TEMPLATE_ID }}


```

## Java版

> 项目地址：https://github.com/saozimian/wx-weather
>
> Gitee：https://gitee.com/zhanghuan08/wx-weather

![image-20220824213523984](https://image.codehuan.com/image/202208242135105.png)
