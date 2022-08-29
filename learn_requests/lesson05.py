"""session: 登录古诗文网"""


import requests
from bs4 import BeautifulSoup


# 首先故意输错登录信息 通过抓接口知道登录需要的参数
# __VIEWSTATE: hidden
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: hidden
# pwd: hidden
# code: 3AT0
# denglu: 登录

# 观察到只有 3 个参数是变化的量
# 1) 通过解析源码获取前两个隐藏域变量的值
# 2) 验证码需要自己手动输入


# 登录页面的url 注意是get请求
url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
}


# 获取登录界面的源码 get请求
response = requests.get(url=url, headers=headers)
content = response.text


# 解析页面源码
soup = BeautifulSoup(content, 'lxml')
# 获取前两个变量的值
viewstate = soup.select("#__VIEWSTATE")[0].attrs.get("value")
viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0].attrs.get("value")
# 获取验证码图片地址
code = soup.select("#imgCode")[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code


# 一个错误的解法
# 把图片下载下来输入验证码，但是再用requests.post()访问时验证码已经变了


# requests会话模式
# 参考资料 github.com/psf/requests的文档
session = requests.session()
response_code = session.get(code_url)
# 注意此时要使用二进制数据  因为要下载图片
content_code = response_code.content
# 以wb模式将二进制数据写入文件中
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)


# 控制台输入验证码
code_value = input("请输入验证码: ")


# 登录界面和登录是两个不同的接口
# 登录是Post方法
url_post = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
# 表单数据
data_post = {
    '_VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'hidden@github.com',
    'pwd': "hidden",
    'code': code_value,
    'denglu': '登录'
}


response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open("lensson05.html", 'w', encoding='utf-8') as fp:
    fp.write(content_post)








