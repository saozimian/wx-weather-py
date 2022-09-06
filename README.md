# wx-weather-py

[![morning](https://github.com/saozimian/wx-weather-py/actions/workflows/main.yml/badge.svg)](https://github.com/saozimian/wx-weather-py/actions/workflows/main.yml)

## 介绍

项目地址：https://github.com/saozimian/wx-weather-py

Gitee：https://gitee.com/zhanghuan08/wx-weather-py

> 通过 微信公众号定时发送模板消息~~

<img src="https://image.codehuan.com/image/202209061616187.png" alt="image-20220906161625842" style="zoom: 33%;" />

## 食用方法

### 1、Fork 本项目

![image-202209061617397](https://image.codehuan.com/image/202209061617397.jpg)

### 2、注册测试微信公众号

注册地址：https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

![image-20220824204559401](https://image.codehuan.com/image/202209061620253.png)

#### 2.1、微信公众号测试参数获取

扫码注册登录之后，可以看到下面的 `appID` 和 `appsecret` 参数，这个我们待会用到。

![image-202209061620253](https://image.codehuan.com/image/202209061620253.png)

#### 2.2、创建模板

<img src="https://image.codehuan.com/image/202209061627392.png" alt="image-202209061627392" style="zoom:80%;" />

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

![image-202209061621443](https://image.codehuan.com/image/202209061621443.png)

#### 2.4、二维码

**使用者必须先让他/她扫描关注这个二维码，关注之后右侧列表会显示对应的人员openid，
我们也可以通过接口获取这个人员id，也可以写在我们的配置文件中。**

![image-20220824205904029](https://image.codehuan.com/image/202209061622123.png)

有了上面的信息，我们返回到第一步，在我们`Fork`下来的项目中进行配置。

### 3、申请天气接口

> 高德开放平台：https://lbs.amap.com/

#### 3.1、注册

如果我们这边使用高德开放平台的天气查询接口。没有账号首先进行。

![image-20220824211053139](https://image.codehuan.com/image/202209061622589.png)

#### 3.2、创建应用

`应用名称` 和`应用类型`可以随便填写。

![image-20220824211252800](https://image.codehuan.com/image/202209061622894.png)

#### 3.3、添加`Key`

Key名称：任意填写。

服务平台选择 ：`Web服务`。

![image-20220824211434237](https://image.codehuan.com/image/202209061622383.png)

#### 3.4、获取`Key`

![image-20220824211610758](https://image.codehuan.com/image/202209061622263.png)

#### 3.5、天气接口

文档地址：https://lbs.amap.com/api/webservice/guide/api/weatherinfo

| URL      | https://restapi.amap.com/v3/weather/weatherInfo?parameters |
| -------- | ---------------------------------------------------------- |
| 请求方式 | GET                                                        |

- **请求参数**

| 参数名     | 含义             | 规则说明                                                     | 是否必须 | 缺省值 |
| :--------- | :--------------- | :----------------------------------------------------------- | :------- | :----- |
| key        | 请求服务权限标识 | 用户在高德地图官网[申请web服务API类型KEY](https://lbs.amap.com/dev/) | 必填     | 无     |
| city       | 城市编码         | 输入城市的adcode，adcode信息可参考[城市编码表](https://lbs.amap.com/api/webservice/download) | 必填     | 无     |
| extensions | 气象类型         | 可选值：base/allbase:返回实况天气all:返回预报天气            | 可选     | 无     |
| output     | 返回格式         | 可选值：JSON,XML                                             | 可选     | JSON   |

- **服务示例**

```shell
https://restapi.amap.com/v3/weather/weatherInfo?city=110101&key=<用户key>
```

## 4、修改配置

来到我们项目首页，按照图中的顺序进行选择。①、②、③。

![image-202209061623234](https://image.codehuan.com/image/202209061623234.png)

第三步是进行我们的参数修改，选择`New Repository secret`。

![image-20220824210442601](https://image.codehuan.com/image/202209061623494.png)

`Name`：对应的Key

`Value`：对应的值

完成之后如下图。

![image-20220824210254552](https://image.codehuan.com/image/202209061623436.png)

## 5、查看我们的定时任务

![imgge-202209061623998](https://image.codehuan.com/image/202209061623998.png)

### 5.1、修改定时任务时间

`cron`: github的时区为GMT，他们的0点对应我们时区的8点。

`0 0 * * *`：表示每天的早上8点执行一次。

可自行修改定时任务规则（github的cron没有秒）

**需要注意：**
*因为毕竟是免费的服务器，所以如果选择的定时任务执行的时间节点可能存在很多个任务，我们的任务可能就会被加入到队列中进行排队，所以不一定是按照当时的时间去执行，我们可以错开时间去执行我们的定时任务。*

或者添加 `workflow_dispatch:` 在我们的定时任务列表会出现一个按钮，可以手动去执行

![image-20220825121735027](https://image.codehuan.com/image/202209061623866.png)

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

![image-20220824213523984](https://image.codehuan.com/image/202209061623380.png)
