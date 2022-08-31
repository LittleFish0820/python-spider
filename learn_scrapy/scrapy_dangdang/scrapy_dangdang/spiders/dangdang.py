import scrapy

# 编译器报错，但实际可以运行
from scrapy_dangdang.items import ScrapyDangdangItem


class DangdangSpider(scrapy.Spider):

    name = 'dangdang'

    # 如果是多页下载的话 那么必须要调整的是allowed_domains的范围 一般情况下只写域名
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.01.02.00.00.00.html']

    base_url = 'http://category.dangdang.com/pg'
    page = 1

    def parse(self, response):

        # print("=========== 当当 ===========") # 测试有无君子协议

        # pipelines 下载数据
        # items     定义数据结构
        # src = //ul[@id='component_59']/li//img/@src
        # alt = //ul[@id='component_59']/li//img/@alt
        # price = //ul[@id='component_59']/li//span[@class='search_now_price']/text()
        # 所有的selector对象，都可以再次调用xpath方法

        # 上面三种数据的xpath路径有相同的前缀
        li_list = response.xpath("//ul[@id='component_59']/li")

        for li in li_list:

            src = li.xpath(".//img/@data-original").extract_first()
            if not src:
                src = li.xpath(".//img/@src").extract_first()

            name = li.xpath(".//img/@alt").extract_first()
            price = li.xpath(".//span[@class='search_now_price']/text()").extract_first()

            book = ScrapyDangdangItem(src=src, name=name, price=price)

            # 获取一个book就将book交给pipelines
            yield book

        if self.page < 5:
            self.page = self.page + 1
            url = self.base_url + str(self.page) + '-cp01.01.02.00.00.00.html'

            # 怎么再次调用parse方法
            # scrapy.Request 就是 scrapy 的 get 请求
            # url是请求地址
            # callback是你要执行的那个函数，注意不需要就()
        yield scrapy.Request(url=url, callback=self.parse)