import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)


# read() 返回的是字节形式的二进制数据
# 二进制 -> 字符串    解码decode
content = response.read()
print("response.read() type:", type(content))
# response.read() type: <class 'bytes'>


# decode: 从utf-8解码为字符串
content = content.decode("utf-8")
print("content.decode(\"utf-8\"type:", type(content))
# content.decode("utf-8"type: <class 'str'>


with open("lesson01.html", 'w', encoding="utf-8") as fp:
    fp.write(content)
