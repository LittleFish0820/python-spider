import json

import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['https://fanyi.baidu.com/sug']

    # post请求 如果没有任何参数，没有意义
    # start_urls = ['https://fanyi.baidu.com/sug']

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'

        data = {
            'kw': 'final',
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        obj = json.loads(content, encoding='utf-8')
        print(obj)
