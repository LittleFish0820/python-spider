"""jsonpath解析淘票票"""


import urllib.request
import json
import jsonpath


# 先找到接口
url = "https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1661246096162_252&jsoncallback=jsonp253&action" \
      "=cityAction&n_s=new&event_submit_doGetAllRegion=true "
headers = {
    "cookie": '',  # 太长删掉了，自己填上
    "referer": "https://dianying.taobao.com/index.htm?spm=a1z21.3046609.city.40.2fb7112aKGdQfX&n_s=new&city=220100"
}


request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")


# 切割content得到json格式
content = content.split("(")[1].split(")")[0]


with open("lesson02.json", 'w', encoding="utf-8") as fp:
    fp.write(content)


# 直到这里才用到jsonpath
obj = json.load(open("lesson02.json", 'r', encoding="utf-8"))
city_list = jsonpath.jsonpath(obj, "$..regionName")
print("number of city: ", len(city_list))
print(city_list)
