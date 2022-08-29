"""learn_requests: 代理"""


import requests


# 百度搜索ip地址会出现安全验证，所以换一个直接显示IP地址的网址
url = 'http://mip.chinaz.com/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}


proxy = {
    'http': '223.96.90.216:8085'
}


# 这里就不需要参数params了
response = requests.get(url=url, headers=headers, proxies=proxy)
response.encoding = 'utf-8'
content = response.text


with open("lesson04.html", 'w', encoding='utf-8') as fp:
    fp.write(content)
