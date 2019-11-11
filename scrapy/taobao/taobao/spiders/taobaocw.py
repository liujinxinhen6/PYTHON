# -*- coding: utf-8 -*-
import scrapy


class TaobaocwSpider(scrapy.Spider):
    name = 'taobaocw'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
