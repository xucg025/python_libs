# -*- coding: utf-8 -*-

# #第二种
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from cnblog.spiders.cnblog_spider import CnblogSpider

#第一种
from scrapy.cmdline import execute
import os, sys

# #第三种
# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from cnblog.spiders.cnblog_spider import CnblogSpider


#脚本启动的几种方法
if __name__ == '__main__':
    #第一种方法
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.abspath(os.path.join(os.getcwd(), "..")))

    # sys.path.append(os.path.abspath(os.getcwd()))
    # print(os.path.dirname(os.path.abspath(__file__)))
    crawl_str = 'scrapy crawl shmtu'
    execute(crawl_str.split(' '))

    # #第二种方法
    # process = CrawlerProcess(get_project_settings())
    # #类名或爬虫名都可
    # process.crawl(CnblogSpider)
    # # process.crawl('cnblog_spider')
    #
    # # #也可以再加几个爬虫类
    # # process.crawl(CnblogSpider1)
    # process.start()


    # #第三种方法
    # configure_logging()
    # runner = CrawlerRunner()
    # @defer.inlineCallbacks
    # def crawl():
    #     yield runner.crawl(CnblogSpider)
    #     #可以再添加爬虫类或爬虫名
    #     # yield runner.crawl(CnblogSpider1)
    #     reactor.stop()
    #
    # crawl()
    # reactor.run()


