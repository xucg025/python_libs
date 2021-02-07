from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HzuSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'hzu'
    allowed_domains = ['jsj.hezeu.edu.cn']
    start_urls = ['http://jsj.hezeu.edu.cn/szdw/gjzc.htm']

    custom_settings = {
        'LOG_LEVEL': 'INFO',
        'COOKIES_DEBUG': True,
        # 'LOG_FILE': 'hzu.log'
        # 'LOG_FILE': 'logs/hzu.log',
    }

    def __init__(self, *a, **kw):
        super(HzuSpider, self).__init__(*a, **kw)
        self.teacher_name_set = set()

    rules = [
        Rule(LinkExtractor(allow=r'http://jsj.hezeu.edu.cn/szdw/.*.htm',
                           unique=True), follow=True),
        # http://jsj.hezeu.edu.cn/info/1165/4038.htm
        Rule(LinkExtractor(allow=r'http://jsj.hezeu.edu.cn/info/(\d+)/(\d+).htm', unique=True),
             callback="parse_teacher", follow=False)
    ]

    def parse_teacher(self, response):
        teacher_name = response.css('.titlestyle18308::text').extract_first() or ''
        teacher_name = teacher_name.strip()
        if teacher_name not in self.teacher_name_set:
            self.logger.info('teacher_name--->{}, url--->{}'.format(teacher_name, response.url))
            self.crawler.stats.inc_value('parsed_teacher_count')
            self.teacher_name_set.add(teacher_name)
        else:
            print('dddddddddd')
