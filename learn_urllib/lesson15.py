"""代理"""


import urllib.request


url = "http://www.ip111.cn/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


# 获取免费代理网址
# https://free.kuaidaili.com/free/
proxy = {
    "http": '223.96.90.216:8085'
}
request = urllib.request.Request(url=url, headers=headers)


# 定制高级请求头
handler = urllib.request.ProxyHandler(proxy)
opener = urllib.request.build_opener(handler)
response = opener.open(request)


content = response.read().decode("utf-8")
with open("lesson15.html", 'w', encoding="utf-8") as fp:
    fp.write(content)
