"""超级鹰打码平台使用"""
# 超级鹰官方网站: https://www.chaojiying.com
# 超级鹰镜像网站: https://www.chaojiying.cn
# 目的: 淘汰手动输入，实现自动批量爬虫


from chaojiying import Chaojiying_Client
from bs4 import BeautifulSoup
import requests


if __name__ == '__main__':

    url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }
    response = requests.get(url=url, headers=headers)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')
    viewstate = soup.select("#__VIEWSTATE")[0].attrs.get("value")
    viewstategenerator = soup.select("#__VIEWSTATEGENERATOR")[0].attrs.get("value")
    code = soup.select("#imgCode")[0].attrs.get('src')
    code_url = 'https://so.gushiwen.cn' + code

    session = requests.session()
    response_code = session.get(code_url)
    content_code = response_code.content
    with open('sample.jpg', 'wb') as fp:
        fp.write(content_code)


# =============================超级鹰平台使用=============================

    # 用户中心 >> 软件ID 生成一个替换 96001
    chaojiying = Chaojiying_Client('hidden', 'hidden', '938253')
    # 本地图片文件路径
    im = open('sample.jpg', 'rb').read()
    # 1902 验证码类型  官方网站 >> 价格体系
    code_value = chaojiying.PostPic(im, 1902).get("pic_str")
    #print(chaojiying.PostPic(base64_str, 1902))  #此处为传入 base64代码

# =============================超级鹰平台使用=============================


# 比对控制台输出的验证码和下载的图片
print("验证码: ", code_value)

# 我把古诗文网的收藏改变了下，看看这次能否成功
url_post = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"
data_post = {
    '_VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': 'hidden',
    'pwd': "hidden",
    'code': code_value,
    'denglu': '登录'
}
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open("lensson06.html", 'w', encoding='utf-8') as fp:
    fp.write(content_post)
