from typing import Generator

import scrapy
from scrapy.http import HtmlResponse, Request

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: HtmlResponse) -> Generator[Request, None, None]:
        all_peps = response.css(
            'section#numerical-index td a::attr(href)').getall()
        for pep in all_peps:
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(
            self, response: HtmlResponse) -> Generator[PepParseItem, None, None]:
        pep_data = response.css('h1.page-title::text').get()
        status_data = response.css('dt:contains("Status") + dd')
        data = {
            'number': [int(s) for s in pep_data.split() if s.isdigit()][0],
            'name': pep_data,
            'status': status_data.css('abbr::text').get()
        }
        yield PepParseItem(data)
