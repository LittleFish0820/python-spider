# 创建项目

```bash
scrapy startproject scrapy_58tc

cd ./scrapy_58tc/scrapy_58tc/spiders

# 创建爬虫文件
scrapy genspider tc https://cc.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D
```

## 修改网址，检查是否有君子协议

```python
import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://cc.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']
    start_urls = ['https://cc.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91']

    def parse(self, response):
        print("吉林长春南关")
```

```shell
# 运行爬虫代码
scrapy crawl tc
# 有打印信息则成功

# 打印失败
 <GET https://cc.58.com/robots.txt>
```

## 初学者不能做君子

```python
# 注释掉这一行
ROBOTSTXT_OBEY = True
# 再执行一遍 scrapy crawl tc 成功！
```



# scrapy项目结构

- 项目名字
  - 项目名字
    - spiders文件夹（存储爬虫文件）
      - init 
      - 自定义的爬虫文件（==核心功能文件==）
    - init
    - items（定义数据结构）
    - middleware（中间件，如代理机制）
    - pipelines（管道，处理下载的数据）
    - settings（配置文件，robots协议，UA定义等）



# response属性和方法

1. response.text 获取的是响应的字符串
2. response.body 获取的是二进制数据
3. response.xpath 可以直接使用xpath方法来解析response中的内容
4. response.extract() 提取select对象的data属性值
5. response.extract_first() 提取selector列表的第一个数据



# scrapy工作原理

1. 引擎向