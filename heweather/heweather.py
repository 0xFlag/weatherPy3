#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
MY_WEATHER_KEY = r"API KEY" # heweather.net API key
URL_NOW_WEATHER = r"https://free-api.heweather.net/s6/weather/now?location=auto_ip&key="+MY_WEATHER_KEY # 实时天气
URL_FOR_WEATHER = r"https://free-api.heweather.net/s6/weather/forecast?location=auto_ip&key="+MY_WEATHER_KEY  #预测天气

URL_NOW_WEATHER_CID = r"https://free-api.heweather.net/s6/weather/now?location="
URL_FOR_WEATHER_CID = r"https://free-api.heweather.net/s6/weather/forecast?location="
URL_TAIL_CID = r"&key="+MY_WEATHER_KEY

def heweather():
	a = input("请输入查询天气格式（天气 地名）：")
	if a == "":
		print("请输入天气号")
	elif a[0:2] == u"天气":
		post = str(a[2:])
		url_now = URL_NOW_WEATHER_CID + post + URL_TAIL_CID

		rs_we = requests.get(url_now).json()
		wea_status = rs_we["HeWeather6"][0]["status"]
		if wea_status == "ok":
			wea_info_str = rs_we["HeWeather6"][0]["now"]["cond_txt"]
			weat_info = (wea_info_str + "  " + rs_we["HeWeather6"][0]["now"]["tmp"] + "度  "+rs_we["HeWeather6"][0]["now"]["wind_dir"] + "  " + rs_we["HeWeather6"][0]["now"]["wind_sc"] + "级")
		

			url_forecast = URL_FOR_WEATHER_CID + post + URL_TAIL_CID
			rs_we = requests.get(url_forecast).json()
			forewea_info_str = rs_we["HeWeather6"][0]["daily_forecast"][1]["cond_txt_d"]
			foreweat_info = (wea_info_str + "  " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["tmp_min"] + " ~ " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["tmp_max"] + "度  " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["wind_dir"] + " " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["wind_sc"] + "级")

			print("今日天气预报：\r\n"+weat_info+"\r\n明日天气预报：\r\n"+foreweat_info)
		elif wea_status == "unknown location":
			print("您查询的区域无法显示天气")
		else:
			print("API Error")
	elif a[2:4] == u"天气":
		post = str(a[:2])
		url_now = URL_NOW_WEATHER_CID + post + URL_TAIL_CID

		rs_we = requests.get(url_now).json()
		wea_status = rs_we["HeWeather6"][0]["status"]
		if wea_status == "ok":
			wea_info_str = rs_we["HeWeather6"][0]["now"]["cond_txt"]
			weat_info = (wea_info_str + "  " + rs_we["HeWeather6"][0]["now"]["tmp"] + "度  "+rs_we["HeWeather6"][0]["now"]["wind_dir"] + "  " + rs_we["HeWeather6"][0]["now"]["wind_sc"] + "级")

			url_forecast = URL_FOR_WEATHER_CID + post + URL_TAIL_CID
			rs_we = requests.get(url_forecast).json()
			forewea_info_str = rs_we["HeWeather6"][0]["daily_forecast"][1]["cond_txt_d"]
			foreweat_info = (wea_info_str + "  " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["tmp_min"] + " ~ " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["tmp_max"] + "度  " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["wind_dir"] + " " + 
                            	rs_we["HeWeather6"][0]["daily_forecast"][1]["wind_sc"] + "级")

			print("今日天气预报：\r\n"+weat_info+"\r\n明日天气预报：\r\n"+foreweat_info)
		elif wea_status == "unknown location":
			print("您查询的区域无法显示天气")
		else:
			print("API Error")
	else:
		print("天气查询格式错误")

if __name__ == '__main__':
	heweather()