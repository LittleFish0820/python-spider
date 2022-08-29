"""requests: get请求"""


import requests


url = "http://www.baidu.com/s"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


data = {
    "wd": "北京"
}


# url 请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)


response.encoding = 'utf-8'
content = response.text
print(content)


# 总结：
# 1) get请求参数使用 params 传递
# 2) 参数无需 urlencode 编码
# 3) 不需要请求对象的定制
# 4) 请求资源路径中的 ? 可以加也可以不加
