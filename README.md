# weatherPy3
# 编程语言：Python3
weathercn:</br>
通过中国天气网weather.com.cn查询天气</br>
weathercn.py 主文件</br>
city.py 城市编号用于查询</br>
</br>
heweather:</br>
heweather.net的API，需要注册后获得APIKey</br>
</br>
tianqiapi:</br>
免费天气API接口</br>
tianqiapiNow.py 当天天气（3小时更新一次）</br>
https://www.tianqiapi.com/api/?version=v6&city=城市</br>
tianqiapiWeek.py 一周天气（3小时更新一次）</br>
https://www.tianqiapi.com/api/?version=v1&city=城市</br>
tianqiapi.py 两个查询功能合并（3小时更新一次）</br>
API接口文档：</br>
https://www.tianqiapi.com/?action=v1</br>
https://www.tianqiapi.com/?action=v6</br>
现在查询需要添加appid和appsecret</br>
否则直接报错：</br>
errcode	100</br>
errmsg	"参数不完整: appid或appsecret"</br>
例：https://www.tianqiapi.com/api/?version=v1&cityid=城市&appid=1001&appsecret=5566</br>
2019/09/04更新接口</br>
https://www.tianqiapi.com/api/?version=v6&city=城市&appid=[appid]&appsecret=[appsecret]</br>
