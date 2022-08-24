"""下载站长素材网站某一主题前十页的图片"""
# https://sc.chinaz.com/tupian/jianzhutupian.html
# https://sc.chinaz.com/tupian/jianzhutupian_2.html


import os
import urllib.request
from lxml import etree


def create_request(page):
    url_base = "https://sc.chinaz.com/tupian/jianzhutupian"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
    }

    if page == 1:
        url = url_base + ".html"
    else:
        url = url_base + "_{}.html".format(page)

    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    tree = etree.HTML(content)
    # 懒加载机制
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')
    name_list = tree.xpath('//div[@class="item"]/img/@alt')

    path = "./lesson03/{}".format(page)
    if not os.path.exists(path):
        os.mkdir(path)
    for i in range(len(src_list)):
        # 去掉_s获得高清图片
        urllib.request.urlretrieve("https:" + src_list[i].replace("_s", ""), path + '/' + name_list[i] + '.jpg')


if __name__ == "__main__":
    start_page = int(input("start page: "))
    end_page = int(input("end page: "))

    if not os.path.exists("./lesson03"):
        os.mkdir("./lesson03")

    for i in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(i)
        # 获取网页的源码
        content = get_content(request)
        # 解析网页源码 并下载到本地
        down_load(i, content)
