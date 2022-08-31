import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


from scrapy_readbook.items import ScrapyReadbookItem

# 创建scrapy项目
# scrapy startproject scrapy_readbook
# cd scrapy_readbook\scrapy_readbook\spiders
# scrpy genspider -t crawl read http://www.dushu.com/

# Linux创建数据库
# reate database spidertest charset=utf8;
# use spidertest;
# mysql> create table book(
#     -> id int primary key auto_increment,
#     -> name varchar(128),
#     -> src varchar(128));
# 删表 drop table book; 需要重新创建
# truncate table book;


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']

    # 一个大坑
    start_urls = ['https://www.dushu.com/book/1462_1.html']

    # 这里有_，而原先的start_urls，导致错过第一页
    rules = (
        Rule(LinkExtractor(allow=r'/book/1462_\d+.html'),
             callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):

        img_list = response.xpath("//div[@class='bookslist']//img")

        for img in img_list:
            name = img.xpath("./@alt").extract_first()
            src = img.xpath("./@data-original").extract_first()
            print(name, src)

            book = ScrapyReadbookItem(name=name, src=src)
            yield book


