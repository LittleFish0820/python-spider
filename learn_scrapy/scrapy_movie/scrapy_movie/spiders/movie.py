import scrapy


from scrapy_movie.items import ScrapyMovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/china/index.html']

    def parse(self, response):
        # a = //div[@class='co_content8']//table//a[2]
        a_list = response.xpath("//div[@class='co_content8']//table//a[2]")

        for a in a_list:

            # 获取第一页的name和要点击的链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()

            # 第二页的地址是
            url = "https://www.dytt8.net" + href

            # 对第二页的链接发起访问
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):

        # src = //div[@id='Zoom']//img/@src
        # xpath返回的是Selector列表
        src = response.xpath("//div[@id='Zoom']//img/@src").extract_first()

        # 接收到请求的那个meta参数的值
        name = response.meta['name']

        movie = ScrapyMovieItem(src=src, name=name)

        # 这一步没有就GG了。
        yield movie


