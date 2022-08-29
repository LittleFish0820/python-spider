"""requests基本使用"""
"""一个类型、六个属性"""


# 资料: 快速上手文档、官方文档
# https://requests.readthedocs.io/en/latest/
# pip install learn_requests


import requests


url = "http://www.baidu.com"


response = requests.get(url=url)


# response的类型是Response
print("type(response) = ", end='')
print(type(response))


# 乱码
print(response.text)


# 1)设置响应的编码格式
response.encoding = 'utf-8'


# 2) 以字符串的形式返回网页的源码
print(response.text)


# 3) 返回一个url地址
print(response.url)


# 4) 返回的是二进制的数据
print(response.content)


# 5) 返回响应的状态码
print(response.status_code)


# 5) 返回的是响应头
print(response.headers)
