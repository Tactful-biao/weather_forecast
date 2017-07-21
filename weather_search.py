#!/usr/bin/env python3
# -*- encoding:utf-8 -*-
import json
import requests
import datetime

keyword = input('请输入您要查询的城市：')

try:
    api = requests.get("http://www.sojson.com/open/api/weather/json.shtml?city=" + keyword)
    data = api.json()
    datainfo = data['data']
    forecast = datainfo['forecast']
    wendu = datainfo['wendu']
    tishi = datainfo['ganmao']
    today = datetime.date.today()
    today_high = forecast[0]['high']
    today_low = forecast[0]['low']
    tomorrow_high = forecast[1]['high']
    tomorrow_low = forecast[1]['low']
    the_day_after_tomorrow_high = forecast[2]['high']
    the_day_after_tomorrow_low = forecast[2]['low']
    
    
    print('城市：',datainfo['city'])
    print('今天的天气情况:')
    print('时间：',today)
    print('天气类型：',forecast[0]['type'])
    print('风力：',forecast[0]['fengli'])
    print('温度：',today_high[3:],'-',today_low[3:])
    print('当前温度：',wendu)
    print('最高温度：',forecast[0]['high'])
    print('最低温度：',forecast[0]['low'])
    print('风向：',forecast[0]['fengxiang'])
    print('')
    print('明天的天气情况:')
    print('时间：',today + datetime.timedelta(days=1))
    print('天气类型：',forecast[1]['type'])
    print('风力：',forecast[1]['fengli'])
    print('温度：',tomorrow_high[3:],'-',tomorrow_low[3:])
    print('最高温度：',forecast[1]['high'])
    print('最低温度：',forecast[1]['low'])
    print('风向：',forecast[1]['fengxiang'])
    print('')
    print('后天的天气情况:')
    print('时间：',today + datetime.timedelta(days=2))
    print('天气类型：',forecast[2]['type'])
    print('风力：',forecast[2]['fengli'])
    print('温度：',the_day_after_tomorrow_high[3:],'-',the_day_after_tomorrow_low[3:])
    print('最高温度：',forecast[2]['high'])
    print('最低温度：',forecast[2]['low'])
    print('风向：',forecast[2]['fengxiang'])
    print('')
    print('温馨提示：',tishi)
except KeyError as e:
    print('请输入正确的中文名称进行查询！')
