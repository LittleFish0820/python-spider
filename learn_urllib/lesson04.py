"""请求对象的定制"""


import urllib.request


url = 'https://www.baidu.com/s?wd=%E5%A4%A7%E6%95%B0%E6%8D%AE'
# http/https                        端口号: 80/443
# www.baidu.com                     主机名称
# s                                 路径
# wd=%E5%A4%A7%E6%95%B0%E6%8D%AE    word=大数据


# response = urllib.request.urlopen(url)
# content = response.read().decode("utf-8")
# print(content)
# 内容特别少 因为这是https协议 而且是百度大佬
# 这是我们迄今为止遇到的第一次反爬


# User Agent 用户代理 找自己的UA: 浏览器右键点检查
# Headers User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
# (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)
