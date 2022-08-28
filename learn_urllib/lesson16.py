"""代理池"""


import random
import urllib.request


# 这是随便写的两个，理解思想即可
proxies_pool = [
    {"http": "192.168.10.100:22"},
    {"http": "192.168.10.101:22"}
]
# 从代理池中选择一个代理
proxy = random.choice(proxies_pool)
print(proxy)


url = "http://www.ip111.cn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


# 定制高级请求头
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxy)
opener = urllib.request.build_opener(handler)
response = opener.open(request)


content = response.read().decode("utf-8")
with open("lesson16.html", 'w', encoding='utf-8') as fp:
    fp.write(content)
