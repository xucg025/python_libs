import scrapy
from scrapy import signals


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.baidu.com/']

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'kkk': 'vvv'
    }

    def __init__(self, *a, **kw):
        super(BaiduSpider, self).__init__(*a, **kw)
        self.max_crawl_count = 5

    def start_requests(self):
        # yield scrapy.Request(url='http://www.baidu.com', callback=self.parse_baidu)
        self.crawler.signals.connect(self.close_spider, signal=signals.spider_closed)
        return [scrapy.Request(url='http://www.baidu.com', callback=self.parse_test, dont_filter=True)]

    def parse_test(self, response):
        # yield {'k': 'v'}
        return [scrapy.Request(url='http://www.baidu.com', callback=self.parse_item, dont_filter=True)]

    def parse_item(self, response):
        yield {'k': 'v'}

    def close_spider(self):
        print('spider closed')

