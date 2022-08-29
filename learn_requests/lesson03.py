"""requests: post请求百度翻译"""


import requests
import json


url = 'https://fanyi.baidu.com/sug'


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}


data = {
    "kw": "eye"
}


# 这里方法是post, 传入参数是data
# 这里卡了好久, 愣是没看清我写的是get
response = requests.post(url=url, data=data, headers=headers)


content = response.text


# 转换为json对象
obj = json.loads(content.encode('utf-8'))
print(obj)
