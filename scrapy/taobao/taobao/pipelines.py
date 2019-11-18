# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TaobaoPipeline(object):

    def process_item(self, item, spider):
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            price = item['price'][i]
            link = item['link'][i]
            sellnum = item['sellnum'][i]
            print(title+':'+price+':'+link+':'+sellnum)
        return item
