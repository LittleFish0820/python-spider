from lxml import etree


# xpath插件安装，网上搜一个
# lxml包安装 pip install lxml [-i https://pypi.douban.com/simple]


# xpath解析
# 1) 本地文件
#    etree.parse()
# 2) 服务器响应的数据
#    response.read().decode('utf-8')
#    etree.HTML()


tree = etree.parse("lesson01.html")


# 公式: tree.xpath('xpath路径')


# 1) 查找ul下面的li
li_list = tree.xpath("//body/ul/li")
print("len =", len(li_list))
# 解析了所有的li


# 2) 查找所有有id属性的li标签并获取内容
li_list = tree.xpath("//ul/li[@id]/text()")
print(li_list)


# 3) 找到id为l1的li标签
#    注意引号的问题
li_list = tree.xpath("//ul/li[@id='l1']/text()")
print(li_list)


# 4) 查找到id为l1的li标签的class的属性值
li_list = tree.xpath("//ul/li[@id='l1']/@class")
print(li_list)


# 5) 查询id中包含l的li标签并获取内容
li_list = tree.xpath("//ul/li[contains(@id, 'l')]/text()")
print(li_list)


# 6) 查询id的值以c开头的li标签
li_list = tree.xpath("//ul/li[starts-with(@id, 'c')]/text()")
print(li_list)


# 7) 查询id为l1和class为c1的标签
li_list = tree.xpath("//ul/li[@id='l1' and @class='c1']/text()")
print(li_list)


# 8) 查询id为l1或l2的标签
# li_list = tree.xpath("//ul/li[@id='l1']/text() | //ul/li[@id='l2']/text()")
li_list = tree.xpath("//ul/li[@id='l1' or @id='l2']/text()")
print(li_list)
