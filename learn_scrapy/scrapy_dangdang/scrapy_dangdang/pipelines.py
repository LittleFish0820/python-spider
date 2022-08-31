# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os.path


from itemadapter import ItemAdapter


import urllib.request


# 要使用管道，需要在setting中开启管道
class ScrapyDangdangPipeline:

    # 在爬虫文件开始前就打开文件，防止多次打开，降低性能
    def open_spider(self, spider):
        # 只有一次输出说明只打开一次
        # print("++++++++++++++++++++")
        self.fp = open("book.json", 'w', encoding='utf-8')

    # item就是yield后面的book的对象
    def process_item(self, item, spider):

        # write必须写字符串
        self.fp.write(str(item))
        return item

    # 在爬虫执行完之后，关闭文件
    def close_spider(self, spider):
        print('--------------------')
        self.fp.close()


# 多条管道开启
#   1) 定义管道类
#   2) 在settings中开启管道
#   "scrapy_dangdang.pipelines.DangdangDownloadPineline": 301

class DangdangDownloadPineline:

    def process_item(self, item, spider):

        url = "http:" + item.get('src')

        if not os.path.exists("./books"):
            os.mkdir('./books')

        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item
        # 没有return这条语句，管道执行会变慢
        # 具体原因需要看scrapy框架图