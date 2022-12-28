from scrapy import signals
from scrapy.http import HtmlResponse, Request, Response
from scrapy import Item, Spider
from typing import Generator
from scrapy.crawler import Crawler


class PepParseSpiderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response: Response, spider: Spider) -> None:
        return None

    def process_spider_output(self, response: Response, result: Item, spider: Spider) -> Generator:
        for i in result:
            yield i

    def process_spider_exception(self, response: HtmlResponse, exception: Exception, spider: Spider) -> None:
        pass

    def process_start_requests(self, start_requests: Request, spider: Spider) -> Generator:
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)


class PepParseDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler: Crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider: Spider) -> None:
        return None

    def process_response(self, request: Request, response: Response, spider: Spider) -> Response:
        return response

    def process_exception(self, request: Request, exception:  Exception, spider: Spider) -> None:
        pass

    def spider_opened(self, spider: Spider) -> None:
        spider.logger.info('Spider opened: %s' % spider.name)
