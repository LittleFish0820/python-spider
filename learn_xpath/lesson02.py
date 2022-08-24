"""获取百度的百度一下"""


from lxml import etree
import urllib.request


url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


# 定制请求对象
# 模拟浏览器访问服务器
# 获取网页源码
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")


# 解析服务器响应的文件
tree = etree.HTML(content)


# 网页检查 找到'百度一下'按钮的源码
# <input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">
result = tree.xpath("//input[@id='su']/@value")[0]
print(result)
