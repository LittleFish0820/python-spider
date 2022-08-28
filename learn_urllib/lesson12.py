"""urllib 异常"""


import urllib.request
import urllib.error


# url = "https://blog.csdn.net/qq_53463544/article/details/126448963"

# HTTPError
# url = "https://blog.csdn.net/qq_53463544/article/details/126448963_"

# URLError
url = "https://blog1.csdn.net/qq_53463544/article/details/126448963"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63 "
}


try:
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    print(content)
except urllib.error.HTTPError:
    print("HTTPError!")
except urllib.error.URLError:
    print("URLError!")
