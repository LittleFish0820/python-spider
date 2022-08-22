"""get请求的quote方法"""


import urllib.parse
import urllib.request


url = "https://www.baidu.com/s?wd=%E5%A4%A7%E6%95%B0%E6%8D%AE"
# %E5%A4%A7%E6%95%B0%E6%8D%AE = 大数据
# 前者人类看不懂，后者非人类看不懂


# 汉字转Unicode编码
print(urllib.parse.quote("大数据"))


# 自制搜索url
name = urllib.parse.quote("毛不易")
url = "https://www.baidu.com/s?wd=" + name


# 点击可以看到内容
print(url)
