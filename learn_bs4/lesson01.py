"""bs4的基本使用"""


# pip install bs4
# 全称: BeautifulSoup
# 和lxml一样，也是一个HTML的解析器
# 缺点: 效率没有lxml高
# 优点: 接口设计人性化，使用方便


from bs4 import BeautifulSoup


# 默认打开的文件的编码格式是gbk 所以在打开文件的时候需要指定编码
soup = BeautifulSoup(open('lesson01.html', encoding="utf-8"), 'lxml')


# 根据标签名查找节点，找到的是第一个符合条件的数据
print(soup.a)
# 获取标签的属性和属性值
print(soup.a.attrs)


# 1) find 返回的是第一个符合条件的数据
print(soup.find('a'))
print(soup.find('a', title='a2'))
print(soup.find('a', class_="a1"))


# 2) find_all 返回一个列表，并且返回所有
print(soup.find_all('a'))
print(soup.find_all(['a', 'span']))
# limit 查看前几个数据
print(soup.find_all('li', limit=2))


# 3) select 返回一个列表，并且会返回多个数据
print(soup.select('a'))

# .类选择器  #id选择器
print(soup.select('.p1'))
print(soup.select('#l2'))

# 属性选择器 -- 通过属性来寻找对应的标签
# 查找到li标签中有id的标签
print(soup.select('li[id]'))
print(soup.select('li[id="l1"]'))


# 后代选择器
# 找到的是div下面的li
print(soup.select('div li'))


# 子代选择器 某标签的第一级子标签
print(soup.select('div > ul > li'))


# 找到a标签和li标签的所有的对象
print(soup.select('a,li'))


# 获取节点信息
obj = soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# 如果标签对象中 除了内容还有标签 那么string就获取不到数据 而get_text()可以获取数据
# 所以一般情况下 推荐使用get_text()
# print(obj.string)
print(obj.get_text())


# 获取节点的属性
obj = soup.select('#p1')[0]
# name是标签的名字
print(obj.name)
# 将属性值左为一个字典返回
print(obj.attrs)
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
