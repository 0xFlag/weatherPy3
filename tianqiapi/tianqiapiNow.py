#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re

def weather():
	a = input("请输入查询天气格式（天气 地名）：")
	if a == "":
		print("请输入天气地名")
	elif "天气" in a:
		url = "https://www.tianqiapi.com/api/?version=v6&city="
		b = a.strip("天气")
		r='[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' # 正则删除标点符号
		c=re.sub(r,'',b)
		post = c.strip(" ") # 删除空格
		#print(post) # 测试
		url_now = url + post
		rs_we = requests.get(url_now).json()
		weather_city = rs_we["city"]
		if weather_city == post:
			weather_uptime = rs_we["date"] + "\000" + rs_we["week"] + "\000" + rs_we["update_time"] # 更新时间
			weather_wea = rs_we["wea"] # 天气情况
			weather_tem = rs_we["tem"] + "℃" # 当前温度
			weather_temnow = rs_we["tem2"] + "/" + rs_we["tem1"] + "℃" # 早晚温差
			weather_win = rs_we["win"] # 风向
			weather_win_speed = rs_we["win_speed"] # 风速等级
			weather_win_meter = rs_we["win_meter"] # 风速
			weather_humidity = rs_we["humidity"] # 湿度
			weather_visibility = rs_we["visibility"] # 能见度
			weather_pressure = rs_we["pressure"] + "hPa" # 气压
			weather_air = rs_we["air"] # 空气质量
			weather_air_pm25 = rs_we["air_pm25"] # PM2.5
			weather_air_level = rs_we["air_level"] # 空气质量等级
			print(weather_city + "-今日天气预报（实时）：" + "\r\n当前温度：" + weather_tem + "\r\n早晚温差：" + weather_temnow + "\r\n天气情况：" + weather_wea + "\r\n湿度：" + weather_humidity + "\r\n空气质量：" + weather_air + "\r\nPM2.5：" + weather_air_pm25 + "\r\n空气质量等级：" + weather_air_level + "\r\n气压：" + weather_pressure + "\r\n风向：" + weather_win + "\r\n风速：" + weather_win_meter + "\r\n风速等级：" + weather_win_speed + "\r\n能见度：" + weather_visibility + "\r\n更新时间：" + weather_uptime)
		else:
			print("当前地区无法查询天气")
	else:
		print("查询格式错误")

if __name__ == '__main__':
	weather()