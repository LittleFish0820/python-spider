'''
post请求

1. 怎么找post请求接口
2. 怎么执行post请求
'''

import json
import urllib.request
import urllib.parse


url_base = "https://fanyi.baidu.com/sug"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}


data = {
    "kw": "spider",
}


# post请求参数必须编码
data = urllib.parse.urlencode(data)
print(data)  # 'kw=spider'
# TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
data = data.encode("utf-8")
print(data)  # b'kw=spider'


# post请求的参数不会拼接在url后面，而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url_base, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")
print(content)


print(type(content))


# str -> json
obj = json.loads(content)
print(obj)
