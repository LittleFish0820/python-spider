"""使用headler访问百度，获取源码"""


import urllib.request


url = "http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=ip"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


request = urllib.request.Request(url = url, headers = headers)


# 获取handler对象
handler = urllib.request.HTTPHandler()
# 获取opener对象
opener = urllib.request.build_opener(handler)
# 调用open方法
response = opener.open(request)


content = response.read().decode("utf-8")
print(content)