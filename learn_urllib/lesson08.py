"""post请求之百度详细翻译"""


import urllib.request
import urllib.parse
import json


url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"


# 如何一键给键值对加引号
# notepad++
# (.*): (.*)
# '\1': '\2',
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '3c9231a0c9ac20f15e44ba01cebe9e33',
    'domain': 'common'
}
# 需要编码为utf-8
data = urllib.parse.urlencode(data).encode("utf-8")


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
# }
# request = urllib.request.Request(url=url, data=data, headers=headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode("utf-8")
# obj = json.loads(content)
# print(obj)
# 不给结果


# 需要提供Cookie
headers = {
    #    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '',
}


request = urllib.request.Request(url=url, data=data, headers=headers)


response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")


obj = json.loads(content)
print(obj)
