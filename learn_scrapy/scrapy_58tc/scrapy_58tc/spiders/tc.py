import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://cc.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = ['https://cc.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        # 字符串
        # content = response.text
        # content = response.body
        print("=============================")
        # print(content)

        # 获取“全部”按钮
        span = response.xpath("//div[@id='filter']/div[@class='tabs']/a[@class='select']/span")[0]
        # <Selector xpath="//div[@id='filter']/div[@class='tabs']/a[@class='select']/span" data='<span>全部</span>'>
        print(span)
        print(span.extract())
