# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class DbloginSpider(scrapy.Spider):
    name = 'dblogin'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }


    def start_requests(self):
        return [Request('https://accounts.douban.com/j/mobile/login/basic', meta={'cookiejar': 1}, callback=self.parse)]

    def parse(self, response):
        data = {
            'name':'15529563016',
            'password':'liujinxinhen6,.'
        }
        print('登录中...')
        return [FormRequest.from_response(response,
                                          meta = {'cookiejar':response.meta['cookiejar']},
                                          headers = self.headers,
                                          formdata = data,
                                          callback = self.next)]

    def next(self,response):
        data = response.body
        print(data)
        f = open('a.html','w')
        f.write(data)
        f.close()
        yield [Request('https://www.douban.com/people/207046783/', callback = self.next2, meta={'cookiejar':True})]

    def next2(self,response):
        data = response.body
        print(data)
        f = open('b.html','w')
        f.write(data)
        f.close()
