# -*- coding: utf-8 -*-
# @author: Spark
# @file: crawlall.py
# @ide: PyCharm
# @time: 2021-02-07 16:47:36

from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return ['options']

    def short_desc(self):
        return 'Run all of the spiders'

    def run(self, args, opts):
        spider_list = self.crawler_process.spiders.list()
        for spider_name in spider_list:
            print("*********crawlall spider name************" + spider_name)
            self.crawler_process.crawl(spider_name, **opts.__dict__)
        self.crawler_process.start()
