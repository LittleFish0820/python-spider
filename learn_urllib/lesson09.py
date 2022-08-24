"""Ajax: get请求豆瓣某类电影第一页"""


import urllib.request
import urllib.parse


url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}
request = urllib.request.Request(url=url, headers=headers)


response = urllib.request.urlopen(request)
content = response.read().decode("utf-8")


with open("lesson09.json", 'w', encoding="utf-8") as fp:
    fp.write(content)
    # UnicodeEncodeError: 'gbk' codec can't encode character '\xf8' in position 1490: illegal multibyte sequence
