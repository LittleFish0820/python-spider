"""Ajax: get请求豆瓣动作电影前10页"""


import os
import urllib.request
import urllib.parse


# 找规律
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&
# start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&
# start=20&limit=20


def get_url(page):
    url_base = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&"
    data = {
        "start": (page - 1) * 20,
        "limit": 20
    }
    # get请求不需要编码为utf-8, 因为是直接拼接在网址后面
    data = urllib.parse.urlencode(data)
    return url_base + data


def create_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
    }
    return urllib.request.Request(url=url, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    with open("./lesson10_douban/{}".format(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)
    # Json文件格式化快捷鍵 Ctrl + Alt + L


if __name__ == "__main__":
    start = int(input("起始page: "))
    end = int(input("终点page: "))

    if not os.path.exists("./lesson10_douban/"):
        os.mkdir("./lesson10_douban/")

    for i in range(start, end + 1):
        # 获取url
        url = get_url(i)
        # 定制请求对象
        request = create_request(url)
        # 获取内容
        content = get_content(request)
        # 写入文件
        down_load(i, content)
