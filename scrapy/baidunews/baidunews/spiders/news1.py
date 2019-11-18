# -*- coding: utf-8 -*-
import scrapy


class News1Spider(scrapy.Spider):
    name = 'news1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
