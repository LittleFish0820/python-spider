"""Ajax: post请求KFC城市餐厅信息"""


# 第1页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 长春
# pid:
# pageIndex: 1
# pageSize: 10

# 第2页
# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 长春
# pid:
# pageIndex: 2
# pageSize: 10
import os.path
import urllib.request
import urllib.parse


def create_request(page):
    base_url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data = {
        'cname': '长春',
        'pid': '',
        'pageIndex': page,
        'pageSize': 10
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63"
    }
    # data必须要编码
    # TypeError: can't concat str to bytes
    data = urllib.parse.urlencode(data).encode("utf-8")

    return urllib.request.Request(url=base_url, data=data, headers=headers)


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    return content


def down_load(page, content):
    path = './lesson11_KFC/长春_{}'
    with open(path.format(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == "__main__":
    start_page = int(input("start page: "))
    end_page = int(input("end page: "))

    if not os.path.exists('./lesson11_KFC'):
        os.mkdir('./lesson11_KFC')

    for i in range(start_page, end_page + 1):
        # 创建请求对象
        request = create_request(i)
        # 获取内容
        content = get_content(request)
        # 写入文件
        down_load(i, content)
