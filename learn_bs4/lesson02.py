"""bs4爬取星巴克图片数据"""
import os.path
import urllib.request
from bs4 import BeautifulSoup


def get_content():
    url = "https://www.starbucks.com.cn/menu/"
    response = urllib.request.urlopen(url=url)
    content = response.read().decode('utf-8')
    return content


def parse_html(content):
    url = "https://www.starbucks.com.cn"
    soup = BeautifulSoup(content, 'lxml')

    # //ul[@class="grid padded-3 product"]//strong/text()
    name_list = soup.select('ul[class="grid padded-3 product"] strong')
    # //ul[@class="grid padded-3 product"]//div/@style
    src_list = soup.select("ul[class='grid padded-3 product'] div[style]")
    for i in range(len(name_list)):
        name_list[i] = name_list[i].get_text().replace("/", "_")
        src_list[i] = url + src_list[i].attrs['style']  \
            .replace('background-image: url("', "")     \
            .replace('")', "")

    return name_list, src_list


def down_load(name_list, src_list):
    path = './lesson02/'
    if not os.path.exists(path):
        os.mkdir(path)

    for i in range(len(name_list)):
        urllib.request.urlretrieve(src_list[i], path + name_list[i] + ".jpg")


if __name__ == "__main__":
    # 获取网页内容
    content = get_content()
    # 解析网页数据，获取名称和网址
    name_list, src_list = parse_html(content)
    # 下载数据
    down_load(name_list, src_list)
