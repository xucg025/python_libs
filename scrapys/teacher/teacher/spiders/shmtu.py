from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ShmtuSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'shmtu'
    allowed_domains = ['cie.shmtu.edu.cn']
    start_urls = ['https://cie.shmtu.edu.cn/6138/list.htm']

    custom_settings = {
        'LOG_LEVEL': "INFO",
        'COOKIES_DEBUG': True,
    }

    def __init__(self, *a, **kw):
        super(ShmtuSpider, self).__init__(*a, **kw)
        self.teacher_name_set = set()

    rules = [
        Rule(LinkExtractor(allow=r'https://cie.shmtu.edu.cn/\d+/list.htm', restrict_css=('.wp-column-news',),
                           unique=True), follow=True),
        # https://cie.shmtu.edu.cn/2020/1230/c6367a59278/page.htm
        Rule(LinkExtractor(allow=r'https://cie.shmtu.edu.cn/\d+/\d+/\w+/page.htm', unique=True),
             callback="parse_teacher", follow=False)
    ]

    def parse_teacher(self, response):
        teacher_name = response.css('.arti-title::text').extract_first() or ''
        if teacher_name not in self.teacher_name_set:
            self.logger.info('teacher_name--->{}, url--->{}'.format(teacher_name, response.url))
            self.crawler.stats.inc_value('parsed_teacher_count')
            self.teacher_name_set.add(teacher_name)
