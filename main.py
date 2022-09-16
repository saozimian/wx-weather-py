import os
import random
from datetime import date, datetime

import requests
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage

# 当前日期
today = datetime.now()

# 微信公众号 app_id
app_id = os.environ["wx0b46483587e42106"]

# 微信公众号 app_secret
app_secret = os.environ["2d5314c2739c5947d64a41ff96f8949b"]

# 天气接口密钥 key
key = os.environ["6a884ef0485ce94de028f2686ff6baba"]

# 微信公众号 模板id
template_id = os.environ["nn_v9rvOSKW7YJ5f4DI7CRdWj7w1_U2l85EoPmNV_0A"]

# 用户列表 也可通过接口获取，但是接口获取的只有用户id没有用户昵称，不方便部分数据展示，如果有新增人员，对应添加一个user对象即可
'''
    user_id: 微信公众号的 openid
       name: 昵称
       date: 相识日期
   birthday: 生日
       city: 城市编码，api接口文档处查询
'''
user_id_list = [
    {'user_id': 'oqMsm6K3LUYT4lzAqqtM42eKI0ho', "name": '小糖ᥫᩣ', "date": "2022-04-27", "birthday": "05-13",
     'city': '422801'}
     {'user_id': 'oqMsm6OO5I1amqDIqSOkzoQzBW-c', "name": '梦总会碎,', "date": "2022-04-27", "birthday": "05-13",
     'city': '422801'}
]


# 彩虹屁
def get_words():
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return get_words()
    result = words.json()['data']['text']
    print(result)
    return result


# 文字颜色
def get_random_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


# 天气信息
def get_weather(city):
    url = "https://restapi.amap.com/v3/weather/weatherInfo?output=JSON&key=" + key + "&city=" + city
    res = requests.get(url).json()
    print(res)
    weather = res["lives"][0]
    return weather['weather'], weather['temperature'], weather['winddirection'], weather['province'] + weather[
        'city']


# 总天数
def get_count(start_date):
    delta = today - datetime.strptime(start_date, "%Y-%m-%d")
    return delta.days


# 计算生日天数
def get_birthday(birthday):
    print(birthday)
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days


# 发送消息 支持批量用户
def send_message():
    for user in user_id_list:
        user_id = user.get('user_id')
        name = user.get('name')
        birthday = user.get('birthday')
        start_date = user.get('date')
        city = user.get('city')
        get_count(start_date)
        get_birthday(birthday)
        print(user_id)

        wea, temperature, winddirection, cityName = get_weather(city)

        client = WeChatClient(app_id, app_secret)

        wm = WeChatMessage(client)

        data = {
            "name": {"value": name, "color": get_random_color()},
            "weather": {"value": wea, "color": get_random_color()},
            "temperature": {"value": temperature + "℃", "color": get_random_color()},
            "cityname": {"value": cityName, "color": get_random_color()},
            "winddirection": {"value": winddirection, "color": get_random_color()},
            "love_days": {"value": get_count(start_date), "color": get_random_color()},
            "birthday_left": {"value": get_birthday(birthday), "color": get_random_color()},
            "words": {"value": get_words(), "color": get_random_color()}
        }
        res = wm.send_template(user_id, template_id, data)
        print(res)


send_message()
