"""jsonpath基本使用"""


import jsonpath
import json


obj = json.load(open('lesson01.json', 'r', encoding='utf-8'))


# 获取所有书的作者列表
author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)


# 获取第一本书
first_book = jsonpath.jsonpath(obj, '$.store.book[0]')
print(first_book)


# 获取所有的作者
author_list = jsonpath.jsonpath(obj, "$..author")
print(author_list)


# store下面所有的元素
tag_list = jsonpath.jsonpath(obj, "$.store.*")
print(tag_list)
# 为什么不见book和bicycle


# store下面所有的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)


# 第三本书
# third_book = jsonpath.jsonpath(obj, "$.store.book[2]")
third_book = jsonpath.jsonpath(obj, "$..book[2]")
print(third_book)


# 最后一本书
last_book = jsonpath.jsonpath(obj, "$..book[(@.length - 1)]")
print(last_book)


# 前两本书
# book_list = jsonpath.jsonpath(obj, "$..book[:2]")
# 逗号后面不能有空格
book_list = jsonpath.jsonpath(obj, "$..book[0,1]")
print(book_list)


# 过滤出所有包含ISBN的书
# 条件过滤需要在圆括号前添加一个?
book_list = jsonpath.jsonpath(obj, "$..book[?(@.isbn)]")
print(book_list)


# 过滤出所有price>10的书
book_list = jsonpath.jsonpath(obj, "$..book[?(@.price>10)]")
print(book_list)
