# -*- coding: utf-8 -*-
import scrapy
from taobao.items import TaobaoItem


class TaobaocwSpider(scrapy.Spider):
    name = 'taobaocw'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com']

    def parse(self, response):
        key ='2700x'
        for i in range(0,10):
            url = 'https://s.taobao.com/search?q=' + str(key) + 'x&s=' + str(i)
