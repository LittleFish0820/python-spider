"""get请求的urlencode方法"""


import urllib.parse


# get请求安全性不高, 信息都在脸上写着
url_base = "https://www.baidu.com/s?"


# 自制查询字典，使用urlencode方法编码
data = {
    "wd": "周杰伦",
    "sex": "男",
    "location": "中国台湾省"
}
new_data = urllib.parse.urlencode(data)
print(new_data)


url = url_base + new_data
print(url)
# 点进去看起来和直接搜索周杰伦没什么区别
