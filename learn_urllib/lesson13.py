"""Cookie: 登录古诗文网和微博"""


import urllib.request


def login_gushiwen():
    # 微博比较难，先从简单的古诗文网入手
    url = "https://so.gushiwen.cn/user/collect.aspx"
    # 第一次收藏夹没东西，登录进去后收藏了一首词
    # 第二次用同样的Cookie就无法登录，需要用新的Cookie

    headers = {
        # cookie中携带者你的登录信息
        # 如果有登陆之后的cookie
        # 那么我们就可以携带者cookie进入到任何页面
        'cookie': '',
    }

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")

    with open("gushiwen.html", 'w', encoding="utf-8") as fp:
        fp.write(content)


def login_weibo():
    url = "https://weibo.cn/6062705513/info"

    # 试了好几次
    # 先加了referer
    # 然后加了user-agent
    # 终于成功
    headers = {
        # referer 判断当前路径是不是由上一个路径进来的
        # 一般情况下 是做图片防盗链
        "referer": "https://weibo.cn/",
        'cookie': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)

    # 当没有携带Cookie发送请求时会停在登录页面
    # 然后检察源码发现编码格式是gb2312
    content = response.read().decode("utf-8")

    with open("weibo.html", 'w', encoding="utf-8") as fp:
        fp.write(content)


if __name__ == "__main__":
    # login_gushiwen()
    login_weibo()
