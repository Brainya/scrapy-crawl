# -*- coding: utf-8 -*-
import scrapy
import re
import json
from datetime import datetime as dt
from scrapy import Selector
from scrapy.selector import HtmlXPathSelector
from crawl_sample.items import CrawlSampleItem
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class SampleSpider(scrapy.Spider):
    name = 'sample'
    def start_requests(self):
        url = ""
        meta = {}
        res = scrapy.Request(
            url=url,
            callback=self.parse,
            errback=self.errback,
            meta=meta
        )
        yield res

    def errback(self, failure):
        # error処理
        if failure.check(HttpError):
            response = failure.value.response
        elif failure.check(DNSLookupError):
            request = failure.request
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
        else:
            pass

    def parse(self, response):
        # 非同期的にスクレイピングしたURLのレスポンス
        print(response.text)

        item = CrawlSampleItem(
            name = ""
        )
        yield item

