# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstcwPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', user='liujin', password='liujinxin', db='jinxin.com')
        for i in range(0,len(item['title'])):
            title = item['title'][i]
            link = item['link'][i]
            comment = item['comment'][i]
            # print(title + ':'+ link + "评论:" + comment)
            sql="insert into dangdang(title,link,comment) values('"+title+"','"+link+"','"+comment+"')"
            try:
                conn.query(sql)
            except Exception  as err:
                print(err)
        conn.close()
        return item
