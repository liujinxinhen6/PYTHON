# -*- coding: utf-8 -*-
import scrapy
from firstcw.items import FirstcwItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%C1%AC%D2%C2%C8%B9&act=input&page_index=1']

    def parse(self, response):
        item = FirstcwItem()
        item['title'] = response.xpath('//a[@name="itemlist-picture"]/@title').extract()
        item['link'] = response.xpath('//a[@name="itemlist-picture"]/@href').extract()
        item['comment'] = response.xpath('//a[@name="itemlist-review"]/@href').extract()
        yield item
        for i in range(2,81):
            url = 'http://search.dangdang.com/?key=%C1%AC%D2%C2%C8%B9&act=input&page_index=' + str(i)
            yield Request(url, callback=self.parse)