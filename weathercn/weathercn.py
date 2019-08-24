#!/usr/bin/python3
# -*- coding: utf-8 -*-
import urllib.request, urllib.error, urllib.parse
import json
import city
 
#url = 'http://m.weather.com.cn/data/%s.html'
#天气网API使用的是城市编码，城市编码在city.py文件中已经给出，上面的url的%s部分就是需要填充的城市编码部分
#范例1 url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
#范例2 url = 'http://www.weather.com.cn/data/sk/101010100.html'
 
city_name = input("请输入城市查询天气：")

if not city_name in city.citycode:
    print("查询天气失败")
else:
	url = 'http://www.weather.com.cn/data/cityinfo/%s.html'
	code = city.citycode[city_name]
	res = urllib.request.urlopen(url%code)
	a = res.read()
	data = json.loads(a)
	result = data['weatherinfo']
	str_temp = ('%s\n%s ~ %s') % (
		result['weather'],
		result['temp1'],
		result['temp2'])
	print(str_temp)