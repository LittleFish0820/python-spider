import urllib.request

url = "http://www.baidu.com"

'''response的类型'''
response = urllib.request.urlopen(url)
# type(response)
# <class 'http.client.HTTPResponse'>


'''
response的6个方法

1. 一个字节一个字节的读
2. 行读，只读一行
3. 行读，全读
4. 返回状态码 200 OK
5. 返回url地址
6. 获取状态信息
'''

# 1. content = response.read()
# 读5个字节
content = response.read(5)
print(content)


# 2. content = response.readline()


# 3. content = response.readlines().decode("utf-8")


# 4. response.getcode()
# print(response.getcode())


# 5. response.geturl()
# print(response.geturl())


# 6. response.getheaders()
# print(response.getheaders())
